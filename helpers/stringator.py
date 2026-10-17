def stringator(input_fasta: str, output_fasta=None):
    """
    Convert a multi-line FASTA file so that each record's sequence is on
    a single line.

    Lines starting with ">" are treated as headers and written unchanged.
    Sequence lines between headers are joined together. Works with DNA,
    RNA, protein sequences and etc.

    Args:
        input_fasta (str): Path to the input FASTA file.
        output_fasta (str, optional): Path to the output file.

    Returns:
        None. The result is written to output_fasta.
    """

    if output_fasta is None:
        if input_fasta.endswith(".fasta"):
            output_fasta = input_fasta[:-6] + "_stringed.fasta"
        else:
            output_fasta = input_fasta + "_stringed.fasta"

    with open(input_fasta, encoding="utf-8") as f, open(output_fasta, "a") as f2:
        str1 = ""
        str2 = ""
        str1 = f.readline()
        while True:
            str2 = f.readline()
            if not str2:
                f2.write(str1)
                break
            if not str1.startswith(">") and not str2.startswith(">"):
                str1 = str1.replace("\n", "")
            f2.write(str1)
            str1 = str2
