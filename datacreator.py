# datacreator.py
# Data Image Creator Script
# Author: alim
# Date: December 5, 2022

image = open('data.txt', 'w')
image.close
image = open('data.txt', 'a')
image.write("v3.0 hex words addressed\n")
image.write("\n")
image.write("00: ")

print("The available amount of data you can put is 256 bytes.\n")

while True:
    data = input(
        "How much data in bytes do you want to store? \n")
    try:
        if int(data) > 256 or int(data) < 1:
            raise ValueError
        else:
            break
    except ValueError:
        print("Data amount has to be an integer in between of 1 and 256 bytes! \n")

print("Input the data in a hex format, without 0x ('01' - 'ff'), byte by byte: \n")

counter = 1
while counter < int(data) + 1:
    print("Byte ", counter)
    while True:
        byte = input(
            "Input the data byte: \n")
        try:
            if int("0x" + byte, 16) > 0xff or int("0x" + byte, 16) < 0x1:
                raise ValueError
            else:
                if len(byte) == 1:
                    image.write("0" + byte + " ")
                else:
                    image.write(byte + " ")
                counter += 1
                break
        except ValueError:
            print("Data byte has to be an hex integer in between of 0x1 and 0xff! \n")

print("Done! Now you can import the \"data.txt\" file into the Logisim Data Memory")
image.close
