# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:34:59 2024

@author: moniq
"""

############################################################
#
#   Importing and cleaning the data
#
############################################################

import pandas as pd

df = pd.DataFrame
df = pd.read_csv("movie_dataset.csv")

df.columns = df.columns.str.replace(' ', '_')

# avg_metascore = df["Metascore"].mean()
# rounded_average = math.ceil(avg_metascore)
# df["Metascore"].fillna(rounded_average, inplace=True)

# df.dropna(inplace=True)

############################################################
#
#   Question 1
#   What is the highest rated movie in the dataset?
#
############################################################

max_rating = df['Rating'].max()
max_rating_name = df.loc[df['Rating'].idxmax(), 'Title']

print("Movie name:", max_rating_name)


############################################################
#
#   Question 2
#   What is the average revenue of all movies in the dataset? 
#
############################################################

avg_revenue = df["Revenue_(Millions)"].mean()

print("Average Revenue:", avg_revenue)


############################################################
#
#   Question 3
#   What is the average revenue of movies from 2015 to 2017 in the dataset? 
#
############################################################

filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue = filtered_df['Revenue_(Millions)'].mean()

print("Average revenue of movies from 2015 to 2017:", average_revenue)


############################################################
#
#   Question 4
#   How many movies were released in the year 2016? 
#
############################################################

movies_2016_count = len(df[df['Year'] == 2016])

print("Number of movies released in 2016:", movies_2016_count)


############################################################
#
#   Question 5
#   How many movies were directed by Christopher Nolan? 
#
############################################################

nolan_movies_count = df['Director'].value_counts().get('Christopher Nolan', 0)

print("Number of movies directed by Christopher Nolan:", nolan_movies_count)


############################################################
#
#   Question 6
#   How many movies in the dataset have a rating of at least 8.0?
#
############################################################

high_rating_movies_count = len(df[df['Rating'] >= 8.0])

print("Number of movies with a rating of at least 8.0:", high_rating_movies_count)


############################################################
#
#   Question 7
#   What is the median rating of movies directed by Christopher Nolan?
#
############################################################

nolan_movies_median_rating = df[df['Director'] == 'Christopher Nolan']['Rating'].median()

print("Median rating of movies directed by Christopher Nolan:", nolan_movies_median_rating)


############################################################
#
#   Question 8
#   Find the year with the highest average rating? 
#
############################################################

average_rating_by_year = df.groupby('Year')['Rating'].mean()

year_highest_avg_rating = average_rating_by_year.idxmax()

print("Year with the highest average rating:", year_highest_avg_rating)


############################################################
#
#   Question 9
#   What is the percentage increase in number of movies made between 2006 and 2016? 
#
############################################################

movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

percentage_increase = ((len(movies_2016) - len(movies_2006)) / len(movies_2006)) * 100

print("Percentage increase in the number of movies between 2006 and 2016:", percentage_increase)


############################################################
#
#   Question 10
#   Find the most common actor in all the movies?
#
############################################################

all_actors = [actor.strip() for actors in df['Actors'] for actor in actors.split(',')]

most_common_actor = pd.Series(all_actors).mode().iloc[0]

print("Most common actor in all movies:", most_common_actor)


############################################################
#
#   Question 11
#   How many unique genres are there in the dataset?
#
############################################################

unique_genres = set(genre.strip() for genres in df['Genre'] for genre in genres.split(','))

num_unique_genres = len(unique_genres)

print("Number of unique genres in the dataset:", num_unique_genres)


############################################################
#
#   Question 12
#   Do a correlation of the numerical features, what insights can you deduce?
#
############################################################

from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Profiling Report")
profile.to_file("your_report.html")

numerical_features = df[['Rank','Year', 'Runtime_(Minutes)', 'Rating', 'Votes', 'Revenue_(Millions)', 'Metascore']]

correlation_matrix = numerical_features.corr()

print("Correlation Matrix:")
print(correlation_matrix)



























