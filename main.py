from tkinter import *
from PIL import ImageTk, Image
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage


root = Tk()
root.title("BOT Mailing System")
root.geometry("1024x576")
root.minsize(1024, 576)
root.maxsize(1024, 576)

# root.maxsize(960, 540)
bg = ImageTk.PhotoImage(file="pvr.jpeg")
btn = PhotoImage(file="button(3).png")
btn1 = PhotoImage(file="button(2).png")
label_in_view = False


def get_label():
    label1.pack(padx=50, pady=140)

    root.after(1000, get_email_info)


def updatelabel(val):
    label1.config(text=val)


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()

    # position label, fontsize
    updatelabel("To : " + receiver + "\nFrom : Parvez\n" + "Subject : " + subject + "\nMSG : " + message +
                "\n\nYour email is sent")

    talk('Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_label()

# creating canvas


my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)

# set image in canvas
my_canvas.create_image(0, 0, image=bg, anchor=NW)
label1 = Label(my_canvas, text="To whom you want to send the email ?", font=("Arial Bold", 14), bg='#FFFFFF',
               activebackground='#FFFFFF')
#label2 = Label(my_canvas, text="What is the subject of your email ?",)

# creating button

button3 = Button(root, image=btn1, bd=0, bg='#1F1E1C', activebackground='#1F1E1C', command=root.destroy, cursor="hand2")
button4 = Button(root, image=btn, bd=0, bg='#1E1C1D', activebackground='#1E1C1D', command=get_label(),
                 cursor="hand2")

# button1_window =my_canvas.create_window(10,800,anchor="nw",window=button1,height=50,width=40)
# button2_window =my_canvas.create_window(100,10,anchor="nw",window=button2)
button3_window = my_canvas.create_window(646, 427, anchor=NW, window=button3, height=50, width=190)
button4_window = my_canvas.create_window(330, 425, anchor=NW, window=button4, height=60, width=190)
listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:

        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # transport layer security
    # Make sure to give app access in your Google account
    server.login('prvzzz.aaa@gmail.com', '') #enter your password in  'password'
    email = EmailMessage()
    email['From'] = 'prvzzz.aaa@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'adnan': 'ady78692@gmail.com',
    'alex': 'sufiyanalisufi786@gmail.com',
    'chotu': 'jcardon713@gmail.com',
    'zakaria': 'zakariayazdani18@gmail.com',
    'pink': 'jennie@blackpink.com',
    'abdullah': 'tariq.a99@gmail.com',
    'ali': 'syedalizafar7@gmail.com',
    'parvez': 'zainm8568@gmail.com',
    'azlan': '78692azlankhan@gmail.com'
}

root.mainloop()
