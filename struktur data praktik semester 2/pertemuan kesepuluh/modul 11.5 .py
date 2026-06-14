def print_fibo(n):
    if n <= 1:
        return n
    return print_fibo(n-1) + print_fibo(n-2)

# input dari pengguna
n = int(input("Masukkan jumlah deret Fibonacci: "))
# output
print("Deret Fibonacci:")
for i in range(n):
    print(print_fibo(i), end=' ')
