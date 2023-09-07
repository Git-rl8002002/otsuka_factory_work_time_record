#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20221102
# Update   : 20230720
# Function : otsuka factory work time record

from argparse import Namespace
from dataclasses import dataclass
from distutils.log import debug
from email import charset
from hashlib import md5
import hashlib , time , logging , random
#import socketio
from tabnanny import check
from flask import Flask,render_template,request,session,url_for,redirect,escape
from flask_socketio import SocketIO , emit 

from control.config import *
from control.web_cloud_dao import web_cloud_dao 

db = web_cloud_dao()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

########
# log
########
log_format = "%(asctime)s %(message)s"
logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S")

##############
# variables
##############
title  = parm['title']


##############################
# /test
##############################
@app.route("/test")
def test():
    #################
    # main content 
    #################
    res      = db.erp_hr_account_list()

    return render_template('test.html' , hr_account=res)    

##############################
# /update_hr_account
##############################
@app.route("/update_hr_account")
def update_hr_account():
    #################
    # main content 
    #################
    res = db.erp_hr_account_list()

    return render_template('update_hr_account.html' , title=title , hr_account=res)    


##############################
# /reload_menu_account_list
##############################
@app.route("/reload_menu_account_list", methods=['POST','GET'])
def reload_menu_account_list():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '權限管理 -  載入帳號清單'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']

        ### r_time
        r_date = time.strftime("%Y-%m-%d" , time.localtime())
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            factory_work_station      = db.factory_work_station()
            factory_work_account_list = db.factory_work_account_list()

            return render_template('ajax/menu_account_management.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_station=factory_work_station , factory_work_account_list=factory_work_account_list)

        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 

#############################
# /submit_add_account_form
#############################
@app.route("/submit_add_account_form", methods=['POST','GET'])
def submit_add_account_form():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '權限管理 -  建立帳號'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']

        ### r_time
        r_date = time.strftime("%Y-%m-%d" , time.localtime())
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            if request.method == 'POST':
                
                a_date     = request.form['a_date']
                a_work_no  = request.form['a_work_no']
                a_name     = request.form['a_name']
                a_user     = request.form['a_user']
                a_position = request.form['a_position']
                a_status   = request.form['a_status']

                res = db.add_account(a_date , a_name , a_work_no , a_position , a_status , a_user)

                if res:
                    return render_template('ajax/add_account_form.html' , user=user , lv=lv , title=title , r_date=r_date , msg='ok')
                
                return render_template('ajax/add_account_form.html' , user=user , lv=lv , title=title , r_date=r_date , msg='no')

        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 

#######################
# /load_account_form
#######################
@app.route("/load_account_form", methods=['POST','GET'])
def load_account_form():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '權限管理 -  新增帳號表'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']

        ### r_time
        r_date = time.strftime("%Y-%m-%d" , time.localtime())
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            factory_work_position = db.factory_work_position()

            return render_template('ajax/add_account_form.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_position=factory_work_position)

        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 

#############################
# /menu_account_management
#############################
@app.route("/menu_account_management")
def menu_account_management():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '權限管理 - 帳號管理'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']

        ### r_time
        r_date = time.strftime("%Y-%m-%d" , time.localtime())
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            factory_work_station = db.factory_work_station()
            factory_work_account_list = db.factory_work_account_list()

            return render_template('menu_account_management.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_station=factory_work_station , factory_work_account_list=factory_work_account_list)

        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 

###################################
# /prouuction_3_work_time_record
###################################
@app.route("/production_3_work_time_record")
def prouuction_3_work_time_record():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '生產三部 - 液劑工時時間記錄表'    

        ### session 
        user       = session['user']
        lv         = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date = time.strftime("%Y-%m-%d" , time.localtime())
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            factory_work_station = db.factory_work_station_3()
            a_work_no = db.search_item('EmployeeID' , user)
            a_name    = db.search_item('EmployeeName' , user)

            return render_template('production_3_work_time_record.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_station=factory_work_station , a_work_no=a_work_no , a_name=a_name , dep_id=dep_id)

        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 

###################################
# /prouuction_1_work_time_record
###################################
@app.route("/production_1_work_time_record")
def prouuction_1_work_time_record():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '生產一部 - 液劑工時時間記錄表'    

        ### session 
        user       = session['user']
        lv         = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date = time.strftime("%Y-%m-%d" , time.localtime())
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            factory_work_station = db.factory_work_station_1()
            a_work_no = db.search_item('EmployeeID' , user)
            a_name    = db.search_item('EmployeeName' , user)

            return render_template('production_1_work_time_record.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_station=factory_work_station , a_work_no=a_work_no , a_name=a_name , dep_id=dep_id)

        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 


##############################
# /department_no_search_val
##############################
@app.route("/department_no_search_val" , methods=['GET','POST'])
def department_no_search_val():
    
    ### session 
    user = session['user']
    lv   = session['lv']
    login_code = session['login_code']
    dep_id     = session['department_id']

    ### r_time
    r_date  = time.strftime("%Y-%m-%d" , time.localtime())
    r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
    r_year  = time.strftime("%Y" , time.localtime())
    r_month = time.strftime("%m" , time.localtime())

    ### check repeat login
    check_repeat_login = db.check_login_code(user,login_code)
    
    operation_record_title = '部門代號查詢結果'    
    ### operation record
    db.operation_record(r_time,user,login_code,operation_record_title)    

    #################
    # main content 
    #################

    if request.method == 'POST':

        employee_name   = request.form['search_name']
        res = db.department_no_search_val(employee_name)
        
        return render_template('ajax/department_no_search.html' , user=user , lv=lv , title=title , operation_record_title=operation_record_title , r_date=r_date , res=res)
    

##########################
# /department_no_search
##########################
@app.route("/department_no_search")
def department_no_search():
    
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '部門代號查詢'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date  = time.strftime("%Y-%m-%d" , time.localtime())
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            
            return render_template('search_department_id.html' , user=user , lv=lv , title=title , operation_record_title=operation_record_title , r_date=r_date , dep_id=dep_id)
        
        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 


##################################
# /submit_add_check_member_data
##################################
@app.route("/submit_add_check_member_data" , methods=['GET','POST'])
def submit_add_check_member_data():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '生產二部 - 新增人員考核表資料'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date  = time.strftime("%Y-%m-%d" , time.localtime())
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            if request.method == 'POST':
                
                employee_id     = request.form['employee_id']
                employee_name   = request.form['employee_name']
                department_id   = request.form['department_id']
                department_name = request.form['department_name']
                job_title       = request.form['job_title']
                b_date          = request.form['b_date']
                end_date        = request.form['end_date']
                check_year      = request.form['check_year']
                check_month     = request.form['check_month']
                self_num1_1     = request.form['self_num1_1']
                self_num1_2     = request.form['self_num1_2']
                self_num1_3     = request.form['self_num1_3']
                self_num1_4     = request.form['self_num1_4']
                self_num2_1     = request.form['self_num2_1']
                self_num2_2     = request.form['self_num2_2']
                self_num2_3     = request.form['self_num2_3']
                self_num3_1     = request.form['self_num3_1']
                self_num3_2     = request.form['self_num3_2']
                self_num3_3     = request.form['self_num3_3']
                self_num4_1     = request.form['self_num4_1']
                self_num4_2     = request.form['self_num4_2']
                self_num4_3     = request.form['self_num4_3']
                self_num4_4     = request.form['self_num4_4']
                self_num5_1     = request.form['self_num5_1']
                self_num5_2     = request.form['self_num5_2']
                self_num5_3     = request.form['self_num5_3']
                self_num6_1     = request.form['self_num6_1']
                self_num6_2     = request.form['self_num6_2']
                self_num6_3     = request.form['self_num6_3']
                self_total      = request.form['self_total']

                session['employee_id']   = request.form['employee_id']
                session['end_date']      = request.form['end_date']

                db.submit_add_check_member_data(employee_id , employee_name , department_id , department_name , job_title , b_date , end_date , check_year , check_month , self_num1_1 , self_num1_2 , self_num1_3 , self_num1_4 , self_num2_1 , self_num2_2 , self_num2_3 , self_num3_1 , self_num3_2 , self_num3_3 , self_num4_1 , self_num4_2 , self_num4_3 , self_num4_4 , self_num5_1 , self_num5_2 , self_num5_3 , self_num6_1 , self_num6_2 , self_num6_3  , self_total)
            
                #################
                # main content 
                #################
                factory_work_station = db.factory_work_station()
                a_work_no            = session['employee_id']
                a_name               = session['user']
                a_end_date           = db.search_item('end_date' , session['user']) 
                a_check_year         = db.search_member_item('check_year' , user)
                a_check_month        = db.search_member_item('check_month' , user)
                a_job_title          = db.factory_check_form_item(user)
                a_member_check_list  = db.factory_check_form_list()
                res_check_list       = db.check_add_check_member_list(user)

                return render_template('production_2_work_check_record.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_station=factory_work_station , a_work_no=a_work_no , a_name=a_name , a_end_date=a_end_date , dep_id=dep_id , check_year=r_year , check_month=r_month , a_job_title=a_job_title , a_member_check_list=a_member_check_list , res_check_list=res_check_list)
                
        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 

##############################
# /submit_add_check_account
##############################
@app.route("/submit_add_check_account" , methods=['GET','POST'])
def submit_add_check_account():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '生產二部 - 新增人員考核帳號表資料'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date  = time.strftime("%Y-%m-%d" , time.localtime())
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            if request.method == 'POST':
                
                employee_id     = request.form['employee_id']
                employee_name   = request.form['employee_name']
                login_id        = request.form['login_id']
                mobile          = request.form['mobile']
                department_name = request.form['department_name']
                department_code = request.form['department_code']
                company_id      = request.form['company_id']
                end_date        = request.form['end_date']

                res = db.submit_add_check_account(employee_id , employee_name , login_id , mobile , department_name , department_code , company_id , end_date)
                
                if res == 'ok':
                    success_msg = '新增帳密完成.'
                    return render_template('ajax/add_check_member_account.html' , user=user , lv=lv , title=title , r_date=r_date , success_msg=success_msg)
                
                elif res == 'no':
                    error_msg = '姓名已被使用 , 重新輸入 !!!'
                    return render_template('ajax/add_check_member_account.html' , user=user , lv=lv , title=title , r_date=r_date , error_msg=error_msg , employee_id=employee_id , employee_name=employee_name , login_id=login_id , mobile=mobile , end_date=end_date)
                
                elif res == 'no_login_id':
                    error_msg = '帳號已被使用 , 重新輸入 !!!'
                    return render_template('ajax/add_check_member_account.html' , user=user , lv=lv , title=title , r_date=r_date , error_msg=error_msg , employee_id=employee_id , employee_name=employee_name , login_id=login_id , mobile=mobile , end_date=end_date)
        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 


##############################
# /add_check_member_account
##############################
@app.route("/add_check_member_account" , methods=['GET','POST'])
def add_check_member_account():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '生產二部 - 載入新增人員考核帳號表'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date  = time.strftime("%Y-%m-%d" , time.localtime())
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################

            return render_template('ajax/add_check_member_account.html' , user=user , lv=lv , title=title , r_date=r_date)
        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 


#################################
# /load_check_member_self_list
#################################
@app.route("/load_check_member_self_list" , methods=['GET','POST'])
def load_check_member_self_list():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '生產二部 - 載入人員考核表資料'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date  = time.strftime("%Y-%m-%d" , time.localtime())
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            if request.method == 'POST':
            
                employee_id     = request.form['employee_id']
                employee_name   = request.form['employee_name']
                check_year      = request.form['check_year']
                check_month     = request.form['check_month']
                a_job_title     = db.factory_check_form_item(user)

                res = db.load_account_data_form_self_item(employee_id , employee_name , check_year , check_month)

                return render_template('ajax/load_account_data_list.html' , user=user , lv=lv , title=title , r_date=r_date , res=res , a_job_title=a_job_title)
        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 


#######################
# /load_account_data
#######################
@app.route("/load_account_data" , methods=['GET','POST'])
def load_account_data():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '生產二部 - 載入人員考核資料'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date  = time.strftime("%Y-%m-%d" , time.localtime())
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        #if check_repeat_login == 'ok':
            
        ### operation record
        db.operation_record(r_time,user,login_code,operation_record_title)    
        
        #################
        # main content 
        #################
        if request.method == 'POST':
            
            load_user = request.form['user']
            
            a_job_title         = db.factory_check_form_item(user)
            a_member_check_list = db.factory_check_form_list()
            res                 = db.load_account_data_item(load_user)
            check_year          = db.load_account_data_form_item('check_year' , load_user)
            check_month         = db.load_account_data_form_item('check_month' , load_user)

            return render_template('ajax/load_account_data.html' , user=user , lv=lv , title=title , r_date=r_date , res=res , a_job_title=a_job_title , a_member_check_list=a_member_check_list , check_year=check_year , check_month=check_month)
            #return render_template('ajax/load_account_data_none.html')
        
        #else:
        #    return redirect(url_for('logout'))

    return redirect(url_for('login')) 

##################################
# /update_submit_check_member_2
##################################
@app.route("/update_submit_check_member_2" , methods=['GET','POST'])
def update_submit_check_member_2():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '生產二部 - 主管評 人員考核表'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date  = time.strftime("%Y-%m-%d" , time.localtime())
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            if request.method == 'POST':
                
                employee_id     = request.form['employee_id']
                employee_name   = request.form['employee_name']
                department_id   = request.form['department_id']
                department_name = request.form['department_name']
                sir_num1_1      = request.form['sir_num1_1']
                sir_num1_2      = request.form['sir_num1_2']
                sir_num1_3      = request.form['sir_num1_3']
                sir_num1_4      = request.form['sir_num1_4']
                sir_num2_1      = request.form['sir_num2_1']
                sir_num2_2      = request.form['sir_num2_2']
                sir_num2_3      = request.form['sir_num2_3']
                sir_num3_1      = request.form['sir_num3_1']
                sir_num3_2      = request.form['sir_num3_2']
                sir_num3_3      = request.form['sir_num3_3']
                sir_num4_1      = request.form['sir_num4_1']
                sir_num4_2      = request.form['sir_num4_2']
                sir_num4_3      = request.form['sir_num4_3']
                sir_num4_4      = request.form['sir_num4_4']
                sir_num5_1      = request.form['sir_num5_1']
                sir_num5_2      = request.form['sir_num5_2']
                sir_num5_3      = request.form['sir_num5_3']
                sir_num6_1      = request.form['sir_num6_1']
                sir_num6_2      = request.form['sir_num6_2']
                sir_num6_3      = request.form['sir_num6_3']
                sir_num7_1      = request.form['sir_num7_1']
                sir_num7_2      = request.form['sir_num7_2']
                sir_num7_3      = request.form['sir_num7_3']
                sir_num7_4      = request.form['sir_num7_4']
                sir_num8_1      = request.form['sir_num8_1']
                sir_num8_2      = request.form['sir_num8_2']
                sir_num8_3      = request.form['sir_num8_3']
                sir_num8_4      = request.form['sir_num8_4']
                sir_num8_5      = request.form['sir_num8_5']
                comment         = request.form['comment']
                other_total     = request.form['other_total']
                sir_total       = request.form['sir_total']
                other_plus_total = request.form['other_plus_total']
                final_total      = request.form['final_total']
                final_comment    = request.form['final_comment']

                #db.update_submit_check_member_2(employee_id , employee_name , department_id , sir_num1_1 , sir_num1_2 , sir_num1_3 , sir_num1_4 , sir_num2_1 , sir_num2_2 , sir_num2_3 , sir_num3_1 , sir_num3_2 , sir_num3_3 , sir_num4_1 , sir_num4_2 , sir_num4_3 , sir_num4_4 , sir_num5_1 , sir_num5_2 , sir_num5_3 , sir_num6_1 , sir_num6_2 , sir_num6_3 , sir_num7_1 , sir_num7_2 , sir_num7_3 , sir_num7_4 , sir_num8_1 , sir_num8_2 , sir_num8_3 , sir_num8_4 , sir_num8_5 , comment , other_total , sir_total , other_plus_total , final_total , final_comment)
                db.update_submit_check_member_2(employee_id , employee_name , department_id , sir_num1_1 , sir_num1_2)
                
        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 


####################################
# /prouuction_2_work_check_record
####################################
@app.route("/production_2_work_check_record")
def production_2_work_check_record():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '生產二部 - 人員考核表'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date  = time.strftime("%Y-%m-%d" , time.localtime())
        r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year  = time.strftime("%Y" , time.localtime())
        r_month = time.strftime("%m" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            session['employee_id'] = db.search_item('employee_id' , user)
            session['end_date']    = db.search_item('end_date' , user)

            factory_work_station = db.factory_work_station()
            a_work_no            = session['employee_id']
            a_name               = session['user']
            a_end_date           = session['end_date']
            a_check_year         = db.search_member_item('check_year' , user)
            a_check_month        = db.search_member_item('check_month' , user)
            a_job_title          = db.factory_check_form_item(user)
            a_member_check_list  = db.factory_check_form_list()
            res_check_list       = db.check_add_check_member_list(user)
            res_check_self_list  = db.check_add_check_member_self_list()

            return render_template('production_2_work_check_record.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_station=factory_work_station , a_work_no=a_work_no , a_name=a_name , a_end_date=a_end_date , dep_id=dep_id , check_year=r_year , check_month=r_month , a_job_title=a_job_title , a_member_check_list=a_member_check_list , res_check_list=res_check_list , res_check_self_list=res_check_self_list)
            
        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 

###################################
# /prouuction_2_work_time_record
###################################
@app.route("/production_2_work_time_record")
def prouuction_2_work_time_record():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '生產二部 - 液劑工時時間記錄表'    

        ### session 
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_date = time.strftime("%Y-%m-%d" , time.localtime())
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################
            factory_work_station = db.factory_work_station()
            a_work_no = db.search_item('EmployeeID' , user)
            a_name    = db.search_item('EmployeeName' , user)

            return render_template('production_2_work_time_record.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_station=factory_work_station , a_work_no=a_work_no , a_name=a_name , dep_id=dep_id)

        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 

######
# /
######
@app.route("/")
def index():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '主頁'    

        ### session 
        user       = session['user']
        lv         = session['lv']
        login_code = session['login_code']
        dep_id     = session['department_id']

        ### r_time
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)

        if check_repeat_login == 'ok':
            
            ### operation record
            db.operation_record(r_time,user,login_code,operation_record_title)    
            
            #################
            # main content 
            #################

            return render_template('index.html' , user=user , lv=lv , title=title , dep_id=dep_id)

        else:
            return redirect(url_for('logout'))

    return redirect(url_for('login')) 

##########
# /login
##########
@app.route("/login" , methods=['GET','POST'])
def login():
    if request.method == 'POST':
        check_account = db.login(request.form['user'] , request.form['pwd'])
        dep_id = db.dep_id(request.form['user'] , request.form['pwd'])

        if check_account is not None:
            
            ### r_time
            r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            
            ### operation record title
            operation_record_title = '登入成功'    
            
            ### session  
            #session['user'] = request.form['user']
            session['user'] = check_account[0]
            
            ### for python3 md5 use method
            m = hashlib.md5()
            m.update(r_time.encode('utf-8'))
            h = m.hexdigest()
            session['login_code'] = h
            session['ip'] = request.remote_addr
            session['lv'] = 3
            session['department_id'] = dep_id
            
            ### login record
            db.login_record(session['user'],session['login_code'],r_time,session['ip'])
            
            ### operation record
            db.operation_record(r_time , session['user'] , session['login_code'] , operation_record_title)    

            #################
            # main content
            #################
            #res_data           = db.realtime_modbus_sensor()

            return render_template('index.html' ,  user=session['user'] , lv=session['lv'] , title=title , dep_id=session['department_id'] )

        else:
            res_data = "登入失敗，帳密有錯，重新輸入 !!!"
            return render_template('login.html' , login_msg=res_data , title=title)

    else:
        return render_template('login.html' , title=title)

#############
# /logout2 
#############
@app.route("/logout2",methods=['POST','GET'])
def logout2():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '登出成功'

        ### session 
        user = session['user']

        ### r_time
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        if request.method == 'GET':
            ### logout record
            try:
                db.logout_record(session['user'] , session['login_code'] , r_time)
            except Exception as e:
                logging.info("< Error > logout record : " + str(e))
            finally:
                pass
            
            ### operation record
            db.operation_record(r_time , user , session['login_code'] , operation_record_title)    

            ### clean up session param
            session.pop('user',None)
            session.pop('login_code',None)
            session.pop('ip',None)
            session.pop('lv',None)
            session.pop('department_id',None)

    return redirect(url_for('index'))


###########
# /logout 
###########
@app.route("/logout")
def logout():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '登出成功'

        ### session 
        user = session['user']

        ### r_time
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
    
        ### logout record
        try:
            db.logout_record(session['user'] , session['login_code'] , r_time)
        except Exception as e:
            logging.info("< Error > logout record : " + str(e))
        finally:
            pass
        
        ### operation record
        db.operation_record(r_time , user , session['login_code'] , operation_record_title)    

        ### clean up session param
        session.pop('user',None)
        session.pop('login_code',None)
        session.pop('ip',None)
        session.pop('lv',None)

    return redirect(url_for('index'))

#####################
# /account_manager
#####################
@app.route("/account_manager",methods=['POST','GET'])
def account_manager():
    if 'user' in session:
        
        ### operation record title
        operation_record_title = '帳號管理'    

        ### session
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']

        ### r_time
        r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())

        ### check repeat login
        check_repeat_login = db.check_login_code(user,login_code)
        
        if check_repeat_login == 'ok':

            ### operation record
            db.operation_record(r_time , user , login_code , operation_record_title)    

            #################
            # main content
            #################
            if request.method == 'POST':
                
                del_no = request.form['del_no']
                res = db.del_menu_money_record(user , del_no)
                
                if res == 'ok':
                    data = db.menu_money_record(user)
                    return render_template('ajax/reload_menu_money_record.html' , msg=data , user=user , lv=lv , title=title)    

        else:
            return redirect(url_for('logout'))
    
    return redirect(url_for('login'))

########################################################################################################################################
#
# start
#
########################################################################################################################################
if __name__ == "__main__":
    
    ##########
    # Flask
    ##########
    app.run(host="0.0.0.0" , port=9095 , debug=True)
    
    