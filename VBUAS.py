import sys
import os
import pyaudio
import wave
import time
import test_speaker
import subprocess
import random
import pickle as cPicle
# import _pickle as cPickle
from sys import byteorder
from array import array
from subprocess import call
from struct import pack
from tkinter.filedialog import askdirectory

import tkinter as tk
from tkinter import *
from tkinter import PhotoImage

DEFAULT_DIR = "E:\VBUAS For Final\TRY"


def AboutUs():
    global image
    global about_screen
    about_screen = Toplevel(root)
    about_screen.title("ABOUT")
    width, height = about_screen.winfo_screenwidth(), about_screen.winfo_screenheight()
    about_screen.geometry('%dx%d+0+0' % (width, height))

    label = Label(about_screen, text="VBUAS 1.0", font="Times 50 bold")
    label.pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    label = Label(
        about_screen, text="Developed By: The Diamond Dox", font="Times 30")
    label.pack()
    label = Label(about_screen, text=" Anmol Thapa Magar ",
                  font="Times 20 italic")
    label.pack()
    label = Label(about_screen, text=" Barun Ojha ", font="Times 20 italic")
    label.pack()
    label = Label(about_screen, text=" Poojan Pradhan ",
                  font="Times 20 italic")
    label.pack()
    label = Label(about_screen, text=" Prashanna Subedi ",
                  font="Times 20 italic")
    label.pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()

    image = PhotoImage(file="VG.png")
    Label(about_screen, image=image).pack()
    Label(root, text="").pack()
    label = Label(about_screen, text=" © All Rights Reserved ")
    label.pack()
    about_screen.iconbitmap('vbuas.ico')
    about_screen.state('zoomed')


def VBUASclass():
    global root
    root = tk.Tk()
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry('%dx%d+0+0' % (width, height))
    root.title("VBUAS")
    label = Label(root, text="Voice Based User Authentication System",
                  fg="black", font="Calibri 30 bold")
    label.pack(padx=5, pady=10, side=tk.LEFT, expand=1)
    Label(root, text="").pack()
    label = Button(root, text="About", command=AboutUs)
    label.pack(padx=5, pady=10, side=tk.RIGHT, expand=1)
    image = PhotoImage(file="go.png")

    button_qwer = Button(root, image=image, height=500,
                         width=500, command=AudioLogin)
    button_qwer.pack(padx=5, pady=20, expand=1)

    label = Label(root, text="Click above mic to Login !",
                  fg="black", font="Times 15 italic")
    label.pack(padx=5, pady=20, expand=1)

    register = Button(root, text="REGISTER",
                      font="Calibri 40 bold", bg="white", command=AudioRegister)
    register.pack(padx=5, pady=30, side=tk.LEFT, expand=1)

    # root.configure(background='orange')
    root.state('zoomed')
    root.iconbitmap('vbuas.ico')
    root.mainloop()


def Voice_register():
    global voice_register
    voice_register = Toplevel(root)
    voice_register.title("Voice Register")
    width, height = voice_register.winfo_screenwidth(
    ), voice_register.winfo_screenheight()
    voice_register.geometry('%dx%d+0+0' % (width, height))
    Button(voice_register, text="SPEAK",
           command=Voice_Input_For_Registration).pack()
    label = Label(
        voice_register, text="Please Click on SPEAK button and speak the upcoming 10 phrases...")
    Label(voice_register,
          text="NOTE: Please, Speak closer to the microphone!", fg="red").pack()
    label.pack()
    voice_register.state('zoomed')
    voice_register.iconbitmap('vbuas.ico')


def AudioRegister():
    global register_screen
    register_screen = Toplevel(root)
    register_screen.title("Register")
    width, height = register_screen.winfo_screenwidth(
    ), register_screen.winfo_screenheight()
    register_screen.geometry('%dx%d+0+0' % (width, height))

    global username
    global password
    global username_entry
    global password_entry
    global name
    global name_entry
    global age
    global age_entry
    global voice
    global voice_entry
    global image
    global var
    global word
    name = StringVar()
    age = IntVar()
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    name_lable = Label(register_screen, text="Name * ")
    name_lable.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()
    age_lable = Label(register_screen, text="Age * ")
    age_lable.pack()
    # age_entry = Entry(register_screen, textvariable=age)
    age_entry = OptionMenu(register_screen, age, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
                           64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                           78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
                           101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                           111, 112, 113, 114, 115, 116, 117, 118, 119, 120)
    age_entry.pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    voice_label = Label(register_screen, text="Enter Voice Here: *")
    voice_label.pack()
    image = PhotoImage(file="images.png")
    Button(register_screen, image=image, command=Voice_register).pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10,
           height=1, command=register_user).pack()

    register_screen.state('zoomed')
    register_screen.iconbitmap('vbuas.ico')


