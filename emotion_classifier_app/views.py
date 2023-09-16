from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .track_utils import create_page_visited_table, add_page_visited_details, view_all_page_visited_details, add_prediction_details, view_all_prediction_details, create_emotionclf_table
import pandas as pd
import joblib
import numpy as np
import base64
import cv2
from keras.models import model_from_json
from django.http import StreamingHttpResponse
import base64
from .camera import VideoCamera, music_data, music_rec, music_rec_data
from .models import Song
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

pipe_lr = joblib.load(open("./models/emotion_classifier_pipe_lr.pkl", "rb"))


def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    return results[0]

def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results

emotions_emoji_dict = {"anger" : "😠", "disgust" : "🤮", "fear" : "😨😱", "happy" : "🤗", "joy" : "😂", "neutral" : "😐", "sad" : "😔", "sadness" : "😔", "shame" : "😳", "surprise" : "😮"}

@login_required
def home(request):
     return render(request, 'emotion_classifier_app/home.html')

music_dist={"anger":"angry","disgust":"disgusted","fear":"fearful","happy":"happy","joy":"happy","neutral":"neutral","sad":"sad","surprise":"surprised","sadness":"sad"}



def music_data(prediction):
    music_pred = Song.objects.filter(emotion=prediction).values('name', 'link', 'album', 'artist')[:10]
    return music_pred

def text(request):
    add_page_visited_details("text", datetime.now())
    
    if request.method == 'POST':
        raw_text = request.POST.get('raw_text')
        
    
        prediction = predict_emotions(raw_text)
        probability = get_prediction_proba(raw_text)
        
      
        emoji_icon = emotions_emoji_dict[prediction]
        
        add_prediction_details(raw_text, prediction, np.max(probability), datetime.now())

        music_pred = music_data(music_dist[prediction])


        context = {
            'raw_text': raw_text,
            'prediction': prediction,
            'emoji_icon': emoji_icon,
            'confidence': np.max(probability),
            'music_pred':music_pred,

        }
    else:
        context = {}
    
    return render(request, 'emotion_classifier_app/text.html', context)





def about(request):
    add_page_visited_details("About", datetime.now())
    return render(request, 'emotion_classifier_app/about.html')


def monitor(request):
    add_page_visited_details("Monitor", datetime.now())
    
    page_visited_details = pd.DataFrame(view_all_page_visited_details(), columns=['Page Name', 'Time of Visit'])
    pg_count = page_visited_details['Page Name'].value_counts().rename_axis('Page Name').reset_index(name='Counts')
    
    prediction_count = pd.DataFrame(view_all_prediction_details(), columns=['Rawtext', 'Prediction', 'Probability', 'Time_of_Visit'])
    prediction_count = prediction_count['Prediction'].value_counts().rename_axis('Prediction').reset_index(name='Counts')
    
    context = {
        'pg_count': pg_count.to_dict(orient='records'),
        'prediction_count': prediction_count.to_dict(orient='records'),
    }
    
    return render(request, 'emotion_classifier_app/monitor.html', context)



music_dist_img={"anger":"songs/angry.csv","disgust":"songs/disgusted.csv ","fear":"songs/fearful.csv","happiness":"songs/happy.csv","neutral":"songs/neutral.csv","sadness":"songs/sad.csv","surprise":"songs/surprised.csv"}

from PIL import Image, ImageDraw, ImageFont


bengali_font_path = 'siyamrupali.ttf'
font_size = 35  

@csrf_exempt  
def image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

       
        selected_language = request.POST['language']

       
        if selected_language == 'bangla':
           
            json_file = open('models/bangla.json', 'r')
            model_weights_file = 'models/bangla.h5'
            emotions = ['নিরপেক্ষ', 'আনন্দিত', 'বিস্ময়', 'বিষণ্ণ', 'রাগী', 'জঘন্য', 'ভয়']
        elif selected_language == 'english':
           
            json_file = open('models/fer.json', 'r')
            model_weights_file = 'models/fer.h5'
            emotions = ['neutral', 'happy', 'surprise', 'sad', 'angry', 'disgusted', 'fearful']
        else:
           
            return HttpResponse("Unsupported language")

        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)

       
        model.load_weights(model_weights_file)

        classifier = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces_detected = classifier.detectMultiScale(gray_img, 1.18, 5)

       
        bengali_font = ImageFont.truetype(bengali_font_path, font_size)

        data = None  

        for (x, y, w, h) in faces_detected:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray_img[y:y + w, x:x + h]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            img_pixels = np.array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            img_pixels = img_pixels.astype('float32') / 255.0  

            predictions = model.predict(img_pixels)
            max_index = int(np.argmax(predictions))

            if selected_language == 'bangla':
                predicted_emotion = emotions[max_index]
            else:
                predicted_emotion = emotions[max_index]

            print(predicted_emotion)

            if selected_language == 'bangla':
                
                image_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                draw = ImageDraw.Draw(image_pil)

                text_position = (int(x), int(y))
                draw.text(text_position, predicted_emotion, font=bengali_font, fill=(255, 255, 255))
                img = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)


                emotions_data = {'নিরপেক্ষ':'neutral', 'আনন্দিত':'happy', 'বিস্ময়':'surprise', 'বিষণ্ণ':'sad', 'রাগী':'angry', 'জঘন্য':'disgusted', 'ভয়':'fearful'}
                data = emotions_data[predicted_emotion]
                print(data)

                data = music_data(data)
                print(data)

            
            if selected_language == 'english':

                cv2.putText(img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)


                data = music_data(predicted_emotion)
                print(data)

        _, buffer = cv2.imencode('.jpg', img)
        img_base64 = base64.b64encode(buffer).decode('utf-8')

        context = {
            'emotion_image': img_base64,
            'data': data,
        }

        return render(request, 'emotion_classifier_app/image.html', context)

    return render(request, 'emotion_classifier_app/image.html')

def music_recommendations(request):
    songs = Song.objects.filter(emotion=music_rec_data())[:10]

    data = [{'Name': song.name, 'Link': song.link, 'Album': song.album, 'Artist': song.artist} for song in songs]
    return JsonResponse(data, safe=False)


def video(request):
    context = {}  

    if request.method == 'POST':
        language = request.POST.get('language', 'bangla')  

       
        video_feed_url = 'video_feed_bangla' if language == 'bangla' else 'video_feed_english'

      
        context = {
            'language': language,
            'video_feed_url': video_feed_url,
        }
  
    return render(request, 'emotion_classifier_app/video.html', context)

def gen(camera):
    while True:
        frame, _ = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed_bangla(request):
    return StreamingHttpResponse(gen(VideoCamera(language='bangla')),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

def video_feed_english(request):
    return StreamingHttpResponse(gen(VideoCamera(language='english')),
                                 content_type='multipart/x-mixed-replace; boundary=frame')




def songs_by_emotion(request, emotion):
    songs = Song.objects.filter(emotion=emotion)
    context = {'songs': songs, 'emotion': emotion}
    return render(request, 'songs_by_emotion.html', context)


