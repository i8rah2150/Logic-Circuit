#-------------
print("Logic Circuit")
#-------------
input_A = int(input("Enter your First input into the circuit: "))
input_B = int(input("Enter your Second input into the circuit: "))
input_C = int(input("Enter the input you want to invert: "))
#---Defining_Functions---
def not_gate(text):
    return not text
def or_gate(A, B):
    return A or B
def and_gate(X, Y):
    return X and Y
#-------------
print(int(not_gate(input_C)))
print(or_gate(input_A, input_B))
print(and_gate(input_A, input_B))
