from flask import Flask
from flaskext.mysql import MySQL
from config import DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_DB

# Initialize MySQL
mysql = MySQL()

# Create the Flask app
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = DATABASE_HOST
app.config['MYSQL_DATABASE_PORT'] = DATABASE_PORT
app.config['MYSQL_DATABASE_USER'] = DATABASE_USER
app.config['MYSQL_DATABASE_PASSWORD'] = DATABASE_PASSWORD
app.config['MYSQL_DATABASE_DB'] = DATABASE_DB

mysql.init_app(app)

# Test the database connection
with app.app_context():
    conn = mysql.connect()
    cursor = conn.cursor()

    # Execute a sample query
    cursor.execute('SELECT 1')
    result = cursor.fetchone()
    print(result)

    # Close the database connection
    cursor.close()
    conn.close()
