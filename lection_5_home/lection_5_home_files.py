fp = open("file.txt", "w", encoding="utf-8")# "w" - создаст новый файл
                                            # "r" - для чтения

#print(fp, type(fp))
fp.seek(6)                                      #поиск по индексу(в кирилице 2 индекса за 1)
txt = fp.read(3)                                 #читать количество символов

print(txt)

#fp.write("флоыавтмойтумтуй") - добавит запись

fp.close()