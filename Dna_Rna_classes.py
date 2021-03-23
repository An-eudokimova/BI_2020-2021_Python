from Bio.Seq import Seq


class Dna:
    def __init__(self, string, info='no'):
        # checking for right characters in input string
        if not set(string).issubset(set('ATGCatgc')):
            raise ValueError('Input sequence\
            contains characters other than the set (A, a, C, c, T, t, G, g)')
        else:
            self.string = string
            # some comment or information about sequence
            self.info = info

    def __iter__(self):  # making iterable object
        return iter(self.string)

    def length(self):  # fast way to find out length of sequence
        return len(self.string)

    # converting to lower or upper case as needed
    def lower(self):
        return self.string.lower()

    def upper(self):
        return self.upper()

    # content of G and C in percent
    def gc_content(self):
        gc_count = 0
        for nucl in self:
            if nucl in set('GCgc'):
                gc_count += 1
        return round(gc_count * 100 / len(self.string), 2)

    # complement and reverse complement sequence
    def complement(self):
        seq = Seq(self.string)
        return str(seq.complement())

    def reverse_complement(self):
        seq = Seq(self.string)
        return str(seq.reverse_complement())

    def __hash__(self):
        return hash(self.string)

    # identical sequences with different register will be considered the same
    def __eq__(self, other):
        return self.string.upper() == other.string.upper()

    # if you need to compare sequences up to case
    def eq_strict(self, other):
        return self.string == other.string

    # transcription (Dna --> Rna, NOT REVERSE!!!)
    def transcribe(self):
        seq = Seq(self.string)
        return Rna(str(seq.transcribe()))


class Rna(Dna):
    def __init__(self, string, info='no'):
        # checking for right characters in input string
        if not set(string).issubset(set('AUGCaugc')):
            raise ValueError('Input sequence\
            contains characters other than the set (A, a, C, c, U, u, G, g)')
        else:
            self.string = string
            self.info = info

    # back transcription (Rna --> Dna, NOT REVERSE!!!)
    def back_transcribe(self):
        seq = Seq(self.string)
        return Dna(str(seq.back_transcribe()))
    
