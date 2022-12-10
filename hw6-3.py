number = float(input("Пожалуйте десятичное число: "))

lst = list(str(number).split('.'))



new_sum = sum(map(int, str(number).replace('.', '')))
print(f"Сумма цифр  равна = {new_sum}")