def delete_user(connection, user_id):
    cursor = connection.cursor()
    query = "DELETE FROM expense_tracker.users WHERE user_id = %s"
    cursor.execute(query, (user_id))
    cursor.commit()
    cursor.close()