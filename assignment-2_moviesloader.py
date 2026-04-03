import pandas as pd
movies = pd.read_csv("movies.csv")


#print(movies)
#print(movies.shape)
#print(movies.head())
#print(movies.info())
#print(movies.describe())
best_movie = movies.loc[movies["Rating"].idxmax()]

print(best_movie)

total_revenue = movies["Revenue"].sum()

print("Total Revenue:", total_revenue)


genre_rating = movies.groupby("Genre")["Rating"].mean()

print(genre_rating)


recent_movies = movies[movies["Year"] > 2010]

print(recent_movies)



import numpy as np

revenue_array = np.array(movies["Revenue"])

print(revenue_array)