def register_user():
    username_info = username.get()
    password_info = password.get()
    name_info = name.get()
    age_info = age.get()

    list_of_files = os.listdir()
    if username_info in list_of_files:
        user_already_in_database()
        return None
    elif username_info == "" or password_info == "" or name_info == "" or age_info == "":
        register_fail()
        return None
    else:
        filepath = os.path.join(
            DEFAULT_DIR, username_info)
        file = open(filepath, "w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write(name_info)
        file.close()
    call(["python", "train_models.py"])

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success",
          fg="green", font=("calibri", 11)).pack()


def AudioLogin():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    # login_screen.geometry("400x400")
    width, height = login_screen.winfo_screenwidth(), login_screen.winfo_screenheight()
    login_screen.geometry('%dx%d+0+0' % (width, height))
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify
    global voice
    global voice_entry
    global image

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry
    global voice_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text=" Direct Login : ").pack()
    Button(login_screen, text="Login", width=10,
           height=1, command=login_verify).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text=" Direct Voice Login : ").pack()
    Label(login_screen, text=" Please Say, 'Dox, Who am I?' ").pack()
    image = PhotoImage(file="images.png")
    Button(login_screen, image=image, command=Voice_Input_For_Login).pack()
    Label(login_screen, text="").pack()
    Label(login_screen,
          text="NOTE: Please, Speak closer to the microphone!", fg="red").pack()
    login_screen.state('zoomed')
    login_screen.iconbitmap('vbuas.ico')


def login_fail():
    global login_fail_screen
    login_fail_screen = Toplevel(login_screen)
    login_fail_screen.title("Failed!")
    login_fail_screen.geometry("360x240")
    Label(login_fail_screen, text="Please, Provide the valid information").pack()
    Button(login_fail_screen, text="OK", command=delete_register_fail).pack()
    login_fail_screen.iconbitmap('vbuas.ico')


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    speaker1 = os.path.join(username1 + "'s Vault")

    list_of_files = os.listdir()
    if username1 in list_of_files:
        # call(["python", "test_speaker.py"])
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            if speaker1 in list_of_files:
                subprocess.check_call(["attrib", "+H", speaker1])
                file1 = os.path.join(
                    DEFAULT_DIR, speaker1)
                os.startfile(file1)
            elif username1 == "unknown":
                user_not_found()
            else:
                os.mkdir(speaker1)
                subprocess.check_call(["attrib", "+H", speaker1])
                file2 = os.path.join(
                    DEFAULT_DIR, speaker1)
                os.startfile(file2)
            delete_login_screen()
        else:
            password_not_recognised()
    elif username1 == "" or password1 == "":
        login_fail()
        delete_login_screen()
    else:
        user_not_found()
        delete_login_screen()

    call(["python", "test_speaker.py"])


def delete_register_fail():
    register_fail_screen.destroy()


def register_fail():
    global register_fail_screen
    register_fail_screen = Toplevel(register_screen)
    register_fail_screen.title("Failed!")
    register_fail_screen.geometry("360x240")
    Label(register_fail_screen, text="Please, Provide the valid information").pack()
    Button(register_fail_screen, text="OK",
           command=delete_register_fail).pack()
    register_fail_screen.iconbitmap('vbuas.ico')


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success!")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",
           command=delete_login_success).pack()
    login_success_screen.iconbitmap('vbuas.ico')


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Not Recognized!")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()
    password_not_recog_screen.iconbitmap('vbuas.ico')


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("User Unavailable!")
    user_not_found_screen.geometry("300x300")
    Label(user_not_found_screen, text="User Not Found. Please, Try again").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()
    user_not_found_screen.iconbitmap('vbuas.ico')


# Deleting popups

def user_already_in_database():
    global user_found_screen
    user_found_screen = Toplevel(register_screen)
    user_found_screen.title("User Already Present!")
    user_found_screen.geometry("150x100")
    Label(user_found_screen, text="Username already exists").pack()
    Button(user_found_screen, text="OK",
           command=delete_user_found_screen).pack()
    user_found_screen.iconbitmap('vbuas.ico')


def delete_login_success():
    login_success_screen.destroy()


def delete_login_screen():
    login_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    delete_login_screen()


def delete_user_found_screen():
    user_found_screen.destroy()


def delete_voice_register():
    voice_register.destroy()


def delete_voice_login():
    login_screen.destroy()


