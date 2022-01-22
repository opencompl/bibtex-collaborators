#!/usr/bin/env python3

from pybtex.database.input import bibtex
import argparse



parser = argparse.ArgumentParser(description='Print recent collaborators')
parser.add_argument('file', type = argparse.FileType('r'))
args = parser.parse_args()

parser = bibtex.Parser()
bib_data = parser.parse_file(args.file)
entries = dict(bib_data.entries)

authors = set()

for key in entries.keys():
    entry = entries[key]
    year = int(entry.fields['year'])
    if year <= 2019:
        continue

    for p in entry.persons['author']:
        p = str(p).split(",")
        p = p[1] + " " + p[0]
        p = p.strip()
        authors.add(p)

authors = list(authors)
authors.sort()
for a in authors:
    print(a)


