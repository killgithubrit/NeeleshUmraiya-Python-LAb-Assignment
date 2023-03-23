def myfunc(n):
  return lambda a: a * n

double = myfunc(6)
print(double(5))
