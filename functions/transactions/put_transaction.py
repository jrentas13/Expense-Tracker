def put_transaction(connection, transaction_id, user_id, category_id, amount, transaction_type, description):
    cursor = connection.cursor()
    query = """UPDATE expense_tracker.transaction SET user_id = %s, category_id = %s,
            amount = %s, transaction_type = %s, description = %s
            WHERE transaction_id = %s"""
    cursor.execute(query, (user_id, category_id, amount, transaction_type, description, transaction_id))
    cursor.commit()
    cursor.close()