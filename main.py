from flask import Flask, render_template, request, redirect
import sqlite3
import random

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def connect_db():
    """Connects to the database and returns a connection and cursor object"""
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    return conn, c

def add_employee_data(c, name, department, salary):
    """Inserts employee data into the database"""
    empl = [str(random.randint(100000, 9999999)), name, department.strip(), salary]
    c.execute('INSERT INTO employees VALUES (?, ?, ?, ?)', empl)
    c.connection.commit()  # commit changes to the database

def print_employee_data(c):
    """Prints all employee data in the database"""
    c.execute('SELECT * FROM employees')
    rows = c.fetchall()
    return rows

"""

def remove_employee_data(c, employee_id):
    #Removes an employee from the database by ID number
    c.execute('SELECT * FROM employees WHERE ID=?', (employee_id,))
    rows = c.fetchall()
    if len(rows) == 1:
        c.execute('DELETE FROM employees WHERE ID=?', (rows[0][0],))
        c.connection.commit()  # commit changes to the database

"""

@app.route('/')
def index():
    conn, c = connect_db()
    employees = print_employee_data(c)
    conn.close()
    return render_template('index.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    conn, c = connect_db()
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    name = first_name.strip() + " " + last_name.strip()
    department = request.form['department']
    salary = request.form['salary']
    add_employee_data(c, name, department, salary)
    conn.commit()
    conn.close()
    return redirect('/')

"""

@app.route('/remove', methods=['POST'])
def remove_employee():
    conn, c = connect_db()
    employee_id = request.form['employee_id']
    remove_employee_data(c, employee_id)
    employees = print_employee_data(c)
    conn.close()
    return render_template('index.html', employees=employees)

"""

if __name__ == '__main__':
    app.run(debug=True)
