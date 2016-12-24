import pymysql
import time

database = pymysql.connect (host = "localhost", user = "root", passwd = "mysql", db = "demo")
cursor = database.cursor()

start_time = time.time()
file_error = open("http_error.txt", "wb+")
file_r = open("MS_S1_U_Http_0711_gaosu.txt", 'rb')
file_http = open("http.txt", "wb+")

ignore_word = ["IMSI", "IMEI", "XDRID", "RAT", "MachineIPAddType", "SGWGGSNIPAdd", "TAC", "AppTypeCode",
               "USER_IPv4", "ProtocolType", "ULIPPacket", "DLIPPacket", "AppType", "AppSubType",
               "UserPort", "L4Protocal", "ULIPFRAGPACKETS", "DLIPFRAGPACKETS", "AppServerPort",
               "WindowSize", "MSSSize", "TCPConnStatus", "SessionIsEnd", "ULIPPacket", "DLIPPacket",
               "URI", "XOnlineHost", "UserAgent", "Cookie", "PortalAppCollection", "ULTCPOoOPacket",
               "ContentLength", "DestBeha", "OperBehaIden", "DLTCPOoOPacket", "TCPSYNAtteDelay",
               "TCPSYNComfirmDelay", "TCPSYNAtte", "TCPConnStatus", "EventType", "HTTPWAPStatus",
               "DestBeha", "OperBehaIden", "OperFinishIden"]

#ignore_list = []
key_word = ["ID"]

title = file_r.readline()
title = title.decode(encoding='utf-8',errors='ignore')

title = title.strip('\r\n')
title = ",ID," + title + ","
table_head = []
order_list = []#begin 0
key_list = []
head = ""
order = 0
second = 0
while(1):
    first = title.find(",", second) + 1
    second = title.find(",", first + 1)
    head = title[first : second]
    if (not(head in ignore_word)):
        order_list.append(order)
        table_head.append(head)
    if (head in key_word):
        key_list.append(order)
    order += 1
    if(second == len(title) - 1):
        break;

cursor.execute("drop table http_test")
long_title = ["HOST","HTTP_content_type"]
for key_iter in range (len(key_word)):
    if(key_iter == 0):
        key_word_string = "(" + key_word[key_iter]
    else:
        key_word_string = key_word_string + ", " + key_word[key_iter]
else:
    key_word_string += ");"
       
for table_iter in range (len(table_head)):
    if (table_iter == 0):
        cursor.execute("create table http_test (" + table_head[table_iter] + " char(30));")
    else:
        cursor.execute("alter table http_test add " + table_head[table_iter] + " char(30);")
    if (table_head[table_iter] in long_title):
        cursor.execute("alter table http_test modify " + table_head[table_iter] + " char(200) not null;")
    if (table_head[table_iter] in key_word):
        cursor.execute("alter table http_test modify " + table_head[table_iter] + " char(30) not null;")

cursor.execute("alter table http_test add constraint pk_orderinfo PRIMARY KEY" + key_word_string)

#cursor.commit()

def delete_comma (temp):
    comma_count = 0
    comma_index = -1
    while(1):
        comma_index = temp.find(",", comma_index + 1)
        comma_count += 1;
        if(comma_count == 53):
            temp = temp[0:comma_index] + temp[comma_index + 1 : len(temp)]
            break
    return temp

    

string = ""
counter = 0
word = ""
while (1):    
    string0 = string
    word_list = []
    
    while(1):
        string = file_r.readline()
        try:
            string = string.decode(encoding='utf-8', errors='ignore')
        except Exception as e:
            file_error.write(bytes(repr(e) + '\n', 'utf-8'))
            print("error = ", counter)
        if (string != string0):
            break
    if(string == ""):
        break
    if(string.count(",") != 60):
        string = delete_comma(string)
    string = string.replace("CMNET", "0");
    string = string.replace("CMWAP", "1");
    string = string.strip('\n')
    string = str(counter + 1) + "," + string + ","
    second = string.find(",")
    first = -1
    order = 0
    word_command = ""
    while(1):
        word = string[first + 1 : second]
        if (order in order_list):
            word_list.append(word)
            word = ""
        if(second == len(string) - 1):
            break;
        first = string.find(",", first + 1)
        second = string.find(",", second + 1)
        order += 1
        
    for word_list_iter in range(len(word_list)):
        word_command += word_list[word_list_iter] + ","
    else:
        word_command = word_command.strip(',')
        word_command = word_command.replace(",", "','")
    '''
    try:
        cursor.execute("insert http_test values ('" + word_command + "');")
    except Exception as e:
        file_error.write(bytes(str(counter) + '\n', 'utf-8'))
        file_error.write(bytes(repr(e) + '\n', 'utf-8'))
        file_error.write(bytes(string + '\n', 'utf-8'))
        print(counter)
    '''
    try:
        file_http.write(bytes(word_command + '\n', 'utf-8'))
    except Exception as e:
        file_error.write(bytes(repr(e) + '\n', 'utf-8'))
        print("error = ", counter)    
    
    counter += 1
    if (counter % 100000 == 0):
        print("right = ", counter)
        print(time.time() - start_time)
    if (counter == 1000000):
        print("pass = ", counter)
        break


'''
add_list = []
string = file_r.readline()
string = string.decode(encoding='utf-8',errors='ignore')
counter = 0
while (((string) != "")):
    string0 = string;
    add_list.append(string)
    temp = string.strip('\n')
    if (temp.count(",") != 60):
        comma_count = 0
        for code_count in range (len(temp)):
            if (temp[code_count] == ","):
                comma_count += 1
                if (comma_count == 53):
                    temp = temp[0:code_count] + temp[code_count + 1 : len(temp)]
                    #print(temp)
                    break
    temp = temp.replace(",", "','")
    #print("insert http_test values ('" + temp + "');")
    try:
        cursor.execute("insert http_test values ('" + temp + "');")
    except Exception as e:
        file_error.write(bytes(str(counter) + '\n', 'utf-8'))
        file_error.write(bytes(repr(e) + '\n', 'utf-8'))
        file_error.write(bytes(string + '\n', 'utf-8'))
        print(counter)
    while(string == string0):
        string = file_r.readline()
        string = string.decode(encoding='utf-8',errors='ignore')
    counter += 1
    
    if(counter == 100000):
        break
'''
cursor.execute("select * from http_test")
data = cursor.fetchall()
#data = cursor.fetchone()
#print(data)
print("counter = ", counter, "\t", "len(data) = ", len(data))
database.close()

file_r.close()
file_http.close()
file_error.close()
print(time.time() - start_time)
print("table_head = ", table_head)
