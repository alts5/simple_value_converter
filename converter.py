class Converter():
    #Меры длины и массы старорусские в СИ (метры и кг)
    oldrussian = {
        "Длина" : {
            "Вершок": 0.044,
            "Пядь": 0.1778,
            "Локоть": 0.42,
            "Аршин": 0.7112,
            "Сажень": 2.1336,
            "Верста": 1066.8,
        },
        "Масса" : {
            "Золотник": 0.00427,
            "Лот": 0.0128,
            "Пуд": 16.38
        }
    }

    # Меры длины и массы американские в СИ (метры и кг)
    american = {
        "Длина" : {
            "Дюйм": 0.0254,
            "Фут": 0.3048,
            "Ярд": 0.9144,
            "Миля": 1609.344,
        },
        "Масса": {
            "Унция" : 0.028,
            "Фунт": 0.454,
            "Стоун": 6.35,
        }
    }

    # Меры длины и массы СИ (в метры и кг)
    SI = {
        "Длина" : {
            "Миллиметр": 0.001,
            "Сантиметр": 0.01,
            "Дециметр": 0.1,
            "Метр": 1,
            "Километр": 1000,
        },
        "Масса" : {
            "Тонна" : 1000,
            "Центнер" : 100,
            "Килограмм" : 1,
            "Грамм" : 0.001
        }
    }

    def convert_from_oldrussian_to_SI(self, type_val, value, type_source, type_result):
        try:
             temp = round(value * self.oldrussian[type_val][type_source] * self.SI[type_val][type_result], 3)
        except:
            print("Ошибка преобразования. Проверьте исходные величины")
            return
        return temp

    def convert_from_american_to_SI(self, type_val, value, type_source, type_result):
        try:
            temp =  round(value * self.american[type_val][type_source] * self.SI[type_val][type_result], 3)
        except:
            print("Ошибка преобразования. Проверьте исходные величины")
            return
        return temp

    def convert_from_SI_to_oldrussian(self, type_val, value, type_source, type_result):
        try:
            temp =  round(self.SI[type_val][type_source] * value / self.oldrussian[type_val][type_result], 3)
        except:
            print("Ошибка преобразования. Проверьте исходные величины")
            return
        return temp

    def convert_from_SI_to_american(self, type_val, value, type_source, type_result):
        try:
            temp =  round(self.SI[type_val][type_source] *  value / self.american[type_val][type_result], 3)
        except:
            print("Ошибка преобразования. Проверьте исходные величины")
            return
        return temp

    def convert_from_american_to_oldrussian(self, type_val, value, type_source, type_result):
        try:
            temp =  round(value * self.american[type_val][type_source] / self.oldrussian[type_val][type_result], 3)
        except:
            print("Ошибка преобразования. Проверьте исходные величины")
            return
        return temp

    def convert_from_oldrussian_to_american(self, type_val, value, type_source, type_result):
        try:
            temp =  round(value *  self.oldrussian[type_val][type_source] / self.american[type_val][type_result], 3)
        except:
            print("Ошибка преобразования. Проверьте исходные величины")
            return
        return temp





