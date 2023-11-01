import matplotlib.pyplot as plt
import numpy as np

# Заданные значения x
x = [0, 10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 360]

# Вычисляем значения y с использованием синуса и k=6
k = 6
y = np.sin(np.radians(x)) * k
t = np.round(np.array(x)/360*0.03, 3)

# Создаем график
plt.figure(figsize=(10, 5))
plt.plot(x, y, marker='o', linestyle='-', color='b', markeredgecolor='black')
plt.title("График синусоидальной ЭДС")
plt.xlabel("t (секунды)")
plt.ylabel("Um (вх)")

# Устанавливаем пределы осей x и y
plt.xlim(0, 360)
plt.ylim(-6.3, 6.3)

# Устанавливаем параметры сетки
plt.grid(which='both', linestyle='--', linewidth=0.5, color='gray', markersize=10)

# Добавляем линии от точек до осей x и y
for i in range(len(x)):
    plt.vlines(x[i], 0, y[i], linestyles='dotted', colors='gray', linewidth=0.5)
    plt.hlines(y[i], 0, x[i], linestyles='dotted', colors='gray', linewidth=0.5)



plt.axhline(0, color='black', linewidth=0.5)

# Устанавливаем значения на осях X и Y
plt.xticks(x,t, rotation=45)
plt.yticks(y)

# Добавляем значения x на линию оси X
for i, val in enumerate(x):
    plt.text(val, 0, str(val)+'°', ha='right', va='top')

# Отображаем график
plt.show()
