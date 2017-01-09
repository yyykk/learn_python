file_r = open("http_1000.txt", 'rb')

def read_file():
    text = file_r.readline()
    text = text.decode(encoding='utf-8',errors='ignore')
    return text

counter = 1;
while(1):
    file_name = "./http10/http" + str(counter) + ".txt"
    file_w = open(file_name, "wb+")
    num = 0;
    while(1):
        text = read_file();
        if (num == 1000000 or text == ""):
            break
        file_w.write(bytes(text, 'utf-8'))
        num += 1;
    print(counter)
    counter += 1;
    file_w.close();
    if (counter == 11):
        break

file_r.close();

