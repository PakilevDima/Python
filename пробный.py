# My programm on Python
def new():
    global nums
    name = input("имя, фамилию, отчество: ")
    with open('basa_coter.txt') as basa_new:
        if name in basa_new:
            print('Такой уже есть')
            return None
    yes = input(f"Вы точно хотите добавить {name}\n ")
    if yes == 'да':
        with open('basa_coter.txt', 'a') as basa_new:
            basa_new.write(f'{name}')
            print(f'Вы добавили {name}')
            return None
    print(f"Вы не добавили {name}")
def delete():
    global basa
    delete_name = input("Введите имя, фамилию, отчество кого хотите удалить: ")
    if delete_name in basa:
        yes = input(f"Вы точно хотите удалить{delete_name}\n ")
        if yes == 'да':
            basa.pop(basa.index(delete_name))
            return None
    print('Такого нет')
def internet():
    name = input("имя, фамилию, отчество: ")
    with open('basa_coter.txt') as basa_new:
        if name in basa_new:
            print('Есть такой')
            return None
        print("Таких нет")
def oll():
    with open('basa_coter.txt') as basa_new:
        for i in basa_new:
            print(f'{i}\n')
def redact():
    name = input('Напишите старое имя, фамилию, отчество: ')
    with open('basa_coter.txt') as basa_new:
        if name in basa_new:
            name_new = input("Введите новое имя, фамилию, отчество: ")
            yes = input(f'Вы точно хотите заминить {name} на {name_new}\n ')
            if yes == 'да':
                with open('basa_coter.txt', 'a') as basa_new:
                    basa_new.write(name_new)
                    print(f'Вы заменили {name} на {name_new}')
                    return None
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