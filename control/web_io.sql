/*
* Author   : JasonHung
* Date     : 20220211
* Update   : 20230419
* Function : JNC CB and sensor value
*/

/*
 * database  tinfar_kedge
 */ 
create database tinfar_kedge DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
use tinfar_kedge;


/* 
 * sensor_setup
 */
create table sensor_setup(
no int not null primary key AUTO_INCREMENT,
r_time datetime null,
r_year varchar(10) null,
r_month varchar(10) null,
r_day varchar(10) null,
account varchar(50) null,
s_position varchar(50) null,
s_tag_name varchar(50) null,
s_tag_high_val varchar(50) null,
s_tag_low_val varchar(50) null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/* 
 * sensor_alarm
 */
create table sensor_alarm(
no int not null primary key AUTO_INCREMENT,
r_time datetime null,
r_year varchar(10) null,
r_month varchar(10) null,
r_day varchar(10) null,
account varchar(50) null,
a_position varchar(50) null,
a_tag_name varchar(50) null,
a_tag_val varchar(50) null,
a_comment text null,
a_time datetime null,
sign_status varchar(50) null,
sign_time datetime null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


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
a_user varchar(200) null,
a_pwd varchar(200) null,
a_lv varchar(10) null,
a_position varchar(10) null,
a_status varchar(50) null,
a_comment text null
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into account (a_user , a_pwd , a_lv , a_status , a_position) VALUES('admin','1qaz#123','1','run' , 'all');
insert into account (a_user , a_pwd , a_lv , a_status , a_position) VALUES('kedge','kedge#123','2','run' , 'all');