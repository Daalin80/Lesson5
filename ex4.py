original_list = [i for i in range(1, 11)]
list_with_zero = []
for i in original_list:
    if i % 2 != 0:
        list_with_zero.append(0)
    elif i % 2 ==0:
        list_with_zero.append(i)
print("Список до замены: ", original_list)
print("Список после замены: ", list_with_zero)

def total_zero(list_with_zero):
    num_of_zero = 0
    for i in list_with_zero:
        if i == 0:
            num_of_zero += 1
    return num_of_zero
print("Всего нулей в списке: ", total_zero(list_with_zero))
