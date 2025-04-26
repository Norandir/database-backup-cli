import typer
from .db_connection import get_connection
import subprocess
import os


def backup_command(
    db_type: str = typer.Option(..., help="Type of the database (e.g., postgres, mysql)"),
    host: str = typer.Option("localhost", help="Database host"),
    port: int = typer.Option(..., help="Database port"),
    username: str = typer.Option(..., help="Database username"),
    password: str = typer.Option(..., prompt=True, hide_input=True, help="Database password"),
    dbname: str = typer.Option(..., help="Database name"),
    output: str = typer.Option("./backups", help="Output directory for backups"),
    backup_type: str = typer.Option("full", help="Backup type: full, incremental, differential")
):
    #if output does not exit creat it
    if not os.path.exists(output):
             os.makedirs(output)
    
    # Placeholder logic
    typer.echo(f"Backing up {db_type} database '{dbname}' on {host}:{port} as a {backup_type} backup...")

    connection = get_connection(db_type, host, port, username, password, dbname)

    if db_type == "postgres" and backup_type == "full":
        

        # Define the backup file path
        backup_file = os.path.join(output, f"{dbname}_full_backup.sql")

        try:
            # subprocess.run allows us to run the shell command pg_dump
            subprocess.run(
                ["pg_dump", "-h", host, "-p", str(port), "-U", username, "-d", dbname, "-F", "c", "-f", backup_file],
                check=True, env={"PGPASSWORD": password}  # Set the password in the environment variable
            )
            print(f"Backup successful! The backup file is saved at {backup_file}")
        
        except subprocess.CalledProcessError as e:
            print(f"Error during backup: {e}")
        
        finally:
            # 4. Close the database connection (if applicable)
            if connection:
                connection.close()
                print("Database connection closed.")

    elif db_type == "mysql" and backup_type == "full":
        # Define the backup file path
        backup_file = os.path.join(output, f"{dbname}_full_backup.sql")

        try:
            # Using `env` to avoid exposing the password in the command line
            env = os.environ.copy()
            env["MYSQL_PWD"] = password


            with open(backup_file, "w", encoding="utf-8") as out_file:
                subprocess.run(
                    ["mysqldump", "-h", host, "-P", str(port), "-u", username, dbname],
                    check=True,
                    stdout=out_file,  # Output to backup file
                    env=env  # Set the environment variable for password
                )
                print(f"Backup successful! The backup file is saved at {backup_file}")
        
        except subprocess.CalledProcessError as e:
            print(f"Error during backup: {e}")
        
        finally:
            # 4. Close the database connection (if applicable)
            if connection:
                connection.close()
                print("Database connection closed.")




#Placeholder command 
def tester(name:str = typer.Option("test", help="Placeholder")):
    typer.echo("Hello World")
