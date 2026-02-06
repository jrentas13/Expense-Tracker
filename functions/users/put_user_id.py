def put_user_id(connection, user_id, username, email):
    cursor = connection.cursor()
    query = """UPDATE expense_tracker.users SET username = %s, email = %s" \
            WHERE user_id = %s """
    cursor.execute(query, (username, email, user_id))
    connection.commit()
    cursor.close()