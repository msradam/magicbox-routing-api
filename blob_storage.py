import psycopg2 

connection = psycopg.connect("dbname=test")
cursor = connection.cursor(  )

cursor.execute("CREATE TABLE justatest (name TEXT, ablob BYTEA)")

try:
	names = 'aramis', 'athos', 'porthos'
	data = {})
