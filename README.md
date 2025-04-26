# Database Backup CLI Tool

## Description

A cross-database command-line application to connect to PostgreSQL and MySQL servers and create full backups easily. Built for developers, database admins, and hobbyists needing a quick and customizable backup solution.

## Features

- CLI interface for managing database backups
- Supports PostgreSQL and MySQL databases
- Full backup functionality for both database types
- Connection validation and error handling
- Secure password input
- Customizable backup file output directory

## Installation Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/your-norandir/backupcli.git
   ```

2. Navigate into the project directory:

   ```bash
   cd backupcli
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional but recommended) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage

Run the CLI using:

```bash
python -m dbtool.main backup --db-type <postgres/mysql> --host <host> --port <port> --username <username> --dbname <dbname> --output <path>
```

It will securely prompt you for your database password.

Example:

```bash
python -m dbtool.main backup --db-type postgres --host localhost --port 5432 --username admin --dbname testdb
```

## Tech Stack

- **Python 3**
- **Typer** for CLI creation
- **psycopg2** for PostgreSQL connections
- **mysql-connector-python** for MySQL connections
- **subprocess** module for running backup utilities (`pg_dump`, `mysqldump`)
- **OS** and **Pathlib** for file and path management

