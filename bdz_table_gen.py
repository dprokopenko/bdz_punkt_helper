import json
from mpmath import mp
mp.dps = 500000
pi = str(mp.pi)[1:]

f = open('table.txt', 'w')

people = [
    "", # не знаю зачем, но так красивее это лучше оставить имхо не трогайте оно вас сожрет
    "Агаев Фархат Чингизович",
    "Аълохужаев Акбархужа Дилмуродхужа угли",
    "Барановская Дарья Геннадьевна",
    "Болычевцев Тимур Дмитриевич",
    "Ваньков Тимур Витальевич",
    "Войтецкий Артем Александрович",
    "Вологодский Михаил Евгеньевич",
    "Даянова Сабина Филюсовна",
    "Карпухин Сергей Евгеньевич",
    "Косакин Даниил Юрьевич",
    "Лебедев Иван Павлович",
    "Лежанкина Александра Игоревна",
    "Минченок Максим Александрович",
    "Наумова Анастасия Константиновна",
    "Петрович Сергей Дмитриевич",
    "Пивоваров Андрей Дмитриевич",
    "Рамусь Владислав Геннадьевич",
    "Руденский Константин Игоревич",
    "Савосин Артем Валерьевич",
    "Сахиуллин Ильдар Раушанович",
    "Семенов Андрей Сергеевич",
    "Семенов Денис Вадимович",
    "Стрипский Даниил Игоревич", 
    "Сумарокова Ксения Ильинична",
    "Токкожин Аспандияр Ерланович",
    "Торчик Лада -",
    "Фальчикова Вероника Евгеньевна",
    "Цыганов Артем Николаевич",
    "Шибанин Георгий Вячеславович",
    "Школьник Мария Дмитриевна"
]

n_group = 185

start = int(input("Введите номер стартовой задачи\n"))
finish = int(input("Введите номер конечной задачи\n")) + 1

fin_dict = {}
help_dict = {}

for i in range(start, finish):
    help_dict[i] = {}
    for j in range(0, 10):
        help_dict[i][j] = []

f.write("\tФИО")
for i in range(start, finish):
    f.write("\t" + str(i))
f.write("\n")

i = 1
for p in people[1:]:
    f.write(str(i) + "\t" + p)
    fin_dict[p] = []
    j = start
    while j != finish:
        in_pi = (j - 1) * 300 + (n_group - 183) * 35 + i
        punkt = int(pi[in_pi])
        fin_dict[p].append(punkt)
        help_dict[j][punkt].append(p)
        f.write("\t" + str(punkt))
        j += 1
    f.write("\n")
    i += 1

f.write("\n\n\tСовпадения:\n")
for i in range(start, finish):
    f.write("\t" + str(i) + " задача:\n")
    for j in range(0, 10):
        f.write("\t\t" + str(j) + " пункт:\n")
        for p in help_dict[i][j]:
            f.write("\t\t\t" + p + "\n")
f.close()

j = open('dicts.json', 'w')
all_in_one = {"dict for rep": help_dict, "normal dict": fin_dict}
j.write(json.dumps(all_in_one, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')))
j.close()