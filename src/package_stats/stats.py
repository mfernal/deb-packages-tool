from src.package_stats.contents import Contents
from typing import Dict, List
from collections import Counter
from dataclasses import dataclass


@dataclass
class Stats(Contents):
    packages = List[str]
    packages_count = Dict[str, int]

    def count_packages(self):
        """
        Method in charge of count the number of files inside a package
        """
        packages_list = [str]
        for package in self.packages:
            package = package.split(' ')
            package = list(filter(None, package))
            if len(package) == 2:  # select only tuple of info filename package
                packages_list.append(package[1])
        self.packages_count = Counter(packages_list)
        self.packages_count = dict(sorted(self.packages_count.items(), key=lambda item: item[1], reverse=True))

    def show_top_10(self):
        """
        Method in charge of show the top 10 packages sorted by number of files
        """
        print(f"{'No.':<15}\t{'Package Name':<60}\tFiles")
        for i, (name, count) in enumerate(self.packages_count.items()):
            if i < 10:
                print(f"{i+1:<15}\t{name:<60}\t{count}")
