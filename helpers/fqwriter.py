import os


def fqwriter(block: str, output_file: str):
    """
    Append a single FASTQ record to the end of the output file.

    Args:
        block (str): FASTQ record of 4 lines.
        output_file (str): Path to the output file. The file is opened
            in append mode ("a").

    Returns:
        None.
    """
    output_file = os.path.basename(output_file)
    os.makedirs("filtered", exist_ok=True)
    output_path = os.path.join("filtered", output_file)

    with open(output_path, "a") as f:
        f.write(block)
