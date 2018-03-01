import os

def encoder(original, fileNumber):

   orig=open(original, 'r') # open file
   part=0   #initialize part counter to 0

   while(True):
     fileName=(str(fileNumber)+''+str(part)+".txt")  #create filename that will hold the sequence
     toDNA('',fileName, fileNumber,20) #write filenumber into DNA sequence
     toDNA('',fileName, part, 10) #write part Number into file
     
     for i in range(0,30): #read in 30 characters and add them to the sequence
         character=orig.read(1)
         if not character:  #if EOF break
             break
         toDNA(character, fileName,0,5)#calls function that translates characters to DNA

     toDNA('',fileName, fileNumber,20)#re write fileNumber at the end

     if(os.path.isfile(os.path.join(os.path.join(".", "DNALibrary"), fileName))):#check if sequence file already exists and deletes it if it does
         os.remove(os.path.join(os.path.join(".", "DNALibrary"), fileName))

     os.rename(os.path.join('.', fileName), os.path.join(os.path.join(".", "DNALibrary"), fileName) )#adds file to sequence folder
     
     part+=1  #increases part counter

     pos=orig.tell() #looks for the end of the file
     char=orig.read(1)
     if not char :
        break
     orig.seek(pos)

     

   orig.close()


def toDNA(character, fileName, number, letters):

    f=open(fileName, "a") #opens file
    lastChar=0 #set lastchar to A
    sequence=[]#holds the sequence

    EncodingTable=[['C','G','T'], ['G','T','A'], ['T','A','C'], ['A','C','G']]

    if(character==''):
        asc=number     #if no char was passed use the number that was passed
    else: 
        asc=ord(character)

    for i in range(letters-1,-1,-1):  #table stuff to find the sequence
        for j in range(2,-1,-1):
            if(asc-j*3**i>=0): 
                asc=asc-j*3**i
                sequence.append(EncodingTable[lastChar][j])
                lastChar=lastChar+j+1
                if(lastChar>3): 
                    lastChar-=4
                break
  
    for n in range(0, letters): #write seqence to the file
        f.write(sequence[n])
  
    f.close()