import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="movie_pipeline",
    port=3306
)

print("✅ Direct PyMySQL connection successful!")
connection.close()
