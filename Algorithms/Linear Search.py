def linSearch(seq, target):
    '''linSearch determines the location of the target in the sequence

    -- param
    seq : iterable/indexable data
    target : any data

    -- return integer
    '''

    if not seq:
        return -1
    else:
        for i in range(len(seq)):
            if seq[i] == target:
                return i
            else:
                return -1

from random import seed
from random import randrange

seed(1)
seq = [randrange(1,100) for x in range(20)]

print('Random List:\n',seq)

print('--\nSearch %d in seq: Found at %d' % (18, linSearch(seq,18)))

print('Search %d in seq: Found at %d' % (61, linSearch(seq,61)))

print('Search %d in seq: Found at %d' % (42, linSearch(seq, 42)))


