

def currency_converter():
    print("Конвертер валют: USD <-> UAH")
    print("1: Конвертировать USD в UAH")
    print("2: Конвертировать UAH в USD")
    
    choice = input("Выберите опцию (1 или 2): ")
    
    if choice == "1":
        usd = float(input("Введите сумму в USD: "))
        exchange_rate = float(input("Введите курс обмена (USD в UAH): "))
        uah = usd * exchange_rate
        print(f"{usd} USD равно {uah:.2f} UAH")
    elif choice == "2":
        uah = float(input("Введите сумму в UAH: "))
        exchange_rate = float(input("Введите курс обмена (USD в UAH): "))
        usd = uah / exchange_rate
        print(f"{uah} UAH равно {usd:.2f} USD")
    else:
        print("Неверный выбор. Пожалуйста, выберите 1 или 2.")


currency_converter()