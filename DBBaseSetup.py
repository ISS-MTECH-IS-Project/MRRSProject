# import sqlite3
# from sqlite3 import Error

# # For the rapid prototype, it uses objects and in memory
# # storage is mainly for trained data :
# # 1) All the pre-trained topics and their tokens
# # 2) Once a conclusion has been given, as a means to archive for further learning etc.

# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)

#     return conn


# def create_table(conn, create_table_sql):
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a CREATE TABLE statement
#     :return:
#     """
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)


# def DBBaseSetup():
#     database = ".\\myDB.db"

#     # arrays are all stringify
#     sql_create_question_table = "CREATE TABLE IF NOT EXISTS projects (" + \
#                                 " questionid integer PRIMARY KEY, " + \
#                                 " question text NOT NULL, " + \
#                                 " tokenArray text NOT NULL, " + \
#                                 " userInputArray text );" 

#     sql_create_topic_table = "CREATE TABLE IF NOT EXISTS topics (" + \
#                                 " topicid integer PRIMARY KEY, " + \
#                                 " name text NOT NULL, " + \
#                                 " type text NOT NULL, " + \
#                                 " factSheet text, " + \
#                                 " tokenArray text NOT NULL, " + \
#                                 " questionArray text, " + \
#                                 " symptomArray text, " + \
#                                 " conditionArray text );" # stringfyArray

#     # create a database connection
#     conn = create_connection(database)

#     # create tables
#     if conn is not None:
#         # create projects table
#         create_table(conn, sql_create_question_table)

#         # create tasks table
#         create_table(conn, sql_create_topic_table)
#     else:
#         print("Error! cannot create the database connection.")


# #if __name__ == '__main__':
# DBBaseSetup()