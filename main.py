from converter import Converter
import unittest

class testConverter(unittest.TestCase):
    converter = Converter()

    def test_vershook_to_millimetr(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Вершок", "Миллиметр",7), 220.0)

    def test_pyad_to_santimetr(self):
        self.assertEqual(self.converter.convert("Длина", 5,"Пядь", "Сантиметр"), 88.9)

    def test_arshin_to_decimetr(self):
        self.assertEqual(self.converter.convert("Длина", 5,"Аршин", "Дециметр"), 35.56)

    def test_sajen_to_metr(self):
        self.assertEqual(self.converter.convert("Длина", 5,"Сажень", "Метр"), 10.668)

    def test_versta_to_kilometr(self):
        self.assertEqual(self.converter.convert("Длина", 5,"Верста", "Километр"), 5.334)

    def test_lokot_to_metr(self):
        self.assertEqual(self.converter.convert("Длина", 5,"Локоть", "Метр"), 2.1)

    def test_duim_to_millimetr(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Дюйм", "Миллиметр"), 127.0)

    def test_fut_to_metr(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Фут", "Метр"), 1.524)

    def test_yard_to_metr(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Ярд", "Метр"), 4.572)

    def test_milya_to_metr(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Миля", "Метр"), 8046.72)

    def test_millimetr_to_vershok(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Миллиметр", "Вершок"), 0.114)

    def test_metr_to_pyad(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Метр", "Пядь"), 28.121)

    def test_metr_to_arshin(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Метр", "Аршин"), 7.03)

    def test_metr_to_sajen(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Метр", "Сажень"), 2.343)

    def test_metr_to_versta(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Метр", "Верста"), 0.005)

    def test_metr_to_lokot(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Метр", "Локоть"), 11.905)

    def test_millimetr_to_duim(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Миллиметр", "Дюйм"), 0.197)

    def test_metr_to_fut(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Метр", "Фут"), 16.404)

    def test_metr_to_yard(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Метр", "Ярд"), 5.468)

    def test_metr_to_milya(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Метр", "Миля"), 0.003)

    def test_duim_to_vershok(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Дюйм", "Вершок"), 2.886)

    def test_fut_to_pyad(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Фут", "Пядь"), 8.571)

    def test_yard_to_arshin(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Ярд", "Аршин"), 6.429)

    def test_vershok_to_duim(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Вершок", "Дюйм"), 8.661)

    def test_pyad_to_fut(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Пядь", "Фут"), 2.917)

    def test_arshin_to_yard(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Аршин", "Ярд"), 3.889)

    def test_zolotnik_to_tonna(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Золотник", "Тонна", 5), 2e-05)

    def test_lot_to_centner(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Лот", "Центнер"), 0.001)

    def test_pud_to_gramm(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Пуд", "Грамм"),81900.0)

    def test_uncia_to_kilogramm(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Унция", "Килограмм"), 0.14)

    def test_funt_to_kilogramm(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Фунт", "Килограмм"), 2.27)

    def test_stoun_to_kilogramm(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Стоун", "Килограмм"), 31.75)

    def test_kilogramm_to_zolotnik(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Килограмм", "Золотник"),1170.96)

    def test_kilogramm_to_lot(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Килограмм", "Лот"), 390.625)

    def test_kilogramm_to_pud(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Килограмм", "Пуд"), 0.305)

    def test_kilogramm_to_unciya(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Килограмм", "Унция"), 178.571)

    def test_kilogramm_to_funt(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Килограмм", "Фунт"), 11.013)

    def test_kilogramm_to_stoun(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Килограмм", "Стоун"), 0.787)

    def test_unciya_to_zolotnik(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Унция", "Золотник"), 32.787)

    def test_funt_to_lot(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Фунт", "Лот"), 177.344)

    def test_stoun_to_pud(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Стоун", "Пуд"), 1.938)

    def test_kilometr_to_metr(self):
        self.assertEqual(self.converter.convert("Длина", 5, "Километр", "Метр"), 5000.0)

    def test_kilogramm_to_gramm(self):
        self.assertEqual(self.converter.convert("Масса", 5, "Килограмм", "Грамм"), 5000.0)

    def test_convert_for_negative_value(self):
        with self.assertRaises(ValueError):
            self.converter.convert("Длина", -5, "Локоть", "Метр")

if __name__ == '__main__':
    unittest.main()