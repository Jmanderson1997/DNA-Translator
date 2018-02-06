from Encoder import encoder
from Decoder import decoder
import filecmp 

orig= open("Example.txt",'r')
trans= open("TranslatedFile.txt",'r+')
new= open("RevertedFile.txt",'r+') 

trans.truncate()
new.truncate()

encoder('Example.txt', "TranslatedFile.txt")
decoder("TranslatedFile.txt", "RevertedFile.txt")

#print("Old text")
#print(orig.read())
#print("DNA Sequence")
#print(trans.read())
#print("new text")
#print(new.read())

orig.close()
trans.close()
new.close()

print(filecmp.cmp("Example.txt","RevertedFile.txt"))
