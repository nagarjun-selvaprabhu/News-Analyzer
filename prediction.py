# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:45:40 2017

@author: NishitP
"""

import pickle

#doc_new = ['obama is running for president in 2016']
text=open("summary.txt","r")
newtext=""
texts=text.readlines()
for characters in texts:
	newtext=newtext+characters
print(newtext)
var =newtext
print("You entered: " + str(var))


#function to run for prediction
def detecting_fake_news(var):    
#retrieving the best model for prediction call
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])
    predictionfile=open("predictionfile.txt","w")
    predictionfile.write(str(prediction[0]))
    predictionfile.close()

    return (print("The given statement is ",prediction[0]),
        print("The truth probability score is ",prob[0][1]))


if __name__ == '__main__':
    detecting_fake_news(var)