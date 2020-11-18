n = int(input("Введите число: "))
def in_prime(n):
    i= 2
    while i < n:
        if n % i != 0:
            i +=1
        else:
            return False
    return True
print(in_prime(n))