'''
Created on Mar 4, 2013

@author: fbravo
'''

import os
import re
import datetime 
from datetime import datetime


FOLDER_PATH="/home/fbravo/EvaluatedTweets/obama2Eval/"


def print_string(inpt1):
    print(inpt1)
  
    
def process_file(file_name):
    f=open(file_name, "rb")
    lines=f.readlines()
    f.close()
    
    names=lines[0].rstrip('\n').split("\t")

    #print names
    
    neutral_count=0.0
    sentiStrength_pos=0
    sentiStrength_neg=0
    
    for line in lines[1:]:
        values=line.rstrip('\n').split("\t")
        sentiStrength_pos+=int(values[names.index("sentiStrength_pos")])
        sentiStrength_neg+=int(values[names.index("sentiStrength_neg")])
        if(values[names.index("supervised_polarity")]=="neutral"):
            neutral_count+=1
            
    #number of observations
    obser=len(lines)-1
    neutral_frac=neutral_count/obser
    
    print obser        
    
    variables={"neutral":neutral_frac,"sentriStrength_pos":sentiStrength_pos,
               "sentiStrength_net":sentiStrength_neg}
    return variables
    
   
        
    

if __name__ == '__main__':
    pass



    files=os.listdir(FOLDER_PATH)
    my_dict={}    
    for f in files:
        if (f.find(':')!=-1):            
            date=datetime.strptime(f.split(":")[1],"%Y-%m-%d")
            my_dict[date]=f
            
    dates=sorted(my_dict.keys())
    
   # for date in dates:
   #     print my_dict.get(date)
    
    for date in dates:
        variables=process_file(FOLDER_PATH+my_dict.get(date))
        print date,variables
        
 

            
    
    
    # values=lines[1].rstrip('\n').split("\t")


   
        

        
    