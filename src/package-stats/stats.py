from dataclasses import dataclass
from requests import get
from requests import HTTPError

@dataclass
class Stats:
    url: str

    def get_stats(self) -> str:
        content = get(self.url)
        if not content:
            raise HTTPError(content.status_code)
        return content.text