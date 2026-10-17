from helpers.blast_parser import blast_parser
from helpers.fqfilter import fqfilter
from helpers.fqreader import fqreader
from helpers.fqwriter import fqwriter
from helpers.stringator import stringator

# Iteration by 4-string blocks in file and write them in a new file


def fqfiltron(
    input_fastq: str,
    output_fastq=None,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
):
    """
    Filter reads in a FASTQ file by GC content, length and mean quality.

    Reads the input file one record at a time, checks each record with
    fqfilter, and writes the records that pass to the output file.

    Args:
        input_fastq (str): Path to the input FASTQ file.
        output_fastq (str, optional): Path to the output file. If not given,
            the name is built from the input file name with the suffix
            "_filtered.fastq".
        gc_bounds (int | float | tuple): GC content bounds in percent.
            A number sets the upper bound (lower bound is 0); a tuple sets
            (lower, upper). Default (0, 100) disables the filter.
        length_bounds (int | float | tuple): Read length bounds. A number
            sets the upper bound; a tuple sets (lower, upper).
            Default (0, 2**32) disables the filter.
        quality_threshold (int | float): Minimum mean Phred33 quality.
            Default 0 disables the filter.

    Returns:
        None. Reads that pass the filters are written to output_fastq.
    """

    if output_fastq is None:
        if input_fastq.endswith(".fastq"):
            output_fastq = input_fastq[:-6] + "_filtered.fastq"
        else:
            output_fastq = input_fastq + "_filtered.fastq"

    for block in fqreader(input_fastq):
        if fqfilter(block, gc_bounds, length_bounds, quality_threshold):
            fqwriter(block, output_fastq)
