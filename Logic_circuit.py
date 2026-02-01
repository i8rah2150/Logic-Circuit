#-------------
print("Logic Circuit")
#---Taking_Input---
input_C = int(input("Enter the input you want to invert: "))
input_A = int(input("Enter your First input into the circuit: "))
input_B = int(input("Enter your Second input into the circuit: "))
#---Defining_Functions---
def not_gate(text):
    return not text
def or_gate(A, B):
    return A or B
def and_gate(X, Y):
    return X and Y
#---User_Circuits---
user_gate = str(input("Enter your desired gate: "))
if user_gate.upper() == 'NOT' :
    print(
        """
────|NOT>o────
"""
    )
elif user_gate.upper() == 'OR' :
    print(
        """   
────{OR>────   
"""
    )
elif user_gate.upper() == 'AND' :
    print(
        """
────|AND)────
"""
    )
else:
    print("Invalid Gate input")
#-------------
print(int(not_gate(input_C)))
print(or_gate(input_A, input_B))
print(and_gate(input_A, input_B))
