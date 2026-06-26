import sqlite3

conn = sqlite3.connect("company.db")
cursor  = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT  NOT NULL,
    designation TEXT NOT NULL,
    department TEXT,
    salary INTEGER,
    hire_date TEXT
)
""")

founders = [
    ('Anil Singh', 'Founder & Ceo', 'Leadership', 0, '2024-01-01'),
    ('Vineet Singh', 'Co-Founder & CTO', 'Leadership', 0, '2024-01-01'),
    ('Asha Rao', 'Senior Software Engineer', 'Engineering', 1800000, '2024-02-15'),
    ('Satakshi Roy', 'Junior Software Engineer', 'Engineering', 1000000, '2024-05-15'),
    ('Priya Verma', 'HR Manager', 'Human Resource', 3000000, '2024-05-15')
]

cursor.executemany(
    "INSERT INTO employees (name, designation, department, salary, hire_date) VALUES (?, ?, ?, ?, ?)", founders
)

conn.commit()


cursor.execute('SELECT * FROM employees')
for row in cursor.fetchall():
    print(row)

conn.close()

