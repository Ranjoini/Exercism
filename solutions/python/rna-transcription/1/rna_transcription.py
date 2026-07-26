"""RNA Transcription."""


def to_rna(dna_strand: str) -> str:
    """Convert the nucleotides in the Dna strand to their rna equivalents."""
    dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna_list = []
    for nucleotide in dna_strand:
        rna_equivalent = dna_to_rna[nucleotide]
        rna_list.append(rna_equivalent)
    return "".join(rna_list)
