# Task 1. Generator of DNA-sequences of length from 1 to entered number
def generator(k):
    if k == 0:
        yield ''
    else:
        for i in range(k):
            for x in generator(i):
                yield x + 'A'
                yield x + 'T'
                yield x + 'G'
                yield x + 'C'


# You can be sure, that it works:
# n = int(input())
# sequence = generator(n)
# print(next(sequence))
