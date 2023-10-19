import matplotlib.pyplot as plt

# Дані
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [1.5, 3.5, 5.5, 7.5, 9.5, 11.5, 13.5, 15.5, 17.5, 19.5]

# Побудова гістограми
plt.bar(x_values, y_values, width=0.8, align='center', alpha=0.7)

# Налаштування відображення
plt.xlabel('Ширина')
plt.ylabel('Довжина')
plt.title('Гістограма з вказаними даними')
plt.xticks(x_values)
plt.grid(True)

# Відображення графіку
plt.show()
