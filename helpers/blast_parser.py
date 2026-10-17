def blast_parser(input_file: str, output_file=None):
    """
    Extract the best protein hits from a BLAST text report.

    Args:
        input_file (str): Path to the BLAST results text file.
        output_file (str, optional): Path to the output file.

    Returns:
        None. The results are written to output_file.
    """

    if output_file is None:
        if input_file.endswith(".txt"):
            output_file = input_file[:-6] + "_parsed.txt"
        else:
            output_file = input_file + "_parsed.txt"

    proteins = []
    with open(input_file, "r") as f:
        for line in f:
            if line.startswith("Sequences producing significant alignments:"):
                header = f.readline()
                f.readline()
                str1 = f.readline()
                lengh = len(header.split("Scientific")[0])
                protein = str1[:lengh].strip()
                proteins.append(protein)
    proteins.sort()
    with open(output_file, "a") as f:
        f.write(proteins)
