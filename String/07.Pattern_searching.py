txt=input("Enter text:")
pat=input("Enter pattern:")
pas=txt.find(pat)
while pas >= 0:
    print(pas)
    pas=txt.find(pat,pas+1)
