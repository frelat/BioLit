import BioLit

BioLit.fqfiltron(
    "data/example_fastq.fastq",
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
)
