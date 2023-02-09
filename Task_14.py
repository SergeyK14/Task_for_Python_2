# Вывести все целые числа степени двойки, не превосходящиe k

k = int (input ("Введите целое число k: "))
listok = []
count = 1
while count < k:
    count = count*2
    listok.append (count)
print (listok)