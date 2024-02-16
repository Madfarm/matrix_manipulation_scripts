def transcribe_dna(dna_sequences):
    # Define the translation table
    translation_table = {
        'A': 'U',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    # Initialize the mRNA sequences
    mrna_sequences = []

    # Iterate through the DNA sequences
    for dna_sequence in dna_sequences:
        # Initialize the mRNA sequence
        mrna_sequence = ''

        # Iterate through the DNA sequence
        for base in dna_sequence:
            # Check if the base is in the translation table
            if base in translation_table:
                # Replace the base with its corresponding mRNA base
                mrna_sequence += translation_table[base]
            # If the base is not in the translation table (e.g. N for unknown), leave it unchanged
            else:
                mrna_sequence += base

        # Add the mRNA sequence to the list
        mrna_sequences.append(mrna_sequence)

    # Write the mRNA sequences to a file
    with open('mRNA_output.txt', 'w') as f:
        for mrna_sequence in mrna_sequences:
            f.write(mrna_sequence + '\n')

# Test the function
dna_sequences = ['ATGCGCTAGCT', 'GCTAGCAGCTA', 'TGCAGCTAGCA']
transcribe_dna(dna_sequences)