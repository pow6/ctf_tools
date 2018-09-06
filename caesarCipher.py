import sys

def encryption(sentence,key):
    for char in sentence:
        if char>='a' and char<='z':
            ret=chr((ord(char)+int(key)-ord('a'))%26 + ord('a'))
        elif char>='A' and char<='Z':
            ret=chr((ord(char)+int(key)-ord('A'))%26 + ord('A'))
        else:
            ret=char
        sys.stdout.write(ret)
    print()

print('caesar cipher program')
sys.stdout.write('[mode] encryption:1 decryption:2>>')

mode=int(input())
while mode!=1 and mode!=2:
    print('wrongnumber\n')
    mode=input()

print('your sentence:')
s=input()
if mode==1:
    #encryption
    sys.stdout.write('[encryption mode] value >>')
    k=input()
    encryption(s,k)
elif mode==2:
    #decryption
    for x in range(27):
        sys.stdout.write(str(x)+':')
        encryption(s,x)