from db import get_db_connection
from functions.users.post_user import post_user
from functions.users.get_users import get_users


db_connection = get_db_connection()

get_users(db_connection)