#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20221102
# Update   : 20230720
# Function : otsuka factory work time record

#############
#
# variable
#
#############
parm = {'title':'台灣大塚製藥'}

###########################
#
# factory monitor device
#
###########################
m_device = {'S-1'   :'製品倉庫(一)25°C' , 'S-2'   :'製品倉庫(一)30°C' ,
            'S-3'   :'原料庫(一)'       , 'S-4'   :'製品倉庫(三)30° C' ,
            'S-5'   :'原料庫(三)30° B'  , 'S-6'   :'製品倉庫(三)25° C' ,
            'S-7'   :'原料庫(三)30° A'  , 'S-8'   :'製品倉庫(二)' ,
            'S-9'   :'原料庫(二)'       , 'S-10'  :'物料倉庫' ,
            'S-11-1':'樣品室-1(25°C)'   , 'S-11-2':'樣品室-1(冰箱)' ,
            'S-12'  :'樣品室-2(20°C)'   , 'S-13'  :'樣品室-3(30°C)' ,
            'S-14'  :'退貨品倉庫'       , 
            'S-15-1':'安全性實驗箱-1'   , 'S-15-2':'安全性實驗箱-2' ,
            'S-15-3':'安全性實驗箱-3'   , 'S-15-4':'安全性實驗箱-4' ,
            'S-15-5':'安全性實驗箱-5'   , 'S-15-6':'安全性實驗箱-6' ,
            'S-16'  :'中間品室'         , 'S-17'  :'製品三倉-溫度' ,
            'S-18'  :'製品二倉-溫度'    , 'S-19'  :'安定性試驗室'
           }

###################
#
# otsuka_factory
#
###################
otsuka_factory  = {'host':'192.168.1.93'    , 'port':3306 , 'user':'otsuka'     , 'pwd':'OtsukatW168!'         , 'db':'otsuka_factory'  , 'charset':'utf8'}
otsuka_factory2 = {'host':'192.168.1.35'    , 'port':3306 , 'user':'HR2BPM'     , 'pwd':'Otsukatw14001297!'    , 'db':'Agentflow'       , 'charset':'utf8'}
otsuka_factory3 = {'host':'192.168.1.31'    , 'port':3306 , 'user':'Jason_Hung' , 'pwd':'e03vu,4timqotu!'      , 'db':'SHRM'            , 'charset':'utf8'}
otsuka_factory4  = {'host':'192.168.111.13' , 'port':3306 , 'user':'backup'     , 'pwd':'Otsukabackup#123'     , 'db':'tinfar_medicine' , 'charset':'utf8'}

#############
#
# txt path
#
#############
txt_path = {'linux_txt_path':'/var/www/html/medicine/txt/' , 'linux_pdf_path':'/var/www/html/medicine/pdf/nas/backup_record.txt'}

