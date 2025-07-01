import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Випадкове ядро
np.random.seed(42)

# Згенеруємо 500 фільмів
genres = ['Drama', 'Comedy', 'Action', 'Horror', 'Sci-Fi', 'Romance']
years = np.random.randint(1980, 2024, 500)
ratings = np.clip(np.random.normal(6.5, 1.0, 500), 1, 10)
data = {
    'title': [f'Film {i}' for i in range(500)],
    'genre': np.random.choice(genres, 500),
    'year': years,
    'rating': ratings.round(1)
}
df = pd.DataFrame(data)
df.head()
genre_rating = df.groupby("genre")["rating"].mean().sort_values()

plt.figure(figsize=(8, 5))
sns.barplot(x=genre_rating.values, y=genre_rating.index, palette="crest")
plt.title("Середній рейтинг фільмів за жанрами")
plt.xlabel("Середній рейтинг")
plt.ylabel("Жанр")
plt.tight_layout()
plt.show()
year_avg = df.groupby("year")["rating"].mean()

plt.figure(figsize=(10, 5))
sns.lineplot(x=year_avg.index, y=year_avg.values, marker='o')
plt.title("Зміна середнього рейтингу фільмів з роками")
plt.xlabel("Рік")
plt.ylabel("Середній рейтинг")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x="genre", y="rating", data=df, palette="Set2")
plt.title("Розподіл рейтингів по жанрах")
plt.xlabel("Жанр")
plt.ylabel("Рейтинг")
plt.tight_layout()
plt.show()
