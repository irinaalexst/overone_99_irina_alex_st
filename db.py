import sqlite3

#create class database in order to connect
class Database:
    def __init__(self,db):
        #to create table for our db/Open a cursor to perform database operations
        #this creates a new table
        #cursor — это объект в памяти компьютера с методами для проведения SQL команд, хранения итогов
        # их выполнения (например части таблицы или вьюшкы (view)) и методов доступа к ним.
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS organiser (id INTEGER PRIMARY KEY,data_text,weight_text,sleep_text,food_text)")
        #write info to db and close it.without data will be lost
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM organiser;")
    #get all the rows
        rows = self.cur.fetchall()
        return rows

    def insert(self,data,weight,sleep,food):
        self.cur.execute("INSERT INTO organiser VALUES(NULL,?,?,?,?)",(data,weight,sleep,food))
        self.conn.commit()

    #to know which part we delete
    def remove(self,id):
        #comma after id, cause we set only one value
        self.cur.execute("DELETE FROM organiser WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,data,weight,sleep,food):
        self.cur.execute("UPDATE organiser SET data=?,weight=?,sleep=?,food=? WHERE id=?",
        (data,weight,sleep,food,id))
        self.conn.commit()
    #in case if all references to the object has been deleted
    def __del__(self):
        self.conn.close()


#create db in order to call all the methods
db = Database('store.db')