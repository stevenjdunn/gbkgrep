#!/usr/bin/env python
import argparse
from Bio import SeqIO

# Version
_verion_= "0.1"

# Argparse Setup
parser = argparse.ArgumentParser(description="A tool for extracting nucleotide sequence of a given gene from a genbank file.")
parser.add_argument("-i", "--input", required=True, help="Locus tag")
parser.add_argument("-g", "--genbank", required=True, help="Path to genbank file.")
args = parser.parse_args()

input_tag = args.input
for entries in SeqIO.parse(args.genbank,"genbank"):
    if entries.features:
        for feature in entries.features:
            if feature.type == "CDS":
                if feature.qualifiers['locus_tag'][0] == input_tag:
                    print(">%s\n%s\n" % (
                        feature.qualifiers['locus_tag'][0],
                        feature.location.extract(entries).seq))
