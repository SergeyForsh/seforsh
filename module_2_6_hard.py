print()
def get_password(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password
for i in range(3, 21):
    result = get_password(i)
    print(f"{i} - {result}")
