#!loginusr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20221102
# Update   : 20230720
# Function : otsuka factory work time record

import pymysql , logging , time , re , requests , json , pymssql , pyodbc

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

    ##################
    # bpm_account_list
    ##################
    def bpm_account_list(self):
        try:
            self.__connect_mssql__()
        except Exception as e:
            logging.info('< Error > bpm_account_list : ' + str(e))
        finally:
            pass


    ########################
    # erp_hr_account_list
    ########################
    def erp_hr_account_list(self):
        try:
            ######################
            #
            # select from MsSQL
            #
            ######################
            conn_str        = f"DRIVER={{SQL Server}};SERVER={otsuka_factory3['host']};DATABASE={otsuka_factory3['db']};UID={otsuka_factory3['user']};PWD={otsuka_factory3['pwd']}"  
            self.conn_mssql = pyodbc.connect(conn_str)
            self.curr_mssql = self.conn_mssql.cursor()
            self.sql        = f"SELECT a.EMPID AS EmployeeID, CASE (isnull(a.HECNAME, '')) WHEN '' THEN '' ELSE a.HECNAME END AS EmployeeName, CASE (isnull(a.HEENAME, '')) WHEN '' THEN '' ELSE a.HEENAME END AS EmployeeEnglishName, CASE (isnull(a.LOGIN_ID, '')) WHEN '' THEN '' ELSE a.LOGIN_ID END AS LoginID, a.CPNYID AS CompanyID, a.DEPT_NO AS DepartmentID, '' AS IdentityID, a.SEX, CASE (isnull(a.EMAIL, '')) WHEN '' THEN '' ELSE a.EMAIL END AS Email, CASE (isnull(a.MOBILNO, '')) WHEN '' THEN '' ELSE a.MOBILNO END AS Mobile, SUBSTRING(a.BIRTHDAY, 1, 4) + '/' + SUBSTRING(a.BIRTHDAY, 5, 2) + '/' + SUBSTRING(a.BIRTHDAY, 5, 2) AS Birthday, a.POSSIE AS JobTitleCode, CASE (isnull(b.POS_NAME, '')) WHEN '' THEN '' ELSE b.POS_NAME END AS JobTitleName, CASE (isnull(a.GRADE, '')) WHEN '' THEN '' ELSE a.GRADE END AS JobGrade, CASE (isnull(a.RANK, '')) WHEN '' THEN '' ELSE a.RANK END AS JobRank, '' AS JobCode, '' AS JobType, SUBSTRING(a.INADATE, 1, 4) + '/' + SUBSTRING(a.INADATE, 5, 2) + '/' + SUBSTRING(a.INADATE, 5, 2) AS EnterDate, CASE (isnull(a.PLACE, '')) WHEN '' THEN '' ELSE a.PLACE END AS WorkPlace, '' AS AreaCode, CASE (isnull(a.MOBILNO, '')) WHEN '' THEN '' ELSE a.MOBILNO END AS HomePhone, CASE (isnull(a.EXT, '')) WHEN '' THEN '' ELSE a.EXT END AS OfficePhone, CASE (isnull(a.COMADDR, '')) WHEN '' THEN '' ELSE a.COMADDR END AS Address, '' AS Synopsis FROM              dbo.HRUSER AS a LEFT OUTER JOIN dbo.POSITION AS b ON a.POSSIE = b.POSSIE" 
            self.curr_mssql.execute(self.sql)
            self.res        = self.curr_mssql.fetchall()

            self.__connect__()
            for val in self.res:
                
                s_dep_code_sql = f"select DEP_CODE , DEP_SHORT_NAME from HRUSER_DEPT_BAS where DEP_NO='{val[5]}'"
                self.curr_mssql.execute(s_dep_code_sql)
                res_dep_code = self.curr_mssql.fetchall()

                for dep_val in res_dep_code:

                    ###########################
                    #
                    # check MsSQL hr account 
                    #
                    ###########################
                    s_sql = f"select employee_name from hr_a where employee_name='{val[1]}'"
                    self.curr.execute(s_sql)
                    s_r = self.curr.fetchone()

                    if s_r is None:
                        ######################
                        #
                        # insert into MySQL
                        #
                        ######################
                        sql =  f"insert into hr_a(employee_id , employee_name , employee_eng_name , login_id , company_id , department_id , identity_id , sex , email , mobile , birthday , job_title_code , job_title_name , job_grade , job_rank , job_code , job_type , end_date , work_place , area_code , home_phone , office_phone , addresses , department_code , department_name) "
                        sql += f"value('{val[0]}','{val[1]}','{val[2]}','{val[3]}','{val[4]}','{val[5]}','{val[6]}','{val[7]}','{val[8]}','{val[9]}','{val[10]}','{val[11]}','{val[12]}','{val[13]}','{val[14]}','{val[15]}','{val[16]}','{val[17]}','{val[18]}','{val[19]}','{val[20]}','{val[21]}','{val[22]}','{dep_val[0]}','{dep_val[1]}')"
                        self.curr.execute(sql)
                        self.conn.commit()
                    else:
                        logging.info(f"{s_r[0]} 已存在.")
            
            self.__disconnect__()

            return self.res
        
        except Exception as e:
            logging.info('< Error > erp_hr_account_list : ' + str(e))

        finally:
            self.curr_mssql.close()
            self.conn_mssql.close()

    #############################
    # department_no_search_val
    #############################
    def department_no_search_val(self , employee_name):
        try:
            
            conn_str        = f"DRIVER={{SQL Server}};SERVER={otsuka_factory3['host']};DATABASE={otsuka_factory3['db']};UID={otsuka_factory3['user']};PWD={otsuka_factory3['pwd']}"  
            self.conn_mssql = pyodbc.connect(conn_str)
            self.curr_mssql = self.conn_mssql.cursor()
            self.sql        = f"SELECT B.DEP_CODE FROM HR_Employee A , HRUSER_DEPT_BAS B WHERE A.DepartmentID = B.DEP_NO AND A.EmployeeName='{employee_name}'"
            self.curr_mssql.execute(self.sql)
            
            self.res        = self.curr_mssql.fetchone()
            self.curr_mssql.commit()
            
            return self.res[0]
        
            self.curr_mssql.close()
            self.conn_mssql.close()
            
        except Exception as e:
            logging.info('< Error > department_no_search_vals : ' + str(e))

        finally:
            pass
            #self.curr_mssql.close()
            #self.conn_mssql.close()

    ################
    # search_item
    ################
    def search_item(self , item , a_user):
        try:
            
            '''
            conn_str        = f"DRIVER={{SQL Server}};SERVER={otsuka_factory2['host']};DATABASE={otsuka_factory2['db']};UID={otsuka_factory2['user']};PWD={otsuka_factory2['pwd']}"  
            self.conn_mssql = pyodbc.connect(conn_str)
            self.curr_mssql = self.conn_mssql.cursor()
            self.sql        = f"select {item} from T_HR_Employee where EmployeeName='{a_user}'"
            self.curr_mssql.execute(self.sql)
            self.res        = self.curr_mssql.fetchone()

            return self.res[0]
            '''
        
            
            self.__connect__()
            
            sql = f"select {item} from hr_a where employee_name='{a_user}'"
            self.curr.execute(sql)
            self.res = self.curr.fetchone()
            
            return self.res[0]
        
        except Exception as e:
            logging.info('< Error > search_item : ' + str(e))

        finally:
            self.__disconnect__()
            #self.curr_mssql.close()
            #self.conn_mssql.close()

    #############################
    # submit_add_check_account
    #############################
    def submit_add_check_account(self , employee_id , employee_name , login_id , mobile , department_name , department_code , company_id , end_date):
        try:
            self.__connect__()
            
            sql = f"select employee_name from hr_a where employee_name='{employee_name}'"
            self.curr.execute(sql)
            self.res = self.curr.fetchone()

            if self.res is None:
                
                sql3 = f"select employee_name from hr_a where login_id='{login_id}'"
                self.curr.execute(sql3)
                self.res3 = self.curr.fetchone()

                if self.res3 is None:
                
                    sql2 = f"insert into hr_a(employee_id , employee_name , login_id , mobile , department_name , department_code , company_id , end_date) value('{employee_id}' , '{employee_name}' , '{login_id}' , '{mobile}' , '{department_name}' , '{department_code}' , '{company_id}' , '{end_date}')" 
                    self.curr.execute(sql2)

                    res_a = 'ok'
                    return res_a
                
                else:

                    res_a = 'no_login_id'
                    return res_a    
            
            else:

                res_a = 'no'
                return res_a
        
        except Exception as e:
            logging.info('< Error > submit_add_check_account : ' + str(e))

        finally:
            self.__disconnect__()

    ###########################
    # load_account_data_item
    ###########################
    def load_account_data_item(self , user):
        try:
            self.__connect__()
            
            sql = f"select employee_id , employee_name , end_date from hr_a where employee_name='{user}'"
            self.curr.execute(sql)
            self.res = self.curr.fetchall()
            
            return self.res
        
        except Exception as e:
            logging.info('< Error > load_account_data_item : ' + str(e))

        finally:
            self.__disconnect__()

    ############################
    # factory_check_form_item
    ############################
    def factory_check_form_item(self , user):
        try:
            self.__connect__()
            
            sql = f"select job_title_name from hr_a where employee_name='{user}'"
            self.curr.execute(sql)
            self.res = self.curr.fetchone()
            
            return self.res[0]
        
        except Exception as e:
            logging.info('< Error > factory_check_form_item : ' + str(e))

        finally:
            self.__disconnect__()

    ############################
    # factory_check_form_list
    ############################
    def factory_check_form_list(self):
        try:
            self.__connect__()
            
            sql = "select employee_name from hr_a where department_code like '1B%' and job_title_name != '經理' order by no desc"
            self.curr.execute(sql)
            self.res = self.curr.fetchall()
            
            return self.res
        
        except Exception as e:
            logging.info('< Error > factory_check_form_list : ' + str(e))

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


    ###########################
    # factory_work_station_3
    ###########################
    def factory_work_station_3(self):
        try:
            self.__connect__()
            
            sql = "select distinct c_content from work_station_3 order by e_name desc"
            self.curr.execute(sql)
            self.res = self.curr.fetchall()
            
            return self.res
        
        except Exception as e:
            logging.info('< Error > factory_work_station_3 : ' + str(e))

        finally:
            self.__disconnect__()

    ###########################
    # factory_work_station_1
    ###########################
    def factory_work_station_1(self):
        try:
            self.__connect__()
            
            sql = "select distinct c_content from work_station_1 order by e_name desc"
            self.curr.execute(sql)
            self.res = self.curr.fetchall()
            
            return self.res
        
        except Exception as e:
            logging.info('< Error > factory_work_statio_1 : ' + str(e))

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

    ###########
    # dep_id
    ###########
    def dep_id(self,user,pwd):
        
        try:
            self.login_id = user
            self.mobile   = pwd
            '''
            conn_str = f"DRIVER={{SQL Server}};SERVER={otsuka_factory2['host']};DATABASE={otsuka_factory2['db']};UID={otsuka_factory2['user']};PWD={otsuka_factory2['pwd']}"  
            self.conn_mssql = pyodbc.connect(conn_str)
            self.curr_mssql = self.conn_mssql.cursor()
            self.sql = f"select DepartmentID from T_HR_Employee where loginID='{self.login_id}' and Mobile='{self.mobile}'"
            self.curr_mssql.execute(self.sql)
            self.res = self.curr_mssql.fetchone()

            self.sql2 = f"select UpperDepartmentID from T_HR_Department where DepartmentID='{self.res[0]}'"
            self.curr_mssql.execute(self.sql2)
            self.res2 = self.curr_mssql.fetchone()

            return self.res2
            '''
            
            self.__connect__()

            self.sql = "select department_code from hr_a where login_id='{0}' and mobile='{1}'".format(self.login_id , self.mobile)
            self.curr.execute(self.sql)
            self.res = self.curr.fetchone()
            self.dep_code = self.res[0]
            self.r_dep_code = self.dep_code[0:2]

            return self.r_dep_code

        except Exception as e:
            logging.info("< Error > dep_id : " + str(e))

        finally:
            self.__disconnect__()
            #self.curr_mssql.close()
            #self.conn_mssql.close()

    ##########
    # login
    ##########
    def login(self,user,pwd):
        
        try:
            self.login_id = user
            self.mobile   = pwd

            #########################
            #
            # connect MsSQL - SHRM
            #
            #########################
            '''
            conn_str = f"DRIVER={{SQL Server}};SERVER={otsuka_factory2['host']};DATABASE={otsuka_factory2['db']};UID={otsuka_factory2['user']};PWD={otsuka_factory2['pwd']}"  
            self.conn_mssql = pyodbc.connect(conn_str)
            self.curr_mssql = self.conn_mssql.cursor()
            self.sql = f"select EmployeeName from T_HR_Employee where loginID='{self.login_id}' and Mobile='{self.mobile}'"
            self.curr_mssql.execute(self.sql)
            self.res = self.curr_mssql.fetchone()

            return self.res
            '''
            
            #########################
            #
            # connect MySQL - hr_a
            #
            #########################
            self.__connect__()

            self.sql = f"select Employee_name from hr_a where login_id='{self.login_id}' and mobile='{self.mobile}'"
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

    ######################
    # __connect_mssql__ 
    ######################
    def __connect_mssql__(self):
        
        try:
            conn_str = f"DRIVER={{SQL Server}};SERVER={otsuka_factory2['host']};DATABASE={otsuka_factory2['db']};UID={otsuka_factory2['user']};PWD={otsuka_factory2['pwd']}"  
            self.conn_mssql = pyodbc.connect(conn_str)
            self.curr_mssql = self.conn_mssql.cursor()
            
        except Exception as e:
            logging.info("< ERROR > __connect_mssql__ " + str(e))

        finally:
            self.curr.close()
            self.conn_mssql.close()
    
    #########################
    # __disconnect_mssql__ 
    #########################
    def __disconnect_mssql__(self):
        
        try:
            self.curr_mssql.close()
            self.conn_mssql.close()
            
        except Exception as e:
            logging.info("< ERROR > __disconnect_mssql__ " + str(e))

        finally:
            pass

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

