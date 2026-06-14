def power_recursion(a, b):
    if b == 0:
        return 1
    return a * power_recursion(a, b - 1)

# input dari pengguna
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
# output
print("Hasil =", power_recursion(a, b))