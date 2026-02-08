def put_category(connection, category_id, category_name):
    cursor = connection.cursor()
    query = """UPDATE expense_tracker.categories SET category_name = %s
            WHERE category_id = %s"""
    cursor.execute(query, (category_id, category_name))
    connection.commit()
    cursor.close()