# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов 
# (складываются числа, у которых "х" в одинаковых степенях).
import re
import itertools
file1 = 'file1.txt'
file2 = 'file2.txt'

# читаем данные
def readfile (file):
    with open(str(file), 'r') as data:
        mnch = data.read()
        
    return mnch
#формируем списки и3 многочленов
def multilist(mnch):
    
    mnch = mnch.replace('=0','')
    mnch = re.sub('[*|^|+]','',mnch).split(' ')
    mnch = [i.split('x') for i in mnch]
    if len(mnch[-1]) == 1:
        mnch[-1].append(0)
       
    return mnch
# переделываем в список коэф. многочленов
def koef(k):
    g = []
    for i in range(len(k)):

        if k[i][1] == '':
            k[i][1] = 1

    for i in range(int(k[0][1])+1):
        for j in range(len(k)):
            if i == int(k[j][1]):
                num = int(k[j][0])
                g.append(num)
                
        if (len(g)-1) < i:
            g.append(0)   
    return g


m1 = readfile(file1)
m2 = readfile(file2)
mm1 = multilist(m1)
mm2 = multilist(m2)


mk1work = koef(mm1)
mk2work = koef(mm2)


mk1work.extend([0,] * (len(mk2work) - len(mk1work)))
mk2work.extend([0,] * (len(mk1work) - len(mk2work)))
# обработка

summ = list(map(sum, zip(mk1work, mk2work)))
summ.reverse()

x = ''
for i in range(len(summ)-2):
        
        if summ[i] != 0: 
            if summ[i] > 0:
                x += str(summ[i]) + "x^" + str(len(summ)-i-1)  +  " + "

            else:
                x += "(" + str(summ[i]) + ")x^" + str(len(summ)-i-1)  +  " + "
if summ[-2] > 0:
    x += str(summ[-2]) + "x +" + str(summ[-1]) + " = 0"
else:
    x += "(" + str(summ[-2]) + ")x +" + str(summ[-1]) + " = 0"

with open('result5task.txt', 'w') as res:
    res.write(x)
