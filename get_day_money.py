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
            logging.info('< Error > init : ' + str(e))
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
                sql = f"select ITEM14 , ITEM72 , ITEM15 , ITEM12 from ART00721676130332682_INS where ITEM26='true' and ITEM44='true' order by ITEM12 desc" 
                curr_mssql.execute(sql)
                res           = curr_mssql.fetchall()

                try:
                    conn = pymysql.connect(host=otsuka_factory['host'],port=otsuka_factory['port'],user=otsuka_factory['user'],password=otsuka_factory['pwd'],database=otsuka_factory['db'],charset=otsuka_factory['charset'])
                    curr = conn.cursor()
                    
                    print("------------------------------------------------------------------------------------------------------------------\n")

                    for val in res:
                        
                        #logging.info(f"{val[0]} , {val[1]} , {val[2]} , {val[3]}")
                        
                        r_year  = val[3][0:4]
                        r_month = val[3][5:7]
                        r_day   = val[3][8:10]

                        s_mysql_sql = f"select * from day_money where r_date='{val[3]}' and t_money='{val[2]}' and c_name='{val[0]}'"
                        curr.execute(s_mysql_sql)
                        mysql_res = curr.fetchone()

                        if mysql_res is None:
                            mysql_sql = f"insert into day_money(r_date , r_year , r_month , r_day , c_name , b_name , t_money) value('{val[3]}' , '{r_year}' ,'{r_month}' , '{r_day}' , '{val[0]}','{val[1]}','{val[2]}')"
                            curr.execute(mysql_sql)
                            conn.commit()
                            
                            logging.info(f"新日當資料 :  日期 : {val[3]} , 填表人 : {val[0]} , 金額 : {val[2]}")
                        
                    print("\n")
                    logging.info('update BPM day money is done.')
                    print("------------------------------------------------------------------------------------------------------------------")

                except Exception as e:
                    logging.info("< ERROR > connect mysql fail : " + str(e))

                finally:
                    curr.close()
                    conn.close()
                

        except Exception as e:
            logging.info("< ERROR > connect mysql fail : " + str(e))

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










