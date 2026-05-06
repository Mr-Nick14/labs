import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Создание данных (например, координаты точек)
x = np.array([21.06, 22.07, 23.05, 24.09, 25.08])  # X координаты точек
y = np.array([2961, 3041, 3255, 2000, 2601])  # Y координаты точек

x = np.log10(x)
y = 1 / (y + 273)
# Нанесение точек на график
plt.scatter(x, y, color='blue', label='Точки')

# Производим линейную регрессию через точки
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)  # Обучаем модель
y_pred = model.predict(x.reshape(-1, 1))  # Предсказываем значения для аппроксимации

# Построение линии прямой аппроксимации
plt.plot(x, y_pred, color='red', label='Линейная аппроксимация')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Линейная аппроксимация точек')
plt.errorbar(x, y, xerr=0.005, yerr=0.0001)
plt.legend()
plt.grid()
plt.show()