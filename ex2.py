print("Сколько ты весишь? (в кг)", end=' ')
weight = float(input()) #weight - вес
print("Каков твой рост? (в см)", end=' ')
height = float(input())#height - рост

IMT = weight/((height/100)**2)

print("Индекс массы твоего тела", IMT)
if IMT < 16:
    print("ТЫ ДРИЩ МАТЬ ТВОЮ, ИДИ ПОЖРИ КУРОЧКИ, УБЛЮДОК")
elif IMT > 16 and IMT < 18.5:
    print("ТЫ КОНЕЧНО ТОЩИЙ, НО НЕ СОВСЕМ УРОД!!!")
elif IMT > 18.5 and IMT < 25:
    print("ТЫ РОВНЫЙ ПОЦЫК. МОЖЕШЬ СОЖРАТЬ ЭТО ГАМБУРГЕР!!!")
elif IMT > 25 and IMT < 30:
    print("ЧУВАК, А ТЫ НЕ ДУМАЛ ЧТО ПОРА ПО МЕНЬШЕ ЖРАТЬ, ЕСЛИ НЕТ ТО Я ТЕБЕ ЭТО ГОВОРЮ")
elif IMT > 30 and IMT < 35:
    print("ЭЙ МЭН, ВЫПЛЮНЬ КУРИЦУ ИЗ РТА МАТЬ ТВОЮ, У ТЕБЯ ОЖИРЕНИЕ ПЕРВОЙ СТЕПЕНИ!!!")
elif IMT > 35 and IMT < 40:
    print("НИГА, ТЫ ПОНИМАЕШЬ ЧТО ПО СРАВНЕНИЮ С ТОБОЙ СЛОН ХУДЫШКА, ПИЗДУЙ В СПОРТЗАЛ, А ТО С ТВОИМ ОЖИРЕНИЕ 2 СТЕПЕНИ ТЫ СКОРО ЛОПНЕШЬ")
elif IMT > 40 and IMT < 50:
    print("ТЫ ЖИРНЫЙ УБЛЮДОК, И ЭТО ВСЕ ЧТО Я МОГУ ТЕБЕ СКАЗАТЬ!!!")
elif IMT > 50:
    print("Что ты вообще такое?!??!")