def BinaryProcessing():
    def BinaryToAscii():
        BinaryText = input("Type in your BINARY code here: ")
        n = int(BinaryText, 2)
        T = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        print("The answer is: ", T)

    def AsciiToBinary():
        ASCII = input("Type in your ASCII code here: ")
        T = bin(int.from_bytes(ASCII.encode(), 'big'))
        print("The answer is: ", T)

    BinaryInp = input("""
    ------------------------------------------
        [1] Convert from: Binary To Ascii
        [2] Convert from: Ascii To Binary
              >> """)
    if BinaryInp == "1":
        BinaryToAscii()
    elif BinaryInp == "2":
        AsciiToBinary()


def HexProcessing():
    def HexToAscii():
        HEXText = input("Type in your HEX code here: ")
        bytes_object = bytes.fromhex(HEXText)
        ascii_string = bytes_object.decode("ASCII")
        print("The answer is: ", ascii_string)

    def AsciiToHex():
        ASCII = input("Type in your ASCII code here: ")
        hex_string = ASCII.encode("utf-8").hex()
        print("The answer is: ", hex_string)

    HexInp = input("""
    ------------------------------------------
        [1] Convert from: Hex To Ascii
        [2] Convert from: Ascii To Hex
              >> """)
    if HexInp == "1":
        HexToAscii()
    elif HexInp == "2":
        AsciiToHex()


Inp1 = input("""
    ------------------------------------------
       [1] HEX & ASCII Pprocessing
       [2] BINARY & ASCII processing
              >> """)
if Inp1 == "1":
    HexProcessing()
elif Inp1 == "2":
    BinaryProcessing()
