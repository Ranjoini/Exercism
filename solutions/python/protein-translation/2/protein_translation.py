"""Protein translation exercise."""

TRANSLATION = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
}


def proteins(strand: str) -> list[str]:
    """Use slicing and a dictionary map to translate the codon and return in a list."""
    # Storage container
    protein = []
    # Used range to find the starting index
    for i in range(0, len(strand), 3):
        # Using the starting index I sliced strand into chunks of 3
        codon = strand[i : i + 3]
        # Checked for the edge case first
        if codon in ["UAA", "UAG", "UGA"]:
            return protein
        protein.append(TRANSLATION[codon])
    return protein
