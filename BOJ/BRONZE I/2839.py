n = int(input())

stack = []

stack.append(n)
for _ in range(n // 5):
    stack.append(n - 5)
    n = stack[-1]

while(0 < len(stack)):
    if stack[-1] % 3 == 0:
        stack.append(n - 3)
        n = stack[-1]
    else:
        stack.pop()

print(len(stack) - 1)

