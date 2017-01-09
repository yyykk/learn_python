create database demo char(20)acter set gbk;

use demo;
create table mme(
	Interface int unsigned  not null,
    XDRID int unsigned  not null primary key,
    RAT int unsigned  not null,
    RequestTime datetime not null,
    EndTime datetime not null,
    Status_m int unsigned not null,
    RequestCause char(20),
    FailureCause char(20),
    MMEUES1APID char(20) ,
    OldMMEGroupID char(20) ,
    OldMTMSI char(20) ,
    MMEGroupID char(20) ,
    MMECode char(20) ,
    MTMSI char(20) ,
    TMSI char(20) ,
    UserIPv4 char(20) ,
	MMEIP char(20) ,
    TAC char(20) ,
    ECI char(20) ,
    OtherTAC char(20) ,
    OtherECI char(20) ,
    APN char(20) 	
);

drop table mme;

use demo;
create table mme_all(
	Interface char(20),
    XDRID char(20) not null primary key,
    RAT int unsigned null,
    IMSI char(20),
    IMEI char(20),
    MSISDN char(20),
    Proceduretype int unsigned null,
    RequestTime datetime not null,
    EndTime datetime not null,
    Status_m int unsigned,
    RequestCause char(20),
    FailureCause char(20),
    MMEUES1APID char(20),
    OldMMEGroupID char(20),
    OldMMECode char(20),
    OldMTMSI char(20),
    MMEGroupID char(20),
    MMECode char(20),
    MTMSI char(20),
    TMSI char(20),
    UserIPv4 char(20),
	MMEIP char(20),
    TAC char(20),
    ECI char(20),
    OtherTAC char(20),
    OtherECI char(20),
    APN char(20) 	
);

select * from mme_all;
grant all on *.* to 'root'@'localhost';
select user,host from mysql.user;

show variables like '%secure_file_priv%';

select RequestTime,EndTime,EndTime-RequestTime from mme_all
where XDRID = "16048321a1dd9c00";

select * from http_test;

alter table http_test
add constraint pk_orderinfo PRIMARY KEY(XDRID, RequestTime, ProcedureEndTime);

load data infile 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/http.txt' 
into table `http_test`
fields terminated by ',';

load data infile 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/http10/http2.txt' 
into table `http_test`
fields terminated by ',';

load data infile 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/http10/http5.txt' 
into table `http_test`
fields terminated by ',';

select RequestTime from http_test ;
select FROM_UNIXTIME('1464973385.641','%Y-%m-%d %H:%i:%s');
SELECT FROM_UNIXTIME(1468239342.226);

select MSISDN , count(MSISDN) from http_test #where Browser != 0
group by MSISDN
order by count(MSISDN) ;

select ECI,  sum(OperDelay) / count(ECI) as value from http_test 
group by ECI
order by value;

select count(*) from http_test;

select * from http_test where ID = 1261;

#alter table http_test engine=innodb;

SHOW PROCESSLIST;

alter table http_test engine = myisam;

alter table http_test modify HOST char(200) null;
alter table http_test modify HTTP_content_type char(200) null;

select 
left(from_unixtime(left(RequestTime, 7) * 1000), 19) as '起始时间',
left(from_unixtime((left(RequestTime, 7) + 1) * 1000), 19) as '终止时间',
sum(ULTraffic) + sum(DLTraffic) as '流量', 
sum(ULTCPOoOPacket)+sum(DLTCPOoOPacket)+sum(ULTCPRetransPacket)+sum(DLTCPRetransPacket) as 'TCP重传',
(sum(ULTCPOoOPacket)+sum(DLTCPOoOPacket)+sum(ULTCPRetransPacket)+sum(DLTCPRetransPacket))*1000000
/
(sum(ULTraffic) + sum(DLTraffic))as 'TCP质量',
sum(TCPSYNAtteDelay)+sum(FirstReqToFirstResDelay) as 'TCP延时',
sum(FirstHTTPResPacketDelay)+sum(LastHTTPPacketDelay) as 'HTTP延时'
from http_test
#where ECI = 121186305
group by left(RequestTime, 7);

select HTTP_content_type
from http_test
group by HTTP_content_type;

select max(left(RequestTime, 8)), min(left(RequestTime, 8))
from http_test;

select 
from_unixtime(max(RequestTime)/1000), 
from_unixtime(min(RequestTime)/1000)
from http_test;

select left(RequestTime, 8)+'00000' as Time from http_test;



