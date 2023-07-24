user_num = int(input("Enter positive integer: "))

# using "while"
i = 0
result = 0
while i <= user_num:
    if not i % 3:
        i += 1
        continue
    result += i ** 3
    i += 1

print(result)

# using "for"
result = 0
for i in range(0, user_num + 1):
    if not i % 3:
        continue
    result += i ** 3

print(result)
