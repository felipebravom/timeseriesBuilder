'''
Created on Mar 4, 2013

@author: fbravo
'''

import os
import sys
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

    print names
    
    # neutral tweets according Twitter Sentiment
    tsent_neutral_count=0.0
    tsent_positive_count=0.0
    tsent_negative_count=0.0
    
    sentiStrength_pos=0.0
    sentiStrength_neg=0.0
    swn3_positiveness=0.0
    swn3_negativeness=0.0
    afinn_positiveness=0.0
    afinn_negativeness=0.0
    lex_positive_words=0.0
    lex_negative_words=0.0
    
    
    
    
    for line in lines[1:]:
        values=line.rstrip('\n').split("\t")
        sentiStrength_pos+=float(values[names.index("sentiStrength_pos")])
        sentiStrength_neg+=float(values[names.index("sentiStrength_neg")])
        
        swn3_positiveness+=float(values[names.index("swn3_positiveness")])
        swn3_negativeness+=float(values[names.index("swn3_negativeness")])
        
        afinn_positiveness+=float(values[names.index("afinn_positiveness")])
        afinn_negativeness+=float(values[names.index("afinn_negativeness")])
        
        lex_positive_words+=float(values[names.index("lex_positive_words")])
        lex_negative_words+=float(values[names.index("lex_negative_words")])
        
        
        
        
        if(values[names.index("supervised_polarity")]=="neutral"):
            tsent_neutral_count+=1
        elif(values[names.index("supervised_polarity")]=="positive"):
            tsent_positive_count+=1
        else:
            tsent_negative_count+=1
        
            
    #number of observations
    obser=len(lines)-1
    tsent_neutral_frac=tsent_neutral_count/obser
    tsent_positive_frac=tsent_positive_count/obser
    tsent_negative_frac=tsent_negative_count/obser
    
    
    avg_sentStrength_pos=sentiStrength_pos/obser
    avg_sentStrength_neg=sentiStrength_neg/obser
    
    avg_swn3_positiveness=swn3_positiveness/obser
    avg_swn3_negativeness=swn3_negativeness/obser
    
    avg_afinn_positiveness=afinn_positiveness/obser
    avg_afinn_negativeness=afinn_negativeness/obser
    avg_lex_positive_words=lex_positive_words/obser
    avg_lex_negative_words=lex_negative_words/obser
    
    
    
    
    
    print obser        
    
    variables={"activity":obser,
               "tsent_neutral_frac":tsent_neutral_frac,
               "tsent_positive_frac":tsent_positive_frac,
               "tsent_negative_frac":tsent_negative_frac,               
               "avg_sentStrength_pos":avg_sentStrength_pos,
               "avg_sentStrength_neg":avg_sentStrength_neg,
               "avg_swn3_positiveness":avg_swn3_positiveness,
               "avg_swn3_negativeness":avg_swn3_negativeness,
               "avg_afinn_positiveness":avg_afinn_positiveness,
               "avg_afinn_negativeness":avg_afinn_negativeness,
               "avg_oppfinder_positive_words":avg_lex_positive_words,
               "avg_oppfinder_negative_words":avg_lex_negative_words              
               }
    return variables
    
   
       # out_file.write(variables.get("activity")+",")
        
        #values=variables.get("activity")+","+variables.get("tsent_neutral_frac")+","+variables.get("tsent_positive_frac")+","+variables.get("tsent_negative_frac")+","+
        #variables.get("avg_sentStrength_pos")+","+variables.get("avg_sentStrength_neg")+","+
        #variables.get("avg_swn3_positiveness")+","+variables.get("avg_swn3_negativeness")+","+
        #variables.get("avg_swn3_positiveness")+","+variables.get("avg_swn3_negativeness")+","+
        #variables.get("avg_afinn_positiveness")+","+variables.get("avg_afinn_negativeness")+","+
        #variables.get("avg_oppfinder_positive_words")+","+variables.get("avg_oppfinder_positive_words")
                
    

if __name__ == '__main__':
    pass


    files=os.listdir(FOLDER_PATH)
    my_dict={}    
    for f in files:
        if (f.find(':')!=-1):  
            try:
                date=datetime.strptime(f.split(":")[1],"%Y-%m-%d")
                my_dict[date]=f
            except:
                print "Unexpected error:", sys.exc_info()[0]
                pass
            
    dates=sorted(my_dict.keys())
    
   # for date in dates:
   #     print my_dict.get(date)
   
    out_file = open(FOLDER_PATH+'workfile', 'w')
    out_file.write("date,activity,tsent_neutral_frac,tsent_positive_frac,tsent_negative_frac,")
    out_file.write("avg_sentStrength_pos,avg_sentStrength_neg,avg_swn3_positiveness,")
    out_file.write("avg_swn3_negativeness,avg_afinn_positiveness,avg_afinn_negativeness,")
    out_file.write("avg_oppfinder_positive_words,avg_oppfinder_positive_words\n")
        
    
    
    for date in dates:
        variables=process_file(FOLDER_PATH+my_dict.get(date))   
        

        out_file.write(str(date)+",")
        out_file.write(str(variables.get("activity"))+",")
        out_file.write(str(variables.get("tsent_neutral_frac"))+",")
        out_file.write(str(variables.get("tsent_positive_frac"))+",")
        out_file.write(str(variables.get("tsent_negative_frac"))+",")
        out_file.write(str(variables.get("avg_sentStrength_pos"))+",")
        out_file.write(str(variables.get("avg_sentStrength_neg"))+",")
        out_file.write(str(variables.get("avg_swn3_positiveness"))+",")
        out_file.write(str(variables.get("avg_swn3_negativeness"))+",")
        out_file.write(str(variables.get("avg_afinn_positiveness"))+",")
        out_file.write(str(variables.get("avg_afinn_negativeness"))+",")
        out_file.write(str(variables.get("avg_oppfinder_positive_words"))+",")
        out_file.write(str(variables.get("avg_oppfinder_positive_words"))+"\n")
          
     
    
         
        
        
        values=str(variables.get("activity"))+","+str(variables.get("tsent_neutral_frac"))+","
        
        
        print date,variables
        
    out_file.close()
        
  
  
    
    
    # values=lines[1].rstrip('\n').split("\t")


   
        

        
    