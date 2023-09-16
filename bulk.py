# bulk_create_songs.py

import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emotion_classifier_project.settings')

# Configure Django settings
django.setup()

# Now you can import your models
from emotion_classifier_app.models import Song  # Update to your app's model import

## Emotion list =  [  angry , disgusted ,  fearful , happy , neutral , sad , surprised ]

def bulk_create_songs():
    songs_to_insert = [
        Song(emotion='sad', name='Happy-13856', album= 'Despicable Me 2 (Original Motion Picture Soundtrack)', artist='Pharrell Williams', link='https://youtu.be/ZbZSe6N_BXs?si=vW81CMKnOzHf0AbG'),
        Song(emotion='sad', name='Takey Olpo Kachhe Dakchhi', album='Album 1', artist='Sohini Mukherjee', link='https://youtu.be/boZFmtxxV-Q?si=RfI3v0FD-i11BnEt'),
        Song(emotion='sad', name='Dilli Wali Girlfriend', album='YEH JAWAANI HAI DEEWANI', artist='ARIJIT SINGH, SUNIDHI CHAUHAN', link='https://youtu.be/1cDoRqPnCXU?si=kwq_mFibK79uCZbu'),
        Song(emotion='sad', name='Tooh (144 BPM)', album='Album 1', artist='Vishal & Shekhar, Mika Singh, Mamta Sharma', link='https://youtu.be/91kbNw9DZBg?si=GSkRouudvTnms7h0'),
        Song(emotion='sad', name='ABHI TOH PARTY SHURU HUI HAI', album='KHOOBSURAT', artist='BADSHAH | AASTHA', link='https://youtu.be/8LZgzAZ2lpQ?si=5XSFgtJxSWNCq2ix'),
        Song(emotion='sad', name='Bom Diggy', album='Album 1', artist='Zack Knight, Jasmin Walia', link='https://youtu.be/yIIGQB6EMAM?si=i8SfMekshK-d292-'),
        Song(emotion='sad', name='London Thumakda', album='QUEEN', artist='LABH JANJUA | SONU KAKKAR | NEHA KAKKAR', link='https://youtu.be/udra3Mfw2oo?si=KpM6uamg7hOE75px'),
        Song(emotion='sad', name='Badtameez Dil (From "Yeh Jawaani Hai Deewani")', album='Album 1', artist='Benny Dayal, Shefali Alvares', link='https://youtu.be/II2EO3Nw4m0?si=sqekyCdKAwOtKcx7'),
        Song(emotion='sad', name='Shaam Shaandaar', album='Shaandaar', artist='Amit Trivedi', link='https://youtu.be/D21Di3NXcYM?si=63CTIDtcEmOnIyq4'),
        Song(emotion='sad', name='03 FEVICOL SE', album='DABANGG 2', artist='MAMTA SHARMA, WAJID, BACK UP VOCALS', link='https://youtu.be/zE7Pwgl6sLA?si=7lMQdV68ADU2MH6_'),
        Song(emotion='sad', name='First Class Full Video Kalank', album='Album 1', artist='Artist 1', link='https://youtu.be/e8B0AzmXPV8?si=ON-Qv9wc55DgeuIL'),
        Song(emotion='sad', name='SLOW MOTION', album='BHARAT', artist='SHREYA GHOSHAL,NAKASH AZIZ', link='https://youtu.be/8AedZtuoVSg?si=S80o2AeNfH1Yg9c7'),
        Song(emotion='sad', name='Khadke Glassy Video Jabariya Jodi', album='Album 1', artist='Artist 1', link='https://youtu.be/YcDw4h3SUfI?si=0m623crje81GyRD-'),
        Song(emotion='sad', name='The Hook Up Song', album='Student Of The Year 2', artist='Vishal - Shekhar', link='https://youtu.be/zuaLWHiRXkg?si=TQsOwq0N7e3KieK5'),
        Song(emotion='sad', name='Kamariya', album='Album 1', artist='Artist 1', link='https://youtu.be/i0_m90T04uw?si=WUw6MEfPVRLm_GV_'),
        Song(emotion='sad', name='O SAKI SAKI', album='BATLA HOUSE', artist='NEHA KAKKAR,TULSI KUMAR,B PRAAK', link='https://youtu.be/_uUdJalMaF8?si=nk_gXos4QQCSdyKt'),
        Song(emotion='sad', name='Dhat Teri Ki', album='Album 1', artist='Vishal & Shekhar, Sanam Puri, Aditi Singh Sharma', link='https://youtu.be/1RaSwAdSEKQ?si=o8uU0WxA4BQlD1-Z'),
        Song(emotion='sad', name='Sunroof', album='Album 1', artist='Nicky Youre, dazy', link='https://youtu.be/G5xSLbYMr-I?si=Ir2O3TIQNPwiwk0P'),
        Song(emotion='sad', name='Classic', album='Album 1', artist='MKTO', link='https://youtu.be/4Ba_qTPA4Ds?si=vRtbQXT-TRpc7R_K'),
        Song(emotion='sad', name='Sunday Best', album='Sunday Best', artist='Surfaces', link='https://youtu.be/lyIhRNPCNiw?si=uRz10vsxc2c-iJO9'),
        Song(emotion='sad', name='Song 1', album='Album 1', artist='Artist 1', link='https://youtu.be/NITT5IZJj5Y?si=DJ6Tv684EUP4ra9l'),
        Song(emotion='sad', name='Aaluma Doluma', album='Album 1', artist='Anirudh Ravichander, Badshah', link='https://youtu.be/2ogKpj5QuSY?si=Jj4JBVbZhfQknczq'),
        Song(emotion='sad', name='Pachchai Vanna', album='Album 1', artist='Yuvanshankar Raja', link='https://youtu.be/4J2PR9GCad0?si=gyEZd5C98fqje1df'),
        Song(emotion='sad', name='Yaanji', album='Yaanji', artist='Sam C.S., Anirudh Ravichander', link='https://youtu.be/Y3-PeuQ7nvY?si=o4u6pIrBH4_-5cFR'),
        Song(emotion='sad', name='EI SANDAKARA', album='Album 1', artist='Dhee', link='https://example.com/song7'),
        Song(emotion='sad', name='Song 1', album='IRUDHI SUTTRU', artist='Artist 1', link='https://youtu.be/tE79eMl1ocE?si=4z74CPv7Ii7DCFBr'),
        Song(emotion='sad', name='Kannala Kannala', album='Album 1', artist='Hiphop Tamizha, Kaushik Krish, Padmalatha', link='https://youtu.be/iHagLitT-nI?si=K3WMeZywOObmTTq1'),
        Song(emotion='sad', name='O PRIYOTOMA', album='Album 1', artist='BALAM', link='https://youtu.be/VXDO1LQNx54?si=0Ue1Sgq-oygPt_qm'),
        Song(emotion='sad', name='Olir Katha Shune Bakul Hase', album='Retro Cool - Bengali', artist='Debolinaa Nandy', link='https://youtu.be/XpYWLmtvvII?si=p8nQhX9BpvHjgbcZ'),
        Song(emotion='sad', name='Takey Olpo Kachhe Dakchhi', album='Album 1', artist='Artist 1', link='https://youtu.be/Nly8TUAGyYI?si=n1TgNArB3s_f6c8A'),

        Song(emotion='sad', name='Megher Nouka', album='Album 1', artist='Artist 1', link='https://youtu.be/nu7xilUwFU4?si=HyWPeYB20Cflk9bA'),
    
        Song(emotion='sad', name='Jar Chobi Ei Mon Eke Jai', album='Album 1', artist='Artist 1', link='https://youtu.be/PUZzMer5quc?si=RjLTqMLAOHtvh7Xw'),
        Song(emotion='happy', name='এ কেমন ভালোবাসা ', album='Album 2', artist='Artist 2', link='https://youtu.be/2tKiJ0iMk7M?si=LSCl2-ZaHT8rYtQq'),
        Song(emotion='happy', name='FERATE PARINI', album='FERATE PARINI', artist='Rehaan Rasul', link='https://youtu.be/PMdjLnhrxxc?si=i-T7sFlv0vyMKlAF'),
        Song(emotion='happy', name='যত চাই ভুলে যেতে', album='Album 2', artist='Artist 2', link='https://youtu.be/H-3P4T9nmbw?si=lRKMOAscvWgTFO1g'),
        Song(emotion='happy', name='Mon Pinjira', album='Mon Pinjira ', artist='Shilpi Biswas', link='https://youtu.be/WshuX7j-bIg?si=C07H-a0-FzF6dm_r'),
        Song(emotion='happy', name='Oviman', album='Oviman ', artist='Tanveer Evan', link='https://youtu.be/rPSH0gnRFb4?si=cP4QwE3Y3UhRMlRz'),
        Song(emotion='happy', name='utshorgo', album='Album 2', artist='Artist 2', link='https://youtu.be/wxflo1WRXM8?si=FBvRk8b-deqVW7Fx'),
        Song(emotion='happy', name='Ajo Khuji Tomay ', album='Album 2', artist='Artist 2', link='https://youtu.be/LiZfjRJ2PE8?si=yM62MggyjxWDqwrI'),
        Song(emotion='happy', name='Obak Nistobdhota', album='Album 2', artist='Artist 2', link='https://youtu.be/j081tCs0esM?si=pLAJfsuM_x2b1ut1'),
        Song(emotion='happy', name='Song 2', album='HEARTLESS', artist='Arijit Singh', link='https://youtu.be/nVGNUIj31ks?si=y1G2x98fi9tVUaIG'),
        Song(emotion='happy', name='প্রেম আমার', album='Album 2', artist='Artist 2', link='https://youtu.be/HOFuxsWKkpk?si=et4WpdTYmGjON07G'),
        Song(emotion='happy', name='𝗢 𝗞𝗵𝘂𝗱𝗮', album='HERO', artist='AMAAL MALLIK | PALAK MUCHCHAL', link='https://youtu.be/adzmgXcRtS4?si=_PEYYpW9sd1tu3yg'),
        Song(emotion='happy', name='কেন লাগে শূন্য শূন্য বলো', album='Album 2', artist='Artist 2', link='https://youtu.be/MMaqEJuj12s?si=0yQhTlh3BTmCU59n'),
        Song(emotion='happy', name='Ekhon Ami', album='Album 2', artist='Shopnolok @ OV', link='https://youtu.be/fl1gPghIMME?si=SHkiqgBxx3zvECY6'),
        Song(emotion='happy', name='Roi Na Je yaad Meri Aayi Ve', album='Album 2', artist='Gippy Grewal, Shipra Goyal', link='https://youtu.be/ykEAN3tKUNA?si=M8NGkQUHVuQUdIMD'),
        Song(emotion='happy', name='Zihaal e Miskin ', album='Album 2', artist='Artist 2', link='https://youtu.be/11OWuPcElJw?si=7HOnGCJEl_KHoxNY'),
        Song(emotion='angry', name='Chap Nai', album='Album 1', artist='Artist 1', link='https://youtu.be/UqMWgsWH7RU?si=9kzjNMCFJQMY8Vx1'),
        Song(emotion='angry', name='Gully Boy Part 3', album='Album 1', artist='Tabib Mahmud', link='https://youtu.be/gYTScf3H6A4?si=cHTfGFkch4JkElut'),
        Song(emotion='angry', name='Mera Intkam Dekhegi Krishna Beura', album='Shaadi Mein Zaroor Aana', artist='Anand Raaj Anand', link='https://youtu.be/BiVyN2ftrrs?si=Lt2DTRdUnr5oN_xY'),
        Song(emotion='angry', name='Band Khepar Dol', album='Album 1', artist='Artist 1', link='https://youtu.be/rvgjDbRPACc?si=DFTsBBS64YJVKqpr'),
        Song(emotion='angry', name='Ami Durbol Noi', album='Album 1', artist='Artist 1', link='https://youtu.be/_yqWPo04BHk?si=0Hvobz0v-M9LlSQl'),
        Song(emotion='Bebshar Poristhiti', name='Song 1', album='Album 1', artist='Artist 1', link='https://youtu.be/CSB8DohoFfA?si=MI0NXmkhQl-p6HoE'),
        Song(emotion='angry', name='Brothers Anthem', album='Album 1', artist='Ajay-Atul, Vishal Dadlani', link='https://youtu.be/IjBAgWKW12Y?si=xrvsRl5aW-1SomVy'),
        Song(emotion='angry', name='About Corona Virus', album='Album 1', artist='Tabib Mahmud', link='https://youtu.be/3paxCPKZOzE?si=irGGkuW3I-pzAX8C'),
        Song(emotion='angry', name='Kortobbo', album='Album 1', artist='Tabib Mahmud', link='https://youtu.be/HWX-Uyw_Okw?si=4rW3ott0rbx4Pi3h'),
       
        Song(emotion='angry', name="I can't breathe", album='Album 1', artist='Artist 1', link='https://youtu.be/2R2vbyW7CE8?si=1qvXTzPHk-gnniKm'),
        Song(emotion='angry', name='Tui Dhorshok ', album='Album 1', artist='Tabib Mahmud', link='https://youtu.be/C10rFT73Baw?si=RT9FDn9OCcoOp-mm'),
        Song(emotion='angry', name='Dipto Bedonapat ', album='Album 1', artist='Artist 1', link='https://youtu.be/YHuZMfmJTwE?si=xEd3MUbuCr9bxUlE'),
        Song(emotion='angry', name='Talking future', album='Album 1', artist='Artist 1', link='https://youtu.be/9L7XuyI0S-k?si=3shBpeQDaUOa0w_Y'),
        Song(emotion='angry', name='La Câlin', album='Album 1', artist='Serhat Durmus', link='https://youtu.be/g-MQTX0FnB0?si=IwD-70i4hCc8vncF'),
        Song(emotion='angry', name='Bad Boy', album='Album 1', artist='Raaban, Tungevaag', link='https://youtu.be/uj3FIwVKjDo?si=G9rkj-tiDyuPUIT6'),
        Song(emotion='disgusted', name='Disgusted', album='Album 2', artist='Artist 2', link='https://example.com/song2'),
        Song(emotion='disgusted', name='Hey You', album='Album 2', artist='Disturbed', link='https://youtu.be/YCGIj7KmwyI?si=Ngu0wNrbUl1GX2lE'),
        Song(emotion='disgusted', name='DJ Baharul', album='Album 2', artist='Artist 2', link='https://youtu.be/3kiS0KCX0-o?si=9GNP23N0yZRIbilb'),
        Song(emotion='disgusted', name='Ekta Chigarette Jalao', album='Album 2', artist='Hero Alom', link='https://youtu.be/2R2vbyW7CE8?si=-xgWq5J_DDkCuSm5'),
        Song(emotion='disgusted', name='তুমি ছাড়া আমি', album='Album 2', artist='Hero Alom & Ranu Mondal', link='https://youtu.be/ezHfNHX6zh4?si=tDQ3gpU5VLzS8o77'),
        Song(emotion='disgusted', name='বাবু খাইছো X কাচা বাদাম ', album='Album 2', artist='Artist 2', link='https://youtu.be/lvyh9JEjAZU?si=L7wgYvc8GkQMey2u'),
        Song(emotion='disgusted', name='Valentines Day', album='Album 2', artist='Artist 2', link='https://youtu.be/WZl2YEwE3ic?si=gGf63eGBmCD87NyZ'),
        Song(emotion='disgusted', name='Beiman ', album='Album 2', artist='Dr. Mahfuzur Rahman', link='https://youtu.be/ukRl-jNQXZk?si=KFDvAipw7UHO05xs'),
        Song(emotion='disgusted', name='ঘুমাতে পারি না', album=' ঘুমাতে পারি না', artist='Artist 2', link='https://youtu.be/QolH7e5bu2g?si=mWBbYtkox4ies8z5'),
        Song(emotion='disgusted', name='Pataka (পটাকা)', album='Album 2', artist='Nusrta Faria', link='https://youtu.be/0QP3JTfQ-GQ?si=7fwhGXvktuEFyExS'),
        Song(emotion='disgusted', name='Ektu Khani Haso', album='Album 2', artist='Artist 2', link='https://youtu.be/QJG6ZHTxn8Y?si=DsYVfvV2OfpO5zvM'),
        Song(emotion='fearful', name='Bhayanaka Fearful', album='Album 1', artist='Bickram Ghosh', link='https://youtu.be/ArWR1UR7Ufc?si=P28jSuuBZmOoakdh'),
        Song(emotion='fearful', name='Stree ', album='Album 1', artist='Artist 1', link='https://youtu.be/X2iFoJ8NAU4?si=NV4_-5fzXe2RuUiO'),
        Song(emotion='fearful', name='Midnight Magic Five Skeletons', album='Album 1', artist='Artist 1', link='https://youtu.be/pDzjAuyCxxI?si=ZSNRxrRZ7SmPlvet'),
        Song(emotion='fearful', name='I Can See You', album='Album 1', artist='Artist 1', link='https://youtu.be/sp9T5NG-bQA?si=Y6x5KXLu_9GYqJpq'),
        Song(emotion='fearful', name='Nei Alo (নেই আলো )', album='Album 1', artist='Artist 1', link='https://youtu.be/sp7_KKHstxI?si=XY91cMk6CNLucokK'),
        Song(emotion='fearful', name='এক যে ছিলাম আমি', album='Album 1', artist='Artist 1', link='https://youtu.be/5PtVfECix1M?si=v5MzYkhPnobLWz1r'),
        Song(emotion='fearful', name='Annabelle Rap Song', album='Album 1', artist='Artist 1', link='https://youtu.be/hkgr5eV0K24?si=GAxaP3DUPsiYIzDn'),
        Song(emotion='fearful', name='Ghost Sounds', album='Album 1', artist='Artist 1', link='https://youtu.be/x-pgysXqdlM?si=gbTtw10SgsLzx-CW'),
        Song(emotion='fearful', name='Wednesday Sings A Song', album='Album 1', artist='Artist 1', link='https://youtu.be/aJwCrAnH6-Y?si=ObNfDSIgIj6VV_dx'),
        Song(emotion='neutral', name='Heeriye', album='Album 2', artist='Artist 2', link='https://youtu.be/RLzC55ai0eo?si=3-LFKWHqewexldIL'),
        Song(emotion='neutral', name='Feelings of love Jukebox', album='Album 2', artist='Artist 2', link='https://youtu.be/Tx_SyNQXhgY?si=oJm9-v6s24lV9NO6'),
        Song(emotion='neutral', name='Soft Songs', album='Album 2', artist='Artist 2', link='https://youtu.be/QN0BfamqA4Y?si=oUpRxLJxe8h98_FE'),
        Song(emotion='neutral', name='amar vin desi tara', album='Album 2', artist='Artist 2', link='https://youtu.be/_ONeq4G8VEE?si=-dnFGWAzS4p3gqXP'),
        Song(emotion='neutral', name='Takey Olpo Kachhe Dakchhi', album='Album 2', artist='Artist 2', link='https://youtu.be/boZFmtxxV-Q?si=UP5tkyqDx1StQwSo'),
        Song(emotion='neutral', name='Tomake', album='Album 2', artist='Artist 2', link='https://youtu.be/Whr3M4P2RKE?si=VjYREq_BRH5b29P8'),
        Song(emotion='surprised', name="Bengali Valentine's Mashup", album='Album 2', artist='Artist 2', link='https://youtu.be/OjfiRe6u3yg?si=ajZu6weUqIz1R8Rx'),
        Song(emotion='surprised', name='Morning songs', album='Album 2', artist='Artist 2', link='https://www.youtube.com/live/BPaYNAXsNmE?si=sbbm6P88pfY_IEUD'),
        Song(emotion='surprised', name='MATARGASHTI ', album='Album 2', artist='Artist 2', link='https://youtu.be/6vKucgAeF_Q?si=u5ADoSz58qWZe2EP'),
        Song(emotion='surprised', name='Sauda Khara Khara', album='Album 2', artist='Artist 2', link='https://youtu.be/LYEqeUr-158?si=I1BEqHG9XpPzFuk8'),
        Song(emotion='surprised', name='Amar Ekla Aakash', album='Album 2', artist='Artist 2', link='https://youtu.be/__zhTIfjPBE?si=5ww4U3Z0E82Iu6SF'),
        Song(emotion='surprised', name='Tomari Achi', album='Album 2', artist='Artist 2', link='https://youtu.be/WJBViwf9L8Q?si=po-qaG1KKBOpZ7Pf'),
        Song(emotion='surprised', name='THE PUNJAABBAN', album='Album 2', artist='Artist 2', link='https://youtu.be/yThYwOixjYg?si=9YwbZGOhtxikUpz-'),
        Song(emotion='surprised', name='Shagorer Tirey', album='Album 2', artist='Artist 2', link='https://youtu.be/Pm3KHU-edJo?si=BlKUnMhC0hjwk2fR'),

        


        # Add more songs to the list with links
    ]

    # Use bulk_create to insert the list of songs into the database
    Song.objects.bulk_create(songs_to_insert)

if __name__ == '__main__':
    bulk_create_songs()
