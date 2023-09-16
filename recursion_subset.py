# k가 포함된 집합 전부 출력된다.
# 0 ~ n-1의 부분집합 모두 출력하라 (2^n개)

def gen_subsets(k):
  if k == n:
    print(S)
  else:
    S.append(k)
    gen_subsets(k+1)
    S.pop()
    gen_subsets(k+1)

S = []
gen_subsets(0)

