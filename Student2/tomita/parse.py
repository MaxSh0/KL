import re
from array import *
import sys
import codecs as cdc

def indexfunc(list1, flag = 'Fact'):#функция на ходящая все служебные слова
    outlist = []
    k = len(content)
    for i in range(k):
        if flag in list1[i]:
            if '}' not in list1[i-1]:
                outlist.append(i-1)
            outlist.append(i+2)
            i-=-3
            while '}' not in list1[i]:
                outlist.append(i)
                i-=-1
    return outlist

StaticServiceFalgs = 'Fact'
f_out = open('documents/text.txt', 'w')
line1 = ''
line2 = ''
with cdc.open('documents/output.txt', 'r',  'utf_8_sig') as f:
    content = f.readlines()
content = [x.strip() for x in content]
indexlist = indexfunc(content)
for i in range(len(indexlist)):
    f_out.writelines(content[indexlist[i]])
    f_out.write('\n')

f_out.close()


    
# Соединение строк если предложение содержит имена нескольких персон
with open('documents/text.txt') as f:
    lines = f.readlines()
str = 'PersonName'
punctuation = '\n'
pattern = re.compile(re.escape(str))
new_line = ''
with open('documents/text.txt', 'w') as f:
    for line in lines:
        result = pattern.search(line)        
        if result != None:
            new_line = new_line +  line + ''           
        else:            
            if new_line != '':
                new_line = new_line.replace(punctuation, "") + '\n'
                new_line = new_line.replace(' ', '_')                                
                new_line = new_line.replace('PersonName_=_', ", ")
                new_line = new_line[2:]
                result_1 = re.compile(re.escape('Attractions')).search(line)
                if result_1 is None:
                    new_line = new_line + '\n'
                f.write(new_line)
                new_line = '';                            
            f.write(line)


# Изменение строк содержащих Attractions
with open('documents/text.txt') as f:
    lines = f.readlines()
str = 'Attractions'
punctuation = '\n'
pattern = re.compile(re.escape(str))
new_line = ''
with open('documents/text.txt', 'w') as f:
    for line in lines:
        #проверка на наличие в строке ключевого слова
        result = pattern.search(line)  
        #если ключевое найдено, то создается новая строка к которой добавляется строка с ключевым словом 
        if result != None:
            new_line = new_line +  line + ''           
        #если не слово не найдено
        else:
            #проверка на содержание новой строки
            #если не пустая, то происходит её редактирование
            if new_line != '':      
                #удаление символов переноса строки
                new_line = new_line.replace(punctuation, "") + '\n'
                #замена пробелов на нижнее подчеркивание
                new_line = new_line.replace(' ', '_')               
                #замена ключевого слова на запятую и пробел
                new_line = new_line.replace('Attractions_=_', ", ")
                #удаление первых двух символов стрки, т.е. удаление ", "
                new_line = new_line[2:]
                #проверка на наличие точки в текущей строке(не новой)
                result_1 = re.compile(re.escape('.')).search(line)
                #если точка найдена, то запись в файл "_\n"
                if result_1 != None:
                    f.write('_\n') 
                #запись в файл новой строки
                f.write(new_line)
                #сброс значения
                new_line = '';
            #запись в файл текущую строку
            f.write(line)
            
            
            
            
            
#костыль для исправления "_\n" в ненужном месте    
with open('documents/text.txt') as f:
    lines = f.readlines()
str = '_\n'
pattern = re.compile(re.escape(str))
new_line = ''
with open('documents/text.txt', 'w') as f:
    for line in lines:
        #проверка на наличие в строке '_\n'
        result = pattern.search(line)  
        #если не найдено
        if result is None:
            #запись в новую строку текущую
            new_line = line  
            #запись в файл текущую строку
            f.write(line)   
        #если найдено
        else:
            #поиск в новой строке наличие точки(если она есть, то это предложение)
            result_1 = re.compile(re.escape('.')).search(new_line)
            #если точка есть, то записывается символ переноса строки
            if result_1 != None:
                f.write('\n')
            #если нет, то ничего не пишется
            
            
#Объяснение
# В результате редактирования строк содержащих Attractions иногда получется неккоректный порядок строк
# Сначала должно идти предложение, потом имя персоны, после достопримечательность
# Если персоны нет, то пишется пустая строка. Если нет достопримечательности, то пишется пустая строка 
# Однако в результате выполнения кода даже если есть и персона, и достопримечательность(что довольно редко бывает), то между ними всё равно есть пустая строка
# Этот недочет был исправлен добавлением не пустой строки, а строки содержащей '_\n'
# После был добавлен код для определения некоррекного места. Если оно найдено, то строка содержащая '_\n' просто не записывалась в файл
# В остальных случаях '_\n' заменялся на символ переноса строки и происходила запись
