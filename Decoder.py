def decoder(translated, newFile) :

    trans= open(translated, 'r')
    new= open(newFile, 'w')
    
    while(True):
      seq=trans.read(4) 
      if not seq: 
          break
      char=toText(seq)
      new.write(char)

    trans.close()
    new.close

def toText(seq):
   
    sum =0 

    for i in range(3,-1, -1):

        if(seq[i]=='G'):
            sum+=3*4**i
            continue

        elif(seq[i]=='C'):
            sum+=2*4**i
            continue

        elif(seq[i]=='T'):
            sum+=1*4**i
            continue

    char = chr(sum) 
    return char 
