#!usr/bin/python3

import seq_data_download as sdd
import argparse
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("file", help="enter the name of the text file to be processed")
parser.add_argument("--separator", "-s", default=" ", action='store')
parser.add_argument("--database", "-db", help="enter the name of the database", choices=["nuccore", "popset", "protein"], default="nuccore", action="store")
parser.add_argument("--retType", "-rt", help="enter the name of the data type to be retrieved", choices=["fasta", "gb", "seqid"], default="fasta", action="store")
parser.add_argument("--retMode", "-rm", help="enter the name of the data type to be retrieved", choices=["text", "xml"], default="text", action="store")
args = parser.parse_args()


def fileProcessor(file, sep=" "):
    '''
    it reads a text file and return a list of lists.
    each internal list corresponds to a line of the original text file.
    each line is splitted according to a "separator" defined by the user
    '''
    with open(file) as f:
        lines = f.readlines()
    lines_list = [l.strip().split(sep) for l in lines]
    return lines_list


search_list = fileProcessor(args.file, args.separator)


for i in range(len(search_list)):
    if (i + 1) % 3 != 0:
        sdd.get_data(args.database, search_list[i], args.retType, args.retMode)
    else:
        sleep(1)
        sdd.get_data(args.database, search_list[i], args.retType, args.retMode)
