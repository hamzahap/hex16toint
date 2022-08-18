import math
import sys

def get_sign(num):
    global signed
    if(num[0] == '1'):
        signed = True
        return -1
    else:
        signed = False
        return 1

def to_int(num):
    x = int(num, 2)
    return x

def binary_to_twoscomplement(num):
    for x in range(len(num)):
        if(num[x] == '0'):
            num = num[:x] + '1' + num[(x+1):]
        else:
            num = num[:x] + '0' + num[(x+1):]
    a = num
    b = "1"
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0
    
    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
 
    if carry != 0:
        result = '1' + result

    return result.zfill(max_len)

def hex_to_binary_table(num):
    hex_binary_table = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }
    return hex_binary_table[num]
    
def hex_to_binary(num):
    binarynum = ""
    for x in range(len(num)):
        binarynum = binarynum + hex_to_binary_table(num[x])
    return binarynum


def main():
    number = str(input('Enter hexadecimal number: '))
    binarynumber = hex_to_binary(number)
    print(binarynumber)
    sign = get_sign(binarynumber)
    inverted = binary_to_twoscomplement(binarynumber)
    #print(inverted)

    if(signed):
        integernumber = to_int(inverted)
        print(sign * integernumber)
    else:
        new = to_int(binarynumber)
        print(new)

main()