def vesyear(x):

  if x % 4 == 0:
    if x % 100 == 0:
      if x % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

x = int(input("Введите год: "))

if vesyear(x):
  print(f"{x} високосный год.")
else:
  print(f"{x} не високосный год.")