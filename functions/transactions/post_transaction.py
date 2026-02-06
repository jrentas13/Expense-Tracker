def post_transaction(connection, user_id, category_id, amount, transaction_type, description):
    cursor = connection.cursor()
    query = """INSERT INTO expense_tracker.transaction (user_id, category_id, amount, transaction_type, description)
            VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, (user_id, category_id, amount, transaction_type, description))
    cursor.commit()
    cursor.close()