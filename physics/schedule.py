import matplotlib.pyplot as plt
import numpy as np

# Значення з таблиці
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [1.5, 3.5, 5.5, 7.5, 9.5, 11.5, 13.5, 15.5, 17.5, 19.5]

# Побудова графіку
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.title('Траєкторія руху вантажу')
plt.xlabel('Горизонтальна відстань (м)')
plt.ylabel('Вертикальна відстань (м)')
plt.grid(True)

# Позначення точок на графіку
for i, (x, y) in enumerate(zip(x_values, y_values)):
    plt.text(x, y, f'({x}, {y})', fontsize=12, ha='right' if i % 2 == 0 else 'left', va='bottom' if i % 2 == 0 else 'top')

plt.show()
