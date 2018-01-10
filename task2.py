def plus(ch):
  sum = 0
  sd = str(ch)
  l = len(sd)
  for i in range(l):
    sum += int(sd[i]) ** 2
  return sum

def func1():
    lst = list()

    for i in range(10, 100):
        if plus(i) % 17 == 0:
            lst.append(i)
    return lst

def func2(n):
    n -= 1
    lst = list()

    for i in range(10 ** n, 10 ** (n + 1)):
        if plus(i) % 17 == 0:
            lst.append(i)
    return lst

if __name__ == "__main__":
    print(func())
