def get_user_id(connection, user_id):
    cursor = connection.cursor()
    query = "SELECT * FROM expense_tracker.users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close
    return user