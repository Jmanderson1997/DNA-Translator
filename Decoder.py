import os
import numpy

def decoder(fileNumber, revertedFile) :

    new= open(revertedFile, 'w')   #open file to recieve contents
    fileParts=[]  #array of all parts of file
 

    for files in os.listdir("./DNALibrary"):  #loop through folder and find all parts of the file
      files=os.path.join("./DNALibrary",files)   
      f=open(files) 
      fileNum=f.read(20)
      sum=toText(fileNum, 20)
      if(sum==fileNumber): 
        fileParts.append(files)
      f.close()

    partNums=[]

    for i in range(0, len(fileParts)) : #sort parts by part numbers
      f=open(fileParts[i])
      f.read(20)
      partSeq=f.read(10)
      partNum=toText(partSeq, 10)
      partNums.append(partNum)
      f.close()
    
    fileParts=numpy.array(fileParts)
    sortedIndecies=numpy.argsort(partNums)
    fileParts=fileParts[sortedIndecies]

    for i in range(0, len(fileParts)):   #read sequences 
      f=open(fileParts[i])
      f.read(30)
      for j in range(0,30): 
        seq=f.read(5)
        char=chr(toText(seq, 5))
        print(char)
        new.write(char)
        save=f.tell()   #check if any chars are left
        test=f.read(21)
        if not test: 
            break
        f.seek(save)
      f.close()        #close file

def toText(seq, length):
   
    lastChar=0
    sum =0 

    EncodingTable=[['C','G','T'], ['G','T','A'], ['T','A','C'], ['A','C','G']]

    for i in range(0,length):
        for j in range(2,-1,-1): 
            if(seq[i]==EncodingTable[lastChar][j]):           
                sum+=j*3**(length-i-1) 
                lastChar=lastChar+j+1
                if(lastChar>3):
                    lastChar-=4 
                break

    return sum 

