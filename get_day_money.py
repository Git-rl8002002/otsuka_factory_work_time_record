#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20221102
# Update   : 20230919
# Function : otsuka factory import excel file

from control.config import *
from control.web_cloud_dao import *

import pandas as pd
import pymysql , logging , pyodbc

########
# log
########
log_format = "%(asctime)s %(message)s"
logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S")

####################################
#
# bpm day money insert into mysql
#
####################################
class day_money:
    
    ########
    # log
    ########
    log_format = "%(asctime)s %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S")
    #logging.disable(logging.INFO)

    #########
    # init
    #########
    def __init__(self):
        try:

            while True: 
                self.bpm_day_money()
                time.sleep(300)
            
        except Exception as e:
            logging.error('< Error > init : ' + str(e))
        finally:
            pass
   
    ##################
    # bpm_day_money
    ##################
    def bpm_day_money(self):
        try: 
                conn_str = f"DRIVER={{SQL Server}};SERVER={otsuka_factory2['host']};DATABASE={otsuka_factory2['db']};UID={otsuka_factory2['user']};PWD={otsuka_factory2['pwd']}"  
                conn_mssql = pyodbc.connect(conn_str)
                curr_mssql = conn_mssql.cursor()  
                #sql = f"select ITEM14 , ITEM72 , ITEM15 , ITEM12 from ART00721676130332682_INS where ITEM26='true' and ITEM44='true' order by ITEM12 desc"
                
                #############################
                #
                # table : ART00851684549915660_INS
                # ITEM12:申請日期
                # ITEM14:填表人(以此為主)
                # ITEM51:申請人
                # ITEM18:日當(true/false)
                # ITEM15:總金額
                # ITEM58:審核後總金額
                # ITEM57: ERP傳票號碼
                # ITEM75:已結案(true/false)
                # ITEM107:表單號碼
                #
                #############################
                sql  = f"select ITEM14 , ITEM51 , ITEM15 , ITEM12 , ITEM58 , ITEM57 , ITEM107 from ART00851684549915660_INS where ITEM75='true' and ITEM18='true'" 
                
                #############################
                #
                # table : ART00851684549915660_INS
                # ITEM12:申請日期
                # ITEM14:填表人(以此為主)
                # ITEM51:申請人
                # ITEM18:日當(true/false)
                # ITEM15:總金額
                # ITEM58:審核後總金額
                # ITEM57: ERP傳票號碼
                # ITEM75:已結案(true/false)
                # ITEM107:表單號碼
                #
                # table : ART00851684549915660ITEM53
                # ITEM1:日期
                # ITEM3:日當
                # ITEM14:註記原因
                # ITEM15:加減金額
                #
                #############################
                sql2  = f"select a.ITEM14 , a.ITEM51 , a.ITEM15 , a.ITEM12 , a.ITEM58 , a.ITEM57 , a.ITEM107 , b.ITEM1 , b.ITEM3 , b.ITEM14 , b.ITEM15 " 
                sql2 += f"from ART00851684549915660_INS a left join ART00851684549915660ITEM53 b on a.INSID=b.INSID " 
                sql2 += f"where a.ITEM75='true' and a.ITEM18='true' and b.ITEM3 != '0' "
                curr_mssql.execute(sql2)
                res  = curr_mssql.fetchall()

                try:
                    conn = pymysql.connect(host=otsuka_factory['host'],port=otsuka_factory['port'],user=otsuka_factory['user'],password=otsuka_factory['pwd'],database=otsuka_factory['db'],charset=otsuka_factory['charset'])
                    curr = conn.cursor()
                    
                    print("------------------------------------------------------------------------------------------------------------------\n")

                    for val in res:
                        
                        #logging.info(f"{val[0]} , {val[1]} , {val[2]} , {val[3]}")
                        
                        r_year  = val[3][0:4]
                        r_month = val[3][5:7]
                        r_day   = val[3][8:10]

                        s_mysql_sql = f"select * from day_money where r_date='{val[3]}' and t_money='{val[2]}' and f_name='{val[0]}' and a_name='{val[1]}' and day_r_date='{val[7]}' and day_t_money='{val[8]}'"
                        curr.execute(s_mysql_sql)
                        mysql_res = curr.fetchone()

                        day_r_year  = val[7][0:4]
                        day_r_month = val[7][5:7]
                        day_r_day   = val[7][8:10]

                        if mysql_res is None:
                            mysql_sql  = f"insert into day_money("
                            mysql_sql += f"r_date , r_year , r_month , r_day , " 
                            mysql_sql += f"f_name , a_name , t_money , c_t_money , erp_num , " 
                            mysql_sql += f"form_num , day_r_date , day_r_year , day_r_month , day_r_day , day_t_money , day_money_mark , day_money_diff" 
                            mysql_sql += f") " 
                            mysql_sql += f"value(" 
                            mysql_sql += f"'{val[3]}' , '{r_year}' , '{r_month}' , '{r_day}' , "
                            mysql_sql += f"'{val[0]}' , '{val[1]}' , '{val[2]}' , '{val[4]}' , '{val[5]}' ," 
                            mysql_sql += f"'{val[6]}' , '{val[7]}' , '{day_r_year}' , '{day_r_month}' , '{day_r_day}' , '{val[8]}' , '{val[9]}' , '{val[10]}'" 
                            mysql_sql += f")"
                            curr.execute(mysql_sql)
                            conn.commit()
                            
                            logging.info(f"新日當資料 > 表單日期 : {val[3]} , 填表人 : {val[0]} , 申請人 : {val[1]} , 總金額 : {val[2]} , 日當日期 : {val[7]} , 日當金額 : {val[8]} , 註記原因 : {val[9]} , 加減金額 : {val[10]}")
                        
                    print("\n")
                    logging.info('update BPM day money is done.')
                    print("------------------------------------------------------------------------------------------------------------------")

                except Exception as e:
                    logging.error("connect mysql fail : " + str(e))

                finally:
                    curr.close()
                    conn.close()
                

        except Exception as e:
            logging.error("connect mysql fail : " + str(e))

        finally:
            curr_mssql.close()
            conn_mssql.close()


#####################################################################################
#
# main
#
#####################################################################################
if __name__ == '__main__':
    
    # check day money
    check_day_money = day_money()










