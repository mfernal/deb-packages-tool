import typer
from src.package_stats.stats import Stats

app = typer.Typer()


@app.command()
def show_statistics(arch: str = typer.Argument(
    "amd64",
    help="Architecture you want to check. Example: amd64, arm64, mips"
)):
    stats = Stats(arch=arch.lower())
    stats.get_dist_files()
    stats.get_contents()
    stats.download_contents()
    stats.count_packages()
    stats.show_top_10()
