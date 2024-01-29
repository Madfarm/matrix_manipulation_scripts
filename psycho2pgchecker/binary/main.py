import psycopg2

try:
    # Connection parameters
    conn_params = {
        'host': 'your_database_host',
        'database': 'your_database_name',
        'user': 'your_username',
        'password': 'your_password'
    }

    # Establish the connection
    conn = psycopg2.connect(**conn_params)

    # Create a cursor for executing queries
    cursor = conn.cursor()

    # Example: Check PostgreSQL version
    cursor.execute('SELECT version()')
    version = cursor.fetchone()
    print("PostgreSQL version:", version)

except (Exception, psycopg2.Error) as error:
    print("Error connecting to PostgreSQL:", error)

finally:
    # Close the communication with the database (important!)
    if conn:
        cursor.close()
        conn.close()
        print("Connection closed.")