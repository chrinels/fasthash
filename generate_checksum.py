import hashlib
import time
import sys


def fast_hashing(path: str, hash_type: str = 'md5', blocks: int = 1):
    if hash_type not in hashlib.algorithms_available:
        return

    h = hashlib.new(hash_type)
    if blocks == 1:
        blocks = int(2**16/h.block_size)
    size = blocks * h.block_size

    proc_time = time.process_time()

    with open(path, 'rb') as f:
        b = f.read(size)
        while len(b) > 0:
            h.update(b)
            b = f.read(size)
    print('{}({}): {}'.format(hash_type, path, h.hexdigest()))
    print("{0:.3f} s".format(time.process_time() - proc_time))
    with open(path + '.' + hash_type, mode='w+') as checksum_file:
        checksum_file.write(h.hexdigest() + '\t' + path)


if __name__ == '__main__':
    args = sys.argv
    fast_hashing(path=args[1], hash_type=args[2])
