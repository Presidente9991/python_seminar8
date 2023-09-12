"""
Сделать консольное приложение Телефонный справочник с внешним хранилищем информации, и чтоб был реализован основной
функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""


def update(data):
    with open("file.txt", "w+") as newfile:
        newfile.writelines(data)


with open("file.txt", "r+") as file:
    file = file.readlines()
print(f"Debug: {file}")
while True:
    print("Добро пожаловать в Телефонный справочник!\n")
    option = int(input('Выберите действие:\n\n'
                       '1 - поиск абонента\n'
                       '2 - редактирование данных абонента\n'
                       '3 - добавление нового абонента\n'
                       '4 - удаление абонента\n'
                       '5 - завершить работу программы\n\n'
                       'Введите номер здесь: '))
    if option == 1:
        search = input("Для поиска абонента введите его Фамилию, Имя, Отчество или Телефон: ")
        print("Найдены следующие абоненты:\n")
        for i in file:
            if search in i:
                print(i)
    elif option == 2:
        search = input("Для редактирования данных об абоненте, введите его Фамилию, Имя, Отчество или Телефон: ")
        for i in range(len(file)):
            if search in file[i]:
                print("Найдены следующие абоненты:\n")
                print(file[i])
                option2 = str(input("Редактировать? Y/N (Y - да, N - нет): "))
                if option2 == 'Y' or option2 == 'y':
                    file.remove(file[i])
                    add = input("Введите новые Фамилию, Имя, Отчество и Телефон абонента: ")
                    file.insert(i, add + '\n')
                    update(file)
                    print("Изменения внесены!\n")
    elif option == 3:
        add = input("Для добавления нового абонента, введите его Фамилию, Имя, Отчество и Телефон: ")
        file.append(add + '\n')
        print("Информация об указанном абонента была добавлена!\n")
        print(file)
        update(file)
    elif option == 4:
        search = input("Для удаления абонента, введите его Фамилию, Имя, Отчество или Телефон: ")
        print("Найдены следующие абоненты:\n")
        for i in range(len(file)):
            if search in file[i]:
                print(file[i])
                option2 = str(input("Удалить? Y/N: (Y - да, N - нет): "))
                if option2 == "Y" or option2 == "y":
                    file.remove(file[i])
                    update(file)
                    print("Информация об указанном абоненте была удалена!\n")
                    break
    elif option == 5:
        print("До встречи!")
        break
