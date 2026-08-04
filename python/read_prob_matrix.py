import numpy as np
import struct

def read_prob_matrix(filename):
    with open(filename, "rb") as f:
        # C++ size_t is usually 8 bytes on 64-bit systems
        header = f.read(16)
        rows, cols = struct.unpack("QQ", header)

        data = np.fromfile(f, dtype=np.float64, count=rows * cols)

    matrix = data.reshape((rows, cols))
    return matrix


prob_matrix = read_prob_matrix("../output/test.bin")

print(prob_matrix.shape)
print(prob_matrix)