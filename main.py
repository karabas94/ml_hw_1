import numpy as np
import pandas as pd

"""numpy"""
"""
1 Створіть масив NumPy із 10 випадкових цілих чисел. Виконайте наступні операції:
Знайдіть середнє, медіану та стандартне відхилення масиву.
Замініть всі парні числа у масиві на 0.
"""
first_array = np.random.randint(0, 100, 10)
print(f'Array: {first_array}')
mean = np.mean(first_array)
print(f'Mean: {mean}')
median = np.median(first_array)
print(f'Median: {median}')
deviation = np.std(first_array)
print(f'Standard Deviation: {deviation}')
replace = first_array[first_array % 2 == 0] = 0
print(f'Replace even number to zero: {first_array}')
print('\n')
"""
2 Індексація та зрізка в NumPy:
Створіть 2D масив NumPy (матрицю) розміром (3, 3) із випадковими цілими числами.
Виведіть перший рядок матриці.
Виведіть останній стовпець матриці.
Виведіть діагональні елементи матриці.
"""
second_array = np.random.randint(1, 100, (3, 3))
print(f'Array:\n {second_array}')
first_row = second_array[0, :]
print(f'First row: {first_row}')
last_column = second_array[:, -1]
print(f'Last column: {last_column}')
diagonal = np.diag(second_array)
print(f'Diagonal: {diagonal}')
print('\n')
"""
3 Створіть 2D масив NumPy розміром (3, 3) та 1D масив розміром (3,). 
Використайте broadcasting для додавання 1D масиву до кожного рядка 2D масиву.
"""
first_array = np.random.randint(0, 10, (3, 3))
second_array = np.random.randint(0, 10, 3)
print(f'First array:\n {first_array}')
print(f'Second array: {second_array}')
result = first_array + second_array
print(f'Result broadcasting:\n {result}')
print('\n')
"""
4 Створіть 2D масив NumPy розміром (5, 5) з випадковими цілими числами.
Знайдіть та виведіть всі унікальні елементи у масиві.
виведіть всі рядки, сума елементів у яких більша за певне значення. (значення оберіть самі)
"""
my_array = np.random.randint(0, 10, (5, 5))
print(f'Array:\n {my_array}')
uniq_element = np.unique(my_array)
print(f'Unique elements: {uniq_element}')
rows = my_array[np.sum(my_array, axis=1) > 20]
print(f'Rows sum > 20: {rows}')
print('\n')
"""
5 Створіть 1D масив NumPy, що містить цілі числа від 1 до 20 (включно).
Використайте оператор shape, щоб перетворити 1D масив у 2D масив розміром (4, 5). 
Переконайтеся, що отриманий перетворений масив має бажаний розмір.
"""
my_array = np.arange(1, 21)
print(f'Array: {my_array}')
new_array = my_array.reshape(4, 5)
print(f'New Array:\n {new_array}')
print(f'\n-----------------------------------------------------------------------------------------------------------')
"""pandas"""
"""
Створіть DataFrame Pandas із щонайменше 5 рядками та 3 стовпцями. 
Стовпці можуть представляти різні атрибути (наприклад, Ім'я, Вік, Місто).
"""
first_df = pd.DataFrame({'Name': ['Elena', 'Victor', 'Oleksandr', 'Iryna', 'Nina'],
                         'Age': [55, 60, 30, 28, 49],
                         'City': ['Kyiv', 'Odessa', 'Izmail', 'Nikolaev', 'Kherson']})
print(first_df)
print('\n')
"""
Додайте новий стовпець до DataFrame, який представляє числове значення.
"""
first_df['Money'] = [2800000, 1000000, 70000, 480000, 280000]
print(f'Added money:\n {first_df}')
print('\n')
"""
Відфільтруйте DataFrame, щоб показати лише рядки, де числове значення більше певного порогу (ви можете визначити поріг).
"""
filter_df = first_df[first_df['Age'] <= 30]
print(f'Filtered DataFrame:\n {filter_df}')
print('\n')
"""
Завантажте набір даних за допомогою Pandas (ви можете використовувати будь-який набір даних у форматі CSV або wine.csv).
"""
read_df = pd.read_csv('wine.csv')
print(read_df)
"""
Відобразіть перші 5 рядків набору даних.
"""
five_rows = read_df.head(5)
print(f'First five rows:\n {five_rows}')
"""
Розрахуйте та виведіть загальну статистику для числових стовпців у наборі даних.
"""
stats = read_df.describe()
print(f'Statistics:\n {stats}')
print('\n')
"""
Знайдіть та виведіть унікальні значення у категорійному стовпці.
"""
unique_category = read_df['1065'].unique()
print(f'Unique value in column:\n {unique_category}')
