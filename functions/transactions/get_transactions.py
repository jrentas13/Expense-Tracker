def get_transactions(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM expense_tracker.transactions"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    return rows