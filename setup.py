import sqlite3

conn = sqlite3.connect("company.db")
cur  = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")

cur.execute("DROP TABLE IF EXISTS employees")
cur.execute("DROP TABLE IF EXISTS departments")

cur.execute("""
CREATE TABLE IF NOT EXISTS departments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    annual_budget INTEGER,
    cost_center TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT  NOT NULL,
    designation TEXT NOT NULL,
    department_id INTEGER,
    salary INTEGER,
    hire_date TEXT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
)
""")

departments = [
    ("Leadership", 0, "CC-100"),
    ("Engineering", 20000000, "CC-200"),
    ("HR", 5000000, "CC-300"),
]
cur.executemany(
    "INSERT INTO departments (name, annual_budget, cost_center) VALUES (?, ?, ?)", departments
)

cur.execute("SELECT id, name FROM departments")
dept_id = {name: id for id, name in cur.fetchall()}

founders = [
    ('Anil Singh', 'Founder & Ceo', dept_id['Leadership'], 0, '2024-01-01'),
    ('Vineet Singh', 'Co-Founder & CTO', dept_id['Leadership'], 0, '2024-01-01'),
    ('Asha Rao', 'Senior Software Engineer', dept_id['Engineering'], 1800000, '2024-02-15'),
    ('Satakshi Roy', 'Junior Software Engineer', dept_id['Engineering'], 1000000, '2024-05-15'),
    ('Priya Verma', 'HR Manager', dept_id['HR'], 3000000, '2024-05-15')
]

cur.executemany(
    "INSERT INTO employees (name, designation, department_id, salary, hire_date) VALUES (?, ?, ?, ?, ?)", founders
)


conn.commit()
conn.close()
print("Database built. Departments and employees seeded.")

