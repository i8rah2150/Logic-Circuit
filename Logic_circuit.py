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
    print(input_C,
        """
────|NOT>o────
"""
(int(not_gate(input_C)))
    )
elif user_gate.upper() == 'OR' :
    print(input_A,"""────{ )
      {OR>────""",or_gate(input_A, input_B))
    print(input_B,"────{ )")
elif user_gate.upper() == 'AND' :
    print(input_A,"""────| )
      |AND)────""",and_gate(input_A, input_B))
    print(input_B,"────| )")
else:
    print("Invalid Gate input")
#-------------

