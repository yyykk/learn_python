import pymysql

database = pymysql.connect (host = "localhost", user = "root", passwd = "mysql", db = "demo")
cursor = database.cursor()
file_error = open("http_error.txt", "wb+")
file_r = open("MS_S1_U_Http_0711_gaosu.txt", 'rb')
title = file_r.readline()
title = title.decode('replace')

title = title.strip('\n')
title += ","
table_head = []
head = ""
for string_iter in range (len(title)):
    if ( title[string_iter] != "," ):
        head += title[string_iter]
    else:
        table_head.append(head)
        head = ""

cursor.execute("drop table http_test")

key_word = ["XDRID","RequestTime","ProcedureEndTime"]
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


add_list = []
string = file_r.readline()
string = string.decode('replace')
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
        string = string.decode('replace')
    counter += 1
    
    if(counter == 100000):
        break

cursor.execute("select * from http_test")
data = cursor.fetchall()
#data = cursor.fetchone()
print("counter = ", counter, "\t", "len(data) = ", len(data))

database.close()
file_r.close()
file_error.close()
print("success")
