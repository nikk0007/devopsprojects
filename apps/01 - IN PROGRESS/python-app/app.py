from flask import Flask, render_template, request
import mysql.connector
from pymemcache.client import base as memcache

from config import DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_DB
from config import MEMCACHE_HOST, MEMCACHE_PORT

app = Flask(__name__)
mc = memcache.Client((MEMCACHE_HOST, MEMCACHE_PORT))

# Connect to the MySQL database
db = mysql.connector.connect(
    host=DATABASE_HOST,
    port=DATABASE_PORT,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    database=DATABASE_DB
)

# # Create the employee table if it doesn't exist
# cursor = db.cursor()
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS employee (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         employee_number INT,
#         name VARCHAR(255),
#         designation VARCHAR(255)
#     )
# """)
# db.commit()


@app.route('/')
def home():
    hostname = request.host.split(':')[0]
    memcache_data = mc.get('employee_data')
    db_data = fetch_data_from_db()
    return render_template('home.html', hostname=hostname, memcache_data=memcache_data, db_data=db_data)


@app.route('/check-memcache')
def check_memcache():
    memcache_data = mc.get('employee_data')
    hostname = request.host.split(':')[0]
    db_data = fetch_data_from_db()
    return render_template('home.html', hostname=hostname, memcache_data=memcache_data, db_data=db_data)


@app.route('/fetch-data')
def fetch_data():
    # Fetch data from the database
    db_data = fetch_data_from_db()
    mc.set('employee_data', db_data)
    hostname = request.host.split(':')[0]
    memcache_data = mc.get('employee_data')
    return render_template('home.html', hostname=hostname, memcache_data=memcache_data, db_data=db_data)


def fetch_data_from_db():
    cursor = db.cursor()
    cursor.execute("SELECT employee_number, name, designation FROM employee")
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in result]
    return data


@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        employee_number = request.form['employee_number']
        name = request.form['name']
        designation = request.form['designation']
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO employee (employee_number, name, designation)
            VALUES (%s, %s, %s)
        """, (employee_number, name, designation))
        db.commit()
        mc.delete('employee_data')  # Clear memcache data after adding a new employee
        return 'Employee added successfully!'

    return render_template('add_employee.html')


@app.route('/health')
def health():
    return 'App is healthy!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
