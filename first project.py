import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Генерація випадкових даних
np.random.seed(42)
months = pd.date_range(start="2023-01-01", end="2023-12-01", freq='MS')
categories = ["Одяг", "Взуття", "Аксесуари", "Спорттовари"]

data = []
for month in months:
    for category in categories:
        sales = np.random.randint(200, 1500)
        revenue = sales * np.random.randint(20, 100)
        data.append([month, category, sales, revenue])

df = pd.DataFrame(data, columns=["Місяць", "Категорія", "Кількість продажів", "Дохід"])

print(df.head())

monthly_revenue = df.groupby("Місяць")["Дохід"].sum().reset_index()
plt.figure(figsize=(12, 5))
plt.plot(monthly_revenue["Місяць"], monthly_revenue["Дохід"], marker='o', linewidth=2)
plt.title("Загальний дохід по місяцях")
plt.xlabel("Місяць")
plt.ylabel("Дохід (грн)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


category_revenue = df.groupby("Категорія")["Дохід"].sum().sort_values()
plt.figure(figsize=(8, 5))
sns.barplot(x=category_revenue.values, y=category_revenue.index, palette="Blues_d")
plt.title("Дохід по категоріях товарів")
plt.xlabel("Дохід (грн)")
plt.ylabel("Категорія")
plt.tight_layout()
plt.show()

