from mpmath import mp
mp.dps = 500000
pi = str(mp.pi)[1:]

n_group = int(input("Введите номер группы:\n"))
n_pers = int(input("Введите ваш номер в группе:\n"))
start = int(input("Введите номер стартовой задачи:\n"))
finish = int(input("Введите номер конечной задачи:\n")) + 1

help_dict = {}

while start != finish:
    in_pi = (start - 1) * 300 + (n_group - 183) * 35 + n_pers
    punkt = int(pi[in_pi])
    help_dict[start] = punkt
    start += 1

print(help_dict)