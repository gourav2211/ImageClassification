#!/usr/bin/env python
# coding: utf-8

# In[10]:


from flask import Flask, jsonify, render_template, request
from flask_restful import Api, Resource
import numpy as np
from keras.models import load_model
import os 
import keras
import tensorflow.compat.v1 as tf
from tensorflow.python.keras.backend import set_session
import urllib
import requests
import cv2

# In[11]:


app = Flask(__name__, template_folder='hm1')
api = Api(app)
folder = 'C:\\Users\\Satwik\\DownLoads\\Images\\data\\natural_images'


# In[12]:




global modelv2
global graph
global session
keras.backend.clear_session()
session = tf.Session()
graph = tf.get_default_graph()
set_session(session)
modelv2 = load_model('ImgClassicationV3.h5')


# In[13]:



def URL_2_Image(url):
    url_response = urllib.request.urlopen(url)
    url_response1 = np.array(bytearray(url_response.read()), dtype = np.uint8)
    print(bytearray(url_response.read()))
    print(type(url_response1))
    image  = cv2.imdecode(url_response1, cv2.IMREAD_COLOR)
    #imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_data1 = cv2.resize(image, (64,64)) 
    img_data1 = img_data1 / 255.0
    return img_data1


# In[14]:

def GetURLType(url):
    response = requests.get(url)
    file_type = response.headers.get('content-type')
    return file_type



# In[15]:

def displayImage():
    img12 = np.array(img_12)
    cv2.imshow('Image',img12)
    cv2.resizeWindow('image', 600, 600)
    cv2.waitKey(0)


# In[16]:




@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/', methods = ['POST'])
#def getValue():
#    url = request.form['Image_url']
#    return render_template('index.html', url1=url)

@app.route('/', methods = ['POST'])
def GET():  
    try:
        url = request.form['Image_url'] 
        urlType = GetURLType(url)
        if 'image' in urlType:        
            img_data1 = URL_2_Image(url)
            arr = np.zeros([1,64,64,3])
            arr[0] = img_data1
            with session.as_default():
                    with session.graph.as_default():
                        x1 = modelv2.predict(arr)              
            index = np.where(x1 == np.amax(x1))[1][0]
            #img_class = os.listdir(folder)[index]    
            return render_template('index.html', url1 = index)
    
        else:
            return ('Not an Image URL')
        
    except:
        return ('Not a URL')
        
    


# In[17]:


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

