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
                #self.update_day_money()
                time.sleep(300)
            
        except Exception as e:
            logging.error('< Error > init : ' + str(e))
        finally:
            pass
   
    #####################
    # update_day_money
    #####################
    def update_day_money(self):
        try:
                    self.conn = pymysql.connect(host=otsuka_factory['host'],port=otsuka_factory['port'],user=otsuka_factory['user'],password=otsuka_factory['pwd'],database=otsuka_factory['db'],charset=otsuka_factory['charset'])
                    self.curr = self.conn.cursor()
                    
                    print("------------------------------------------------------------------------------------------------------------------\n")

                    #month = '0' + month if int(month) < 10 else month

                    # all day by month 
                    name_sql = f"select a_name from day_money where day_r_year='2023' and day_r_month='09' group by a_name order by day_r_day asc"
                    self.curr.execute(name_sql)
                    name_res = self.curr.fetchall() 

                    for name_val in name_res:
                        
                        day_sql = f"select day_r_day from day_money where day_r_year='2023' and day_r_month='09' group by day_r_day order by day_r_day asc"
                        self.curr.execute(day_sql)
                        day_res = self.curr.fetchall()

                        for day_val in day_res:
                             
                             search_sql = f"select * from day_money where day_r_year='2023' and day_r_month='09' and day_r_day='{day_val[0]}' and a_name='{name_val[0]}'"
                             self.curr.execute(search_sql)
                             search_res = self.curr.fetchone()

                             if search_res is None:
                                add_sql = f"insert into day_money(day_r_year , day_r_month , day_r_day , a_name , day_t_money) value('2023','09','{day_val[0]}','{name_val[0]}','0')"
                                self.curr.execute(add_sql)  
                    
                    #return day_res
                    self.conn.commit()
                    print("\n")
                    logging.info('< Msg > synchronization day money is done.')
                    print("------------------------------------------------------------------------------------------------------------------")

        except Exception as e:
            logging.error("< Error > connect mysql fail : " + str(e))

        finally:
            self.curr.close()
            self.conn.close()

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
                        
                        r_year      = val[3][0:4]
                        r_month     = val[3][5:7]
                        r_day       = val[3][8:10]
                        day_r_year  = val[7][0:4]
                        day_r_month = val[7][5:7]
                        day_r_day   = val[7][8:10]
                        
                        ###############################################
                        #
                        # Check if there are records in the database
                        #
                        ###############################################
                        #s_mysql_sql = f"select * from day_money where r_date='{val[3]}' and t_money='{val[2]}' and f_name='{val[0]}' and a_name='{val[1]}' and day_r_date='{val[7]}' and day_t_money='{val[8]}'"
                        s_mysql_sql = f"select * from day_money where r_date='{val[3]}' and t_money='{val[2]}' and f_name='{val[0]}' and a_name='{val[1]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}'"
                        curr.execute(s_mysql_sql)
                        mysql_res = curr.fetchone()

                        #logging.info(s_mysql_sql)

                        day_money = val[8]

                        #####################################
                        #
                        # get english name by chinese name
                        #
                        #####################################
                        g_e_mysql_sql = f"select employee_eng_name from hr_a where employee_name='{val[1]}'"
                        curr.execute(g_e_mysql_sql)
                        g_e_name = curr.fetchone()

                        if mysql_res is None:
                            
                            mysql_sql  = f"insert into day_money("
                            mysql_sql += f"r_date , r_year , r_month , r_day , " 
                            mysql_sql += f"f_name , a_name , e_name , t_money , c_t_money , erp_num , " 
                            mysql_sql += f"form_num , day_r_year , day_r_month , day_t_money , day_money_mark , day_money_diff" 
                            mysql_sql += f") " 
                            mysql_sql += f"value(" 
                            mysql_sql += f"'{val[3]}' , '{r_year}'     , '{r_month}'     , '{r_day}'  , "
                            mysql_sql += f"'{val[0]}' , '{val[1]}'     , '{g_e_name[0]}' , '{val[2]}' , '{val[4]}' , '{val[5]}' ," 
                            mysql_sql += f"'{val[6]}' , '{day_r_year}' , '{day_r_month}' , '{0}' , '{val[9]}' , '{val[10]}'" 
                            mysql_sql += f")"
                            curr.execute(mysql_sql)
                            
                            #logging.info(f"新日當資料 > 表單日期 : {val[3]} , 填表人 : {val[0]} , 申請人 : {val[1]} {g_e_name[0]} , 總金額 : {val[2]} , 日當日期 : {val[7]} , 日當金額 : {val[8]} , 註記原因 : {val[9]} , 加減金額 : {val[10]}")
                        
                        elif str(day_r_day) == '01':
                            mysql_sql  = f"update day_money set day_t_money1='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()

                        elif str(day_r_day) == '02':
                            mysql_sql  = f"update day_money set day_t_money2='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()

                        elif str(day_r_day) == '03':
                            mysql_sql  = f"update day_money set day_t_money3='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        
                        elif str(day_r_day) == '04':
                            mysql_sql  = f"update day_money set day_t_money4='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        
                        elif str(day_r_day) == '05':
                            mysql_sql  = f"update day_money set day_t_money5='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        
                        elif str(day_r_day) == '06':
                            mysql_sql  = f"update day_money set day_t_money6='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        
                        elif str(day_r_day) == '07':
                            mysql_sql  = f"update day_money set day_t_money7='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '08':
                            mysql_sql  = f"update day_money set day_t_money8='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        
                        elif str(day_r_day) == '09':
                            mysql_sql  = f"update day_money set day_t_money9='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        
                        elif str(day_r_day) == '10':
                            mysql_sql  = f"update day_money set day_t_money10='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '11':
                            mysql_sql  = f"update day_money set day_t_money11='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '12':
                            mysql_sql  = f"update day_money set day_t_money12='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '13':
                            mysql_sql  = f"update day_money set day_t_money13='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '14':
                            mysql_sql  = f"update day_money set day_t_money14='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '15':
                            mysql_sql  = f"update day_money set day_t_money15='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '16':
                            mysql_sql  = f"update day_money set day_t_money16='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '17':
                            mysql_sql  = f"update day_money set day_t_money17='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '18':
                            mysql_sql  = f"update day_money set day_t_money18='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '19':
                            mysql_sql  = f"update day_money set day_t_money19='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '20':
                            mysql_sql  = f"update day_money set day_t_money20='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '21':
                            mysql_sql  = f"update day_money set day_t_money21='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '22':
                            mysql_sql  = f"update day_money set day_t_money22='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '23':
                            mysql_sql  = f"update day_money set day_t_money23='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '24':
                            mysql_sql  = f"update day_money set day_t_money24='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '25':
                            mysql_sql  = f"update day_money set day_t_money25='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '26':
                            mysql_sql  = f"update day_money set day_t_money26='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '27':
                            mysql_sql  = f"update day_money set day_t_money27='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '28':
                            mysql_sql  = f"update day_money set day_t_money28='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '29':
                            mysql_sql  = f"update day_money set day_t_money29='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '30':
                            mysql_sql  = f"update day_money set day_t_money30='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        elif str(day_r_day) == '31':
                            mysql_sql  = f"update day_money set day_t_money31='{day_money}' where "
                            mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                            mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                            mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                            
                            curr.execute(mysql_sql)
                            conn.commit()
                        
                        mysql_sql  = f"update day_money set day_t_total=("
                        mysql_sql += f"day_t_money1+day_t_money2+day_t_money3+day_t_money4+day_t_money5+day_t_money6+day_t_money7+day_t_money8+day_t_money9+day_t_money10+"
                        mysql_sql += f"day_t_money11+day_t_money12+day_t_money13+day_t_money14+day_t_money15+day_t_money16+day_t_money17+day_t_money18+day_t_money19+day_t_money20+"
                        mysql_sql += f"day_t_money21+day_t_money22+day_t_money23+day_t_money24+day_t_money25+day_t_money26+day_t_money27+day_t_money28+day_t_money29+day_t_money30+day_t_money31"
                        mysql_sql += f") "
                        mysql_sql += "where "
                        mysql_sql += f"r_date='{val[3]}'   and r_year='{r_year}'         and r_month='{r_month}'         and r_day='{r_day}'           and " 
                        mysql_sql += f"f_name='{val[0]}'   and a_name='{val[1]}'         and e_name='{g_e_name[0]}'      and t_money='{val[2]}'        and c_t_money='{val[4]}'      and erp_num='{val[5]}' and " 
                        mysql_sql += f"form_num='{val[6]}' and day_r_year='{day_r_year}' and day_r_month='{day_r_month}' and day_money_mark='{val[9]}' and day_money_diff='{val[10]}'" 
                        
                        curr.execute(mysql_sql)
                        conn.commit()
                        

                    print("\n")
                    logging.info('< Msg > update BPM day money is done.')
                    print("------------------------------------------------------------------------------------------------------------------")

                except Exception as e:
                    logging.error("< Error > connect mysql fail : " + str(e))

                finally:
                    curr.close()
                    conn.close()

        except Exception as e:
            logging.error("< Error > connect mysql fail : " + str(e))

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

    











