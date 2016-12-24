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
    string = string.strip('\n')
    string += ","
    second = string.find(",")
    first = 0
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
    try:
        file_http.write(bytes(word_command + '\n', 'utf-8'))
    except Exception as e:
        file_error.write(bytes(repr(e) + '\n', 'utf-8'))
        print("error = ", counter)    
    counter += 1
    if (counter % 100000 == 0):
        print("right = ", counter)
        print(time.time() - start_time)
    if (counter == 10000000):
        print("pass = ", counter)
        break