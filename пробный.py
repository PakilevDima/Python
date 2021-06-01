basa = []
# My programm on Python
def new():
    global nums
    name = input("имя, фамилию, отчество: ")
    if name in basa:
        print('Такой уже есть')
        return None
    nums += 1
    yes = input(f"Вы точно хотите добавить {name} ")
    if yes == 'да':
        basa.append(name)
        print(f'Вы добавили {name}')
    else:
        print(f"Вы не добавили {name}")
def delete():
    global basa
    delete_name = input("Введите имя, фамилию, отчество кого хотите удалить: ")
    if delete_name in basa:
        yes = input(f"Вы точно хотите удалить{delete_name} ")
        if yes == 'да':
            basa.pop(basa.index(delete_name))
    else:
        print('Такого нет')
def internet():
    name = input("имя, фамилию, отчество: ")
    if name in basa:
        print('Есть такой')
    else:
        print('Нет таких')
def oll():
    for i in basa:
        print(i)
        print()
def redact():
    name = input('Напишите старое имя, фамилию, отчество: ')
    if name in basa:
        name_new = input("Введите новое имя, фамилию, отчество: ")
        yes = input(f'Вы точно хотите заминить {name} на {name_new} ')
        if yes == 'да':
            ind = basa.index(name)
            basa.pop(ind)
            basa.insert(ind, name_new)
while True:
    print('Введите число: '
          '\n1.Найти'
          '\n2.Удалить'
          '\n3.Редактировать'
          '\n4.Добавить'
          '\n5.Вывести всех')
    num = int(input())
    nums = 0
    if num == 2:
        delete()
    if num == 1:
        internet()
    if num == 4:
        new()
    if num == 5:
        oll()
    if num == 3:
        redact()
    print(basa)