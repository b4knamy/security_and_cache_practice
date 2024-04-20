import sqlite3

def db_execute(command, save=False):

    with sqlite3.connect('data.db') as db:
        cursor = db.cursor()

        if save:
            try:
                cursor.execute(command)
            except Exception as error:
                print(f'Error: {error}')
            finally:
                db.commit()
                return
        
        try:
            data = cursor.execute(command)
        except Exception as error:
            data = None
            print(f'Error: {error}')
        finally:
            return data




        #    CODE TO CREATE THE DATAS

# from faker import Faker

# fk = Faker(locale=['pt_BR'])
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE if not exists names (
#             id integer primary key autoincrement not null,
#             name varchar not null
#                );""")
# cursor.execute("""
# CREATE TABLE if not exists domain (
#                id integer primary key autoincrement not null,
#                domain varchar(200) not null
# );
# """)

# for _ in range(100):
#     f_name = fk.name()
#     cursor.execute(f"""INSERT INTO names (name) VALUES ("{f_name}");""")

# cursor.close()
# conn.commit()
