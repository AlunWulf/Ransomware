import os
from cryptography.fernet import Fernet

files=[]
for file in os.listdir():
    if file =="ransomware.py" or file=="thekey.key" or file=="decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key","rb") as key:
        secretkey=key.read()

secret="alunwulf"
user_input=input("what is secret key?:")
if user_input==secret:
    for file in files:
        with open(file,"rb") as thefile:
                contents=thefile.read()
        contents_decryption=Fernet(secretkey).decrypt(contents)
        with open(file,"wb") as thefile:
                thefile.write(contents_decryption)
        print("File in decrypt")

else:
    print("Wrong Key")