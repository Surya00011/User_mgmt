from flask import Flask, render_template, flash, request, redirect, url_for
from flask_mysqldb import MySQL



# # OR (recommended: use os.urandom for randomness)
# import os
# app.secret_key = os.urandom(24)

app = Flask(__name__)
# Set a secret key (must be unique & secret)
app.secret_key = "Hello@123"  # Simple key for demonstration

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mysql@123'
app.config['MYSQL_DB'] = 'crud'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM users"
    con.execute(sql)
    data=con.fetchall()
    return render_template('home.html', users=data)

# Add User
@app.route('/addUser', methods=['GET','POST'])
def addUser():
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        contact = request.form['contact']
        city = request.form['city']
        con = mysql.connection.cursor()
        sql = "INSERT INTO users(Name,Age,Contact,City) VALUES(%s,%s,%s,%s)"
        con.execute(sql,(name,age,contact,city))
        mysql.connection.commit()
        flash("User Added Successfully")
        return redirect(url_for('home'))
    return render_template('addUser.html')


# Edit User
@app.route('/editUser/<string:id>', methods=['GET','POST'])
def editUser(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        contact = request.form['contact']
        city = request.form['city']
        sql = "UPDATE users SET Name=%s, Age=%s, Contact=%s, City=%s WHERE ID=%s"
        con.execute(sql,(name, age, contact, city, id))
        mysql.connection.commit()
        flash("User Updated Successfully")
        return redirect(url_for('home'))
    sql = "SELECT * FROM users WHERE ID=%s"
    con.execute(sql,(id,))
    data = con.fetchone()
    return render_template('editUser.html', user=data)

# Delete User
@app.route('/deleteUser/<string:id>', methods=['GET','POST'])
def deleteUser(id):
    con = mysql.connection.cursor()
    sql = "DELETE FROM users WHERE ID=%s"
    con.execute(sql,(id,))
    mysql.connection.commit()
    flash("User Deleted Successfully")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)