"""
CBC mode :
C_0 = IV
C_i = E_k(P_i XOR C_(i-1))

P_i = D_k(C_i) XOR C_(i-1)

"""


"""
Padding scheme:
if F(b) is amount of bytes needed to pad to multiple of block size length,
add F(b) bytes each with value F(b).
"""
