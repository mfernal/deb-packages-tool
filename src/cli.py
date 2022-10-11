import typer
from src.

app = typer.Typer()


@app.command()
def show_statistics(arch: str = typer.Argument(
    "amd64",
    help="Architecture you want to check. Example: amd64, arm64, mips"
)):
    typer.echo("Hello World")


@app.command()
def bye():
    typer.echo("Bye World")


if __name__ == "__main__":
    app()
