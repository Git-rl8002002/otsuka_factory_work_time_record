#!/usr/bin/python3
# -*- coding: UTF-8 -*-

 # Author   : JasonHung
 # Date     : 20221102
 # Update   : 202230421
 # Function : kedge web cloud platform

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
socketio = SocketIO(app)  

########
# log
########
log_format = "%(asctime)s %(message)s"
logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%Y-%m-%d %H:%M:%S")

##############
# variables
##############
title  = parm['title']

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
# socketIO - WebSocket - Flask-SocketIO 
#
########################################################################################################################################

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    logging.info('Client disconnected')

'''
@socketio.on('connect', namespace='/')
def test_connect():
    while True:
        socketio.sleep(5)
        t = random_int_list(1, 100, 10)
        emit('server_response',{'data': t},namespace='/')
 
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
  
@socketio.on('disconnect', namespace='/')  
def test_disconnect():  
    logging.info('Client disconnected')  
'''


########################################################################################################################################
#
# start
#
########################################################################################################################################
if __name__ == "__main__":
    
    ##########
    # Flask
    ##########
    #app.run(host="0.0.0.0" , port=8080 , debug=True)
    
    ###################
    # Flask-SocketIO
    ###################
    socketio.run(app , host="0.0.0.0" , port=9095 , debug=True)