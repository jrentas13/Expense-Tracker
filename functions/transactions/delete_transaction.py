def delete_transaction(connection, transaction_id):
    cursor = connection.cursor()
    query = "DELETE FROM expense_tracker.transactions WHERE transaction_id = %s"
    cursor.execute(query, (transaction_id))
    cursor.commit()
    cursor.close()