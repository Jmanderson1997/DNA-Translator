from Encoder import encoder,toDNA
from Decoder import decoder, toText
from LedgerManager import numAssign
from GCAT import gcat
import filecmp 

orig= open("Example.txt",'r')
 
fileNum=numAssign("Example.txt")
encoder('Example.txt',fileNum)
decoder(fileNum, "RevertedFile.txt")
#gcat("10.txt")

#print("Old text")
#print(orig.read())
#print("DNA Sequence")
#print(trans.read())
#print("new text")
#print(new.read())

orig.close()

print(filecmp.cmp("Example.txt","RevertedFile.txt"))
