import matplotlib.pyplot as plt

# Пример данных
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='--')
plt.title('Пример графика с использованием Matplotlib')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
