import os
import pandas as pd
from pandas import ExcelWriter
from Decoder import toText

def numAssign(fileName): 

  fileNames=pd.read_csv("FileLedger.xlsx", usecols=["FileNames","FileNumber"])
  fileNames_df=pd.DataFrame(fileNames)

  for i in len(fileNames_df): 
      if(fileNames_df[i][0]==fileName): 
          return fileNames_df[i][1]

  for i in len(fileNames_df): 
      if(fileNames[i][0]==""):
          fileNames_df[i][0]=fileName
          fileNames_df[i][1]=i
          writer = ExcelWriter('FileLedger.xlsx')
          fileNames.to_excel(writer)
          return fileNames[i][1] 
  
  

   



