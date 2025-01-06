#!/usr/bin/env python

import sys
import os

PHONEBOOK_ENTRIES = "python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        f = open(PHONEBOOK_ENTRIES, "a")
        f.write(sys.argv[2] + " " + sys.argv[3] + "\n")
        exit(0)

    elif sys.argv[1] == "list":
        if (
            not os.path.isfile(PHONEBOOK_ENTRIES)
            or os.path.getsize(PHONEBOOK_ENTRIES) == 0
        ):
            print("phonebook is empty")
        else:
            with open(PHONEBOOK_ENTRIES, "r") as f:
                for line in f.readlines():
                    print(line, end="")
        exit(0)

    elif sys.argv[1] == "lookup":
        name = " ".join(sys.argv[2:])
        with open(PHONEBOOK_ENTRIES, "r") as f:
            lookup = list(filter(lambda line: name in line, f.readlines()))
            for line in lookup:
                print(line, end="")
        exit(0)

    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:])
        with open(PHONEBOOK_ENTRIES, "r+") as f:
            lines_to_keep = list(filter(lambda line: name not in line, f.readlines()))
            f.seek(0)
            f.truncate()
            f.writelines(lines_to_keep)

    elif sys.argv[1] == "clear":
        os.remove(PHONEBOOK_ENTRIES)
        exit(0)

    else:
        print(f"unknown command {sys.argv[1]}, try <new|list|lookup|remove|clear>")


if __name__ == "__main__":
    main()
