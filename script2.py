def convert():
  print("Доступные единицы: km, m, cm, mm, mi, yd")
  base = input("Из какой единицы конвертировать? ").lower()
  konvert = input("В какую единицу конвертировать? ").lower()

  dist = float(input("Введите значение: "))

  if base == "km":
    meters = dist * 1000
  elif base == "m":
    meters = dist
  elif base == "cm":
    meters = dist * 0.01
  elif base == "mm":
    meters = dist * 0.001
  elif base == "mi":
    meters = dist * 1609.34
  elif base == "yd":
    meters = dist * 0.9144
  else:
    print("Ошибка: Неверная исходная единица.")
    return

  if konvert == "km":
    result = meters / 1000
  elif konvert == "m":
    result = meters
  elif konvert == "cm":
    result = meters / 0.01
  elif konvert == "mm":
    result = meters / 0.001
  elif konvert == "mi":
    result = meters / 1609.34
  elif konvert == "yd":
    result = meters / 0.9144
  else:
    print("Ошибка")
    return

  print(f"{dist} {base} = {result} {konvert}")

convert()