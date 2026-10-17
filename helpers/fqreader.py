def fqreader(input_file):
    with open(input_file, encoding="utf-8") as f:
        while True:
            block = ""
            for _ in range(4):
                block += f.readline()
            if not block or len(block.split("\n")) < 4:
                return
            yield block
