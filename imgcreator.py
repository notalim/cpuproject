# imgcreator.py
# Insruction Image Creator Script
# Author: alim
# Date: December 2, 2022

REGISTERS_TO_USE = 8 # change only upto 32

def operationInput():
    print("Instruction " + str(counter + 1))
    while True:
        operation = input("Operation: ")
        try:
            if not operation.lower() in ["add", "sub", "ldr"]:
                raise ValueError
            else:
                break
        except ValueError:
            print("Instruction has to be ADD, SUB or LDR! Try again. \n")
    return operation


def rInput(reg: int):
    while True:
        if (reg == 3):
            print("Destination register ")
        else:
            print("Register " + str(reg))
        try:
            register = input("R")
            if int(register) in range(0, REGISTERS_TO_USE):
                return register
            else:
                raise ValueError
        except ValueError:
            print("Register should be an integer from 1 to " + str(REGISTERS_TO_USE) + "!\n")


image = open('image.txt', 'w')
image.close
image = open('image.txt', 'a')
image.write("v3.0 hex words addressed\n")
image.write("\n")
image.write("00: ")
image.write("00000000 ")

while True:
    COUNT = input(
        "How many instructions do you want? Insert an integer from 1 to 32.\n")
    try:
        if int(COUNT) > 32 or int(COUNT) < 1:
            raise ValueError
        # print("Instructions:", int(COUNT)
        else:
            break
    except ValueError:
        print("Instructions amount should be an integer from 1 to 32!\n")

COUNT = int(COUNT)
counter = 0

print(
    "\nThe instructions available are: \n ADD RD, R1, R2 \n SUB RD, R1, R2 \n LDR RD, R1, R2 (in ARM: LDR RD, [R1, R2]) \n")
print(
    "The registers available are: 0-7. \n")

op_list = ["00", "01", "10", "11", "101"]

while (counter < COUNT):

    op = operationInput()
    op = op.lower()

    r3 = rInput(3)

    if (op == "sub"):
        op_bin = op_list[0]
        r1 = rInput(1)
        r2 = rInput(2)
        print(op.upper() + " R" + r3 + ", R" + r1 + ", R" + r2 + "\n")
    if (op == "add"):
        op_bin = op_list[1]
        r1 = rInput(1)
        r2 = rInput(2)
        print(op.upper() + " R" + r3 + ", R" + r1 + ", R" + r2 + "\n")
    if (op == "ldr"):
        op_bin = op_list[3]
        r1 = rInput(1)
        r2 = rInput(2)
        print(op.upper() + " R" + r3 + ", [R" + r1 + ", R" + r2 + "]\n")
    # if (op == "mov"):
    #     op_bin = op_list[2]
    

    op_code = format(int(op_bin), "011b") + format(int(r2), "05b") + "111000" + format(int(r1), "05b") + format(int(r3), "05b")
    decimal_representation = int(op_code, 2)

    hex_op_code = "0x{:08x}".format(decimal_representation)
    image.write(hex_op_code[2:] + " ")

    counter += 1

print("Done! Now you can import the \"image.txt\" file into the Logisim Instruction Memory!")
image.close
