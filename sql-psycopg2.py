import psycopg2 

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

# Query1 

# cursor.execute('SELECT * FROM "artist"')

# cursor.execute('SELECT "name" FROM "artist"')

# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', [51])

# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

# cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Nando Reis"])

cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["test"])

results = cursor.fetchall()

# results = cursor.fetchone()

connection.close()

for result in results:
    print(result)