import mysql.connector

def execute_query(query):
    db = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

if __name__ == "__main__":
    user_input = input("Enter a SQL query: ")
    results = execute_query(user_input)
    print(results)
