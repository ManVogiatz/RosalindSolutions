dna_sequence = input("Insert DNA sequence here: ")
def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    reversed_dna = dna_sequence[::-1]
    
    reversed_complement_dna = ''.join(complement[nucleotide] for nucleotide in reversed_dna)
    
    return reversed_complement_dna

print(reverse_complement(dna_sequence))