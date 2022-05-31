from Bio import SeqIO

if __name__ == '__main__':
    for record in SeqIO.parse("data/animalBlast.fasta", "fasta"):
        name, binomen = record.id.split('|')
        sequence = record.seq
        print(f"{name} ({binomen}): {sequence}")