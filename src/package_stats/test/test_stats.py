import pytest
from src.package_stats.stats import Stats


@pytest.fixture
def stats():
    stats = Stats("amd64")
    stats.get_dist_files()
    stats.get_contents()
    stats.download_contents()
    return stats


@pytest.fixture
def stats_with_count():
    stats = Stats("amd64")
    stats.get_dist_files()
    stats.get_contents()
    stats.download_contents()
    stats.count_packages()
    return stats


def test_files_packages_count_not_empty(stats):
    stats.count_packages()
    assert stats.packages_count != {}


def test_not_empty_output(capfd, stats_with_count):
    stats_with_count.show_top_10()
    out, err = capfd.readouterr()
    assert out != ""
