
import typer
from .backup import backup_command
from .backup import tester

app = typer.Typer()

# Register the function as a CLI command with a custom name
app.command(name="backup")(backup_command)
app.command(name="Test")(tester)