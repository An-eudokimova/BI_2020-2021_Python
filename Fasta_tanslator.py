# Task 2. Fasta reading and translating generator
def translator(path):
    from Bio.Seq import Seq
    from Bio import SeqIO
    for fasta in SeqIO.parse(open(path), 'fasta'):
        coding_dna = Seq(str(fasta.seq))
        yield coding_dna.translate(table="Standard")


# You can be sure, that it works:
# path_to_fasta = input('Input path to fasta file without quotes: ')
# proteins = translator(path_to_fasta)
# print(next(proteins))
# print(next(proteins))
