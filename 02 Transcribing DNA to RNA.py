dna_sequence = input("Insert DNA sequence here: ")
def transcription(dna_sequence):
    tbdna = dna_sequence.replace("T", "U")
    return tbdna

print(transcription(dna_sequence))