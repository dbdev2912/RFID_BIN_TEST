ascii_str = "PR0PW01E00F3"
head_bin = "1110"
tail = "10"*18 # 38 char in bin

def char_to_bin(chars):
	bins = [format(x, 'b') for x in bytearray(chars, 'utf-8')]
	
	result = [ head_bin + "" + x for x in bins ]
	result.append(tail)
	return ", ".join(result)


def binaryToDecimal(binary):
    binary1 = int(binary)
    decimal, i, n = 0, 0, 0
     
    while(binary1 != 0):
        dec = binary1 % 10
        decimal = decimal + dec * pow(2, i)
        binary1 = binary1//10
        i += 1
    return(decimal)


def decToHexa(n):
    hexaDeciNum = ['0'] * 100 
    i = 0
    hexa_result = ""
    while(n != 0):
        temp = 0
        temp = n % 16
        if(temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)
 
    j = i - 1
    while(j >= 0):        
        hexa_result += (hexaDeciNum[j])
        j = j - 1
    return hexa_result
 

def binToHexa(n):	
	bin_string = n.replace(" ", "")
	bin_string = bin_string.replace(",", "")
	decimal = binaryToDecimal(bin_string)
	return decToHexa(decimal)


binary_result = char_to_bin(ascii_str)
print("Binary result:")
print(binary_result)
print("\nHexa result:")

splited_bin = binary_result.split(", ")
hex_splited = [binToHexa(x) for x in splited_bin]

print( hex_splited )