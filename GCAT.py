def gcat(sequence):

    seq=open(sequence, "r")
    
    aCounter=0 
    tCounter=0 
    cCounter=0 
    gCounter=0 

    while(True):
     nucleotide=seq.read(1)
     if not nucleotide: 
         break
    
     if(nucleotide=='A'):
        aCounter+= 1
    
     elif(nucleotide=='T'):
        tCounter+= 1
    
     elif(nucleotide=='G'):
        gCounter+= 1

     else:
        cCounter+= 1

     
    gaRatio=gCounter/aCounter 
    ctRatio=cCounter/tCounter

    print("G-A ratio is: ",gaRatio, "C-T ratio is: " ,ctRatio)
