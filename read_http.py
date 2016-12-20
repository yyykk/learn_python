file_r = open("MS_S1_U_Http_0711_gaosu.txt")
file_w = open("http_all.txt", "wb+")
str = file_r.readline()
counter = 0
while (((str) != "")):
    temp = str.replace(",", "\t")
    file_w.write(bytes(temp, 'utf-8'))
    str0 = str;
    while(str == str0):
        str = file_r.readline();
    counter += 1

file_r.close()
file_w.close()
print("success")
