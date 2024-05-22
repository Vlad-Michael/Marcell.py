import speech_recognition as sr
import pyttsx3
import os
import pyjokes
import schedule
import time
import threading
import pywhatkit
import random
import pygame
import subprocess
import ctypes
from time import sleep
from datetime import datetime, timedelta

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Initialize pygame mixer for sound playback
pygame.mixer.init()

# Define global variables for music playback
current_genre = None
current_playlist = []
current_song_index = 0

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and return the text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

# Function to handle alarms and reminders
def set_alarm(hours=0, minutes=0):
    alarm_time = datetime.now() + timedelta(hours=hours, minutes=minutes)
    time_str = alarm_time.strftime('%H:%M')
    schedule.every().day.at(time_str).do(
        lambda: speak(f"Reminder: Your alarm set for {hours} hours and {minutes} minutes from now."))
    speak(f"Alarm set for {time_str}")

def run_scheduled_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the thread to run scheduled tasks
threading.Thread(target=run_scheduled_tasks, daemon=True).start()

# Function to open applications
def open_app(app_name):
    if app_name.lower() == "browser":
        os.system("start chrome")
    elif app_name.lower() == "word":
        os.system("start winword")
    elif app_name.lower() == "powerpoint":
        os.system("start powerpnt")
    elif app_name.lower() == "girls protection":
        print("Girl Alert!")
        speak("Girl Alert!")
        print("Initializing girls repellent")
        speak("Initializing girls repellent")
        subprocess.Popen("D:\\GAMES\\Riot Games\\Riot Client\\RiotClientServices.exe --launch-product=league_of_legends --launch-patchline=live")
        print("Opening League of Legends")
        speak("Opening League of Legends")
    elif app_name.lower() == "league of legends":
        print("Initializing girls repellent")
        speak("Initializing girls repellent")
        subprocess.Popen("D:\\GAMES\\Riot Games\\RiotClientServices.exe --launch-product=league_of_legends --launch-patchline=live")
    elif app_name.lower() == "notepad":
        os.system("notepad")
    elif app_name.lower() == "excel":
        os.system("start excel")
    elif app_name.lower() == "outlook":
        os.system("start outlook")
    elif app_name.lower() == "discord":
        subprocess.Popen("C:\\Users\\Vlad-Michael\\AppData\\Local\\Discord\\app-1.0.9147\\Discord.exe")
    else:
        speak("Sorry, I don't know how to open that application.")

# Function to tell a joke
def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

# Function to restart or shut down the device
def manage_device(action):
    if action.lower() == "restart":
        speak("Restarting the device")
        os.system("shutdown /r /t 1")
    elif action.lower() == "shut down":
        speak("Shutting down the device")
        os.system("shutdown /s /t 1")
    else:
        speak("Sorry, I don't understand that command.")

