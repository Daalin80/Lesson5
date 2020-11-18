from datetime import date
def is_date(y, m, d):
    try:
        date(y, m, d)
        return True
    except:
        return False
print(is_date(int(input("Введите год: ")),
              int(input("Введите месяц: ")),
              int(input("Введите день: "))))
