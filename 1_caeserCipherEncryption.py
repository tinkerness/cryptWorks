'''Implementation of a Caesar Cipher'''

k = int(input("enter value of k : "))
plain = input("enter the plaintext : ")
p = ""

for char in str.lower(plain):
    if char!=" ":
    #if (ord(char) > 96 || ord(char) < 123):
        charint = ord(char) - 97
        if charint < 10:
            p = p + "0" + str(charint)
        else:
            p = p + str(charint)
print("\np = ",p)

c1,c2,c = "","",""
for i in range(0,len(p),2):
    c1 = p[i] + p[i+1]
    c2 = (int(c1) + k) % 26
    if c2 < 10:
        c = c + "0" + str(c2)
    else:
        c = c + str(c2)
print("c = ",c)

c3,cipher = "",""
for i in range(0,len(c),2):
    c3 = c[i] + c[i+1]
    cipher = cipher + chr(int(c3)+97)
print("\nciphertext = ",cipher)
