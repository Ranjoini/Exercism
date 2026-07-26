"""RNA transcription."""


def to_rna(dna_strand: str) -> str:
    """Convert the nucleotides to their rna equivalents."""
    return dna_strand.translate(str.maketrans("GCTA", "CGAU"))