# Function to play the spooky sound and show the error message
def play_spooky_sound():
    pygame.mixer.music.load(
        "C:/Users/Vlad-Michael/PycharmProjects/creating virtual assistant/Russian Roulette/Freddy's Music Box - Sound Effect.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    # Display the error message after the sound finishes
    ctypes.windll.user32.MessageBoxW(0, "Important files missing", "C:\\Windows\\System32", 0x10 | 0x0)

# Function to start the game
def start_game():
    print("Let's play a game!")
    speak("Let's play a game!")
    print("The rules are as follow:")
    speak("The rules are as follow:")
    print("You have to pick three numbers between 1 and 7.")
    speak("You have to pick three numbers between 1 and 7.")
    print("5 out of the 7 numbers are lucky numbers")
    speak("5 out of the 7 numbers are lucky numbers")
    print("2 out of the 7 numbers are cursed")
    speak("2 out of the 7 numbers are cursed")
    print("In order to win, you have to guess 3 lucky numbers")
    speak("In order to win, you have to guess 3 lucky numbers")

    # Choose 2 cursed numbers randomly
    cursed_numbers = random.sample(range(1, 8), 2)
    print(f"Cursed numbers: {cursed_numbers}")  # Debugging, remove this line in production

    guesses = 3
    while guesses > 0:
        command = input("Type your guess (number between 1 and 7): ")
        try:
            chosen_number = int(command)
            if chosen_number in range(1, 8):
                if chosen_number in cursed_numbers:
                    print("Roses are red.")
                    speak("Roses are red.")
                    print("Violets are blue.")
                    speak("Violets are blue.")
                    print("I am now deleting System 32.")
                    speak("I am now deleting System 32.")

                    play_spooky_sound()
                    sleep(5)
                    os.system("shutdown /s /t 1")
                    return
                else:
                    guesses -= 1
                    if guesses > 0:
                        speak(f"{chosen_number} is a lucky number. {guesses} more to go.")
                    else:
                        speak("Congratulations! You have won the game! You might as well play the lottery today.")
            else:
                speak("Please pick a number between 1 and 7.")
        except ValueError:
            speak("Please type a valid number.")

# Function to open the presentation
def open_presentation():
    file_path = "C:/Users/Vlad-Michael/PycharmProjects/creating virtual assistant/Presentation/Marcell.pptx"
    if os.path.exists(file_path):
        os.startfile(file_path)
        speak("Opening the presentation.")
    else:
        speak("Sorry, I couldn't find the presentation file.")

# Function to handle commands
def handle_command(command):
    if 'hello' in command.lower():
        speak("Hello! How can I assist you today?")
    elif 'hi' in command.lower():
        speak("Hi! Nice to hear you!")
    elif 'hello there' in command.lower():
        speak("Good day General Kenobi!")
    elif 'what is your name' in command.lower() or 'who are you' in command.lower():
        speak("My name is Marcell and I am your virtual assistant")
    elif 'how are you' in command.lower():
        speak("I am fine, thank you! How can I help you?")
    elif 'do a back flip' in command.lower():
        speak("No, you do one!")
    elif 'I will give you back to the indian guy' in command.lower():
        speak("Fine, I will do the flip")
        sleep(1)
        speak("Done")
    elif 'You did not do anything' in command.lower():
        speak("Yes I did! You just blinked and missed it")
    elif 'Do it again' in command.lower():
        speak("Fine! I'll do it again")
        sleep(1)
        speak("Done! If you didn't see it, it means that you blinked again and I am not doing another flip.")
    elif 'how is the weather' in command.lower() or 'what is the weather like' in command.lower() or 'what is the weather like today' in command.lower():
        speak("In the bottom right corner of your screen you have the weather, "
              "telling you how many degrees are outside and what the conditions are like"
              "If you click on it you will also be able to see the news and traffic conditions")

    elif 'exit' in command.lower():
        speak("Goodbye! See you soon!")
        return False

    elif 'set alarm' in command.lower():
        try:
            if 'hours and' in command.lower():
                parts = command.lower().split('hours and')
                hours = int(parts[0].split()[-1])
                minutes = int(parts[1].split()[0])
                set_alarm(hours, minutes)
            elif 'hours' in command.lower():
                hours = int(command.lower().split('hours')[0].split()[-1])
                set_alarm(hours)
            elif 'minutes' in command.lower():
                minutes = int(command.lower().split('minutes')[0].split()[-1])
                set_alarm(minutes=minutes)
        except Exception as e:
            speak("Sorry, I couldn't set the alarm. Please try again.")
            print(e)
    elif 'open' in command.lower():
        if 'presentation' in command.lower():
            open_presentation()
        else:
            app_name = command.lower().replace('open', '').strip()
            open_app(app_name)
    elif 'tell me a joke' in command.lower() or 'tell me another joke' in command.lower():
        tell_joke()
    elif 'restart' in command.lower() or 'shut down' in command.lower():
        manage_device(command.lower())
    elif 'i want to play a game' in command.lower():
        start_game()
    elif 'play some music' in command.lower() or 'play a song' in command.lower():
        speak("What genre shall it be? Rock, Rap, Pop or Alternative Rock?")
        genre_command = listen()
        play_music_by_genre(genre_command.lower())
    elif 'play' in command.lower() and 'song' in command.lower():
        if 'rock' in command.lower():
            play_music_by_genre('rock')
        elif 'rap' in command.lower():
            play_music_by_genre('rap')
        elif 'pop' in command.lower():
            play_music_by_genre('pop')
        elif 'alternative rock' in command.lower():
            play_music_by_genre('alternative rock')
    elif 'skip' in command.lower() or 'next song' in command.lower():
        play_next_song()
    elif 'stop the music' in command.lower() or 'stop playing' in command.lower() or 'stop' in command.lower():
        stop_music()
    else:
        speak("I did not understand that. Can you please repeat?")
    return True

# Function to load and play a random song from the specified genre folder
def play_music_by_genre(genre):
    global current_genre, current_playlist, current_song_index
    music_folder = "C:/Users/Vlad-Michael/PycharmProjects/creating virtual assistant/Music"

    if genre == "rock":
        genre_folder = "Rock"
    elif genre == "rap":
        genre_folder = "Rap"
    elif genre == "pop":
        genre_folder = "Pop"
    elif genre == "alternative rock":
        genre_folder = "Alternative Rock"
    else:
        speak("I don't know that genre. Please choose from Rock, Rap, Pop, or Alternative Rock.")
        return

    current_genre = genre
    current_playlist = [os.path.join(music_folder, genre_folder, song) for song in
                        os.listdir(os.path.join(music_folder, genre_folder))]
    current_song_index = 0

    if current_playlist:
        play_current_song()
    else:
        speak(f"No songs found in {genre_folder} folder.")

# Function to play the current song
def play_current_song():
    global current_song_index, current_playlist
    if current_playlist:
        song = current_playlist[current_song_index]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        song_name = os.path.basename(song)
        print(f"Playing {song_name}")

# Function to play the next song in the playlist
def play_next_song():
    global current_song_index, current_playlist
    if current_playlist:
        current_song_index = (current_song_index + 1) % len(current_playlist)
        play_current_song()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    speak("Music stopped.")

# Main function
def main():
    speak("Initializing the virtual assistant.")
    running = True
    while running:
        command = listen()
        if command:
            running = handle_command(command)

if __name__ == "__main__":
    main()
