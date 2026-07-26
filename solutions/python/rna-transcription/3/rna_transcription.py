"""RNA transcription."""


def to_rna(dna_strand: str) -> str:
    """Convert the nucleotides in the Dna strand to their rna equivalents."""
    swap = (("G", "X"), ("C", "G"), ("X", "C"), ("A", "U"), ("T", "A"))
    for x, y in swap:
        dna_strand = dna_strand.replace(x, y)
    return dna_strand
