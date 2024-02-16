import datetime

def transcribe_dna(dna_sequences):
    # Define the translation table
    translation_table = {
        'A': 'U',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    # Initialize the output list
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

        # Add the mRNA sequence to the output list
        mrna_sequences.append(mrna_sequence)

    # Get the current date and time
    now = datetime.datetime.now()

    # Open the file in append mode
    with open('mrna_output.txt', 'a') as f:
        # Write the date and time
        f.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        # Write each mRNA sequence with an empty line between each
        for mrna_sequence in mrna_sequences:
            f.write(mrna_sequence + '\n\n')

# Test the function
dna_sequences = ['ATGCGCTAGCT', 'CGTGCAGCTAG', 'GATCGAGCTCG']
transcribe_dna(dna_sequences)