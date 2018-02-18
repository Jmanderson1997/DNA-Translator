from Encoder import encoder,toDNA
from Decoder import decoder, toText
from NumberAssigner import numAssign
from GCAT import gcat
import filecmp 

orig= open("Example.txt",'r')
 
print(numAssign("Example.txt"))
#encoder('Example.txt',17)
#decoder(17, "RevertedFile.txt")
#gcat("10.txt")



#print("Old text")
#print(orig.read())
#print("DNA Sequence")
#print(trans.read())
#print("new text")
#print(new.read())

orig.close()

print(filecmp.cmp("Example.txt","RevertedFile.txt"))
