import sqlite3  
import os

def create_teble():
    connection = sqlite3.connect('save.db')
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS saves (savename TEXT, race TEXT, name TEXT, spec TEXT, mnt_pts INT, max_eng INT, max_hlt INT, cut_hlt INT,level INT, off_hand TEXT, main_hand TEXT, armour TEXT, stats TEXT, skill TEXT, abp INT, money INT, XP INT, inv TEXT, date TEXT)""")
    connection.commit()
    connection.close()
    
def view():
    os.system('cls')
    print(" Name \        Date")
    conn=sqlite3.connect("save.db")
    cur=conn.cursor()
    cur.execute("SELECT savename, date FROM saves")
    rows=cur.fetchall()
    conn.close()
    for i in rows:
        print(i)
        
def load(a):
    conn=sqlite3.connect("save.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM saves WHERE savename==?",(a,))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(a):
    conn=sqlite3.connect("save.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM saves WHERE savename=?",(a,))
    conn.commit()
    conn.close()

def add_row(savename, race, name, spec, mnt_pts, max_eng, max_hlt, cut_hlt, level, off_hand, main_hand, armour, stats, skill, abp, money, XP, inv, date):
    conn=sqlite3.connect("save.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO saves VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(savename, race, name, spec, mnt_pts, max_eng, max_hlt, cut_hlt, level, off_hand, main_hand, armour, stats, skill, abp, money, XP, inv, date))
    conn.commit()
    conn.close()
    
create_teble()