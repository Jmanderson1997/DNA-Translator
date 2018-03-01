import pandas as pd

def numAssign(fileName): 

  fileNames=pd.read_csv("FileLedger.csv", usecols=["FileName","FileNumber"])
  fileNames_df=pd.DataFrame(fileNames)
  num=0
  found=False

  for i, row in fileNames_df.iterrows():
      if(row['FileName']==fileName): 
          return row ['FileNumber']

  while not found:
      for i, row in fileNames_df.iterrows():
          if(row['FileNumber']==num): 
             num+=1
             found=False
             break
          found=True

  newItem_df=pd.DataFrame({'FileNumber':num, 'FileName':fileName}, index=[0])
  fileNames_df=fileNames_df.append(newItem_df)
  fileNames_df.to_csv('fileLedger.csv', encoding='utf-8', index=False) 
  print(fileNames_df)
  return num      
          
  
  

   



