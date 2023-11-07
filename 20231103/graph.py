import math
import matplotlib.pyplot as plt
import numpy as np

# Известные параметры
rho_20 = 0.13  # Ом*мм^2/м
l_np = 1200     # м
d = 0.35        # мм
alpha_t = 0.00625  # 1/°C

# Расчет сопротивления для температур от 0°C до 500°C с шагом 1°C
temperatures = np.arange(0, 501, 1)
resistances = rho_20 * (4 * l_np) / (math.pi * (d ** 2) / (1 + alpha_t * (temperatures - 20)))

# Отображаемые значения температур
displayed_temperatures = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
displayed_resistances = []

# Находим соответствующие значения сопротивления для отображаемых температур
for temperature in displayed_temperatures:
    resistance = resistances[temperature]
    displayed_resistances.append(resistance)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(temperatures, resistances, color='blue', linewidth=2)
plt.scatter(displayed_temperatures, displayed_resistances, color='red', s=50, zorder=5)  # Отображение отмеченных точек
plt.scatter(0, resistances[0], color='red', s=50, zorder=5)  # Красная точка на X=0
plt.xlabel('Температура (°C)')
plt.ylabel('Сопротивление (Ом)')
plt.title('Зависимость сопротивления проводника от температуры')
plt.xticks(displayed_temperatures)  # Устанавливаем значения на оси X
plt.yticks(displayed_resistances)  # Устанавливаем значения на оси Y
plt.xlim(0, 550)  # Ограничение по оси X от 0 до 500
plt.ylim(0, 7000)  # Ограничение по оси Y
plt.grid(False)  # Убираем сетку

# Построение линий от красных точек к осям X и Y
for temperature, resistance in zip(displayed_temperatures, displayed_resistances):
    plt.plot([temperature, temperature], [0, resistance], color='gray', linestyle='--', linewidth=0.5)  # Линии по оси Y
    plt.plot([0, temperature], [resistance, resistance], color='gray', linestyle='--', linewidth=0.5)  # Линии по оси X

plt.show()
