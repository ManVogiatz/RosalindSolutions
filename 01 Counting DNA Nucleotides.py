dna_sequence = input("Insert DNA sequence here: ")
def count_bases(dna_sequence):
    base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    for base in dna_sequence:
        if base in base_counts:
            base_counts[base] += 1
    
    return base_counts

counts = count_bases(dna_sequence)
print(counts['A'], counts['T'], counts['C'], counts['G'])