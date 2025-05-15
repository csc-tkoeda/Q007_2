"""
N M
A(1) ... A(N)
B(1) ... B(M)

5 3
260 510 980 170 630
500 999 300
"""

num_product, num_customer = list(map(int, input().split()))
prices = sorted(list(map(int, input().split())), reverse=True)
budgets = list(map(int, input().split()))

sales = {}

for i in range(num_product):
    for j in range(num_customer):
        if not sales.get(j):
            if prices[i] <= budgets[j]:
                sales[j] = prices[i]

print(sum(sales.values()))
