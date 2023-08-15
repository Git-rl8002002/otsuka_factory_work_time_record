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
            factory_work_station = db.factory_work_station_3()
            a_work_no = db.search_item('a_work_no' , user)
            a_name = db.search_item('a_name' , user)

            return render_template('production_3_work_time_record.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_station=factory_work_station , a_work_no=a_work_no , a_name=a_name)

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
            factory_work_station = db.factory_work_station_1()
            a_work_no = db.search_item('a_work_no' , user)
            a_name = db.search_item('a_name' , user)

            return render_template('production_1_work_time_record.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_station=factory_work_station , a_work_no=a_work_no , a_name=a_name)

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
            a_work_no = db.search_item('a_work_no' , user)
            a_name = db.search_item('a_name' , user)

            return render_template('production_2_work_time_record.html' , user=user , lv=lv , title=title , r_date=r_date , factory_work_station=factory_work_station , a_work_no=a_work_no , a_name=a_name)

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
        user = session['user']
        lv   = session['lv']
        login_code = session['login_code']

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
            return render_template('index.html' , user=user , lv=lv , title=title)

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

        if type(check_account) == tuple:
            
            ### r_time
            r_time = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            
            ### operation record title
            operation_record_title = '登入成功'    
            
            ### session  
            session['user'] = request.form['user']
            
            ### for python3 md5 use method
            m = hashlib.md5()
            m.update(r_time.encode('utf-8'))
            h = m.hexdigest()
            session['login_code'] = h
            session['ip'] = request.remote_addr
            session['lv'] = check_account[0]
            
            ### login record
            db.login_record(session['user'],session['login_code'],r_time,session['ip'])
            
            ### operation record
            db.operation_record(r_time , session['user'] , session['login_code'] , operation_record_title)    

            #################
            # main content
            #################
            #res_data           = db.realtime_modbus_sensor()

            return render_template('index.html' ,  user=session['user'] , lv=session['lv'] , title=title )

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
    
    