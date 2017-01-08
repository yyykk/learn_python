NeedTitleFile = open("NeedTitle.txt", "rb")

need_word = [];

while(1):
    title = NeedTitleFile.readline()
    title = title.decode(encoding='utf-8',errors='ignore')
    title = title.strip('\r\n')
    if (title == ""):
        break;
    need_word.append(title);

print(need_word);
    
