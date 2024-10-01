from converter import Converter


converter = Converter()

print(converter.convert("Длина", 5, "Вершок", "Миллиметр",7))
print(converter.convert("Длина", 5,"Пядь", "Сантиметр"))
print(converter.convert("Длина", 5,"Аршин", "Дециметр"))
print(converter.convert("Длина", 5,"Сажень", "Метр"))
print(converter.convert("Длина", 5,"Верста", "Километр"))
print(converter.convert("Длина", 5,"Локоть", "Метр"))

print()

print(converter.convert("Длина", 5, "Дюйм", "Миллиметр"))
print(converter.convert("Длина", 5,"Фут", "Метр"))
print(converter.convert("Длина", 5,"Ярд", "Метр"))
print(converter.convert("Длина", 5,"Миля", "Метр"))

print()

print(converter.convert("Длина", 5, "Миллиметр", "Вершок"))
print(converter.convert("Длина", 5,"Метр","Пядь"))
print(converter.convert("Длина", 5,"Метр","Аршин"))
print(converter.convert("Длина", 5,"Метр","Сажень"))
print(converter.convert("Длина", 5,"Метр","Верста"))
print(converter.convert("Длина", 5,"Метр","Локоть"))

print()

print(converter.convert("Длина", 5, "Миллиметр", "Дюйм"))
print(converter.convert("Длина", 5,"Метр", "Фут"))
print(converter.convert("Длина", 5,"Метр", "Ярд"))
print(converter.convert("Длина", 5,"Метр", "Миля"))

print()

print(converter.convert("Длина", 5, "Дюйм", "Вершок"))
print(converter.convert("Длина", 5,"Фут","Пядь"))
print(converter.convert("Длина", 5,"Ярд","Аршин"))

print()

print(converter.convert("Длина", 5, "Вершок", "Дюйм"))
print(converter.convert("Длина", 5,"Пядь", "Фут"))
print(converter.convert("Длина", 5,"Аршин", "Ярд"))

print(converter.convert("Длина", 5,"Аршин", "Ярд"))



print("--------------------------------------")

''' Масса '''
print(converter.convert("Масса", 5, "Золотник", "Тонна"))
print(converter.convert("Масса", 5,"Лот", "Центнер"))
print(converter.convert("Масса", 5,"Пуд", "Грамм"))


print()

print(converter.convert("Масса", 5, "Унция", "Килограмм"))
print(converter.convert("Масса", 5,"Фунт", "Килограмм"))
print(converter.convert("Масса", 5,"Стоун", "Килограмм"))


print()

print(converter.convert("Масса", 5, "Килограмм", "Золотник"))
print(converter.convert("Масса", 5,"Килограмм","Лот"))
print(converter.convert("Масса", 5,"Килограмм","Пуд"))


print()

print(converter.convert("Масса", 5, "Килограмм", "Унция"))
print(converter.convert("Масса", 5,"Килограмм", "Фунт"))
print(converter.convert("Масса", 5,"Килограмм", "Стоун"))

print()

print(converter.convert("Масса", 5, "Унция", "Золотник"))
print(converter.convert("Масса", 5,"Фунт","Лот"))
print(converter.convert("Масса", 5,"Стоун","Пуд"))

print()

print(converter.convert("Масса", 5, "Золотник", "Унция"))
print(converter.convert("Масса", 5,"Лот", "Фунт"))
print(converter.convert("Масса", 5,"Пуд", "Стоун"))

print()

print(converter.convert("Длина", 5,"Километр", "Метр"))
print(converter.convert("Масса", 5,"Килограмм", "Грамм"))

