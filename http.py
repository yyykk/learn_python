import time

start_time = time.time()
file_error = open("http_error.txt", "wb+")
file_r = open("MS_S1_U_Http_0711_gaosu.txt", 'rb')
file_http = open("http.txt", "wb+")

need_word = ['ID', 'MSISDN', 'ECI', 'APN', 'RequestTime', 'ProcedureEndTime', 'AppType', 'AppSubType',
             'AppContent', 'AppStatus', 'L4Protocal', 'AppServerIP_IPv4', 'AppServerPort',
             'ULTraffic', 'DLTraffic', 'ULTCPOoOPacket', 'DLTCPOoOPacket', 'ULTCPRetransPacket',
             'DLTCPRetransPacket', 'TCPSYNAtteDelay', 'TCPSYNComfirmDelay', 'TCPSYNSuccFirstReqDelay',
             'FirstReqToFirstResDelay', 'TCPSYNAtte', 'TCPConnStatus', 'FirstHTTPResPacketDelay',
             'LastHTTPPacketDelay', 'LastACKPacketDelay', 'HOST', 'HTTP_content_type']



title = file_r.readline()
title = title.decode(encoding='utf-8',errors='ignore')

title = title.strip('\r\n')
title = ",ID," + title + ","
table_head = []
order_list = []#begin 0
head = ""
order = 0
second = 0
while(1):
    first = title.find(",", second) + 1
    second = title.find(",", first + 1)
    head = title[first : second]
    if (head in need_word):
        order_list.append(order)
    order += 1
    if(second == len(title) - 1):
        break;

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

    

string0 = ""
counter = 0
word = ""
while (1):
    word_list = []

    while(1):
        string = file_r.readline()
        try:
            string = string.decode(encoding='utf-8', errors='ignore')
        except Exception as e:
            file_error.write(bytes(repr(e) + '\n', 'utf-8'))
            print("error = ", counter)
        if (string != string0):
            string0 = string
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
    #print(word_list)    
    for word_list_iter in range(len(word_list)):
        word_command += word_list[word_list_iter] + ","
    else:
        word_command = word_command[0:len(word_command) - 1]
    try:
        file_http.write(bytes(word_command + '\n', 'utf-8'))
    except Exception as e:
        file_error.write(bytes(repr(e) + '\n', 'utf-8'))
        print("error = ", counter)    
    
    counter += 1
    if (counter % 100000 == 0):
        print("right = ", counter)
        print(time.time() - start_time)
    if (counter == 1000):
        print("pass = ", counter)
        break





file_r.close()
file_http.close()
file_error.close()
print(time.time() - start_time)
print("need_word = ", need_word)
