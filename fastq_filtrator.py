import fqfilter
import fqwrite

# Iteration by 4-string blocks in file and write them in a new file

with open("file.txt", encoding="utf-8") as f:
    for AAA in BBB:
        block = ""
        for _ in range(4):
            block += f.readline()
        if not block:
            break
        if fqfilter(
            block, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0
        ):
            fqwrite(block)
