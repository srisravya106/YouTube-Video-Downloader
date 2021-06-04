import tkinter.font as font
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3
import webbrowser

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg = "green")

    else:
        locationError.config(text = "Please Choose Folder!!!",fg = "red")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text = "")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive = True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive = True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio = True).first()

        else:
            ytdError.config(text = "Paste Link again!!",fg = "red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text = "Download Completed!!!")

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

root = Tk()
root.title("YouTube Video Downloader")
root.geometry("500x500") #set window
root.configure(bg = 'gray13')
root.columnconfigure(0,weight = 1)#set all content in center.

#Ytd Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",fg = "white",bg="gray28",font = ("Lucida Fax",13,"bold"))
ytdLabel.grid(pady= 10)

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width = 50,textvariable = ytdEntryVar)
ytdEntry.grid(pady= 2)

#Error Msg
ytdError = Label(root,text = "Error in finding link",fg = "red",font = ("Times",8))
ytdError.grid(pady= 5)

#Asking save file label
saveLabel = Label(root,text = "Save the Video File",fg = "white",bg="gray28",font = ("Lucida Fax",13,"bold"))
saveLabel.grid(pady= 10)

#btn of save file
buttonFont = font.Font(family='Comic Sans MS', size=10, weight='bold')
saveEntry = Button(root,width = 10,bg = "red",fg = "white",text = "Choose Path",font=buttonFont,command = openLocation)
saveEntry.grid(pady= 2)

#Error Msg location
locationError = Label(root,text = "Error in finding Path",fg = "red",font = ("Times",8))
locationError.grid(pady= 5)

#Download Quality
ytdQuality = Label(root,text = "Select Quality",fg = "white",bg="gray28",font = ("Lucida Fax",13,"bold"))
ytdQuality.grid(pady= 10)

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values = choices)
ytdchoices.grid(pady= 2)

#download btn
#buttonFont = font.Font(family='Comic Sans MS', size=10, weight='bold')
downloadbtn = Button(root,text = "Download",width = 10,bg = "red",fg = "white",font=buttonFont,command = DownloadVideo)
downloadbtn.grid(pady= 5)

#YouTube Downloader Label
#photo = PhotoImage(file = r"C:\Users\Sravya\AppData\Local\Programs\Python\Python39\youtube-logo.png")
#photoimage = photo.subsample(3, 3)
YTdownloaderlabel = Label(root,text="YouTube Video Downloader",bg = "gray28",fg = "white",font=("Lucida Console",13,"bold italic"))
#Create a Label to display the link
link = Label(root, text="<click here to go to YouTube>",font=('Lucida Fax', 10,"bold underline"), fg="white",bg="gray28", cursor="hand2")
link.bind("<Button-1>", lambda e:
callback("http://www.youtube.com"))
link.grid(pady=10)
YTdownloaderlabel.grid(pady= 10)

root.mainloop()
