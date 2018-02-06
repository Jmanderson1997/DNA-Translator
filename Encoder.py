def encoder(original, translated):

   orig=open(original, 'r')
   trans= open(translated, 'w')

   while(True):
     character=orig.read(1)
     if not character: 
         break
     seq= toDNA(character)
     trans.write(seq[3])
     trans.write(seq[2])
     trans.write(seq[1])
     trans.write(seq[0])

   orig.close()
   trans.close()


def toDNA(character):

    asc= ord(character) 
    sequence=[]

    for i in range(3,-1, -1): 
     
        if((asc-3*4**i)>=0):
            sequence.append('G')
            asc-=3*4**i
            continue

        elif((asc-2*4**i)>=0):
            sequence.append('C')
            asc-=2*4**i
            continue

        elif((asc-4**i)>=0):
            sequence.append('T')
            asc-=4**i
            continue 

        else :
            sequence.append('A')


    return sequence


