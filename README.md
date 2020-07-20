# fas-gb_retriever

*fas-gb-retriever* is a simple command-line and stand-alone pyton code written to help sistematists to retrieve data from GenBank. It is based on NCBI E-utilitiesis and is mainly focused on retrieving sequences in two file formats: fasta and genbak. Currently, there is no support for inclusion of api key. For those interested in a more powerful tool, I would suggest using Biopython libraries.

# Before using this code

Please, before downloading, using or modifying this code, you should read and comply with [NCBI Disclaimer and Copyright](https://www.ncbi.nlm.nih.gov/home/about/policies/), from which I quote:
  * **If you have more than 100 requests**, you should run this code on weekends or between 9 pm and 5 am Eastern Time weekdays.
  * You should **not make more than 3 requests every 1 second** (the code was written to comply with this rule, If you notice, this is not the case, please, contact me (just create an issue in github).
In addition, I would recommend that you **do not use** this code to retrieve abstracts from PubMeda database.

# Usage
*fas-gb-retriever* only requires a simple text file in which the search terms are arranged along the columns. Terms disposed in lines, separated by spaces, will be combined in a single query (using the AND operator). Typically, you will search for species names (or *txid*, for a more precise results), that may (or may not) be followed by gene/protein names.
In most cases you can simply run:

```
python fas-gb-retriever.py <file-name.txt>
```

By default *fas-gb-retriever* will retrieve nucleotide sequences (from nuccore) in fasta file format. It will create a fasta file for each query (i.e. each line in the text file).
If you need help on how to run the code, simply type `python fas-gb-retriever.py -h` and the following help message will show up on your terminal.

```
usage: fas-gb-retriever.py [-h] [--separator SEPARATOR]
                           [--database {nuccore,popset,protein}]
                           [--retType {fasta,gb,seqid}] [--retMode {text,xml}]
                           file

positional arguments:
  file                  enter the name of the text file to be processed

optional arguments:
  -h, --help            show this help message and exit
  --separator SEPARATOR, -s SEPARATOR
  --database {nuccore,popset,protein}, -db {nuccore,popset,protein}
                        enter the name of the database
  --retType {fasta,gb,seqid}, -rt {fasta,gb,seqid}
                        enter the name of the data type to be retrieved
  --retMode {text,xml}, -rm {text,xml}
                        enter the name of the data type to be retrieved

```
