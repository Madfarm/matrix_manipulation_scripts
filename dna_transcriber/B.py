def transcribe_dna(dna_sequence):
    """
    Transcribes a DNA sequence into an mRNA sequence.

    Args:
        dna_sequence (str): The DNA sequence to transcribe.

    Returns:
        str: The corresponding mRNA sequence.
    """
    # Define the transcription rules
    transcription_rules = {
        'A': 'U',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    # Initialize the mRNA sequence
    mrna_sequence = ''

    # Iterate through the DNA sequence
    for base in dna_sequence:
        # Apply the transcription rules
        try:
            mrna_sequence += transcription_rules[base]
        except KeyError:
            # Handle unknown base exceptions
            raise ValueError(f"Unknown base {base} in DNA sequence")

    return mrna_sequence

dna_sequence = 'ATGCGCTAGCT'
mrna_sequence = transcribe_dna(dna_sequence)
print(mrna_sequence)  # Output: UUGCCGAUCGU