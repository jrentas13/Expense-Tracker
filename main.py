from db import get_db_connection
from functions.transactions.post_transaction import post_transaction
from functions.categories.post_category import post_category
from functions.transactions.get_transactions import get_transactions


db_connection = get_db_connection()

post_transaction(db_connection, 1, 1, 25, 'payment', 'Bought McDonalds')
get_transactions(db_connection)