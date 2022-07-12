import numpy as np
from PIL import Image
import tensorflow as tf
from flask import jsonify
import cv2

def getPrediction(filename):
    
    
    
    # classes = ['Glioma Tumor' , 'No Tumor' , 'Meningioma Tumor' , 'Pituitary Tumor']
    # le = LabelEncoder()
    # le.fit(classes)
    # le.inverse_transform([2])
    

    #Load model
    my_model=tf.keras.models.load_model("./effnet.h5")


    SIZE = 150 #Resize to same size as training images
    img_path = 'static/images/'+filename
    img = np.asarray(Image.open(img_path)) #.resize((SIZE,SIZE)))
    img = cv2.resize(img , (SIZE , SIZE))
    
    # img = img/255.      #Scale pixel values
    img = np.expand_dims(img, axis=0)  #Get it tready as input to the network       
    if img.shape != (1,150,150,3):
        pred = 'incompitable image shape please make sure image has three channels'
        facts = ''
        return pred , facts
    
    pred = my_model.predict(img) #Predict 
    predict = np.array(pred)
    predict = predict.ravel()
    max_pred = max(predict) 
    
    pred = np.argmax(pred,axis=1)[0]                  
    


        
    if pred == 0:
        
            
        
        prediction = str(round(max_pred*100 ,3)) + ' %Confidence there is Glioma Tumor'
                
        facts = 'Glioma is a type of tumor that occurs in the brain and spinal cord.\
                            A glioma can affect your brain function and be life-threatening depending on\
                            its location and rate of growth. Gliomas are one of the most common types of primary brain tumors.'
                
        # return prediction , facts 
    
    elif pred == 1:
        
    
            
        prediction = str(round(max_pred*100 ,3)) + ' %Confidence there is No tumor'
                
        facts = 'there is no tumor and the brain is in a good condition'
                
        # return prediction , facts 
        
    elif pred == 2:

            
        prediction = str(round(max_pred*100 ,3)) + ' %Confidence there is meningioma Tumor'
                
        facts = 'A meningioma is a tumor that arises from the meninges, the membranes that surround your brain.\
                            Most meningiomas grow very slowly, often over many years without causing symptoms.\
                            They occur more commonly in women.'
                            
        # return prediction , facts 
        

            
    elif pred == 3:
            
        prediction = str(round(max_pred*100 ,3)) + ' %Confidence there is Pituitary Tumor'
                
        facts = 'Pituitary tumors are abnormal growths that develop in your pituitary gland.\
                            Most pituitary tumors are noncancerous (benign) growths that remain in your pituitary\
                            gland or surrounding tissues.'
                            
        # return prediction , facts 
        
    return prediction , facts    
        
            
            
     
    

