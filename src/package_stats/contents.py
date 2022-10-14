from dataclasses import dataclass
from requests import get
from requests import HTTPError
from gzip import decompress
from bs4 import BeautifulSoup


@dataclass
class Contents:
    arch: str = "amd64"
    raw_dist_files: str = ""
    url: str = "http://ftp.uk.debian.org/debian/dists/stable/main/"
    contents_url = ""
    avaiable_arch = "amd64, arm64, armel, armhf, i386, mips, mips64el, mipsel, ppc64el, s390x, source"

    def get_dist_files(self):
        """
        Method in charge of get all the different names inside /debian/dists/stable/main/
        """
        avaible_arch = ["amd64", "arm64", "armel", "armhf", "i386", "mips", "mips64el", "mipsel", "ppc64el", "s390x", "source"]
        exists = [self.arch for architecture in avaible_arch if self.arch == architecture]
        if not exists:
            raise ValueError("The architecture doesn't exist")
        
        content = get(self.url)
        if content.status_code != 200:
            raise HTTPError(content.status_code)
        self.raw_dist_files = content.text

    def get_contents(self):
        """
        Method in charge of get the contents url related with the arch given
        """
        soup = BeautifulSoup(self.raw_dist_files, features="html.parser")
        dist_files_list = soup.find_all("a")

        for filename in dist_files_list:
            if "Contents" in filename.text and self.arch in filename.text and "udeb" not in filename.text:  # Just picking non udeb contents
                self.contents_url = f"{self.url}{filename.text}"

    def download_contents(self):
        """
        Method in charge of download the file and save it inside the runtime memory
        """
        with get(self.contents_url, stream=True) as buffer:
            if buffer.status_code != 200:
                raise HTTPError(buffer.status_code)
            extracted = decompress(buffer.content)
            self.packages = [line.decode() for line in extracted.split(b'\n')]
