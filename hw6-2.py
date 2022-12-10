#Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

text1 = 'Какой-то каабвdк текст теабв в который коабвтор понапихали пихабвали абв куда абвуд ни попадя пабвопп'
print(text1)
def dell(text1):
    text1 = list(filter(lambda x: 'абв' not in x, text1.split()))
    return " ".join(text1)

text1 = dell(text1)
print(text1)