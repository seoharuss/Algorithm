# Algorithm
알고리즘 관련 코드를 저장하는 곳

## Tip

### 시간복잡도
- n의 다항시간 = polynomial time<br>
- n의 지수시간 = exponential time<br><br>
`O(logn) < O(n) < O(n^2) < O(n^k) < O(2^n) < O(n!) < O(n^n)`<br><br>
- Language에서 제공하는 함수도 시간복잡도를 따로 고려해야 한다.<br>Ex) slicing, 리스트의 덧셈연산, ...

### 재귀
재귀 = 점화식<br>
재귀의 수행시간은 점화식으로 표현된다.
### 약수의 개수<br>
1. 약수의 개수는 1 ~ n^(1/2)까지만 확인하면 된다.
2. 하지만 제곱수인 경우 1개만 count 하므로 while문 밖에 작성<br>
ex) 1, 4, 9, 16, ...

## Add file record
- 2023/09/16 -> measure_count, reverse, subset