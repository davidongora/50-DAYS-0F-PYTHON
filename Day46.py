import pandas as pd # Creating a dictionary
table = {'year': [2009, 2002, 2009, 2010, 2009],
        'title': ["Brothers", "Spider-Man", "WatchMen", "Inception", "Avatar"],
        'genre': ["Drama", "Sci-fi", "Drama", "Sci-fi", "Fantasy"]}
movies = pd.DataFrame(table) 
print(movies)

# EXTRA CHALLENGE
import pandas as pd
# Accessing the website
web = pd.read_html("https://en.wikipedia.org/wiki/Python_(programming_language)") # Using slicing to get table number 1
table = web[1]
print(table)