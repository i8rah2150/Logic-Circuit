import gates
#-------------
print("Logic Circuit")
#-------------

#---Taking_Input---
input_X = str(input("Do you want to invert any input? (yes/no): "))
if input_X.lower() == "yes":
    input_Y = int(input("Enter the input you want to invert (0/1): "))
    #---Not_Gate---
    NOT_GATE = f"""
    {input_Y}────|NOT>o───{int(gates.not_gate(input_Y))}
    """
#---
else:
    input_A = int(input("Enter your First input into the circuit: "))
    input_B = int(input("Enter your Second input into the circuit: "))
    #---Logic_Gate---
    #---Or_Gate---
    OR_GATE = f"""
    {input_A}●──┐
        ├{{OR)───{gates.or_gate(input_A, input_B)}
    {input_B}●──┘
    """
    #---

    #---And_Gate---
    AND_GATE = f"""
    {input_A}●──┐
        ├|AND)───{gates.and_gate(input_A, input_B)}
    {input_B}●──┘
    """
    #---

    #---Nor_Gate---
    NOR_GATE = f"""
    {input_A}●──┐
        ├{{NOR)o───{gates.nor_gate(input_A, input_B)}
    {input_B}●──┘
    """
    #---

    #---Nand_Gate---
    NAND_GATE = f"""
    {input_A}●──┐
        ├|NAND)o───{gates.nand_gate(input_A, input_B)}
    {input_B}●──┘
    """
    #---

    #---Xor_Gate---
    XOR_GATE = f"""
    {input_A}●──┐
        ├{{XOR)───{gates.xor_gate(input_A, input_B)}
    {input_B}●──┘
    """
    #---

#-------------


#---Output_arrow *in_working*---
OUTPUT_ARROW = """
───▶{undefined}
"""
#----------------
set_func = []
#---User_Circuits---


if input_X.lower() == "yes":
    print(NOT_GATE)
else:
    print(
    """
    Available Gates:-
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
        if user_gate.lower() == "or":
            print(OR_GATE)
        elif user_gate.lower() == "and":
            print(AND_GATE)
        elif user_gate.lower() == "nor":    
            print(NOR_GATE)
        elif user_gate.lower() == "nand":    
            print(NAND_GATE)
        elif user_gate.lower() == "xor":    
            print(XOR_GATE)
    while True:
        user_oput = input("Do your want to build a circuit using the above gates? (yes/no): ")
        if user_oput.lower() == "yes":
            set_func.append(str(input("Enter the output of the gate you want to use: ")))
        else:
            break
#-------------

#---Logic_Gate---
#---OR_Gate_using_NAND---


#-------------
#---Full_Truth_Table *coming soon*---
