number_one = int(input("Введите число: "))
if number_one == 0:
    print("Программа завершена.")
else:
    while True:
        number_two = int(input("Введите число: "))
        if number_two == 0:
            break
sthet = number_one * number_two
print("Произведение:", sthet)