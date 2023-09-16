import numpy as np
import cv2
from PIL import Image
from emotion_classifier_app.models import Song
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from pandastable import Table, TableModel
from tensorflow.keras.preprocessing import image
import datetime
from threading import Thread
# from Spotipy import *  
import time
import pandas as pd
# from Spotipy import *  
import time
import pandas as pd
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, BatchNormalization, Activation
from PIL import Image, ImageDraw, ImageFont

face_cascade=cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")


ds_factor=0.6

emotion_model = Sequential()
emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))
emotion_model.load_weights('bangla.h5')

cv2.ocl.setUseOpenCL(False)

#emotion_dict = {0:"Angry",1:"Disgusted",2:"Fearful",3:"Happy",4:"Neutral",5:"Sad",6:"Surprised"}



music_dist={0:"songs/angry.csv",1:"songs/disgusted.csv ",2:"songs/fearful.csv",3:"songs/happy.csv",4:"songs/neutral.csv",5:"songs/sad.csv",6:"songs/surprised.csv"}
global last_frame1                                    
last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
 
show_text=[0]

last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
show_text = [0]

global pred
pred = []

emotion_dict = {0:"রাগী",1:"জঘন্য",2:"ভয়",3:"আনন্দিত",4:"নিরপেক্ষ",5:"বিষণ্ণ",6:"বিস্ময়"}

emotion_dict_english = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

class VideoCamera(object):
    def __init__(self, src=0, language='bangla'):
        self.stream = cv2.VideoCapture(src, cv2.CAP_DSHOW)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.language = language  # Default to 'bangla'

    def __del__(self):
        self.stream.release()

    def get_frame(self):
        global pred

        ret, image = self.stream.read()
        image = cv2.resize(image, (600, 500))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        df1 = pd.read_csv(music_dist[show_text[0]])
        df1 = df1[['Name', 'Album', 'Artist']]
        df1 = df1.head(15)

        for (x, y, w, h) in face_rects:
            cv2.rectangle(image, (x, y - 50), (x + w, y + h + 10), (0, 255, 0), 2)
            roi_gray_frame = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
            prediction = emotion_model.predict(cropped_img)

            maxindex = int(np.argmax(prediction))
            show_text[0] = maxindex

            if self.language == 'bangla':
                emotion_text = emotion_dict.get(maxindex, "অজানা")

                # Display the emotion text using PIL
                pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                draw = ImageDraw.Draw(pil_image)
                font = ImageFont.truetype('siyamrupali.ttf', 36)  # Specify the path to your Bengali font
                text_position = (x + 20, y - 60)
                draw.text(text_position, emotion_text, fill=(255, 255, 255), font=font)
                image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

            else:
                cv2.putText(image, emotion_dict_english[maxindex], (x + 20, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            df1 = music_rec()
            pred.append(show_text[0])

        global last_frame1
        last_frame1 = image.copy()
        img = Image.fromarray(last_frame1)
        img = np.array(img)
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes(), df1

def music_rec():
    if not pred:  
        return pd.DataFrame(columns=['Name', 'Album', 'Artist']) 
    
    last_index = pred[-1]  #last item from 'pred'

    
    if last_index in music_dist:
        csv_path = music_dist[last_index]
        df = pd.read_csv(csv_path)
        df = df[['Name', 'Album', 'Artist']]
        df = df.head(15)
        return df
    else:
        return pd.DataFrame(columns=['Name', 'Album', 'Artist'])  
    



text={0:"angry",1:"disgusted ",2:"fearful",3:"happy",4:"neutral",5:"sad",6:"surprised"}
   
def music_rec_data():
    if not pred:  
        return pd.DataFrame(columns=['Name', 'Link','Album', 'Artist'])  
    
    last_index = pred[-1]  # last item from 'pred'
    print(last_index)
    
    if last_index in text:
        db_path = text[last_index]
        print(db_path)
        return db_path
    else:
        return pd.DataFrame(columns=['Name','Link', 'Album', 'Artist'])  
    

from random import sample

def music_data(prediction):
    music_preds = Song.objects.filter(emotion=prediction)
    music_preds = sample(list(music_pred), 10)
    for music_pred in music_preds:
        name = music_pred.Name
        link = music_pred.Link
        album = music_pred.Album
        artist = music_pred.Artist
    return music_pred






