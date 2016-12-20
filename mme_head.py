import pymysql

#database = pymysql.connect (host = "localhost", user = "root", passwd = "mysql", db = "demo")
#cursor = database.cursor()

file_r = open("MS_S1_MME_0711_gaosu.txt", 'rb')
file_error = open("mme_error.txt", "wb+")

ignore_word = ["Interface","RAT"]
key_word = ["XDRID", "RequestTime"]

title = file_r.readline()
title = title.decode(encoding='utf-8',errors='repalce')

title = title.strip('\n')
title += ","
table_head = []
order_list = []#begin 0
key_list = []
head = ""
order = 0
for string_iter in range (len(title)):
    if ( title[string_iter] != "," ):
        head += title[string_iter]
    else:
        if (not(head in ignore_word)):
            order_list.append(order)
            table_head.append(head)
        if (head in key_word):
            key_list.append(order)
        order += 1
        head = ""

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
string = file_r.readline()
string = string.decode(encoding='utf-8',errors='repalce')
counter = 0
add_list = []
word = ""
while (((string) != "")):
    order = 0
    word_command = ""
    key = ""
    word_list = []
    string0 = string
    for string_iter in range (len(string)):
        if ( string[string_iter] != "," ):
            word += string[string_iter]
        else:
            if (order in order_list):
                word_list.append(word)
            if (order in key_list):
                key += word
            order += 1
            word = ""
    if (key in key_list):
        continue
    else:
        add_list.append(key)
    for word_list_iter in range(len(word_list)):
        word_command += word_list[word_list_iter] + ","
    else:
        word_command = word_command.strip(',')
    word_command = word_command.replace(",", "','")
    #print(word_command)
    while(string == string0):
        string = file_r.readline()
        string = string.decode(encoding='utf-8', errors='repalce')
    counter += 1
    if (counter == 1000000):
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
'''t
file_r.close()
file_error.close()
print("success")
