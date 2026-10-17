# BioLit
Some bioinformatic utilits for simple data processing

## Installation
Clone the repository from GitHub:
```bash
git clone git@github.com:frelat/BioLit.git
```

## Dependencies
Python 3 (developed with Python 3.14.8).
No external libraries are required.

## Functions
### FASTQ filtering
`fqfiltron()` filters FASTQ reads by:
- GC percentage
- Sequence length
- Mean quality (Phred33)

### FASTA conversion 
`stringator()` converts multiline FASTA sequences into single line sequences.

### BLAST parsing
`blast_parser()` parses blast-file, gets the best hit for each query and saves it.

## Usage
To use this package, import the BioLit.py file, and then you can call any of the functions.
### FASTQ
The `fqfiltron` function takes 5 arguments: `input_fastq`, `output_fastq`, `gc_bounds`, `length_bounds`, and `quality_threshold`:
- `input_fastq` — the path to the input FASTQ file.
- `output_fastq` — the name of the output file. Filtered reads are saved into a directory named `filtered` (which may not exist yet) under the filename `output_fastq`.
- `gc_bounds` — the GC content range (in percent) defaults to `(0, 100)`. If a single number is provided, it is treated as the upper bound.
- `length_bounds` — the read length range used for filtering. It keeps all reads by default with `(0, 2**32)`.
- `quality_threshold` — the threshold for the average quality of a read (based on the Phred33 scale); it defaults to `0`. Reads with an average quality score (across all nucleotides) below this threshold are discarded.

### FASTA

The `stringator` function.

It takes two arguments (`input_fasta` and `output_fasta`). The function reads the source FASTA file—in which a sequence (DNA, RNA, protein, etc.) may be split across multiple lines—and saves the data to a new FASTA file, in which each sequence is contained on a single line.

### BLAST
The `parse_blast_output` function.

It takes two arguments as input (`input_file`, `output_file`). The program reads the specified text file, selects the first entry from the `Description` column for each `QUERY`, and saves the resulting set of proteins to a new file as a single, alphabetically sorted column.