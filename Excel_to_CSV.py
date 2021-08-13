# Эта программа преобразует данные Excel в CSV.

# Импорт библиотеки pandas как pd.
import pandas as pd

# Читаем исходный Excel файл (Text.xlsx) и преобразуем его в объект датафрейма.
df = pd.DataFrame(pd.read_excel("Test.xlsx"))

# Показать датафрейм.
print('-' * 30)
print('Содержание Excel файла: \n', df)

# Считываем и сохраняем данные из Excel файла в новый файл CSV (Test.csv).
read_file = pd.read_excel("Test.xlsx")
read_file.to_csv("Test.csv",
                 index=None,
                 header=True)

# Читаем CSV файл и преобразуем его в объект датафрейма.
df = pd.DataFrame(pd.read_csv("Test.csv"))

# Показать датафрейм.
print('-' * 30)
print('Содержание CSV файла: \n', df)
