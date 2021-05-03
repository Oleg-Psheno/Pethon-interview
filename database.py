import sqlite3

db = 'sqlite.db'


def creation_categories(db=db):
    conn = sqlite3.connect(db)
    conn.execute('DROP TABLE IF EXISTS categories;')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS categories(
        category_name VARCHAR(36) NOT NULL PRIMARY KEY,
        category_description VARCHAR(255));
    """)
    conn.commit()
    conn.close()


def creation_units(db=db):
    conn = sqlite3.connect(db)
    conn.execute('DROP TABLE IF EXISTS units;')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS units(
        unit VARCHAR(36) NOT NULL PRIMARY KEY);
    """)
    conn.commit()
    conn.close()


def creation_positions(db=db):
    conn = sqlite3.connect(db)
    conn.execute('DROP TABLE IF EXISTS positions;')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS positions(
        position VARCHAR(36) NOT NULL PRIMARY KEY);
    """)
    conn.commit()
    conn.close()


def creation_goods(db=db):
    conn = sqlite3.connect(db)
    conn.execute('DROP TABLE IF EXISTS goods;')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS goods(
        good_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        good_name VARCHAR(255),
        good_unit VARCHAR(36),
        good_cat VARCHAR,
        FOREIGN KEY (good_cat) REFERENCES  categories(category_name),
        FOREIGN KEY (good_unit) REFERENCES units(unit));
    """)
    conn.commit()
    conn.close()


def creation_employees(db=db):
    conn = sqlite3.connect(db)
    conn.execute('DROP TABLE IF EXISTS employees;')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        employe_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        employee_fio VARCHAR(255),
        employee_position VARCHAR(36),
        FOREIGN KEY (employee_position) REFERENCES positions(position));
    """)
    conn.commit()
    conn.close()


def creation_vendors(db=db):
    conn = sqlite3.connect(db)
    conn.execute('DROP TABLE IF EXISTS vendors;')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS vendors(
        vendor_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        vendor_name VARCHAR(255),
        vendor_ownerchipform VARCHAR ,
        vendor_address VARCHAR,
        vendor_phone VARCHAR(15),
        vendor_email VARCHAR );
    """)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    '''
    Внимание: запуск этого метода очистит БД!
    '''
    confirm = input('Подтвердите действие, введите 1 для продолжения: ')
    if confirm == '1':
        creation_categories()
        creation_units()
        creation_positions()
        creation_goods()
        creation_employees()
        creation_vendors()
