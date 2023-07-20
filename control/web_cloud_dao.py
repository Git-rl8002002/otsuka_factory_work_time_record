#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20221102
# Update   : 20230719
# Function : otsuka factory work time record

import pymysql , logging , time , re , requests , json

from control.config import *

########################################################################################################################################
#
# web_cloud_dao
#
########################################################################################################################################
class web_cloud_dao:

    ########
    # log
    ########
    log_format = "%(asctime)s %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S")
    #logging.disable(logging.INFO)

    ################
    # search_item
    ################
    def search_item(self , item , a_user):
        try:
            self.__connect__()
            
            sql = "select {0} from account where a_user='{1}' and a_lv='3' and a_position='生二部' order by no desc".format(item , a_user)
            self.curr.execute(sql)
            self.res = self.curr.fetchone()
            
            return self.res[0]
        
        except Exception as e:
            logging.info('< Error > search_item : ' + str(e))

        finally:
            self.__disconnect__()

    ##############################
    # factory_work_account_list
    ##############################
    def factory_work_account_list(self):
        try:
            self.__connect__()
            
            sql = "select a_user , a_name , a_pwd , a_status , a_work_no from account where a_lv='3' and a_position='生二部' order by no desc"
            self.curr.execute(sql)
            self.res = self.curr.fetchall()
            
            return self.res
        
        except Exception as e:
            logging.info('< Error > factory_work_account_list : ' + str(e))

        finally:
            self.__disconnect__()

    ################
    # add_account
    ################
    def add_account(self , a_date , a_name , a_work_no , a_position , a_status , a_user):
        try:
            self.__connect__()
            
            ### time record
            now_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime()) 
            r_year   = time.strftime("%Y" , time.localtime()) 
            r_month  = time.strftime("%m" , time.localtime()) 
            r_day    = time.strftime("%d" , time.localtime()) 
            r_time   = time.strftime("%H:%M:%S" , time.localtime()) 
            a_pwd    = 'm' + a_work_no
            a_lv     = 3

            sql = "select a_user from account where a_user='{0}'".format(a_user)
            self.curr.execute(sql)
            self.res = self.curr.fetchone()

            if self.res is None:
                
                if a_status == '使用':
                    a_status = 'run'
                else:
                    a_status = 'stop'

                add_sql  = "insert into account(r_year , r_month , r_day , r_time , a_name , a_pwd , a_work_no , a_position , a_status , a_lv , a_user)"
                add_sql += " value ('{0}' , '{1}' ,'{2}' ,'{3}' ,'{4}' ,'{5}' ,'{6}' ,'{7}' ,'{8}' ,'{9}' , '{10}')".format(r_year , r_month , r_day , r_time , a_name , a_pwd , a_work_no , a_position , a_status , a_lv , a_user)

                self.curr.execute(add_sql)
                return True
                
            else:
                return False
        
        except Exception as e:
            logging.info('< Error > add_account : ' + str(e))

        finally:
            self.__disconnect__()

    #########################
    # factory_work_position
    #########################
    def factory_work_position(self):
        try:
            self.__connect__()
            
            sql = "select distinct c_content from work_position order by e_name desc"
            self.curr.execute(sql)
            self.res = self.curr.fetchall()
            
            return self.res
        
        except Exception as e:
            logging.info('< Error > factory_work_position : ' + str(e))

        finally:
            self.__disconnect__()

    #########################
    # factory_work_station
    #########################
    def factory_work_station(self):
        try:
            self.__connect__()
            
            sql = "select distinct c_content from work_station order by e_name desc"
            self.curr.execute(sql)
            self.res = self.curr.fetchall()
            
            return self.res
        
        except Exception as e:
            logging.info('< Error > factory_work_station : ' + str(e))

        finally:
            self.__disconnect__()

    #####################
    # check_login_code
    #####################
    def check_login_code(self,user,login_code):
        
        try:
            self.user = user
            self.login_code = login_code

            self.__connect__()

            sql = "select login_code from login_out_record where a_user='{0}' order by no desc limit 0,1".format(self.user)
            self.curr.execute(sql)
            self.res = self.curr.fetchone()

            if self.res[0] == self.login_code:
                return 'ok'

        except Exception as e:
            logging.info("< Error > check login code : " + str(e))

        finally:
            self.__disconnect__()

    ##########
    # login
    ##########
    def login(self,user,pwd):
        
        try:
            self.user = user
            self.pwd  = pwd

            self.__connect__()

            self.sql = "select a_lv from account where a_user='{0}' and a_pwd='{1}' and a_status='run'".format(self.user , self.pwd)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchone()

            return self.res

        except Exception as e:
            logging.info("< Error > login : " + str(e))

        finally:
            self.__disconnect__()
        
    #################
    # login_record   
    ################# 
    def login_record(self,user,login_code,r_time,ip):
        
        try:
            self.user       = user
            self.login_code = login_code
            self.r_time     = r_time
            self.ip         = ip

            self.__connect__()

            self.sql2 = "insert into login_out_record(a_user,login_code,login_time,login_ip) value('{0}','{1}','{2}','{3}')".format(self.user , self.login_code , self.r_time , self.ip)
            self.curr.execute(self.sql2)

        except Exception as e:
            logging.info("< Error > login record : " + str(e))

        finally:
            self.__disconnect__()
    
    #####################
    # operation_record
    #####################
    def operation_record(self,r_time,user,login_code,item):
        
        try:
            self.r_time     = r_time
            self.user       = user
            self.item       = item
            self.login_code = login_code

            self.__connect__()
            self.sql = "insert into operation_record(r_time,a_user,item,login_code) value('{0}','{1}','{2}','{3}')".format(self.r_time , self.user , self.item , self.login_code)
            self.curr.execute(self.sql)

        except Exception as e:
            logging.info("< Error > operation record : " + str(e))

        finally:
            self.__disconnect__()
    
    ##################
    # logout_record
    ##################
    def logout_record(self,user,login_code,r_time):
        
        try:
            self.user = user
            self.login_code = login_code
            self.r_time = r_time

            self.__connect__()    

            self.sql = "update login_out_record set logout_time='{0}' where login_code='{1}' and a_user='{2}'".format(self.r_time , self.login_code , self.user)
            self.curr.execute(self.sql)

        except Exception as e:
            logging.info("< Error > logout record : " + str(e))

        finally:
            self.__disconnect__()

    ################
    # __connect__ 
    ################
    def __connect__(self):
        
        try:
            self.conn = pymysql.connect(host=otsuka_factory['host'],port=otsuka_factory['port'],user=otsuka_factory['user'],password=otsuka_factory['pwd'],database=otsuka_factory['db'],charset=otsuka_factory['charset'])
            self.curr = self.conn.cursor()
        except Exception as e:
            logging.info("< ERROR > __connect__ " + str(e))
        finally:
            pass

    ###################
    # __disconnect__
    ###################
    def __disconnect__(self):
        
        try:
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            logging.info("< ERROR > __disconnect__ : " + str(e))
        finally:
            pass

