def reverse(A):
  if len(A) == 1: return A
  return reverse(A[1:] + [A[0]])

def reverse_2(A, start, stop):
  if start < stop-1:
    A[start], A[stop-1] = A[stop-1], A[start]
    reverse(A, start+1, stop-1)