from converter import Converter

converter = Converter()

print(converter.convert_length_from_oldrussian_to_SI("Длина", 5, "Вершок", "Метр"))
print(converter.convert_length_from_oldrussian_to_SI("Длина", 5,"Пядь", "Метр"))
print(converter.convert_length_from_oldrussian_to_SI("Длина", 5,"Аршин", "Метр"))
print(converter.convert_length_from_oldrussian_to_SI("Длина", 5,"Сажень", "Метр"))
print(converter.convert_length_from_oldrussian_to_SI("Длина", 5,"Верста", "Метр"))
print(converter.convert_length_from_oldrussian_to_SI("Длина", 5,"Локоть", "Метр"))

print()

print(converter.convert_length_from_american_to_SI("Длина", 5, "Дюйм", "Метр"))
print(converter.convert_length_from_american_to_SI("Длина", 5,"Фут", "Метр"))
print(converter.convert_length_from_american_to_SI("Длина", 5,"Ярд", "Метр"))
print(converter.convert_length_from_american_to_SI("Длина", 5,"Миля", "Метр"))
