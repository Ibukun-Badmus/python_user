import mysql.connector

from mysql.connector import Error


def connect_insert():
    """function to connect and insert a row in a database"""

    # create a variable for the connector object
    conn = None

    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='firsttable',
            user='Ibukun',
            password='oluwaibukun')
        print('Connecting to database')
        if conn.is_connected:
            print('connected to the database')
            db_cursor = conn.cursor()

        # create a variable to contain the sql query to be executed
        sql = "INSERT INTO Human (name, color, gender, bloodgroup, age) VALUES (%s, %s, %s, %s, %s)"

        # craete a list variable to contain all the values we want to insert into the database
        val = [
            # ('Hannah', 'White', 'Female', 'B-', 25),
            ('1009', 'Michael', 'brown', 'Male', 45),
            ('1010', 'Sandy', 'Black', 'Male', 56),
            ('1011', 'Green', 'Yellow', 'Male', 67),
            ('1012', 'Richard', 'Black', 'Wale', 60)
        ]

        # esecute the query using the executemany function
        db_cursor.executemany(sql, val)

        # commit to the database
        conn.commit()

        # print a success message
        print(db_cursor.rowcount, "rows was inserted.")

        # close the cursor
        db_cursor.close()

    except Error as e:
        print('connection failed due to the following:', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close
            print('Disconnected from database')


# call the function we just created
connect_insert()