def Voice_Input_For_Registration():
    print("Recording SESSION started!!")
    # while counter < 5:
    username_info = username.get()
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 4
    word = do()
    p = pyaudio.PyAudio()

    print("Started Recording!")

    for i in range(11):
        p = pyaudio.PyAudio()

        if i == 0:
            print("First Text Record")
            time.sleep(1.0)
            os.system('cls' if os.name == 'nt' else 'clear')
            # print1(word)
            Label(voice_register, text="1. Dox, Where are you?", fg="blue").pack()
            voice_register.update()
            # print("Speak your name in {} seconds".format(j))
            i += 1

        elif i == 1:
            print("Second Text Record")

            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            # print1(word)
            Label(voice_register, text="2. Dox, How are you?", fg="blue").pack()
            voice_register.update()
            # print("Speak your name in {} seconds".format(j))
            i += 1

        elif i == 2:
            print("Third Text Record")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            # print1(word)
            Label(voice_register, text="3. Dox, I don't understand.",
                  fg="blue").pack()
            voice_register.update()
            # print("Speak your name in {} seconds".format(j))
            i += 1

        elif i == 3:
            print("Fourth Text Record")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            # print1(word)
            Label(voice_register, text="4. Dox, I am learning English",
                  fg="blue").pack()
            voice_register.update()
            # print("Speak your name in {} seconds".format(j))
            i += 1

        elif i == 4:
            print("Fifth Text Record")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            # print1(word)
            Label(voice_register, text="5. Dox, What do you mean?", fg="blue").pack()
            voice_register.update()
            # print("Speak your name in {} seconds".format(j))
            i += 1

        elif i == 5:
            print("Sixth Text Record")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            # print1(word)
            Label(voice_register, text="6. Dox, How do you spell that?",
                  fg="blue").pack()
            voice_register.update()
            # print("Speak your name in {} seconds".format(j))
            i += 1

        elif i == 6:
            print("Seventh Text Record")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            # print1(word)
            Label(voice_register,
                  text="7. Dox, Make sure you understand this.", fg="blue").pack()
            voice_register.update()
            # print("Speak your name in {} seconds".format(j))
            i += 1

        elif i == 7:
            print("Eight Text Record")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            # print1(word)
            Label(voice_register, text="8. Dox, Where are you?", fg="blue").pack()
            voice_register.update()
            # print("Speak your name in {} seconds".format(j))
            i += 1

        elif i == 8:
            print("Ninth Text Record")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            # print1(word)
            Label(voice_register, text="9. Dox, Make a call for me", fg="blue").pack()
            voice_register.update()
            # print("Speak your name in {} seconds".format(j))
            i += 1

        elif i == 9:
            print("Final Text Record")
            time.sleep(2.0)
            # print3(word)
            Label(voice_register, text="10. Dox, Thank you", fg="blue").pack()
            voice_register.update()
            # print("Speak your name one last time")
            time.sleep(0.8)
            i += 1

        else:
            print("Recording Cancelled!")
            # Button(voice_register, text="OK", command=delete_voice_register).pack()
            voice_register.destroy()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("Recording Ongoing!")
        Label(voice_register, text="* Recording").pack()
        voice_register.update()

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            data_chunk = array('h', data)
            vol = max(data_chunk)
            if vol >= 1000:
                print("something said")
                frames.append(data)
            else:
                print("nothing")
            print("\n")

        Label(voice_register, text="Done Recording!").pack()
        voice_register.update()

        stream.stop_stream()
        stream.close()
        p.terminate()

        counter = 0
        if username_info == "":
            Label(voice_register,
                  text="Please! Give your detailed information first").pack()
            Button(voice_register, text="OK",
                   command=delete_voice_register).pack()
            voice_register.update()
            break
        else:
            filename = username_info + "-" + "{}.wav"
            while os.path.isfile(filename.format(counter)):
                counter += 1
            filename = filename.format(counter)

            filepath = DEFAULT_DIR + filename
            wf = wave.open(filepath, "wb")
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            os.chdir(DEFAULT_DIR)
            filepath = DEFAULT_DIR + 'development_set_enroll.txt'
            file = open(filepath, "a")
            file.write(filename + "\n")
            file.close()


