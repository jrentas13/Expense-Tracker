def post_user(connection, username, email):
    cursor = connection.cursor()
    query = "INSERT INTO expense_tracker.users (username, email) VALUES (%s, %s)"
    cursor.execute(query, (username, email))
    connection.commit()
    cursor.close()