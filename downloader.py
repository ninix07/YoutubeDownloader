import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog, messagebox
from pytube import YouTube
import shutil

def button(window, text, color, command, fg,width=40):
    button= tk.Button(
        window,
        text=text,
        fg= fg,
        bg= color,
        height=2,
        width= width,
        command=command,
        activebackground="lightgreen",
    )
    return button

def canvas(window, height, width):
    canvas= tk.Canvas(
        window,
        height= height,
        width= width,
    )
    return canvas
class Downloader:
    def __init__(self):
        self.path=''
        self.window= tk.Tk()
        self.window.title("Youtube Video Downloader")
        self.window.geometry("1000x800+400+300")
        self.window.configure(bg="white")
        self.download_button= button(self.window,"Download","Green",self.download,"white")
        self.download_button.place(x=320,y=680)
        self.canvas=canvas(self.window,300,300)
        self.canvas.pack()
        self.img= Image.open("./youtube .jpg")
        resize= self.img.resize((300,300),Image.ANTIALIAS)
        self.new_image= ImageTk.PhotoImage(resize)
        self.canvas.create_image(150,150,image=self.new_image)
        self.canvas.place(x=320,y=100)
        self.title =  tk.Label(self.window, text= "Youtube Video Downloader",font= ("Times New Roman", 32))
        self.title.config(background="white")
        self.title.place(x=250, y= 400)
        self.download_label= tk.Label(self.window,text="Enter the download Link:", font=("Times New Roman",16), background="white")
        self.download_label.place(x=320,y=500)
        self.link_field= tk.Entry(self.window, width=50,font=("Times New Roman",12))
        self.link_field.place(x=320,y=530)
        self.browse_label= tk.Label(self.window,text="Select Path For Download:", font=("Times New Roman",16), background="white")
        self.browse_label.place(x=320,y=590)
        self.browse_button= button(self.window,"Browse","Grey",self.browse,"black", width= 20)
        self.browse_button.place(x=560,y=580)


    def download(self):
        if self.path == '':
             messagebox.showerror("No Path", "Error! Please Select a path")
        else:
            self.link = self.link_field.get()
            if self.link != '':
                video = YouTube(self.link).streams.get_highest_resolution().download()
                shutil.move(video, self.path)
                messagebox.showinfo("Download Complete","The video has been downlaoded!")
            else:
                messagebox.showerror("No Link", "Error! Please Enter Youtube Link")
            



    def browse(self):
        self.path= filedialog.askdirectory()



    def start(self):
        self.window.mainloop()

if __name__=='__main__':
    downloader= Downloader()
    downloader.start()