def Voice_Input_For_Login():
    global label
    username_info = username_verify.get()
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 2

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    Label(login_screen, text="Please speak your designated word").pack()
    login_screen.update()
    Label(login_screen, text="* Recording").pack()
    login_screen.update()

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        data_chunk = array('h', data)
        vol = max(data_chunk)
        if vol >= 1000:
            print("something said")
            frames.append(data)
        else:
            print("nothing")
        print("\n")

    Label(login_screen, text="Done Recording!").pack()
    login_screen.update()

    stream.stop_stream()
    stream.close()
    p.terminate()

    counter = 0
    filename = username_info + "-" + "{}.wav"
    while os.path.isfile(filename.format(counter)):
        counter += 1
    filename = filename.format(counter)

    filepath = DEFAULT_DIR + filename
    wf = wave.open(filepath, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    """
    os.chdir(DEFAULT_DIR)
    filepath = DEFAULT_DIR + 'development_set_enroll.txt'
    file = open(filepath, "a+")
    file.write(filename + "\n")
    file.close()
    """
    os.chdir(DEFAULT_DIR)
    filepath1 = DEFAULT_DIR + 'development_set_test.txt'
    file = open(filepath1, "w+")
    file.write(filename + "\n")
    file.close()

    call(["python", "test_speaker.py"])

    speaker = test_speaker.VbuasLogin()
    if speaker:
        # label = Label(login_screen, text="Welcome " + " " + speaker)
        # label.pack()
        speaker1 = os.path.join(speaker + "'s Vault")
        list_of_files = os.listdir()
        if speaker1 in list_of_files:
            subprocess.check_call(["attrib", "+H", speaker1])
            file1 = os.path.join(DEFAULT_DIR, speaker1)
            os.startfile(file1)
            os.remove(filepath)
            root.destroy()
        elif speaker == "unknown":
            os.remove(filepath)
            user_not_found()
        else:
            os.mkdir(speaker1)
            subprocess.check_call(["attrib", "+H", speaker1])
            file2 = os.path.join(DEFAULT_DIR, speaker1)
            os.startfile(file2)
            os.remove(filepath)
        # delete_voice_login()
        # Button(login_screen, text="OK", command=delete_voice_login).pack()
        delete_login_screen()
    else:
        user_not_found()


""" 
def print1(text):
    Label(voice_register, text="Please, Say " + text).pack(fg="blue")
    voice_register.update()


def print2(text):
    Label(voice_register, text="Please, Say" + text + "once again").pack(fg="blue")
    voice_register.update()


def print3(text):
    Label(voice_register, text="Please, Say " + text + "one last time").pack(fg="blue")
    voice_register.update()


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
"""


def do():
    noun = [
        'people',
        'history',
        'way',
        'art',
        'world',
        'information',
        'map',
        'two',
        'family',
        'government',
        'health',
        'system',
        'computer',
        'meat',
        'year',
        'thanks',
        'music',
        'person',
        'reading',
        'method',
        'data',
        'food',
        'understanding',
        'theory',
        'law',
        'bird',
        'literature',
        'problem',
        'software',
        'control',
        'knowledge',
        'power',
        'ability',
        'economics',
        'love',
        'internet',
        'television',
        'science',
        'library',
        'nature',
        'fact',
        'product',
        'idea',
        'temperature',
        'investment',
        'area',
        'society',
        'activity',
        'story',
        'industry',
        'media',
        'thing',
        'oven',
        'community',
        'definition',
        'safety',
        'quality',
        'development',
        'language',
        'management',
        'player',
        'variety',
        'video',
        'week',
        'security',
        'country',
        'exam',
        'movie',
        'organization',
        'equipment',
        'physics',
        'analysis',
        'policy',
        'series',
        'thought',
        'basis',
        'boyfriend',
        'direction',
        'strategy',
        'technology',
        'army',
        'camera',
        'freedom',
        'paper',
        'environment',
        'child',
        'instance',
        'month',
        'truth',
        'marketing',
        'university',
        'writing',
        'article',
        'department',
        'difference',
        'goal',
        'news',
        'audience',
        'fishing',
        'growth',
        'income',
        'marriage',
        'user',
        'combination',
        'failure',
        'meaning',
        'medicine',
        'philosophy',
        'teacher',
        'communication',
        'night',
        'chemistry',
        'disease',
        'disk',
        'energy',
        'nation',
        'road',
        'role',
        'soup',
        'advertising',
        'location',
        'success',
        'addition',
        'apartment',
        'education',
        'math',
        'moment',
        'painting',
        'politics',
        'attention',
        'decision',
        'event',
        'property',
        'shopping',
        'student',
        'wood',
        'competition',
        'distribution',
        'entertainment',
        'office',
        'population',
        'president',
        'unit',
        'category',
        'cigarette',
        'context',
        'introduction',
        'opportunity',
        'performance',
        'driver',
        'flight',
        'length',
        'magazine',
        'newspaper',
        'relationship',
        'teaching',
        'cell',
        'dealer',
        'debate',
        'finding',
        'lake',
        'member',
        'message',
        'phone',
        'scene',
        'appearance',
        'association',
        'concept',
        'customer',
        'death',
        'discussion',
        'housing',
        'inflation',
        'insurance',
        'mood',
        'woman',
        'advice',
        'blood',
        'effort',
        'expression',
        'importance',
        'opinion',
        'payment',
        'reality',
        'responsibility',
        'situation',
        'skill',
        'statement',
        'wealth',
        'application',
        'city',
        'county',
        'depth',
        'estate',
        'foundation',
        'grandmother',
        'heart',
        'perspective',
        'photo',
        'recipe',
        'studio',
        'topic',
        'collection',
        'depression',
        'imagination',
        'passion',
        'percentage',
        'resource',
        'setting',
        'ad',
        'agency',
        'college',
        'connection',
        'criticism',
        'debt',
        'description',
        'memory',
        'patience',
        'secretary',
        'solution',
        'administration',
        'aspect',
        'attitude',
        'director',
        'personality',
        'psychology',
        'recommendation',
        'response',
        'selection',
        'storage',
        'version',
        'alcohol',
        'argument',
        'complaint',
        'contract',
        'emphasis',
        'highway',
        'loss',
        'membership',
        'possession',
        'preparation',
        'steak',
        'union',
        'agreement',
        'cancer',
        'currency',
        'employment',
        'engineering',
        'entry',
        'interaction',
        'limit',
        'mixture',
        'preference',
        'region',
        'republic',
        'seat',
        'tradition',
        'virus',
        'actor',
        'classroom',
        'delivery',
        'device',
        'difficulty',
        'drama',
        'election',
        'engine',
        'football',
        'guidance',
        'hotel',
        'match',
        'owner',
        'priority',
        'protection',
        'suggestion',
        'tension',
        'variation',
        'anxiety',
        'atmosphere',
        'awareness',
        'bread',
        'climate',
        'comparison',
        'confusion',
        'construction',
        'elevator',
        'emotion',
        'employee',
        'employer',
        'guest',
        'height',
        'leadership',
        'mall',
        'manager',
        'operation',
        'recording',
        'respect',
        'sample',
        'transportation',
        'boring',
        'charity',
        'cousin',
        'disaster',
        'editor',
        'efficiency',
        'excitement',
        'extent',
        'feedback',
        'guitar',
        'homework',
        'leader',
        'mom',
        'outcome',
        'permission',
        'presentation',
        'promotion',
        'reflection',
        'refrigerator',
        'resolution',
        'revenue',
        'session',
        'singer',
        'tennis',
        'basket',
        'bonus',
        'cabinet',
        'childhood',
        'church',
        'clothes',
        'coffee',
        'dinner',
        'drawing',
        'hair',
        'hearing',
        'initiative',
        'judgment',
        'lab',
        'measurement',
        'mode',
        'mud',
        'orange',
        'poetry',
        'police',
        'possibility',
        'procedure',
        'queen',
        'ratio',
        'relation',
        'restaurant',
        'satisfaction',
        'sector',
        'signature',
        'significance',
        'song',
        'tooth',
        'town',
        'vehicle',
        'volume',
        'wife',
        'accident',
        'airport',
        'appointment',
        'arrival',
        'assumption',
        'baseball',
        'chapter',
        'committee',
        'conversation',
        'database',
        'enthusiasm',
        'error',
        'explanation',
        'farmer',
        'gate',
        'girl',
        'hall',
        'historian',
        'hospital',
        'injury',
        'instruction',
        'maintenance',
        'manufacturer',
        'meal',
        'perception',
        'pie',
        'poem',
        'presence',
        'proposal',
        'reception',
        'replacement',
        'revolution',
        'river',
        'son',
        'speech',
        'tea',
        'village',
        'warning',
        'winner',
        'worker',
        'writer',
        'assistance',
        'breath',
        'buyer',
        'chest',
        'chocolate',
        'conclusion',
        'contribution',
        'cookie',
        'courage',
        'dad',
        'desk',
        'drawer',
        'establishment',
        'examination',
        'garbage',
        'grocery',
        'honey',
        'impression',
        'improvement',
        'independence',
        'insect',
        'inspection',
        'inspector',
        'king',
        'ladder',
        'menu',
        'penalty',
        'piano',
        'potato',
        'profession',
        'professor',
        'quantity',
        'reaction',
        'requirement',
        'salad',
        'sister',
        'supermarket',
        'tongue',
        'weakness',
        'wedding',
        'affair',
        'ambition',
        'analyst',
        'apple',
        'assignment',
        'assistant',
        'bathroom',
        'bedroom',
        'beer',
        'birthday',
        'celebration',
        'championship',
        'cheek',
        'client',
        'consequence',
        'departure',
        'diamond',
        'dirt',
        'ear',
        'fortune',
        'friendship',
        'funeral',
        'gene',
        'girlfriend',
        'hat',
        'indication',
        'intention',
        'lady',
        'midnight',
        'negotiation',
        'obligation',
        'passenger',
        'pizza',
        'platform',
        'poet',
        'pollution',
        'recognition',
        'reputation',
        'shirt',
        'sir',
        'speaker',
        'stranger',
        'surgery',
        'sympathy',
        'tale',
        'throat',
        'trainer',
        'uncle',
        'youth',
        'time',
        'work',
        'film',
        'water',
        'money',
        'example',
        'while',
        'business',
        'study',
        'game',
        'life',
        'form',
        'air',
        'day',
        'place',
        'number',
        'part',
        'field',
        'fish',
        'back',
        'process',
        'heat',
        'hand',
        'experience',
        'job',
        'book',
        'end',
        'point',
        'type',
        'home',
        'economy',
        'value',
        'body',
        'market',
        'guide',
        'interest',
        'state',
        'radio',
        'course',
        'company',
        'price',
        'size',
        'card',
        'list',
        'mind',
        'trade',
        'line',
        'care',
        'group',
        'risk',
        'word',
        'fat',
        'force',
        'key',
        'light',
        'training',
        'name',
        'school',
        'top',
        'amount',
        'level',
        'order',
        'practice',
        'research',
        'sense',
        'service',
        'piece',
        'web',
        'boss',
        'sport',
        'fun',
        'house',
        'page',
        'term',
        'test',
        'answer',
        'sound',
        'focus',
        'matter',
        'kind',
        'soil',
        'board',
        'oil',
        'picture',
        'access',
        'garden',
        'range',
        'rate',
        'reason',
        'future',
        'site',
        'demand',
        'exercise',
        'image',
        'case',
        'cause',
        'coast',
        'action',
        'age',
        'bad',
        'boat',
        'record',
        'result',
        'section',
        'building',
        'mouse',
        'cash',
        'class',
        'nothing',
        'period',
        'plan',
        'store',
        'tax',
        'side',
        'subject',
        'space',
        'rule',
        'stock',
        'weather',
        'chance',
        'figure',
        'man',
        'model',
        'source',
        'beginning',
        'earth',
        'program',
        'chicken',
        'design',
        'feature',
        'head',
        'material',
        'purpose',
        'question',
        'rock',
        'salt',
        'act',
        'birth',
        'car',
        'dog',
        'object',
        'scale',
        'sun',
        'note',
        'profit',
        'rent',
        'speed',
        'style',
        'war',
        'bank',
        'craft',
        'half',
        'inside',
        'outside',
        'standard',
        'bus',
        'exchange',
        'eye',
        'fire',
        'position',
        'pressure',
        'stress',
        'advantage',
        'benefit',
        'box',
        'frame',
        'issue',
        'step',
        'cycle',
        'face',
        'item',
        'metal',
        'paint',
        'review',
        'room',
        'screen',
        'structure',
        'view',
        'account',
        'ball',
        'discipline',
        'medium',
        'share',
        'balance',
        'bit',
        'black',
        'bottom',
        'choice',
        'gift',
        'impact',
        'machine',
        'shape',
        'tool',
        'wind',
        'address',
        'average',
        'career',
        'culture',
        'morning',
        'pot',
        'sign',
        'table',
        'task',
        'condition',
        'contact',
        'credit',
        'egg',
        'hope',
        'ice',
        'network',
        'north',
        'square',
        'attempt',
        'date',
        'effect',
        'link',
        'post',
        'star',
        'voice',
        'capital',
        'challenge',
        'friend',
        'self',
        'shot',
        'brush',
        'couple',
        'exit',
        'front',
        'function',
        'lack',
        'living',
        'plant',
        'plastic',
        'spot',
        'summer',
        'taste',
        'theme',
        'track',
        'wing',
        'brain',
        'button',
        'click',
        'desire',
        'foot',
        'gas',
        'influence',
        'notice',
        'rain',
        'wall',
        'base',
        'damage',
        'distance',
        'feeling',
        'pair',
        'savings',
        'staff',
        'sugar',
        'target',
        'text',
        'animal',
        'author',
        'budget',
        'discount',
        'file',
        'ground',
        'lesson',
        'minute',
        'officer',
        'phase',
        'reference',
        'register',
        'sky',
        'stage',
        'stick',
        'title',
        'trouble',
        'bowl',
        'bridge',
        'campaign',
        'character',
        'club',
        'edge',
        'evidence',
        'fan',
        'letter',
        'lock',
        'maximum',
        'novel',
        'option',
        'pack',
        'park',
        'plenty',
        'quarter',
        'skin',
        'sort',
        'weight',
        'baby',
        'background',
        'carry',
        'dish',
        'factor',
        'fruit',
        'glass',
        'joint',
        'master',
        'muscle',
        'red',
        'strength',
        'traffic',
        'trip',
        'vegetable',
        'appeal',
        'chart',
        'gear',
        'ideal',
        'kitchen',
        'land',
        'log',
        'mother',
        'net',
        'party',
        'principle',
        'relative',
        'sale',
        'season',
        'signal',
        'spirit',
        'street',
        'tree',
        'wave',
        'belt',
        'bench',
        'commission',
        'copy',
        'drop',
        'minimum',
        'path',
        'progress',
        'project',
        'sea',
        'south',
        'status',
        'stuff',
        'ticket',
        'tour',
        'angle',
        'blue',
        'breakfast',
        'confidence',
        'daughter',
        'degree',
        'doctor',
        'dot',
        'dream',
        'duty',
        'essay',
        'father',
        'fee',
        'finance',
        'hour',
        'juice',
        'luck',
        'milk',
        'mouth',
        'peace',
        'pipe',
        'stable',
        'storm',
        'substance',
        'team',
        'trick',
        'afternoon',
        'bat',
        'beach',
        'blank',
        'catch',
        'chain',
        'consideration',
        'cream',
        'crew',
        'detail',
        'gold',
        'interview',
        'kid',
        'mark',
        'mission',
        'pain',
        'pleasure',
        'score',
        'screw',
        'sex',
        'shop',
        'shower',
        'suit',
        'tone',
        'window',
        'agent',
        'band',
        'bath',
        'block',
        'bone',
        'calendar',
        'candidate',
        'cap',
        'coat',
        'contest',
        'corner',
        'court',
        'cup',
        'district',
        'door',
        'east',
        'finger',
        'garage',
        'guarantee',
        'hole',
        'hook',
        'implement',
        'layer',
        'lecture',
        'lie',
        'manner',
        'meeting',
        'nose',
        'parking',
        'partner',
        'profile',
        'rice',
        'routine',
        'schedule',
        'swimming',
        'telephone',
        'tip',
        'winter',
        'airline',
        'bag',
        'battle',
        'bed',
        'bill',
        'bother',
        'cake',
        'code',
        'curve',
        'designer',
        'dimension',
        'dress',
        'ease',
        'emergency',
        'evening',
        'extension',
        'farm',
        'fight',
        'gap',
        'grade',
        'holiday',
        'horror',
        'horse',
        'host',
        'husband',
        'loan',
        'mistake',
        'mountain',
        'nail',
        'noise',
        'occasion',
        'package',
        'patient',
        'pause',
        'phrase',
        'proof',
        'race',
        'relief',
        'sand',
        'sentence',
        'shoulder',
        'smoke',
        'stomach',
        'string',
        'tourist',
        'towel',
        'vacation',
        'west',
        'wheel',
        'wine',
        'arm',
        'aside',
        'associate',
        'bet',
        'blow',
        'border',
        'branch',
        'breast',
        'brother',
        'buddy',
        'bunch',
        'chip',
        'coach',
        'cross',
        'document',
        'draft',
        'dust',
        'expert',
        'floor',
        'god',
        'golf',
        'habit',
        'iron',
        'judge',
        'knife',
        'landscape',
        'league',
        'mail',
        'mess',
        'native',
        'opening',
        'parent',
        'pattern',
        'pin',
        'pool',
        'pound',
        'request',
        'salary',
        'shame',
        'shelter',
        'shoe',
        'silver',
        'tackle',
        'tank',
        'trust',
        'assist',
        'bake',
        'bar',
        'bell',
        'bike',
        'blame',
        'boy',
        'brick',
        'chair',
        'closet',
        'clue',
        'collar',
        'comment',
        'conference',
        'devil',
        'diet',
        'fear',
        'fuel',
        'glove',
        'jacket',
        'lunch',
        'monitor',
        'mortgage',
        'nurse',
        'pace',
        'panic',
        'peak',
        'plane',
        'reward',
        'row',
        'sandwich',
        'shock',
        'spite',
        'spray',
        'surprise',
        'till',
        'transition',
        'weekend',
        'welcome',
        'yard',
        'alarm',
        'bend',
        'bicycle',
        'bite',
        'blind',
        'bottle',
        'cable',
        'candle',
        'clerk',
        'cloud',
        'concert',
        'counter',
        'flower',
        'grandfather',
        'harm',
        'knee',
        'lawyer',
        'leather',
        'load',
        'mirror',
        'neck',
        'pension',
        'plate',
        'purple',
        'ruin',
        'ship',
        'skirt',
        'slice',
        'snow',
        'specialist',
        'stroke',
        'switch',
        'trash',
        'tune',
        'zone',
        'anger',
        'award',
        'bid',
        'bitter',
        'boot',
        'bug',
        'camp',
        'candy',
        'carpet',
        'cat',
        'champion',
        'channel',
        'clock',
        'comfort',
        'cow',
        'crack',
        'engineer',
        'entrance',
        'fault',
        'grass',
        'guy',
        'hell',
        'highlight',
        'incident',
        'island',
        'joke',
        'jury',
        'leg',
        'lip',
        'mate',
        'motor',
        'nerve',
        'passage',
        'pen',
        'pride',
        'priest',
        'prize',
        'promise',
        'resident',
        'resort',
        'ring',
        'roof',
        'rope',
        'sail',
        'scheme',
        'script',
        'sock',
        'station',
        'toe',
        'tower',
        'truck',
        'witness',
        'a',
        'you',
        'it',
        'can',
        'will',
        'if',
        'one',
        'many',
        'most',
        'other',
        'use',
        'make',
        'good',
        'look',
        'help',
        'go',
        'great',
        'being',
        'few',
        'might',
        'still',
        'public',
        'read',
        'keep',
        'start',
        'give',
        'human',
        'local',
        'general',
        'she',
        'specific',
        'long',
        'play',
        'feel',
        'high',
        'tonight',
        'put',
        'common',
        'set',
        'change',
        'simple',
        'past',
        'big',
        'possible',
        'particular',
        'today',
        'major',
        'personal',
        'current',
        'national',
        'cut',
        'natural',
        'physical',
        'show',
        'try',
        'check',
        'second',
        'call',
        'move',
        'pay',
        'let',
        'increase',
        'single',
        'individual',
        'turn',
        'ask',
        'buy',
        'guard',
        'hold',
        'main',
        'offer',
        'potential',
        'professional',
        'international',
        'travel',
        'cook',
        'alternative',
        'following',
        'special',
        'working',
        'whole',
        'dance',
        'excuse',
        'cold',
        'commercial',
        'low',
        'purchase',
        'deal',
        'primary',
        'worth',
        'fall',
        'necessary',
        'positive',
        'produce',
        'search',
        'present',
        'spend',
        'talk',
        'creative',
        'tell',
        'cost',
        'drive',
        'green',
        'support',
        'glad',
        'remove',
        'return',
        'run',
        'complex',
        'due',
        'effective',
        'middle',
        'regular',
        'reserve',
        'independent',
        'leave',
        'original',
        'reach',
        'rest',
        'serve',
        'watch',
        'beautiful',
        'charge',
        'active',
        'break',
        'negative',
        'safe',
        'stay',
        'visit',
        'visual',
        'affect',
        'cover',
        'report',
        'rise',
        'walk',
        'white',
        'beyond',
        'junior',
        'pick',
        'unique',
        'anything',
        'classic',
        'final',
        'lift',
        'mix',
        'private',
        'stop',
        'teach',
        'western',
        'concern',
        'familiar',
        'fly',
        'official',
        'broad',
        'comfortable',
        'gain',
        'maybe',
        'rich',
        'save',
        'stand',
        'young',
        'heavy',
        'hello',
        'lead',
        'listen',
        'valuable',
        'worry',
        'handle',
        'leading',
        'meet',
        'release',
        'sell',
        'finish',
        'normal',
        'press',
        'ride',
        'secret',
        'spread',
        'spring',
        'tough',
        'wait',
        'brown',
        'deep',
        'display',
        'flow',
        'hit',
        'objective',
        'shoot',
        'touch',
        'cancel',
        'chemical',
        'cry',
        'dump',
        'extreme',
        'push',
        'conflict',
        'eat',
        'fill',
        'formal',
        'jump',
        'kick',
        'opposite',
        'pass',
        'pitch',
        'remote',
        'total',
        'treat',
        'vast',
        'abuse',
        'beat',
        'burn',
        'deposit',
        'print',
        'raise',
        'sleep',
        'somewhere',
        'advance',
        'anywhere',
        'consist',
        'dark',
        'double',
        'draw',
        'equal',
        'fix',
        'hire',
        'internal',
        'join',
        'kill',
        'sensitive',
        'tap',
        'win',
        'attack',
        'claim',
        'constant',
        'drag',
        'drink',
        'guess',
        'minor',
        'pull',
        'raw',
        'soft',
        'solid',
        'wear',
        'weird',
        'wonder',
        'annual',
        'count',
        'dead',
        'doubt',
        'feed',
        'forever',
        'impress',
        'nobody',
        'repeat',
        'round',
        'sing',
        'slide',
        'strip',
        'whereas',
        'wish',
        'combine',
        'command',
        'dig',
        'divide',
        'equivalent',
        'hang',
        'hunt',
        'initial',
        'march',
        'mention',
        'spiritual',
        'survey',
        'tie',
        'adult',
        'brief',
        'crazy',
        'escape',
        'gather',
        'hate',
        'prior',
        'repair',
        'rough',
        'sad',
        'scratch',
        'sick',
        'strike',
        'employ',
        'external',
        'hurt',
        'illegal',
        'laugh',
        'lay',
        'mobile',
        'nasty',
        'ordinary',
        'respond',
        'royal',
        'senior',
        'split',
        'strain',
        'struggle',
        'swim',
        'train',
        'upper',
        'wash',
        'yellow',
        'convert',
        'crash',
        'dependent',
        'fold',
        'funny',
        'grab',
        'hide',
        'miss',
        'permit',
        'quote',
        'recover',
        'resolve',
        'roll',
        'sink',
        'slip',
        'spare',
        'suspect',
        'sweet',
        'swing',
        'twist',
        'upstairs',
        'usual',
        'abroad',
        'brave',
        'calm',
        'concentrate',
        'estimate',
        'grand',
        'male',
        'mine',
        'prompt',
        'quiet',
        'refuse',
        'regret',
        'reveal',
        'rush',
        'shake',
        'shift',
        'shine',
        'steal',
        'suck',
        'surround',
        'anybody',
        'bear',
        'brilliant',
        'dare',
        'dear',
        'delay',
        'drunk',
        'female',
        'hurry',
        'inevitable',
        'invite',
        'kiss',
        'neat',
        'pop',
        'punch',
        'quit',
        'reply',
        'representative',
        'resist',
        'rip',
        'rub',
        'silly',
        'smile',
        'spell',
        'stretch',
        'stupid',
        'tear',
        'temporary',
        'tomorrow',
        'wake',
        'wrap',
        'yesterday']

    ranword = random.choice(noun)

    return ranword


if __name__ == '__main__':
    VBUASclass()
