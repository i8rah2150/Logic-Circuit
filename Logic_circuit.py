#-------------
print("Logic Circuit")

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

#---Taking_Input---
input_X = str(input("Do you want to invert any input? (yes/no): "))
if input_X.lower() == "yes":
    input_Y = int(input("Enter the input you want to invert (0/1): "))
    input_Y = not_gate(input_Y)
    print(f"Inverted Input: {int(input_Y)}")
else:
    input_A = int(input("Enter your First input into the circuit: "))
    input_B = int(input("Enter your Second input into the circuit: "))

#-------------

#---Logic_Gate---
#---Not_Gate---
NOT_GATE = f"""
{input_A}────|NOT>o───▶{input_B}
"""
#---

#---Or_Gate---
OR_GATE = f"""
{input_A}●──┐
            ├{{OR)───▶
{input_B}●──┘
"""
#---

#---And_Gate---
AND_GATE = f"""
{input_A}●──┐
            ├|AND)───▶
{input_B}●──┘
"""
#---

#---Nor_Gate---
NOR_GATE = f"""
{input_A}●──┐
            ├{{NOR)o───▶
{input_B}●──┘
"""
#---

#---Nand_Gate---
NAND_GATE = f"""
{input_A}●──┐
            ├|NAND)o───▶
{input_B}●──┘
"""
#---
#---Xor_Gate---
XOR_GATE = f"""
{input_A}●──┐
            ├{{XOR)───▶
{input_B}●──┘
"""
#---
#----------------
#---User_Circuits---
print(
    """
Available Gates
● NOT
● OR
● AND
● NOR
● NAND
● XOR
"""
)
while True:
    user_gate = str(input("Enter your desired gate(s) [or enter 'done' to exit]: "))
    if user_gate.lower() == "done":
        break
    if user_gate.lower():
        print()

#-------------

#---Logic_Gate---
#---OR_Gate_using_NAND---


#-------------
#---Full_Truth_Table *coming soon*---
