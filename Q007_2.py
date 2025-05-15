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

total_sales = 0

for i in range(num_customer):
    for j in range(num_product):
        if prices[j] <= budgets[i]:
            total_sales += prices[j]
            break

print(total_sales)
