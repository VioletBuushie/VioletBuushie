import random as r

t = input("If you would like to encrypt type 0, if you want to decrypt type 1: ")
##Input right there
div = r.randrange(1, 100)
##print(div)
##Generates divisor
key = ""
##key = chr(div)
def sigma(number, power):
    k = 0
    for i in range(1, number + 1):
        if number % i == 0:
            d = number / i
            ##print("divisor" + str(d))
            k += (int(d) * int(power))
            ##print("Multiplied: " + str(power))
            ##print(chr(k))
            ##print("Encryption number " + str(k))
    return chr(k)
def keygen(number, power):
    g = ""
    k = 0
    for i in range(2, number + 1):
        if number % i == 0:
            d = number / i
            ##print("Key divisor: " + str(d))
            k += (int(d) * int(power))
            ##print("Key number: " + str(k))
            ##print(chr(k))
    g += chr(k)
    g += chr(power)
    return g
def omega(encr, ke):
    word = ""
    for i in range(len(encr)):
        g = ord(encrypt[i])
        s = ord(ke[i*2])
        ##print(chr(s))
        d = ord(ke[(i*2)+1])
        ##print(chr(d))
        v = g - s
        ##print(v)
        ##print(chr(int(v/d)))
        word += chr(int(v/d))
    return word
def encrypt():
    key = ""
    n = input("Input a word: ")
    g = ""
    for i in range(len(n)):
        q = ord(n[i])
    ##print(q)
        mod = (q % div) + 1
    ##print("Mod: " + str(mod))
        g += sigma(q, mod)
        key += keygen(q, mod)
    print("encrypted: " + g)
    print("key:" + key)
if t == "0":
    encrypt()
elif t == "1":
    key = input("Insert key: ")
    encrypt = input("Insert encryption: ")
    word = omega(encrypt, key)
    print(word)
else:
    print("Screw you")
    

##word = omega(encrypt, key)
##print("secret word:" + word)
