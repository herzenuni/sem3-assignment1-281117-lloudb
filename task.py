def plus(ch):
  sum = 0
  sd = str(ch)
  l = len(sd)
  for i in range(l):
    sum += int(sd[i])
  return sum

if __name__ == "__main__":
  ch = int(input('Введите число:'))
print('Сумма чисел равна = {}'.format(plus(ch)))
