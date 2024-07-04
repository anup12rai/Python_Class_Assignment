from playsound import playsound
import random

user_input = int(input("Enter the number of songs you want to play: "))

# Corrected dictionary with keys and values
song_dict = {
    "song1": r"C:\Users\ACER\Documents\Desktop\assigment\E4L39FT-cat-meow.mp3",
    "song2": r"C:\Users\ACER\Documents\Desktop\assigment\Z5QVAKY-dog.mp3"
}

def random_song():
    song = random.choice(list(song_dict.keys())) 
    return song_dict[song] 
for i in range(user_input):
    playsound(random_song())
