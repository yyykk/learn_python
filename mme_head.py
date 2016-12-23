import pymysql
import time
#database = pymysql.connect (host = "localhost", user = "root", passwd = "mysql", db = "demo")
#cursor = database.cursor()

start_time = time.time()
file_r = open("MS_S1_MME_0711_gaosu.txt", 'rb')
file_error = open("mme_error.txt", "wb+")
file_mme = open("mme.txt", "wb+")

ignore_word = ["Interface", "RAT", "RequestCause", "FailureCause", "MMEUES1APID", "OldMTMSI", "MMEGroupID", "TMSI", "MTMSI", "UserIPv4", "TAC", "APN\r"]
key_word = ["XDRID", "RequestTime"]

title = file_r.readline()
title = title.decode(encoding='utf-8',errors='ignore')

title = title.strip('\n')
title += ","
title = "," + title
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
        
#try:
#    cursor.execute("drop table mme_test")
#except Exception as e:
#    file_error.write(bytes(repr(e), 'utf-8'))


'''
for key_iter in range (len(key_word)):
    if(key_iter == 0):
        key_word_string = "(" + key_word[key_iter]
    else:
        key_word_string = key_word_string + ", " + key_word[key_iter]
else:
    key_word_string += ");"
       
for table_iter in range (len(table_head)):
    if (table_iter == 0):
        cursor.execute("create table mme_test (" + table_head[table_iter] + " char(30));")
    else:
        cursor.execute("alter table mme_test add " + table_head[table_iter] + " char(30);")
    if (table_head[table_iter] in long_title):
        cursor.execute("alter table mme_test modify " + table_head[table_iter] + " char(200) not null;")
    if (table_head[table_iter] in key_word):
        cursor.execute("alter table mme_test modify " + table_head[table_iter] + " char(30) not null;")

cursor.execute("alter table mme_test add constraint pk_orderinfo PRIMARY KEY" + key_word_string)
'''


string = ""
counter = 0
word = ""
while (1):
    order = 0
    word_command = ""
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
    #string = string.strip('\n')
    if(string == ""):
        break
    string = string.strip('\n')
    string += ","
    second = string.find(",")
    first = 0
    while(1):
        word = string[first + 1 : second]
        if (order in order_list):
            word_list.append(word)
            word = ""
        first = string.find(",", first + 1)
        second = string.find(",", second + 1)
        order += 1
        if(second == len(string) - 1):
            break;
    for word_list_iter in range(len(word_list)):
        word_command += word_list[word_list_iter] + ","
    else:
        word_command = word_command.strip(',')
    try:
        pass
        file_mme.write(bytes(word_command + '\n', 'utf-8'))
    except Exception as e:
        file_error.write(bytes(repr(e) + '\n', 'utf-8'))
        print("error = ", counter)    
    counter += 1
    if (counter % 1000000 == 0):
        print("right = ", counter)
    if (counter == 11000000):
        print("pass = ", counter)
        break

    
'''
add_list = []
string = file_r.readline()
string = string.decode(encoding='utf-8',errors='repalce')
counter = 0
while (((string) != "")):
    string0 = string;
    add_list.append(string)
    temp = string.strip('\n')

    temp = temp.replace(",", "','")
    
    try:
        cursor.execute("insert mme_test values ('" + temp + "');")
    except Exception as e:
        file_error.write(bytes(str(counter) + '\n', 'utf-8'))
        file_error.write(bytes(repr(e) + '\n', 'utf-8'))
        file_error.write(bytes(string + '\n', 'utf-8'))
        print(counter)
    while(string == string0):
        string = file_r.readline()
        string = string.decode(encoding='utf-8',errors='repalce')
    counter += 1
    
    #if(counter == 100000):
        #break

cursor.execute("select * from mme_test")
data = cursor.fetchall()
#data = cursor.fetchone()
print("counter = ", counter, "\t", "len(data) = ", len(data))

database.close()
'''
file_r.close()
file_mme.close()
file_error.close()
print("spend time = ", time.time() - start_time)
print("table_head = ", table_head)
