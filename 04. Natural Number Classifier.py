"""
자연수가 과잉수/완전수/부족수인지를 각각 구하는 함수를 작성하라.
분류기는 수학적 개념인 진약수의 합을 사용하라.
"""

def get_aliquot_sum(n):
    return sum([i for i in range(1, n) if n % i == 0])

# 완전수
def is_perfect(n):
    return get_aliquot_sum(n) == n

# 과잉수
def is_abundant(n):
    return get_aliquot_sum(n) > n

# 부족수
def is_deficient(n):
    return get_aliquot_sum(n) < n