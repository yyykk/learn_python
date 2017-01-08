import pymysql

database = pymysql.connect (host = "localhost", user = "root", passwd = "mysql0278", db = "demo")
cursor = database.cursor()

need_word = ['ID', 'MSISDN', 'ECI', 'APN', 'RequestTime', 'ProcedureEndTime', 'AppType', 'AppSubType',
             'AppContent', 'AppStatus', 'L4Protocal', 'AppServerIP_IPv4', 'AppServerPort',
             'ULTraffic', 'DLTraffic', 'ULTCPOoOPacket', 'DLTCPOoOPacket', 'ULTCPRetransPacket',
             'DLTCPRetransPacket', 'TCPSYNAtteDelay', 'TCPSYNComfirmDelay', 'TCPSYNSuccFirstReqDelay',
             'FirstReqToFirstResDelay', 'TCPSYNAtte', 'TCPConnStatus', 'FirstHTTPResPacketDelay',
             'LastHTTPPacketDelay', 'LastACKPacketDelay', 'HOST', 'HTTP_content_type']

key_word = ["ID"]

cursor.execute("drop table http_test")
long_title = ["HOST","HTTP_content_type"]

for key_iter in range (len(key_word)):
    if(key_iter == 0):
        key_word_string = "(" + key_word[key_iter]
    else:
        key_word_string = key_word_string + ", " + key_word[key_iter]
else:
    key_word_string += ");"
       
for table_iter in range (len(need_word)):
    if (table_iter == 0):
        cursor.execute("create table http_test (" + need_word[table_iter] + " char(30));")
    else:
        cursor.execute("alter table http_test add " + need_word[table_iter] + " char(30);")
    if (need_word[table_iter] in long_title):
        print("alter table http_test modify " + need_word[table_iter] + " char(200) not null;")
        cursor.execute("alter table http_test modify " + need_word[table_iter] + " char(200) not null;")
    if (need_word[table_iter] in need_word):
        cursor.execute("alter table http_test modify " + need_word[table_iter] + " char(30) not null;")

cursor.execute("alter table http_test add constraint pk_orderinfo PRIMARY KEY" + key_word_string)

database.close()
