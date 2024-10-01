from behave import *
from converter import Converter

@given('конвертер запущен')
def step_given(context):
	context.converter = Converter()
@when('ввод "{var1}" "{var2}" "{var3}" "{var4}" "{var5}"')
def step_when(context, var1, var2, var3, var4, var5):
	context.result = context.converter.convert(var1,int(var2),var3,var4,int(var5))
@then('вывод "{result}"')
def step_then(context, result):
	assert context.result == float(result), f'Ожидалось {result} ({type(result)}), получено {context.result} ({type(context.result)})'
