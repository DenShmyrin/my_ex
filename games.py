from random import randint

c, e = 1, 0 #граница рандома, очки
h = [0]

def random(h):
    h[0] = randint(0,c)
    return

#print('В этой игре тебе надо угадать случайное число. С каждым угаданным числом ты получаешь 1 очко, а диапазон увеличивается на 1.')
#print()

while True:
    b = int(input('Введи число: '))
    random(h)
    if b > c:
        print ('Ты вышел за диапазон. Введи число от 0 до',c)
        continue
    elif b == h[0]:
        e += 1
        c += 1
        print('Угадал')
        print('Кол-во очков:',e)
        print()
        random(h)
    elif b != h[0] :
        print()
        print('Не угадал. Диапазон от 0 до', c)
        print()