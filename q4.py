def is_palindromic(num):
    return str(num) == str(num)[::-1]

f1 = 999
f2 = 999

pal = []

while f2 > 99:
    f1 = f2
    while not is_palindromic(f1*f2) and f1 > 99:
        f1 -= 1
    if is_palindromic(f1*f2):
        pal.append(f1*f2)
    f2 -= 1

print(pal)
print(max(pal))
