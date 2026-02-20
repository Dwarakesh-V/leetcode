a = "1111001"
num=14
print(int(a,2)) # Arg 2 tells about the base. 0 means python should find out the base itself
binary_str_fstring = f'{num:b}' #0o -> octal, 0x -> hexa, b -> binary
print(binary_str_fstring,type(binary_str_fstring))
print(len(      10100101000001111010011100))