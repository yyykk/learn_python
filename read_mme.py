file_r = open("MS_S1_MME_0711_gaosu.txt")
file_w = open("mme_1000.txt", "wb+")
str = file_r.readline()
counter = 1;
while (((str) != "")):
    str = str.replace(",", "\t")
    #print(str)
    file_w.write(bytes(str, 'utf-8'))
    str = file_r.readline()
    counter += 1
    if (counter == 5000):
        break
file_r.close()
file_w.close()
print("success")
