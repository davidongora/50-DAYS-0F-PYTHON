import sqlite3
con = sqlite3.connect('movies.db')
cur = con.cursor()
# Creating a table in the database
cur.execute('CREATE TABLE movies(year,title, genre)')
# Creating a variable of all the movies
movies = [(2009, 'Brothers', 'Drama'), 
          (2002, 'Spider-Man', 'Sci-fi'),
          (2009, 'WatchMen', 'Drama'), 
          (2010, 'Inception', 'Sci-fi'), 
          (2009, 'Avatar', 'Fantasy')]
cur .executemany('''INSERT INTO movies VALUES(?, ?, ?); ''', movies)
# commit and close
con.commit()
con.close()

con = sqlite3.connect('movies.db') 
cur = con.cursor()
row = cur.fetchall()
for row in cur.execute('SELECT * FROM Movies;'):
    print(row)

con = sqlite3.connect('movies.db')
cur = con.cursor()
row = cur.fetchall()
for row in cur.execute('SELECT * FROM Movies WHERE ' 'title ="Brothers";'):
    print(row)
    
con = sqlite3.connect('movies.db')
cur = con.cursor()
row = cur.fetchall()
for row in cur.execute('SELECT * FROM Movies WHERE '
'year = 2009'):
    print(row)
    
con = sqlite3.connect('movies.db')
cur = con.cursor()
row = cur.fetchall()
for row in cur.execute('SELECT * FROM Movies WHERE ''genre = "Fantasy" OR genre = "Drama";'):
    print(row)
    
con = sqlite3.connect('movies.db') 
cur = con.cursor() 
cur.execute('DELETE FROM movies;')
con.commit()