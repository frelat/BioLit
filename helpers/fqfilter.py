def fqfilter(
    block: str,
    gc_bounds: (int | float | tuple),
    length_bounds: (int | float | tuple),
    quality_threshold: (int | float),
) -> bool:
    """
    Check whether a single FASTQ record passes all filters.

    Filters run in this order: GC content -> length -> mean quality.
    If the read fails a filter, the remaining checks are skipped.

    Args:
        block (str): FASTQ record of 4 lines joined into one string
            (header, sequence, "+", quality string).
        gc_bounds (int | float | tuple): GC content bounds in percent.
            A number sets the upper bound (lower bound is 0); a tuple sets
            (lower, upper). (0, 100) disables the filter.
        length_bounds (int | float | tuple): Read length bounds. A number
            sets the upper bound; a tuple sets (lower, upper).
            (0, 2**32) disables the filter.
        quality_threshold (int | float): Minimum mean Phred33 quality.
            0 disables the filter.

    Returns:
        bool: True if the read passes all filters, False otherwise.
    """

    def fqfilter_qt(block, quality_threshold=0):
        if quality_threshold == 0:
            return True
        else:
            seq = block.split("\n")[3].strip()
            quality_sum = 0
            for i in seq:
                quality_sum = quality_sum + (ord(i) - 33)
            quality_sum = quality_sum / len(seq)

            return quality_sum >= quality_threshold

    def fqfilter_lb(seq, length_bounds=(0, 2**32)):

        if length_bounds == (0, 2**32):
            return fqfilter_qt(block, quality_threshold)

        else:
            if isinstance(length_bounds, (int, float)):
                lower = 0
                upper = length_bounds
            else:
                lower = length_bounds[0]
                upper = length_bounds[1]

            if lower <= len(seq) <= upper:
                return fqfilter_qt(block, quality_threshold)
            else:
                return False

    def fqfilter_gc(block, gc_bounds=(0, 100)):
        """
        Принимает запись FASTQ (4 строки одной строкой) и возвращает True,
        если рид проходит фильтр. Последовательность - вторая строка записи.
        """
        seq = block.split("\n")[1].strip().upper()

        if gc_bounds == (0, 100):
            return fqfilter_lb(seq, length_bounds)

        else:
            if isinstance(gc_bounds, (int, float)):
                lower = 0
                upper = gc_bounds
            else:
                lower = gc_bounds[0]
                upper = gc_bounds[1]

            count_result = (seq.count("G") + seq.count("C")) / len(seq) * 100
            if lower <= count_result <= upper:
                return fqfilter_lb(seq, length_bounds)
            else:
                return False

    return fqfilter_gc(block, gc_bounds)
