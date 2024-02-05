# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:39:42 2024

@author: vmbay
"""
# QUESTION 1 cleaning the data
import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print(df)
print(df.info())
df.dropna(inplace = True)
df = df.reset_index(drop=True)
print(df)
print(df.info())
# Sample dataset (replace this with your actual dataset)
movie_dataset = df
  
# This code filters the DataFrame to include only rows where the 'Rating' column is equal to the maximum rating in the dataset, and then it prints the title and rating of the highest-rated movie.


import pandas as pd

#  my DataFrame is named df herein referred to as movie_data:
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]

print("Highest-rated movie:")
print(highest_rated_movie[['Title', 'Rating']])

# My DataFrame/movie_dataset is named df
# This code first filters the DataFrame to include only rows where the 'Year' column is between 2015 and 2017 (inclusive), and then it calculates the mean (average) of the 'Revenue (Millions)' column in the filtered DataFrame. The result is printed formatted as currency with two decimal places.



# QUESTION 2
average_revenue = df['Revenue (Millions)'].mean()

print("Average Revenue of All Movies: ${:,.2f}".format(average_revenue))

# QUESTION 2 second method
# Another code for calculating the average_revenue is:

# Calculate the average revenue of all movies
average_revenue = df['Revenue (Millions)'].mean()

# Display the result
print(f"The average revenue of all movies in the dataset is {average_revenue:.2f} million dollars.")



# QUESTION 3
# Convert the 'Year' column to datetime format
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Filter the DataFrame for movies released from 2015 to 2017
filtered_df = df[(df['Year'] >= '2015-01-01') & (df['Year'] <= '2017-12-31')]

# Calculate the average revenue of movies from 2015 to 2017
average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

# Display the result
print(f"The average revenue of movies from 2015 to 2017 is {average_revenue_2015_to_2017:.2f} million dollars.")




# QUESTION 4
import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print(df)
print(df.info())


# Assuming 'df' is your DataFrame
# If not, load your DataFrame using pd.read_csv() or other methods

# Filter the DataFrame for movies released in the year 2016
movies_2016 = df[df['Year'] == 2016]

# Get the count of movies released in 2016
num_movies_2016 = len(movies_2016)

# Print the result
print(f"The number of movies released in the year 2016 is: {num_movies_2016}")




# QUESTION 5
import pandas as pd

# Assuming 'df' is your DataFrame
# If not, load your DataFrame using pd.read_csv() or other methods

# Filter the DataFrame for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Get the count of movies directed by Christopher Nolan
num_nolan_movies = len(nolan_movies)

# Print the result
print(f"The number of movies directed by Christopher Nolan is: {num_nolan_movies}")





# QUESTION 6

import pandas as pd

# Assuming you have the DataFrame as described in your provided information
# df = ... (your DataFrame)

# Filter the DataFrame for movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]

# Count the number of such outstanding movies
number_of_high_rated_movies = len(high_rated_movies)

# Display the result
print(f"The number of movies in the dataset with a rating of at least 8.0 is {number_of_high_rated_movies}.")





# QUESTION 7

import pandas as pd

# Assuming you have the DataFrame as described in your provided information
# df = ... (your DataFrame)

# Filter the DataFrame for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies['Rating'].median()

# Display the result
print(f"The median rating of movies directed by Christopher Nolan is {median_rating_nolan_movies}.")

# QUESTION 8

import pandas as pd

# Assuming you have the DataFrame as described in your provided information
# df = ... (your DataFrame)

# Calculate the average rating for each year
average_rating_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

# Display the result
print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}.")

# QUESTION 9

import pandas as pd

# Assuming you have the DataFrame as described in your provided information
# df = ... (your DataFrame)

# Filter the DataFrame for movies made in 2006 and 2016
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

# Count the number of movies made in each year
count_2006 = len(movies_2006)
count_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((count_2016 - count_2006) / count_2006) * 100

# Display the result
print(f"The percentage increase in the number of movies made between 2006 and 2016 is {percentage_increase:.2f}%.")



# QUESTION 10

import pandas as pd

# Assuming you have the DataFrame as described in your provided information
# df = ... (your DataFrame)

# Split the multiple actors in the "Actors" column and create a new DataFrame
actors_df = df['Actors'].str.split(', ', expand=True)

# Reshape the DataFrame to have one column for each actor
actors_list = actors_df.values.flatten()

# Create a Series to count the occurrences of each actor
actors_count = pd.Series(actors_list).value_counts()

# Get the most common actor
most_common_actor = actors_count.idxmax()

# Display the result
print(f"The most common actor in all the movies is: {most_common_actor}")




# QUESTION 11


import pandas as pd

# Assuming you have the DataFrame as described in your provided information
# df = ... (your DataFrame)

# Split the multiple genres in the "Genre" column and create a new DataFrame
genres_df = df['Genre'].str.split(', ', expand=True)

# Reshape the DataFrame to have one column for each genre
genres_list = genres_df.values.flatten()
# Assuming the dataset has a 'Genres' column, replace it with your actual column name
genres_column = 'Genre'
# Extract unique genres from the dataset
unique_genres = df[genres_column].str.split(',').explode().str.strip().unique()
# Count the number of unique genres
num_unique_genres = len(unique_genres)
# Print the result

print(f"The number of unique genres in the dataset is: {num_unique_genres}")












