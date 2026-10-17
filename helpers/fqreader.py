def fqreader(input_file: str) -> str:
    """
    Generator that reads FASTQ records from a file one at a time.

    Reads 4 lines (one FASTQ record) per step and yields them as a single
    block. Stops at the end of the file or when the last record is
    incomplete.

    Args:
        input_file (str): Path to the FASTQ file.

    Yields:
        str: FASTQ record of 4 lines, including newline characters.
    """

    with open(input_file, encoding="utf-8") as f:
        while True:
            block = ""
            for _ in range(4):
                block += f.readline()
            if not block or len(block.split("\n")) < 4:
                return
            yield block
