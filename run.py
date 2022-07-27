import psycopg2

# Connect to chinook database - You can include password values and other values also but not needed for this.
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database - Anything that is queried from the database becomes part of this cursor object
cursor = connection.cursor()

# QUERIES - always use single quotes to wrap query, and double quotes for particular values. psycopg2 is very precise with quotes
# To see any of these queries work, just uncomment the one that you want to see work. They won't all work together at the same time.
# query 1:
# cursor.execute('SELECT * FROM "Artist"')

# query 2:
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3: - If only getting a single record, using Where to specify etc, we need to enter python string (%s)
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 4: - same as query 3,  python string (%s) however notice that we can use different data types in the array. This time it's int rather than string.
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5: - same as query 4 but accessing different table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Fetch all results from the cursor object.
results = cursor.fetchall()

# Once results have been fetched - need to end the connection to the database, so it's not always active
connection.close()

# Print results

for result in results:
    print(result)