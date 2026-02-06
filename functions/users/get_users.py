def get_users(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM expense_tracker.users"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    return rows