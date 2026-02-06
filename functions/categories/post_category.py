def post_category(connection, category_name):
    cursor = connection.cursor()
    query = "INSERT INTO expense_tracker.categories (category_name) VALUE (%s)"
    cursor.execute(query, (category_name))
    cursor.commit()
    cursor.close()