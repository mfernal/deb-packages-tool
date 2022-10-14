import pytest
from src.package_stats.contents import Contents


@pytest.fixture
def contents():
    return Contents("amd64")


@pytest.fixture
def contents_wrong():
    return Contents("am4")


def test_architecture(contents_wrong):
    with pytest.raises(ValueError):
        contents_wrong.get_dist_files()
