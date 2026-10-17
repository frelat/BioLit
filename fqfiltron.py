from helpers.fqfilter import fqfilter
from helpers.fqreader import fqreader
from helpers.fqwriter import fqwriter

# Iteration by 4-string blocks in file and write them in a new file


def fqfiltron(
    input_fastq,
    output_fastq=None,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
):
    if output_fastq is None:
        output_fastq = input_fastq + "_filtered"

    for block in fqreader(input_fastq):
        if fqfilter(block, gc_bounds, length_bounds, quality_threshold):
            fqwriter(block, output_fastq)
