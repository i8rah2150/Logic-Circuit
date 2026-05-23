#---Defining_Functions---
def not_gate(text):
    return not text
def or_gate(A, B):
    return A or B
def and_gate(X, Y):
    return X and Y
def nand_gate(C, D):
    in1 = C and D
    return int(not in1) 
def nor_gate(N, M):
    in2 = N or M
    return int(not in2)
def xor_gate(J, K):
    ins1 = not J 
    ins2 = not K
    ins3 = ins1 and K
    ins4 = ins2 and J
    return ins3 or ins4
#-------------