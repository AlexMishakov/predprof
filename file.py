f = open('student_new.csv', 'w')

DATA = [
    ('11 М', 3.5),
    ('11 И', 2.5),
    ('10 М', 3.5)
]

s = 'Класс, Средняя оценка\n'

for klass, mark in DATA:
    s += f'{klass}, {mark}\n'

f.write(s)
f.close()
