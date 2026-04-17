tasks = []
while True:
    print("\n1. Добавить\n2. Просмотреть\n3. Удалить\n4. Выход")
    choice = input("Выберите: ")
    if choice == '1':
        tasks.append(input("Задача: "))
        print("Добавлена!")
    elif choice == '2':
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Пусто.")
    elif choice == '3':
        if tasks:
            try:
                del tasks[int(input("Номер: ")) - 1]
                print("Удалена.")
            except (ValueError, IndexError):
                print("Неверный номер.")
        else:
            print("Пусто.")
    elif choice == '4':
        print("Пока!")
        break
    else:
        print("Ошибка.")
