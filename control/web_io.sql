/*****************************************************************
*
* Author   : JasonHung
* Date     : 20221102
* Update   : 20230908
* Function : otsuka for factory work time system
*
******************************************************************/

/****************************** 
 *
 * database : otsuka_factory
 *
 ******************************/
create database otsuka_factory DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
use otsuka_factory;

/************************* 
 *
 * card_reader_20230913
 *
 *************************/
create table card_reader_20230913(
no int not null primary key AUTO_INCREMENT,
r_date date null,
r_time time null,
p_id varchar(30) null,
p_name varchar(30) null,
e_id varchar(30) null,
e_name varchar(30) null,
position varchar(30) null,
c_action varchar(30) null,
c_id varchar(30) null,
c_remark varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/************************* 
 *
 * card_reader_position
 *
 *************************/
create table card_reader_p(
no int not null primary key AUTO_INCREMENT,
p_id int null,
p_name varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/***************** 
 *
 * work_time
 *
 *****************/
create table work_time(
no int not null primary key AUTO_INCREMENT,
e_id int null,
e_name varchar(50) null,
dep_id varchar(10) null,
b_date varchar(30) null , 
r_year varchar(10) null , 
r_month varchar(10) null , 
r_day varchar(10) null , 
total_time varchar(50) null,
normal_time varchar(50) null,
over_time varchar(50) null,
availability_time varchar(50) null,

w_s_1 varchar(100) null,
w_s_1_product varchar(100) null,
w_s_1_num varchar(100) null,
w_s_1_normal_time varchar(100) null,
w_s_1_over_time varchar(100) null,
w_s_1_avail_time varchar(100) null,
w_s_1_remark varchar(100) null,

w_s_2 varchar(100) null,
w_s_2_product varchar(100) null,
w_s_2_num varchar(100) null,
w_s_2_normal_time varchar(100) null,
w_s_2_over_time varchar(100) null,
w_s_2_avail_time varchar(100) null,
w_s_2_remark varchar(100) null,

w_s_3 varchar(100) null,
w_s_3_product varchar(100) null,
w_s_3_num varchar(100) null,
w_s_3_normal_time varchar(100) null,
w_s_3_over_time varchar(100) null,
w_s_3_avail_time varchar(100) null,
w_s_3_remark varchar(100) null,

w_s_4 varchar(100) null,
w_s_4_product varchar(100) null,
w_s_4_num varchar(100) null,
w_s_4_normal_time varchar(100) null,
w_s_4_over_time varchar(100) null,
w_s_4_avail_time varchar(100) null,
w_s_4_remark varchar(100) null,

w_s_5 varchar(100) null,
w_s_5_product varchar(100) null,
w_s_5_num varchar(100) null,
w_s_5_normal_time varchar(100) null,
w_s_5_over_time varchar(100) null,
w_s_5_avail_time varchar(100) null,
w_s_5_remark varchar(100) null,

w_s_6 varchar(100) null,
w_s_6_product varchar(100) null,
w_s_6_num varchar(100) null,
w_s_6_normal_time varchar(100) null,
w_s_6_over_time varchar(100) null,
w_s_6_avail_time varchar(100) null,
w_s_6_remark varchar(100) null,

w_s_7 varchar(100) null,
w_s_7_product varchar(100) null,
w_s_7_num varchar(100) null,
w_s_7_normal_time varchar(100) null,
w_s_7_over_time varchar(100) null,
w_s_7_avail_time varchar(100) null,
w_s_7_remark varchar(100) null,

w_s_8 varchar(100) null,
w_s_8_product varchar(100) null,
w_s_8_num varchar(100) null,
w_s_8_normal_time varchar(100) null,
w_s_8_over_time varchar(100) null,
w_s_8_avail_time varchar(100) null,
w_s_8_remark varchar(100) null,

w_s_9 varchar(100) null,
w_s_9_product varchar(100) null,
w_s_9_num varchar(100) null,
w_s_9_normal_time varchar(100) null,
w_s_9_over_time varchar(100) null,
w_s_9_avail_time varchar(100) null,
w_s_9_remark varchar(100) null,

w_s_10 varchar(100) null,
w_s_10_product varchar(100) null,
w_s_10_num varchar(100) null,
w_s_10_normal_time varchar(100) null,
w_s_10_over_time varchar(100) null,
w_s_10_avail_time varchar(100) null,
w_s_10_remark varchar(100) null,

w_s_11 varchar(100) null,
w_s_11_product varchar(100) null,
w_s_11_num varchar(100) null,
w_s_11_normal_time varchar(100) null,
w_s_11_over_time varchar(100) null,
w_s_11_avail_time varchar(100) null,
w_s_11_remark varchar(100) null,

w_s_12 varchar(100) null,
w_s_12_product varchar(100) null,
w_s_12_num varchar(100) null,
w_s_12_normal_time varchar(100) null,
w_s_12_over_time varchar(100) null,
w_s_12_avail_time varchar(100) null,
w_s_12_remark varchar(100) null

)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/***************** 
 *
 * check_member
 *
 *****************/
create table check_member(
no int not null primary key AUTO_INCREMENT,
employee_id int null,
employee_name varchar(50) null,
department_id varchar(50) null,
department_name varchar(50) null,
b_date varchar(10) null , 
end_date varchar(10) null,
check_year varchar(10) null,
check_month varchar(10) null,
self_item_1_1 int null,
self_item_1_2 int null,
self_item_1_3 int null,
self_item_1_4 int null,
other_item_1_1 int null,
other_item_1_2 int null,
other_item_1_3 int null,
other_item_1_4 int null,
sir_item_1_1 int null,
sir_item_1_2 int null,
sir_item_1_3 int null,
sir_item_1_4 int null,

self_item_2_1 int null,
self_item_2_2 int null,
self_item_2_3 int null,
other_item_2_1 int null,
other_item_2_2 int null,
other_item_2_3 int null,
sir_item_2_1 int null,
sir_item_2_2 int null,
sir_item_2_3 int null,

self_item_3_1 int null,
self_item_3_2 int null,
self_item_3_3 int null,
other_item_3_1 int null,
other_item_3_2 int null,
other_item_3_3 int null,
sir_item_3_1 int null,
sir_item_3_2 int null,
sir_item_3_3 int null,

self_item_4_1 int null,
self_item_4_2 int null,
self_item_4_3 int null,
self_item_4_4 int null,
other_item_4_1 int null,
other_item_4_2 int null,
other_item_4_3 int null,
other_item_4_4 int null,
sir_item_4_1 int null,
sir_item_4_2 int null,
sir_item_4_3 int null,
sir_item_4_4 int null,

self_item_5_1 int null,
self_item_5_2 int null,
self_item_5_3 int null,
other_item_5_1 int null,
other_item_5_2 int null,
other_item_5_3 int null,
sir_item_5_1 int null,
sir_item_5_2 int null,
sir_item_5_3 int null,

self_item_6_1 int null,
self_item_6_2 int null,
self_item_6_3 int null,
other_item_6_1 int null,
other_item_6_2 int null,
other_item_6_3 int null,
sir_item_6_1 int null,
sir_item_6_2 int null,
sir_item_6_3 int null,

sir_item_7_1 int null,
sir_item_7_2 int null,
sir_item_7_3 int null,
sir_item_7_4 int null,

sir_item_8_1 int null,
sir_item_8_2 int null,
sir_item_8_3 int null,
sir_item_8_4 int null,
sir_item_8_5 int null,

comment text null,

self_total int null,
other_total int null,
sir_total int null,
other_plus_total int null,
final_total int null,
final_comment text null,

self_check varchar(5) null,
other_check varchar(5) null,
sir_check varchar(5) null

)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/***************** 
 *
 * hr_a
 *
 *****************/
create table hr_a(
no int not null primary key AUTO_INCREMENT,
employee_id int null,
employee_name varchar(50) null,
employee_eng_name varchar(50) null,
login_id varchar(50) null,
company_id varchar(50) null,
department_id varchar(50) null,
department_code varchar(10) null,
department_name varchar(30) null,
identity_id varchar(50) null,
sex varchar(5) null,
email varchar(300) null,
mobile varchar(50) null,
birthday varchar(50) null,
job_title_code varchar(50) null,
job_title_name varchar(50) null,
job_grade varchar(50) null,
job_rank varchar(50) null,
job_code varchar(50) null,
job_type varchar(50) null,
end_date varchar(50) null,
work_place varchar(50) null,
area_code varchar(50) null,
home_phone varchar(50) null,
office_phone varchar(50) null,
addresses varchar(300) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/***************** 
 *
 * work_station_3
 *
 *****************/
create table work_station_3(
no int not null primary key AUTO_INCREMENT,
e_name varchar(10) null,
c_content varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into work_station_3 (e_name , c_content) VALUES('W','W-倉庫相關');
insert into work_station_3 (e_name , c_content) VALUES('W1','W1-領料');
insert into work_station_3 (e_name , c_content) VALUES('W2','W2-稱料');
insert into work_station_3 (e_name , c_content) VALUES('W3','W3-退料');

insert into work_station_3 (e_name , c_content) VALUES('Y','Y-設備相關');
insert into work_station_3 (e_name , c_content) VALUES('Y1','Y1-裝機');
insert into work_station_3 (e_name , c_content) VALUES('Y2','Y2-調機');
insert into work_station_3 (e_name , c_content) VALUES('Y3','Y3-試機');

insert into work_station_3 (e_name , c_content) VALUES('K','故障相關');
insert into work_station_3 (e_name , c_content) VALUES('K1','K1-設備故障');
insert into work_station_3 (e_name , c_content) VALUES('K2','K2-支援系統異常');

insert into work_station_3 (e_name , c_content) VALUES('V','V1-機器拆卸 / 清機');

insert into work_station_3 (e_name , c_content) VALUES('F','F-充填作業');

insert into work_station_3 (e_name , c_content) VALUES('ST','ST-滅菌作業');

insert into work_station_3 (e_name , c_content) VALUES('Q','Q-檢視作業');

insert into work_station_3 (e_name , c_content) VALUES('T','T-教育訓練');
insert into work_station_3 (e_name , c_content) VALUES('T1','T1-部內教育訓練');
insert into work_station_3 (e_name , c_content) VALUES('T2','T2-部外教育訓練');

insert into work_station_3 (e_name , c_content) VALUES('L','L-其他');
insert into work_station_3 (e_name , c_content) VALUES('L1','L1-其它 - 5S活動');
insert into work_station_3 (e_name , c_content) VALUES('L2','L2-其它 - 參觀活動');
insert into work_station_3 (e_name , c_content) VALUES('L3','L3-其它 - 部內會議');
insert into work_station_3 (e_name , c_content) VALUES('L4','L4-其它 - 部外會議');

insert into work_station_3 (e_name , c_content) VALUES('U','U-休息');

insert into work_station_3 (e_name , c_content) VALUES('A','A-調製相關');
insert into work_station_3 (e_name , c_content) VALUES('A1','A1-預備工作');
insert into work_station_3 (e_name , c_content) VALUES('A2','A2-調製過程');

insert into work_station_3 (e_name , c_content) VALUES('PW','PW-制水 , 鹽滅');

insert into work_station_3 (e_name , c_content) VALUES('M','M-蓋印 / 打印 / 貼標');

insert into work_station_3 (e_name , c_content) VALUES('P','P-包裝作業');

insert into work_station_3 (e_name , c_content) VALUES('RE','RE-再檢作業');

insert into work_station_3 (e_name , c_content) VALUES('S','S-停工待料');

insert into work_station_3 (e_name , c_content) VALUES('R','R-支援工作');

insert into work_station_3 (e_name , c_content) VALUES('D','D-請假');

insert into work_station_3 (e_name , c_content) VALUES('J','J-確效驗證 , 校正');

insert into work_station_3 (e_name , c_content) VALUES('C','C-環境清潔');

/***************** 
 *
 * work_station_1
 *
 *****************/
create table work_station_1(
no int not null primary key AUTO_INCREMENT,
e_name varchar(10) null,
c_content varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into work_station_3 (e_name , c_content) VALUES('W','W-倉庫相關');
insert into work_station_1 (e_name , c_content) VALUES('W1','W1-領料');
insert into work_station_1 (e_name , c_content) VALUES('W2','W2-稱料');
insert into work_station_1 (e_name , c_content) VALUES('W3','W3-退料');

insert into work_station_1 (e_name , c_content) VALUES('Y','Y-設備相關');
insert into work_station_1 (e_name , c_content) VALUES('Y1','Y1-裝機');
insert into work_station_1 (e_name , c_content) VALUES('Y2','Y2-調機');
insert into work_station_1 (e_name , c_content) VALUES('Y3','Y3-試機');

insert into work_station_1 (e_name , c_content) VALUES('K','故障相關');
insert into work_station_1 (e_name , c_content) VALUES('K1','K1-設備故障');
insert into work_station_1 (e_name , c_content) VALUES('K2','K2-支援系統異常');

insert into work_station_1 (e_name , c_content) VALUES('V','V1-機器拆卸 / 清機');

insert into work_station_1 (e_name , c_content) VALUES('F','F-充填作業');

insert into work_station_1 (e_name , c_content) VALUES('ST','ST-滅菌作業');

insert into work_station_1 (e_name , c_content) VALUES('Q','Q-檢視作業');

insert into work_station_1 (e_name , c_content) VALUES('T','T-教育訓練');
insert into work_station_1 (e_name , c_content) VALUES('T1','T1-部內教育訓練');
insert into work_station_1 (e_name , c_content) VALUES('T2','T2-部外教育訓練');

insert into work_station_1 (e_name , c_content) VALUES('L','L-其他');
insert into work_station_1 (e_name , c_content) VALUES('L1','L1-其它 - 5S活動');
insert into work_station_1 (e_name , c_content) VALUES('L2','L2-其它 - 參觀活動');
insert into work_station_1 (e_name , c_content) VALUES('L3','L3-其它 - 部內會議');
insert into work_station_1 (e_name , c_content) VALUES('L4','L4-其它 - 部外會議');

insert into work_station_1 (e_name , c_content) VALUES('P','P-包裝作業');

insert into work_station_1 (e_name , c_content) VALUES('RE','RE-再檢作業');

insert into work_station_1 (e_name , c_content) VALUES('C','C-環境清潔');

insert into work_station_1 (e_name , c_content) VALUES('U','U-休息');

insert into work_station_1 (e_name , c_content) VALUES('B','B-中栓');
insert into work_station_1 (e_name , c_content) VALUES('B1','B1-栓');
insert into work_station_1 (e_name , c_content) VALUES('B2','B2-外蓋');

insert into work_station_1 (e_name , c_content) VALUES('I','I-成型');
insert into work_station_1 (e_name , c_content) VALUES('I1','I1-吊具');
insert into work_station_1 (e_name , c_content) VALUES('I2','I2-無吊具');

insert into work_station_1 (e_name , c_content) VALUES('A','A-調製相關');
insert into work_station_1 (e_name , c_content) VALUES('A1','A1-預備工作');
insert into work_station_1 (e_name , c_content) VALUES('A2','A2-調製過程');

insert into work_station_1 (e_name , c_content) VALUES('PW','PW-制水 , 鹽滅');

insert into work_station_1 (e_name , c_content) VALUES('M','M-蓋印 / 打印 / 貼標');

insert into work_station_1 (e_name , c_content) VALUES('S','S-停工待料');

insert into work_station_1 (e_name , c_content) VALUES('R','R-支援工作');

insert into work_station_1 (e_name , c_content) VALUES('D','D-請假');

insert into work_station_1 (e_name , c_content) VALUES('J','J-確效驗證 , 校正');

/***************** 
 *
 * work_position
 *
 *****************/
create table work_position(
no int not null primary key AUTO_INCREMENT,
e_name varchar(10) null,
c_content varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into work_position (e_name , c_content) VALUES('p1','生一部');
insert into work_position (e_name , c_content) VALUES('p2','生二部');
insert into work_position (e_name , c_content) VALUES('p3','生三部');

/***************** 
 *
 * work_station
 *
 *****************/
create table work_station(
no int not null primary key AUTO_INCREMENT,
e_name varchar(10) null,
c_content varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into work_station_3 (e_name , c_content) VALUES('W','W-倉庫相關');
insert into work_station (e_name , c_content) VALUES('W1','W1-領料');
insert into work_station (e_name , c_content) VALUES('W2','W2-稱料');
insert into work_station (e_name , c_content) VALUES('W3','W3-退料');

insert into work_station (e_name , c_content) VALUES('A','A-造粒');
insert into work_station (e_name , c_content) VALUES('A1','A1-結合劑調製');
insert into work_station (e_name , c_content) VALUES('A2','A2-濕式造粒');
insert into work_station (e_name , c_content) VALUES('A3','A3-乾式整粒');

insert into work_station (e_name , c_content) VALUES('E','E-打錠');

insert into work_station (e_name , c_content) VALUES('Y1','Y1-裝機');
insert into work_station (e_name , c_content) VALUES('Y2','Y2-調機');
insert into work_station (e_name , c_content) VALUES('Y3','Y3-試機');

insert into work_station (e_name , c_content) VALUES('V1','V1-機器拆卸');
insert into work_station (e_name , c_content) VALUES('V2','V2-清機');

insert into work_station (e_name , c_content) VALUES('K1','K1-機械故障');
insert into work_station (e_name , c_content) VALUES('K2','K2-維修');

insert into work_station (e_name , c_content) VALUES('M1','M1-蓋印');
insert into work_station (e_name , c_content) VALUES('M2','M2-打印');

insert into work_station (e_name , c_content) VALUES('O','O-泡殼分裝');

insert into work_station (e_name , c_content) VALUES('P','P-包裝作業');

insert into work_station (e_name , c_content) VALUES('Q','Q-檢視作業');

insert into work_station (e_name , c_content) VALUES('S','S-停工待料');

insert into work_station (e_name , c_content) VALUES('C','C-環境清潔');

insert into work_station (e_name , c_content) VALUES('J','J-確效驗證');

insert into work_station (e_name , c_content) VALUES('R','R-支援工作');

insert into work_station (e_name , c_content) VALUES('T','T-教育訓練');
insert into work_station (e_name , c_content) VALUES('T1','T1-部內教育訓練');
insert into work_station (e_name , c_content) VALUES('T2','T2-部外教育訓練');

insert into work_station (e_name , c_content) VALUES('U','U-休息');

insert into work_station (e_name , c_content) VALUES('D','D-請假');

insert into work_station (e_name , c_content) VALUES('L','L-其他');
insert into work_station (e_name , c_content) VALUES('L1','L1-其它 - 5S活動');
insert into work_station (e_name , c_content) VALUES('L2','L2-其它 - 參觀活動');
insert into work_station (e_name , c_content) VALUES('L3','L3-其它 - 部內會議');
insert into work_station (e_name , c_content) VALUES('L4','L4-其它 - 部外會議');

/***************** 
 *
 * operation_record
 *
 *****************/
create table operation_record(
no int not null primary key AUTO_INCREMENT,
a_user varchar(200) null,
login_code varchar(200) null,
r_time datetime null,
item varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/********************* 
 *
 * login_out_record
 *
 *********************/
create table login_out_record(
no int not null primary key AUTO_INCREMENT,
a_user varchar(200) null,
login_code varchar(200) null,
login_ip varchar(100) null,
login_time datetime null,
logout_time datetime null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/********************* 
 *
 * account
 *
 *********************/
create table account(
no int not null primary key AUTO_INCREMENT,
r_year varchar(100) null,
r_month varchar(100) null,
r_day varchar(100) null,
r_time time null,
a_work_no int null,
a_user varchar(100) null,
a_name varchar(100) null,
a_pwd varchar(100) null,
a_lv varchar(10) null,
a_position varchar(10) null,
a_status varchar(50) null,
a_comment text null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into account (a_work_no , a_user , a_pwd , a_lv , a_status , a_position) VALUES('1','admin','1qaz#123','1','run' , 'all');
insert into account (a_work_no , a_user , a_pwd , a_lv , a_status , a_position) VALUES('2','otsuka','otsuka','2','run' , 'all');
insert into account (a_work_no , a_user , a_pwd , a_lv , a_status , a_position) VALUES('3','normal','normal','3','run' , 'all');