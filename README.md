# Company DB — A Business Simulation in Python & SQLite

Learning how a company is structured and run by modeling one as a relational
database — built incrementally over four weeks, starting from a three-person
founding team and growing into a full organization.

## Why this project

Two goals at once:

1. **Understand how a business actually works** — departments, roles and
   responsibilities, reporting hierarchy, how HR / Operations / Engineering
   function, and how money flows in and out.
2. **Strengthen database skills** — by modeling that company in SQLite, since
   you can't model a business without first understanding its structure. The
   modeling *is* the learning.

## Current status

**Week 1 · Day 1 complete** — a single `employees` table seeded with the
founding team (CEO, CTO, and the first senior engineer).

## Tech

- **Python 3** — standard library only. Uses the built-in `sqlite3` module, so
  there are no dependencies to install.
- **SQLite** — a single-file relational database.

## Getting started

```bash
python3 day1.py
```

This creates `company.db` (if it doesn't already exist) and prints the founding
team to the terminal.

## Project structure

```
.
├── day1.py      # creates the employees table and seeds the founding team
├── README.md
└── .gitignore
```

> **Note:** `company.db` is *generated* by running the script and is
> deliberately **not** committed to git (see `.gitignore`). The Python code is
> the source of truth; the database file is just a build artifact you can
> recreate any time by re-running the script.

## Roadmap

- **Week 1 — Foundations.** What a business is; first tables; first
  relationships. Model people and structure.
- **Week 2 — People & roles.** Departments, the full hierarchy
  (junior → senior → lead → manager → director → C-suite), reporting lines, and
  what each designation is responsible for. Foreign keys and linking tables.
- **Week 3 — How the company runs.** Projects, tasks, and day-to-day work; how
  HR, Operations, and Engineering hand work to each other; payroll, revenue, and
  costs. Joins and queries that answer real business questions.
- **Week 4 — Bring it alive.** Simulate time passing — run the company for a
  month, hire as it grows, and build the reports a manager uses to make
  decisions.

## Progress log

- **Day 1** — Set up SQLite from Python; created the `employees` table; seeded
  the founding team. *Concepts learned:* connections and cursors, `CREATE
  TABLE` and column types, parameterized inserts (`?` placeholders) and why they
  prevent SQL injection, and `commit()` / persistence.