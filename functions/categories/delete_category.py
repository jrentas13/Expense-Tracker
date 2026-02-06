def delete_category(connection, category_id):
    cursor = connection.cursor()
    query = "DELETE FROM expense_tracker.categories WHERE category_id = %s"
    cursor.execute(query, (category_id))
    cursor.commit()
    cursor.close()