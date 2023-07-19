#!/usr/bin/python3
# -*- coding: UTF-8 -*-

 # Author   : JasonHung
 # Date     : 20221102
 # Update   : 202230421
 # Function : kedge web cloud platform

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
            self.conn = pymysql.connect(host=kedge_db['host'],port=kedge_db['port'],user=kedge_db['user'],password=kedge_db['pwd'],database=kedge_db['db'],charset=kedge_db['charset'])
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

