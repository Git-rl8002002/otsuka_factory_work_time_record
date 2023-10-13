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

######################
#
# insert into mysql
#
######################
'''
try:
    file  = '20230919工廠在職.xlsx'
    sheet = 'new sheet'
    df = pd.read_excel(file , sheet_name=sheet)

    try:
        conn = pymysql.connect(host=otsuka_factory['host'],port=otsuka_factory['port'],user=otsuka_factory['user'],password=otsuka_factory['pwd'],database=otsuka_factory['db'],charset=otsuka_factory['charset'])
        curr = conn.cursor()

        for index , row in df.iterrows():
            
            s_sql = f"select e_name from factory_hr_a where e_name='{row['中文姓名']}'"
            curr.execute(s_sql)
            res = curr.fetchone()

            if res is None:
                
                val1 = str(row['流程組別']).strip()
                val2 = str(row['單位代碼']).strip()
                val3 = str(row['單位名稱']).strip()
                val4 = str(row['員工編號']).strip()
                val5 = str(row['中文姓名']).strip()
                val6 = str(row['登入帳號']).strip()
                val7 = str(row['性別']).strip()
                val8 = str(row['職稱中文']).strip()
                val9 = str(row['到職日期']).strip()
                val10 = str(row['電子信箱']).strip()
                
                a_sql  = f"insert into factory_hr_a"
                a_sql += f"(d_name , d_id , d_name2 , e_id , e_name , l_account , sex , j_name , j_date , email)"
                a_sql += f"value("
                a_sql += f"'{val1}' , '{val2}' , '{val3}' , '{val4}' , '{val5}' , '{val6}' , '{val7}' , '{val8}' , '{val9}' , '{val10}')"
                curr.execute(a_sql)
            else:
                logging.info(f"< ERROR > {row['流程組別'] } , {row['中文姓名']} , 已經存在資料庫 !")
            
        conn.commit()
        
        logging.info('data insert successfully.')

    except Exception as e:
        logging.info("< ERROR > connect mysql fail : " + str(e))

    finally:
        curr.close()
        conn.close()

except FileExistsError as e:
    logging.info('< ERROR > : ' + str(e))

finally:
    pass
'''








