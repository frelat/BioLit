def fqwriter(block, output_file):
    with open(output_file, "a") as f:
        f.write(block)
