#DataFlair Tutorial for sending messages to telegram users using python
#Import necessary modules
from telethon import TelegramClient, events, sync
from tkinter import *
from tkinter import messagebox
import sys
import socks
import os
os.environ['HTTP_PROXY'] = 'socks5://127.0.0.1:10808'

#Sender function
def send_message():
    #API details
    user_details = user_entry.get()
    message_content = message_entry.get("1.0","end-1c")
    
    #Raise a warning if no input if given
    if (len(user_details) <=0) & (len(message_content)<=1):
        messagebox.showerror(message = "ENTER USER DETAILS" )
    else:
        #These API codes wont work, hence create your own
        api_id = 130347
        api_hash = '3c0cef102579e8959c4c43ee9cb37b22'


        #Initialise telegram client with API codes
        client = TelegramClient('session_name', api_id, api_hash)
        #Start the process
        client.start()
        #Send the message
        client.send_message(user_details, message_content)
        messagebox.showinfo(message = "MESSAGE SENT (:" )

#Define the user interface
telegram_mess = Tk()
telegram_mess.geometry("400x300")
telegram_mess.title("DataFlair's Telegram Message Sender")

bg_img = PhotoImage(file = "D:\\Folder.png")
  
# Show image using label
label1 = Label(telegram_mess, image = bg_img, bd=0)
label1.pack()

#Application Title in the window
title_label  = Label(telegram_mess, text="DataFlair's Telegram Message Sender", bg="#1d8bd6")
title_label.place(x=80,y=10)

#Input for user entry
user_label = Label(telegram_mess, text="ENTER USER DETAILS:", bg="#2591D9")
info_label = Label(telegram_mess, text="Note: Phone number with code or username with @", bg="#2C99DC")
user_label.place(x=0,y=40)
info_label.place(x=0,y=70)
user_entry = Entry(telegram_mess, width=20)
user_entry.place(x=160,y=40)

#Message input
message_label = Label(telegram_mess, text="ENTER MESSAGE:", bg ="#35A1DF")
message_label.place(x=0,y=100)
message_entry = Text(telegram_mess, width=30, height=3)
message_entry.place(x=130,y=99)

#send button
send_button = Button(telegram_mess, text="Send Button", command=send_message, relief= RAISED)
send_button.place(relx=0.5,rely=0.59, anchor=CENTER)

telegram_mess.mainloop()

