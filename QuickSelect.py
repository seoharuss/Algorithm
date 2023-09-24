def QuickSelect(L, k):
  pivot = L[0]
  A = [] # 미만
  B = [] # 초과
  C = [] # 동일
  for i in L:
    if pivot > i:
      A.append(i)
    elif pivot < i:
      B.append(i)
    else:
      C.append(i)
  if k > len(A) + len(C):
    return QuickSelect(B, k - len(A) - len(C))
  elif k <= len(A):
    return QuickSelect(A, k)
  else:
    return pivot


n, k = map(int, input().split())
L = list(map(int,input().split()))

print(QuickSelect(L, k))
