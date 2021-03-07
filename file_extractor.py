import os
import sys
from typing import List
from shutil import copyfile


def main():
    path = parse_args()
    search_files(path, path)


def search_files(root: str, current: str):
    print(f"Searching %s" % current)

    for item in os.listdir(current):
        path = os.path.join(current, item)
        if (os.path.isdir(path)):
            search_files(root, path)
        else:
            if current != root:
                copyfile(path, os.path.join(root, item))
                print(
                    f"\tCopied %s" % item)


def parse_args() -> List[str]:
    if len(sys.argv) < 2 and os.path.isdir(sys.argv[1]):
        print(f"Usage: extractor <directory>")
        exit(1)

    return sys.argv[1]


if __name__ == '__main__':
    main()
