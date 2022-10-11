import typer

app = typer.Typer()


@app.command()
def hello():
    typer.echo("Hello World")


@app.command()
def bye():
    typer.echo("Bye World")


if __name__ == "__main__":
    app()
