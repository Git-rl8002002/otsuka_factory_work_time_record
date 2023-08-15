/*
* Author   : JasonHung
* Date     : 20221102
* Update   : 20230719
* Function : otsuka factory work time record
*/

/*
 * database  tinfar_kedge
 */ 
create database otsuka_factory DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
use otsuka_factory;

/* 
 * work_station_3
 */
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

/* 
 * work_station_1
 */
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


/* 
 * work_position
 */
create table work_position(
no int not null primary key AUTO_INCREMENT,
e_name varchar(10) null,
c_content varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into work_position (e_name , c_content) VALUES('p1','生一部');
insert into work_position (e_name , c_content) VALUES('p2','生二部');
insert into work_position (e_name , c_content) VALUES('p3','生三部');

/* 
 * work_station
 */
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

/* 
 * operation_record
 */
create table operation_record(
no int not null primary key AUTO_INCREMENT,
a_user varchar(200) null,
login_code varchar(200) null,
r_time datetime null,
item varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/* 
 * login_out_record
 */
create table login_out_record(
no int not null primary key AUTO_INCREMENT,
a_user varchar(200) null,
login_code varchar(200) null,
login_ip varchar(100) null,
login_time datetime null,
logout_time datetime null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


/* 
 * account
 */
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