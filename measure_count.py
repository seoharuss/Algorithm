def count(n):
  c = 0
  k = 1
  while k * k < n:
    if n % k == 0:
      c = c + 2
    k = k + 1
  if k * k == n:
    c = c + 1
  return c