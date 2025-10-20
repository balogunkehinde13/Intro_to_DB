import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update with your credentials)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
