def currency_converter():
    history = []
    
    while True:
        print("\n" + "="*40)
        print("Конвертер валют: USD <-> UAH")
        print("1: Конвертировать USD в UAH")
        print("2: Конвертировать UAH в USD")
        print("3: Выйти из программы")
        
        while True:
            choice = input("Выберите опцию (1-3): ")
            if choice in ("1", "2", "3"):
                break
            print("Ошибка: выберите 1, 2 или 3!")

        if choice == "3":
            print("Программа завершена. До свидания!")
            break
        
        def get_input(prompt):
            while True:
                try:
                    value = float(input(prompt))
                    if value <= 0:
                        print("Ошибка: значение должно быть положительным!")
                        continue
                    return value
                except ValueError:
                    print("Ошибка: введите числовое значение!")
        
        amount = get_input("Введите сумму: ")
        
        while True:
            exchange_rate = get_input("Введите курс обмена (USD в UAH): ")
            if exchange_rate < 10 or exchange_rate > 50:
                print("Предупреждение: курс выходит за обычные границы (10-50)!")
                confirm = input("Вы уверены? (да/нет): ")
                if confirm.lower() == "да":
                    break
            else:
                break
        
        if choice == "1":
            result = f"{amount} USD = {amount * exchange_rate:.2f} UAH"
            print(result)
        else:
            result = f"{amount} UAH = {amount / exchange_rate:.2f} USD"
            print(result)
        
        history.append(result)
        
        while True:
            repeat = input("\nСделать еще операцию? (да/нет): ").lower()
            if repeat in ("да", "нет"):
                break
            print("Ошибка: введите 'да' или 'нет'!")
        
        if repeat == "нет":
            print("\nИстория операций:")
            for i, op in enumerate(history, 1):
                print(f"{i}. {op}")
            print("\nСпасибо за использование конвертера!")
            break
currency_converter()