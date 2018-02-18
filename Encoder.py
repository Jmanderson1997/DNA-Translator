import os

def encoder(original, fileNumber):

   orig=open(original, 'r')
   part=0

   while(True):
     fileName=(str(fileNumber)+''+str(part)+".txt")
     toDNA('',fileName, fileNumber,20)
     toDNA('',fileName, part, 10)
     
     for i in range(0,30):
         character=orig.read(1)
         if not character: 
             break
         toDNA(character, fileName,0,5)

     toDNA('',fileName, fileNumber,20)

     if(os.path.isfile(os.path.join(os.path.join(".", "DNALibrary"), fileName))):
         os.remove(os.path.join(os.path.join(".", "DNALibrary"), fileName))

     os.rename(os.path.join('.', fileName), os.path.join(os.path.join(".", "DNALibrary"), fileName) )
     
     part+=1  

     pos=orig.tell()
     char=orig.read(1)
     if not char :
        break
     orig.seek(pos)

     

   orig.close()


def toDNA(character, fileName, number, letters):

    f=open(fileName, "a")
    lastChar=0
    sequence=[]

    EncodingTable=[['C','G','T'], ['G','T','A'], ['T','A','C'], ['A','C','G']]

    if(character==''):
        asc=number
    else: 
        asc=ord(character)

    for i in range(letters-1,-1,-1):  
        for j in range(2,-1,-1):
            if(asc-j*3**i>=0): 
                asc=asc-j*3**i
                sequence.append(EncodingTable[lastChar][j])
                lastChar=lastChar+j+1
                if(lastChar>3): 
                    lastChar-=4
                break
  
    for n in range(0, letters): 
        f.write(sequence[n])
  
    f.close()