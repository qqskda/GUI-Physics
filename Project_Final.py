import time
import random
from threading import Thread
import tkinter as tk
import webbrowser
import tkinter.messagebox as tm
from datetime import datetime
from PIL import ImageTk
from tkinter import *
import tkinter.messagebox as tm
from PIL import ImageTk
import PIL.Image
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import N,E,W,S
from tkinter.ttk import Entry
from tkinter import *
from PIL import ImageTk
from PIL import Image
from random import randrange
import pygame
import os, subprocess
import runpy

#Creating a LoginFrame.
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure( background= '#a1dbcd')
        self.label_1 = Label(self, text="Please Type Your ID and Password", fg='#383a39', bg='#a1dbcd', font=("Helvetica",14))
        self.label_2 = Label(self, text="Username", fg= '#383a39', bg='#a1dbcd')
        self.label_3 = Label(self, text="Password", fg= '#383a39', bg='#a1dbcd')
        self.entry_2 = Entry(self)
        self.entry_3 = Entry(self, show="*")

        self.label_1.grid()
        self.label_2.grid(row=1, sticky=W)
        self.label_3.grid(row=2, sticky=W)
        self.entry_2.grid(row=1, column=0)
        self.entry_3.grid(row=2, column=0)

        # This is just showing off. Not working
        self.checkbox = Checkbutton(self, text="Remember Me",  fg= '#383a39', bg='#a1dbcd')
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked, fg= '#a1dbcd', bg='#383a39')
        self.logbtn.grid(columnspan=2)

        self.pack()



    def _login_btn_clickked(self):
        username = self.entry_2.get()
        password = self.entry_3.get()

        if username == "Ineedsleep" and password == "Really":
            app = SampleApp()
            app.mainloop()
        else:
            tm.showerror("Error!", "Possible Typo?")

class ScrolledCanvas(Frame):
    #Included this function to show there are two ways to open up image under tkinter for the class.
     def __init__(self, parent= None, **kwargs):
          Frame.__init__(self, parent)
          self.pack(expand=YES, fill=BOTH)
          canv = Canvas(self, relief=SUNKEN)
          canv.config(width=1700, height=600)

          canv.config(highlightthickness=0)

          sbarVertical = Scrollbar(self, orient=VERTICAL)
          sbarHorizontal = Scrollbar(self, orient=HORIZONTAL)

          sbarVertical.config(command=canv.yview)
          sbarHorizontal.config(command=canv.xview)

          canv.config(yscrollcommand=sbarVertical.set)
          canv.config(xscrollcommand=sbarHorizontal.set)

          sbarVertical.pack(side=RIGHT, fill=Y)
          sbarHorizontal.pack(side=BOTTOM, fill=X)

          canv.pack(side=LEFT, expand=YES, fill=BOTH)
          self.im = PIL.Image.open("HMM\C1P1Q.PNG")
          width, height = self.im.size
          canv.config(scrollregion=(0, 0, width, height))
          self.im2 = ImageTk.PhotoImage(self.im)
          self.imgtag = canv.create_image(0, 0, anchor="nw", image=self.im2)

          Canvas.__init__(self, parent, **kwargs)
          print(self.winfo_reqwidth(), self.winfo_reqheight())  # >>>854, 404
          self.bind("<Configure>", self.on_resize)



     def on_resize(self, event):
         self.width = event.width  # >>>854
         self.height = event.height  # >>>404
         self.config(width=self.width, height=self.height)




class SampleApp(tk.Tk):
    #Main App;  creating frames and setting attributes.

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Study Guide for Dr. Bochanski's PHY-200")
        #self.geometry()
        self.title_font = tkfont.Font(family='Helvetica', size=12, weight="bold", slant="italic")
        self.configure(background="#a1dbcd")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, AQA, QQ, ETM, RC, CP1, CP23, CP45, CP5, CP67, CP9, CP10, CP913, LTFun):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, columnspan=2, sticky="nsew")

        self.show_frame("StartPage")
        self.wm_minsize()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    #Starting Frame.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background_img = tk.PhotoImage(file = 'HMM\\newton.png')

        label = tk.Label(self, text="\nThis Program is to prepare upcoming final exam\n", font=controller.title_font)
        label.grid(row=0, columnspan= 1,sticky = N, pady = 8)


        label2 =tk.Label(self,text='Until The final:',font=controller.title_font)
        label2.grid(row=9, columnspan= 1,sticky = N, pady = 8)

        button1 = tk.Button(self, text="Assignments Questions/Answers", width = 30,
                            command=lambda: controller.show_frame("AQA"))
        button1.grid(row=1,columnspan=1)
        button2 = tk.Button(self, text="Quiz Questions", width = 30,
                            command=lambda: controller.show_frame("QQ"))
        button2.grid(row=2,columnspan=1)
        button3 = tk.Button(self, text="Exams - Two Midterms", width = 30,
                            command=lambda: controller.show_frame("ETM"))
        button3.grid(row=3,columnspan=1)
        button4 = tk.Button(self, text="Related Contents", width = 30,
                            command=lambda: controller.show_frame("RC"))
        button4.grid(row=4, columnspan=1)
        button5 = tk.Button(self, text="Little Fun", width=30,
                            command=lambda: controller.show_frame("LTFun"))
        button5.grid(row=5, columnspan=1)
        button6 = tk.Button(self, text="Close", width = 30,
                            command=lambda: root.quit())
        button6.grid(row=6, columnspan=1, pady = 5)

        days = str(15 - int(datetime.now().strftime('%d')))
        hours = str(24 - int(datetime.now().strftime('%H')))
        mins = str(59 - int(datetime.now().strftime('%M')))
        secs = str(59 - int(datetime.now().strftime('%S')))

        time_str = days + ' days ' + hours + ' hours ' + mins + ' mins ' + secs + ' seconds'


        label3 = tk.Label(self, text= str(time_str), font=controller.title_font)
        label3.grid(row = 11, columnspan =2)





class AQA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Assignments", font=controller.title_font)
        label.grid(row=0, columnspan=2, pady = 15)

        button1 = tk.Button(self, text="Chapter 1", width=18,
                            command=lambda: controller.show_frame("CP1"))
        button1.grid(row=1, columnspan=2)
        button2 = tk.Button(self, text="Chapter 2 and 3", width=18,
                            command=lambda: controller.show_frame("CP23"))
        button2.grid(row=2, columnspan=2)
        button3 = tk.Button(self, text="Chapter 4 and 5", width=18,
                            command=lambda: controller.show_frame("CP45"))
        button3.grid(row=3, columnspan=2)
        button4 = tk.Button(self, text="Chapter 5", width=18,
                            command=lambda: controller.show_frame("CP5"))
        button4.grid(row=4, columnspan=2)
        button5 = tk.Button(self, text="Chapter 6 and 7", width=18,
                            command=lambda: controller.show_frame("CP67"))
        button5.grid(row=5, columnspan=2)
        button6 = tk.Button(self, text="Chapter 9", width=18,
                            command=lambda: controller.show_frame("CP9"))
        button6.grid(row=6, columnspan=2)
        button7 = tk.Button(self, text="Chapter 10", width=18,
                            command=lambda: controller.show_frame("CP10"))
        button7.grid(row=7, columnspan=2)
        button8 = tk.Button(self, text="Chapter 9 and 13", width=18,
                            command=lambda: controller.show_frame("CP913"))
        button8.grid(row=8, columnspan=2)
        button9 = tk.Button(self, text="Go to the First page", width=18,
                            command=lambda: controller.show_frame("StartPage"))
        button9.grid(row=9, columnspan=3)


class CP1(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Assignment 1: Ch 1", font=controller.title_font)
        label.grid(row=0, columnspan=2, sticky=N)

        #a = lambda self: print(''.join('C1P' + self['text'][8] + 'A')) if len(self['text']) == 9 else ''.join('C1P' + self['text'][8:10] + 'A')

        button1 = tk.Button(self, text="Problem 1", width=18,
                            command=lambda: controller.show_frame(ScrolledCanvas().mainloop()))

        button2 = tk.Button(self, text="Problem 1 - Answer", width=18,
                            command=lambda img =Image.open('HMM\C1P1A.png'): img.show())
        button3 = tk.Button(self, text="Problem 3", width=18,
                            command=lambda img=Image.open('HMM\C1P3Q.png'): img.show())
        button4 = tk.Button(self, text="Problem 3 - Answer", width=18,
                            command=lambda img=Image.open('HMM\C1P3A.png'): img.show())
        button5 = tk.Button(self, text="Problem 5", width=18,
                            command=lambda img=Image.open('HMM\C1P5Q.png'): img.show())
        button6 = tk.Button(self, text="Problem 5 - Answer", width=18,
                            command=lambda img=Image.open('HMM\C1P5A.png'): img.show())
        button7 = tk.Button(self, text="Problem 7", width=18,
                            command=lambda img=Image.open('HMM\C1P7Q.png'): img.show())
        button8 = tk.Button(self, text="Problem 7 - Answer", width=18,
                            command=lambda img=Image.open('HMM\C1P7A.png'): img.show())
        button9 = tk.Button(self, text="Problem 8", width=18,
                            command=lambda img=Image.open('HMM\C1P8A.png'): img.show())
        button10 = tk.Button(self, text="Problem 8 - Answer", width=18,
                            command=lambda img=Image.open('HMM\C1P8Q.png'): img.show())
        button11 = tk.Button(self, text="Problem 10", width=18,
                            command=lambda img=Image.open('HMM\C1P10Q.png'): img.show())
        button12 = tk.Button(self, text="Problem 10 - Answer", width=18,
                            command=lambda img=Image.open('HMM\C1P10A.png'): img.show())
        button13 = tk.Button(self, text="Problem 12", width=18,
                            command=lambda img=Image.open('HMM\C1P12Q.png'): img.show())
        button14 = tk.Button(self, text="Problem 12 - Answer", width=18,
                            command=lambda img=Image.open('HMM\C1P12A.png'): img.show())
        button15 = tk.Button(self, text="Problem 13", width=18,
                            command=lambda img=Image.open('HMM\C1P13Q.png'): img.show())
        button16 = tk.Button(self, text="Problem 13 - Answer", width=18,
                            command=lambda img=Image.open('HMM\C1P13A.png'): img.show())
        button17 = tk.Button(self, text="Problem 15", width=18,
                            command=lambda img=Image.open('HMM\C1P15Q.png'): img.show())
        button18 = tk.Button(self, text="Problem 15 - Answer", width=18,
                            command=lambda img=Image.open('HMM\C1P15A.png'): img.show())
        button19 = tk.Button(self, text="Problem 20", width=18,
                            command=lambda img=Image.open('HMM\C1P20Q.png'): img.show())
        button20 = tk.Button(self, text="Problem 20 - Answer", width=18,
                            command=lambda img=Image.open('HMM\C1P20A.png'): img.show())
        button21 = tk.Button(self, text="Problem 21", width=18,
                            command=lambda img=Image.open('HMM\C1P21Q.png'): img.show())
        button22 = tk.Button(self, text="Problem 21 - Answer", width=18,
                            command=lambda img=Image.open('HMM\C1P21A.png'): img.show())
        button23 = tk.Button(self, text="Go to the First page", width=18,
                            command=lambda: controller.show_frame("StartPage"))
        button23.grid(row=12, column=0)


        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=3, column=0)
        button6.grid(row=3, column=1)
        button7.grid(row=4, column=0)
        button8.grid(row=4, column=1)
        button9.grid(row=5, column=0)
        button10.grid(row=5, column=1)
        button11.grid(row=6, column=0)
        button12.grid(row=6, column=1)
        button13.grid(row=7, column=0)
        button14.grid(row=7, column=1)
        button15.grid(row=8, column=0)
        button16.grid(row=8, column=1)
        button17.grid(row=9, column=0)
        button18.grid(row=9, column=1)
        button19.grid(row=10, column=0)
        button20.grid(row=10, column=1)
        button21.grid(row=11, column=0)
        button22.grid(row=11, column=1)

class CP23(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Assignment 2: Ch 2&3", font=controller.title_font)
        label.grid(row=0, column=0, sticky=N)

        button1 = tk.Button(self, text="Ch2 Problem 3", width=24,
                            command=lambda img=Image.open('HMM\C2P3Q.png'): img.show())
        button2 = tk.Button(self, text="Ch2 Problem 3 - Answer", width=24,
                            command=lambda img=Image.open('HMM\C2P3A.png'): img.show())
        button3 = tk.Button(self, text="Ch2 Problem 5", width=24,
                            command=lambda img=Image.open('HMM\C2P5Q.png'): img.show())
        button4 = tk.Button(self, text="Ch2 Problem 5 - Answer", width=24,
                            command=lambda img=Image.open('HMM\C2P5A.JPG'): img.show())
        button5 = tk.Button(self, text="Ch2 Problem 16", width=24,
                            command=lambda img=Image.open('HMM\C2P16Q.png'): img.show())
        button6 = tk.Button(self, text="Ch2 Problem 16 - Answer", width=24,
                            command=lambda img=Image.open('HMM\C2P16A.png'): img.show())
        button7 = tk.Button(self, text="Ch2 Problem 26", width=24,
                            command=lambda img=Image.open('HMM\C2P26Q.png'): img.show())
        button8 = tk.Button(self, text="Ch2 Problem 26 - Answer", width=24,
                            command=lambda img=Image.open('HMM\C2P26A.png'): img.show())
        button9 = tk.Button(self, text="Ch2 Problem 31", width=24,
                            command=lambda img=Image.open('HMM\C2P31A.png'): img.show())
        button10 = tk.Button(self, text="Ch2 Problem 31 - Answer", width=24,
                             command=lambda img=Image.open('HMM\C2P31Q.png'): img.show())
        button11 = tk.Button(self, text="Ch2 Problem 34", width=24,
                             command=lambda img=Image.open('HMM\C2P34Q.png'): img.show())
        button12 = tk.Button(self, text="Ch2 Problem 34 - Answer", width=24,
                             command=lambda img=Image.open('HMM\C2P34A.png'): img.show())
        button13 = tk.Button(self, text="Ch2 Problem 37", width=24,
                             command=lambda img=Image.open('HMM\C2P37Q.png'): img.show())
        button14 = tk.Button(self, text="Ch2 Problem 37 - Answer", width=24,
                             command=lambda img=Image.open('HMM\C2P37A.png'): img.show())
        button15 = tk.Button(self, text="Ch2 Problem 60", width=24,
                             command=lambda img=Image.open('HMM\C2P60Q.png'): img.show())
        button16 = tk.Button(self, text="Ch2 Problem 60 - Answer", width=24,
                             command=lambda img=Image.open('HMM\C2P60A.png'): img.show())
        button17 = tk.Button(self, text="Ch2 Problem 62", width=24,
                             command=lambda img=Image.open('HMM\C2P62Q.png'): img.show())
        button18 = tk.Button(self, text="Ch2 Problem 62 - Answer", width=24,
                             command=lambda img=Image.open('HMM\C2P62A.png'): img.show())
        button19 = tk.Button(self, text="Ch3 Problem 9", width=24,
                             command=lambda img=Image.open('HMM\C3P9Q.png'): img.show())
        button20 = tk.Button(self, text="Ch3 Problem 9 - Answer", width=24,
                             command=lambda img=Image.open('HMM\C3P9A.png'): img.show())
        button21 = tk.Button(self, text="Ch3 Problem 21", width=24,
                             command=lambda img=Image.open('HMM\C3P21Q.png'): img.show())
        button22 = tk.Button(self, text="Ch3 Problem 21 - Answer", width=24,
                             command=lambda img=Image.open('HMM\C3P21A.png'): img.show())
        button23 = tk.Button(self, text="Ch3 Problem 57", width=24,
                             command=lambda img=Image.open('HMM\C3P57Q.png'): img.show())
        button24 = tk.Button(self, text="Ch3 Problem 57 - Answer", width=24,
                             command=lambda img=Image.open('HMM\C3P57A.png'): img.show())
        button25 = tk.Button(self, text="Go to the First page", width=24,
                             command=lambda: controller.show_frame("StartPage"))


        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=3, column=0)
        button6.grid(row=3, column=1)
        button7.grid(row=4, column=0)
        button8.grid(row=4, column=1)
        button9.grid(row=5, column=0)
        button10.grid(row=5, column=1)
        button11.grid(row=6, column=0)
        button12.grid(row=6, column=1)
        button13.grid(row=7, column=0)
        button14.grid(row=7, column=1)
        button15.grid(row=8, column=0)
        button16.grid(row=8, column=1)
        button17.grid(row=9, column=0)
        button18.grid(row=9, column=1)
        button19.grid(row=10, column=0)
        button20.grid(row=10, column=1)
        button21.grid(row=11, column=0)
        button22.grid(row=11, column=1)
        button23.grid(row=12, column=0)
        button24.grid(row=12, column=1)
        button25.grid(row=13, column=0)

class CP45(tk.Frame):
    def __init__(self,parent, controller):

        ButtonName= ['Chapter 4 Problem 3',
                'Chapter 4 Problem 3 - Answer',
                'Chapter 5 Problem 4',
                'Chapter 5 Problem 4 - Answer',
                'Chapter 4 Problem 14',
                'Chapter 4 Problem 14 - Answer',
                'Chapter 4 Problem 15',
                'Chapter 4 Problem 15 - Answer',
                'Chapter 4 Problem 17',
                'Chapter 4 Problem 17 - Answer',
                'Chapter 4 Problem 21',
                'Chapter 4 Problem 21 - Answer',
                'Chapter 4 Problem 23',
                'Chapter 4 Problem 23 - Answer',
                'Chapter 4 Problem 24',
                'Chapter 4 Problem 24 - Answer',
                'Chapter 4 Problem 28',
                'Chapter 4 Problem 28 - Answer',
                'Chapter 4 Problem 29',
                'Chapter 4 Problem 29 - Answer',
                'Chapter 4 Problem 35',
                'Chapter 4 Problem 35 - Answer',
                'Chapter 5 Problem 2',
                'Chapter 5 Problem 2 - Answer',
                'Chapter 5 Problem 10',
                'Chapter 5 Problem 10 - Answer']

        Filename = ['HMM\C4P3Q.png',
                    'HMM\C4P3A.png',
                    'HMM\C5P4Q.png',
                    'HMM\C5P4A.png',
                    'HMM\C4P14Q.png',
                    'HMM\C4P14A.png',
                    'HMM\C4P15Q.png',
                    'HMM\C4P15A.png',
                    'HMM\C4P17Q.png',
                    'HMM\C4P17A.png',
                    'HMM\C4P21Q.png',
                    'HMM\C4P21A.png',
                    'HMM\C4P23Q.png',
                    'HMM\C4P23A.png',
                    'HMM\C4P24Q.png',
                    'HMM\C4P24A.png',
                    'HMM\C4P28Q.png',
                    'HMM\C4P28A.png',
                    'HMM\C4P29Q.png',
                    'HMM\C4P29A.png',
                    'HMM\C4P35Q.png',
                    'HMM\C4P35A.png',
                    'HMM\C5P2Q.png',
                    'HMM\C5P2A.png',
                    'HMM\C5P10Q.png',
                    'HMM\C5P10A.png']


        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Assignment 3: Ch 4&5", font=controller.title_font)
        label.grid(row=0, column=0, sticky=E)

        button1 = tk.Button(self, text=ButtonName[0], width=24,
                            command=lambda img=Image.open(Filename[0]): img.show())
        button2 = tk.Button(self, text=ButtonName[1], width=24,
                            command=lambda img=Image.open(Filename[1]): img.show())
        button3 = tk.Button(self, text=ButtonName[2], width=24,
                            command=lambda img=Image.open(Filename[2]): img.show())
        button4 = tk.Button(self, text=ButtonName[3], width=24,
                            command=lambda img=Image.open(Filename[3]): img.show())
        button5 = tk.Button(self, text=ButtonName[4], width=24,
                            command=lambda img=Image.open(Filename[4]): img.show())
        button6 = tk.Button(self, text=ButtonName[5], width=24,
                            command=lambda img=Image.open(Filename[5]): img.show())
        button7 = tk.Button(self, text=ButtonName[6], width=24,
                            command=lambda img=Image.open(Filename[6]): img.show())
        button8 = tk.Button(self, text=ButtonName[7], width=24,
                            command=lambda img=Image.open(Filename[7]): img.show())
        button9 = tk.Button(self, text=ButtonName[8], width=24,
                            command=lambda img=Image.open(Filename[8]): img.show())
        button10 = tk.Button(self, text=ButtonName[9], width=24,
                             command=lambda img=Image.open(Filename[9]): img.show())
        button11 = tk.Button(self, text=ButtonName[10], width=24,
                             command=lambda img=Image.open(Filename[10]): img.show())
        button12 = tk.Button(self, text=ButtonName[11], width=24,
                             command=lambda img=Image.open(Filename[11]): img.sow())
        button13 = tk.Button(self, text=ButtonName[12], width=24,
                             command=lambda img=Image.open(Filename[12]): img.show())
        button14 = tk.Button(self, text=ButtonName[13], width=24,
                             command=lambda img=Image.open(Filename[13]): img.show())
        button15 = tk.Button(self, text=ButtonName[14], width=24,
                             command=lambda img=Image.open(Filename[14]): img.show())
        button16 = tk.Button(self, text=ButtonName[15], width=24,
                             command=lambda img=Image.open(Filename[15]): img.show())
        button17 = tk.Button(self, text=ButtonName[16], width=24,
                             command=lambda img=Image.open(Filename[16]): img.show())
        button18 = tk.Button(self, text=ButtonName[17], width=24,
                             command=lambda img=Image.open(Filename[17]): img.show())
        button19 = tk.Button(self, text=ButtonName[18], width=24,
                             command=lambda img=Image.open(Filename[18]): img.show())
        button20 = tk.Button(self, text=ButtonName[19], width=24,
                             command=lambda img=Image.open(Filename[19]): img.show())
        button21 = tk.Button(self, text=ButtonName[20], width=24,
                             command=lambda img=Image.open(Filename[20]): img.show())
        button22 = tk.Button(self, text=ButtonName[21], width=24,
                             command=lambda img=Image.open(Filename[21]): img.show())
        button23 = tk.Button(self, text=ButtonName[22], width=24,
                             command=lambda img=Image.open(Filename[22]): img.show())
        button24 = tk.Button(self, text=ButtonName[23], width=24,
                             command=lambda img=Image.open(Filename[23]): img.show())
        button25 = tk.Button(self, text=ButtonName[24], width=24,
                             command=lambda img=Image.open(Filename[24]): img.show())
        button26 = tk.Button(self, text=ButtonName[25], width=24,
                             command=lambda img=Image.open(Filename[25]): img.show())
        button27 = tk.Button(self, text="Go to the First page", width=24,
                             command=lambda: controller.show_frame("StartPage"))



        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=3, column=0)
        button6.grid(row=3, column=1)
        button7.grid(row=4, column=0)
        button8.grid(row=4, column=1)
        button9.grid(row=5, column=0)
        button10.grid(row=5, column=1)
        button11.grid(row=6, column=0)
        button12.grid(row=6, column=1)
        button13.grid(row=7, column=0)
        button14.grid(row=7, column=1)
        button15.grid(row=8, column=0)
        button16.grid(row=8, column=1)
        button17.grid(row=9, column=0)
        button18.grid(row=9, column=1)
        button19.grid(row=10, column=0)
        button20.grid(row=10, column=1)
        button21.grid(row=11, column=0)
        button22.grid(row=11, column=1)
        button23.grid(row=12, column=0)
        button24.grid(row=12, column=1)
        button25.grid(row=13, column=0)
        button26.grid(row=13, column=1)
        button27.grid(row=14, column=0)

class CP5(tk.Frame):
    def __init__(self,parent, controller):

        ButtonName= [ 'Ch 5 Problem 3',
            'Ch 5 Problem 3 - Answer',
            'Ch 5 Problem 4',
            'Ch 5 Problem 4 - Answer',
            'Ch 5 Problem 8',
            'Ch 5 Problem 8 - Answer',
            'Ch 5 Problem 10',
            'Ch 5 Problem 10 - Answer',
            'Ch 5 Problem 11',
            'Ch 5 Problem 11 - Answer',
            'Ch 5 Problem 13',
            'Ch 5 Problem 13 - Answer',
            'Ch 5 Problem 15',
            'Ch 5 Problem 15 - Answer',
            'Ch 5 Problem 17',
            'Ch 5 Problem 17 - Answer',
            'Ch 5 Problem 19',
            'Ch 5 Problem 19 - Answer',
            'Ch 5 Problem 25',
            'Ch 5 Problem 25 - Answer',
            'Ch 5 Problem 26',
            'Ch 5 Problem 26 - Answer',
            'Ch 5 Problem 27',
            'Ch 5 Problem 27 - Answer',
            'Ch 5 Problem 30',
            'Ch 5 Problem 30 - Answer',
            'Ch 5 Problem 51',
            'Ch 5 Problem 51 - Answer']

        Filename = ['HMM\C5P3Q.png',
                    'HMM\C5P3A.png',
                    'HMM\C5P4Q.png',
                    'HMM\C5P4A.png',
                    'HMM\C5P8Q.png',
                    'HMM\C5P8A.png',
                    'HMM\C5P10Q.png',
                    'HMM\C5P10A.png',
                    'HMM\C5P11Q.png',
                    'HMM\C5P11A.png',
                    'HMM\C5P13Q.png',
                    'HMM\C5P13A.png',
                    'HMM\C5P15Q.png',
                    'HMM\C5P15A.png',
                    'HMM\C5P17Q.png',
                    'HMM\C5P17A.png',
                    'HMM\C5P19Q.png',
                    'HMM\C5P19A.png',
                    'HMM\C5P25Q.png',
                    'HMM\C5P25A.png',
                    'HMM\C5P26Q.png',
                    'HMM\C5P26A.png',
                    'HMM\C5P27Q.png',
                    'HMM\C5P27A.png',
                    'HMM\C5P30Q.png',
                    'HMM\C5P30A.png',
                    'HMM\C5P51Q.png',
                    'HMM\C5P51A.png'
                    ]


        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Assignment 4: Ch 5", font=controller.title_font)
        label.grid(row=0, column=0, sticky=E)

        button1 = tk.Button(self, text=ButtonName[0], width=24,
                            command=lambda img=Image.open(Filename[0]): img.show())
        button2 = tk.Button(self, text=ButtonName[1], width=24,
                            command=lambda img=Image.open(Filename[1]): img.show())
        button3 = tk.Button(self, text=ButtonName[2], width=24,
                            command=lambda img=Image.open(Filename[2]): img.show())
        button4 = tk.Button(self, text=ButtonName[3], width=24,
                            command=lambda img=Image.open(Filename[3]): img.show())
        button5 = tk.Button(self, text=ButtonName[4], width=24,
                            command=lambda img=Image.open(Filename[4]): img.show())
        button6 = tk.Button(self, text=ButtonName[5], width=24,
                            command=lambda img=Image.open(Filename[5]): img.show())
        button7 = tk.Button(self, text=ButtonName[6], width=24,
                            command=lambda img=Image.open(Filename[6]): img.show())
        button8 = tk.Button(self, text=ButtonName[7], width=24,
                            command=lambda img=Image.open(Filename[7]): img.show())
        button9 = tk.Button(self, text=ButtonName[8], width=24,
                            command=lambda img=Image.open(Filename[8]): img.show())
        button10 = tk.Button(self, text=ButtonName[9], width=24,
                             command=lambda img=Image.open(Filename[9]): img.show())
        button11 = tk.Button(self, text=ButtonName[10], width=24,
                             command=lambda img=Image.open(Filename[10]): img.show())
        button12 = tk.Button(self, text=ButtonName[11], width=24,
                             command=lambda img=Image.open(Filename[11]): img.sow())
        button13 = tk.Button(self, text=ButtonName[12], width=24,
                             command=lambda img=Image.open(Filename[12]): img.show())
        button14 = tk.Button(self, text=ButtonName[13], width=24,
                             command=lambda img=Image.open(Filename[13]): img.show())
        button15 = tk.Button(self, text=ButtonName[14], width=24,
                             command=lambda img=Image.open(Filename[14]): img.show())
        button16 = tk.Button(self, text=ButtonName[15], width=24,
                             command=lambda img=Image.open(Filename[15]): img.show())
        button17 = tk.Button(self, text=ButtonName[16], width=24,
                             command=lambda img=Image.open(Filename[16]): img.show())
        button18 = tk.Button(self, text=ButtonName[17], width=24,
                             command=lambda img=Image.open(Filename[17]): img.show())
        button19 = tk.Button(self, text=ButtonName[18], width=24,
                             command=lambda img=Image.open(Filename[18]): img.show())
        button20 = tk.Button(self, text=ButtonName[19], width=24,
                             command=lambda img=Image.open(Filename[19]): img.show())
        button21 = tk.Button(self, text=ButtonName[20], width=24,
                             command=lambda img=Image.open(Filename[20]): img.show())
        button22 = tk.Button(self, text=ButtonName[21], width=24,
                             command=lambda img=Image.open(Filename[21]): img.show())
        button23 = tk.Button(self, text=ButtonName[22], width=24,
                             command=lambda img=Image.open(Filename[22]): img.show())
        button24 = tk.Button(self, text=ButtonName[23], width=24,
                             command=lambda img=Image.open(Filename[23]): img.show())
        button25 = tk.Button(self, text=ButtonName[24], width=24,
                             command=lambda img=Image.open(Filename[24]): img.show())
        button26 = tk.Button(self, text=ButtonName[25], width=24,
                             command=lambda img=Image.open(Filename[25]): img.show())
        button27 = tk.Button(self, text=ButtonName[26], width=24,
                             command=lambda img=Image.open(Filename[26]): img.show())
        button28 = tk.Button(self, text=ButtonName[27], width=24,
                             command=lambda img=Image.open(Filename[27]): img.show())
        button29 = tk.Button(self, text="Go to the First page", width=24,
                             command=lambda: controller.show_frame("StartPage"))


        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=3, column=0)
        button6.grid(row=3, column=1)
        button7.grid(row=4, column=0)
        button8.grid(row=4, column=1)
        button9.grid(row=5, column=0)
        button10.grid(row=5, column=1)
        button11.grid(row=6, column=0)
        button12.grid(row=6, column=1)
        button13.grid(row=7, column=0)
        button14.grid(row=7, column=1)
        button15.grid(row=8, column=0)
        button16.grid(row=8, column=1)
        button17.grid(row=9, column=0)
        button18.grid(row=9, column=1)
        button19.grid(row=10, column=0)
        button20.grid(row=10, column=1)
        button21.grid(row=11, column=0)
        button22.grid(row=11, column=1)
        button23.grid(row=12, column=0)
        button24.grid(row=12, column=1)
        button25.grid(row=13, column=0)
        button26.grid(row=13, column=1)
        button27.grid(row=14, column=0)
        button28.grid(row=14, column=1)
        button29.grid(row=15, column=0)

class CP67(tk.Frame):
    def __init__(self,parent, controller):

        ButtonName= [  'Ch 6 Problem 12',
                    'Ch 6 Problem 12 - Answer',
                    'Ch 6 Problem 16',
                    'Ch 6 Problem 16 - Answer',
                    'Ch 6 Problem 23',
                    'Ch 6 Problem 23 - Answer',
                    'Ch 6 Problem 27',
                    'Ch 6 Problem 27 - Answer',
                    'Ch 6 Problem 2',
                    'Ch 6 Problem 2 - Answer',
                    'Ch 6 Problem 30','Ch 6 Problem 30 - Answer',
                    'Ch 6 Problem 4','Ch 6 Problem 4 - Answer',
                    'Ch 6 Problem 5','Ch 6 Problem 5 - Answer',
                    'Ch 6 Problem 8','Ch 6 Problem 8 - Answer',
                    'Ch 6 Problem 9','Ch 6 Problem 9 - Answer',
                    'Ch 7 Problem 17','Ch 7 Problem 17 - Answer',
                    'Ch 7 Problem 26','Ch 7 Problem 26 - Answer',
                    'Ch 7 Problem 5','Ch 7 Problem 5 - Answer',
                    'Ch 7 Problem 8', 'Ch 7 Problem 8 - Answer']

        Filename = ['HMM\C6P12Q.png',
                    'HMM\C6P12A.png',
                    'HMM\C6P16Q.png',
                    'HMM\C6P16A.png',
                    'HMM\C6P23Q.png',
                    'HMM\C6P23A.png',
                    'HMM\C6P27Q.png',
                    'HMM\C6P27A.png',
                    'HMM\C6P2Q.png',
                    'HMM\C6P2A.png',
                    'HMM\C6P30Q.png',
                    'HMM\C6P30A.png',
                    'HMM\C6P4Q.png',
                    'HMM\C6P4A.png',
                    'HMM\C6P5Q.png',
                    'HMM\C6P5A.png',
                    'HMM\C6P8Q.png',
                    'HMM\C6P8A.png',
                    'HMM\C6P9Q.png',
                    'HMM\C6P9A.png',
                    'HMM\C7P17Q.png',
                    'HMM\C7P17A.png',
                    'HMM\C7P26Q.png',
                    'HMM\C7P26A.png',
                    'HMM\C7P5Q.png',
                    'HMM\C7P5A.png',
                    'HMM\C7P8Q.png',
                    'HMM\C7P8A.png']


        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Assignment 5: Ch 6&7", font=controller.title_font)
        label.grid(row=0, column=0, sticky=E)

        button1 = tk.Button(self, text=ButtonName[0], width=24,
                            command=lambda img=Image.open(Filename[0]): img.show())
        button2 = tk.Button(self, text=ButtonName[1], width=24,
                            command=lambda img=Image.open(Filename[1]): img.show())
        button3 = tk.Button(self, text=ButtonName[2], width=24,
                            command=lambda img=Image.open(Filename[2]): img.show())
        button4 = tk.Button(self, text=ButtonName[3], width=24,
                            command=lambda img=Image.open(Filename[3]): img.show())
        button5 = tk.Button(self, text=ButtonName[4], width=24,
                            command=lambda img=Image.open(Filename[4]): img.show())
        button6 = tk.Button(self, text=ButtonName[5], width=24,
                            command=lambda img=Image.open(Filename[5]): img.show())
        button7 = tk.Button(self, text=ButtonName[6], width=24,
                            command=lambda img=Image.open(Filename[6]): img.show())
        button8 = tk.Button(self, text=ButtonName[7], width=24,
                            command=lambda img=Image.open(Filename[7]): img.show())
        button9 = tk.Button(self, text=ButtonName[8], width=24,
                            command=lambda img=Image.open(Filename[8]): img.show())
        button10 = tk.Button(self, text=ButtonName[9], width=24,
                             command=lambda img=Image.open(Filename[9]): img.show())
        button11 = tk.Button(self, text=ButtonName[10], width=24,
                             command=lambda img=Image.open(Filename[10]): img.show())
        button12 = tk.Button(self, text=ButtonName[11], width=24,
                             command=lambda img=Image.open(Filename[11]): img.sow())
        button13 = tk.Button(self, text=ButtonName[12], width=24,
                             command=lambda img=Image.open(Filename[12]): img.show())
        button14 = tk.Button(self, text=ButtonName[13], width=24,
                             command=lambda img=Image.open(Filename[13]): img.show())
        button15 = tk.Button(self, text=ButtonName[14], width=24,
                             command=lambda img=Image.open(Filename[14]): img.show())
        button16 = tk.Button(self, text=ButtonName[15], width=24,
                             command=lambda img=Image.open(Filename[15]): img.show())
        button17 = tk.Button(self, text=ButtonName[16], width=24,
                             command=lambda img=Image.open(Filename[16]): img.show())
        button18 = tk.Button(self, text=ButtonName[17], width=24,
                             command=lambda img=Image.open(Filename[17]): img.show())
        button19 = tk.Button(self, text=ButtonName[18], width=24,
                             command=lambda img=Image.open(Filename[18]): img.show())
        button20 = tk.Button(self, text=ButtonName[19], width=24,
                             command=lambda img=Image.open(Filename[19]): img.show())
        button21 = tk.Button(self, text=ButtonName[20], width=24,
                             command=lambda img=Image.open(Filename[20]): img.show())
        button22 = tk.Button(self, text=ButtonName[21], width=24,
                             command=lambda img=Image.open(Filename[21]): img.show())
        button23 = tk.Button(self, text=ButtonName[22], width=24,
                             command=lambda img=Image.open(Filename[22]): img.show())
        button24 = tk.Button(self, text=ButtonName[23], width=24,
                             command=lambda img=Image.open(Filename[23]): img.show())
        button25 = tk.Button(self, text=ButtonName[24], width=24,
                             command=lambda img=Image.open(Filename[24]): img.show())
        button26 = tk.Button(self, text=ButtonName[25], width=24,
                             command=lambda img=Image.open(Filename[25]): img.show())
        button27 = tk.Button(self, text=ButtonName[26], width=24,
                             command=lambda img=Image.open(Filename[26]): img.show())
        button28 = tk.Button(self, text=ButtonName[27], width=24,
                             command=lambda img=Image.open(Filename[27]): img.show())
        button29 = tk.Button(self, text="Go to the First page", width=24,
                             command=lambda: controller.show_frame("StartPage"))


        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=3, column=0)
        button6.grid(row=3, column=1)
        button7.grid(row=4, column=0)
        button8.grid(row=4, column=1)
        button9.grid(row=5, column=0)
        button10.grid(row=5, column=1)
        button11.grid(row=6, column=0)
        button12.grid(row=6, column=1)
        button13.grid(row=7, column=0)
        button14.grid(row=7, column=1)
        button15.grid(row=8, column=0)
        button16.grid(row=8, column=1)
        button17.grid(row=9, column=0)
        button18.grid(row=9, column=1)
        button19.grid(row=10, column=0)
        button20.grid(row=10, column=1)
        button21.grid(row=11, column=0)
        button22.grid(row=11, column=1)
        button23.grid(row=12, column=0)
        button24.grid(row=12, column=1)
        button25.grid(row=13, column=0)
        button26.grid(row=13, column=1)
        button27.grid(row=14, column=0)
        button28.grid(row=14, column=1)
        button29.grid(row=15, column=0)

class CP9(tk.Frame):
    def __init__(self,parent, controller):

        ButtonName= [
            'Chapter 9 Problem 1',
            'Chapter 9 Problem 1 - Answer',
            'Chapter 9 Problem 2',
            'Chapter 9 Problem 2 - Answer',
            'Chapter 9 Problem 4',
            'Chapter 9 Problem 4 - Answer',
            'Chapter 9 Problem 6',
            'Chapter 9 Problem 6 - Answer',
            'Chapter 9 Problem 9',
            'Chapter 9 Problem 9 - Answer',
            'Chapter 9 Problem 10',
            'Chapter 9 Problem 10 - Answer',
            'Chapter 9 Problem 13',
            'Chapter 9 Problem 13 - Answer',
            'Chapter 9 Problem 18',
            'Chapter 9 Problem 18 - Answer',
            'Chapter 9 Problem 23',
            'Chapter 9 Problem 23 - Answer',
            'Chapter 9 Problem 26',
            'Chapter 9 Problem 26 - Answer',
            'Chapter 9 Problem 31',
            'Chapter 9 Problem 31 - Answer']

        Filename = ['HMM\C9P10Q.png',
                    'HMM\C9P10A.png',
                    'HMM\C9P13Q.png',
                    'HMM\C9P13A.png',
                    'HMM\C9P18Q.png',
                    'HMM\C9P18A.png',
                    'HMM\C9P1Q.png',
                    'HMM\C9P1A.png',
                    'HMM\C9P23Q.png',
                    'HMM\C9P23A.png',
                    'HMM\C9P26Q.png',
                    'HMM\C9P26A.png',
                    'HMM\C9P2Q.png',
                    'HMM\C9P2A.png',
                    'HMM\C9P31Q.png',
                    'HMM\C9P31A.png',
                    'HMM\C9P4Q.png',
                    'HMM\C9P4A.png',
                    'HMM\C9P6Q.png',
                    'HMM\C9P6A.png',
                    'HMM\C9P9Q.png',
                    'HMM\C9P9A.png']


        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Assignment 6: Ch 9", font=controller.title_font)
        label.grid(row=0, column=0, sticky=E)

        button1 = tk.Button(self, text=ButtonName[0], width=24,
                            command=lambda img=Image.open(Filename[0]): img.show())
        button2 = tk.Button(self, text=ButtonName[1], width=24,
                            command=lambda img=Image.open(Filename[1]): img.show())
        button3 = tk.Button(self, text=ButtonName[2], width=24,
                            command=lambda img=Image.open(Filename[2]): img.show())
        button4 = tk.Button(self, text=ButtonName[3], width=24,
                            command=lambda img=Image.open(Filename[3]): img.show())
        button5 = tk.Button(self, text=ButtonName[4], width=24,
                            command=lambda img=Image.open(Filename[4]): img.show())
        button6 = tk.Button(self, text=ButtonName[5], width=24,
                            command=lambda img=Image.open(Filename[5]): img.show())
        button7 = tk.Button(self, text=ButtonName[6], width=24,
                            command=lambda img=Image.open(Filename[6]): img.show())
        button8 = tk.Button(self, text=ButtonName[7], width=24,
                            command=lambda img=Image.open(Filename[7]): img.show())
        button9 = tk.Button(self, text=ButtonName[8], width=24,
                            command=lambda img=Image.open(Filename[8]): img.show())
        button10 = tk.Button(self, text=ButtonName[9], width=24,
                             command=lambda img=Image.open(Filename[9]): img.show())
        button11 = tk.Button(self, text=ButtonName[10], width=24,
                             command=lambda img=Image.open(Filename[10]): img.show())
        button12 = tk.Button(self, text=ButtonName[11], width=24,
                             command=lambda img=Image.open(Filename[11]): img.sow())
        button13 = tk.Button(self, text=ButtonName[12], width=24,
                             command=lambda img=Image.open(Filename[12]): img.show())
        button14 = tk.Button(self, text=ButtonName[13], width=24,
                             command=lambda img=Image.open(Filename[13]): img.show())
        button15 = tk.Button(self, text=ButtonName[14], width=24,
                             command=lambda img=Image.open(Filename[14]): img.show())
        button16 = tk.Button(self, text=ButtonName[15], width=24,
                             command=lambda img=Image.open(Filename[15]): img.show())
        button17 = tk.Button(self, text=ButtonName[16], width=24,
                             command=lambda img=Image.open(Filename[16]): img.show())
        button18 = tk.Button(self, text=ButtonName[17], width=24,
                             command=lambda img=Image.open(Filename[17]): img.show())
        button19 = tk.Button(self, text=ButtonName[18], width=24,
                             command=lambda img=Image.open(Filename[18]): img.show())
        button20 = tk.Button(self, text=ButtonName[19], width=24,
                             command=lambda img=Image.open(Filename[19]): img.show())
        button21 = tk.Button(self, text=ButtonName[20], width=24,
                             command=lambda img=Image.open(Filename[20]): img.show())
        button22 = tk.Button(self, text=ButtonName[21], width=24,
                             command=lambda img=Image.open(Filename[21]): img.show())
        button23 = tk.Button(self, text="Go to the First page", width=24,
                             command=lambda: controller.show_frame("StartPage"))

        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=3, column=0)
        button6.grid(row=3, column=1)
        button7.grid(row=4, column=0)
        button8.grid(row=4, column=1)
        button9.grid(row=5, column=0)
        button10.grid(row=5, column=1)
        button11.grid(row=6, column=0)
        button12.grid(row=6, column=1)
        button13.grid(row=7, column=0)
        button14.grid(row=7, column=1)
        button15.grid(row=8, column=0)
        button16.grid(row=8, column=1)
        button17.grid(row=9, column=0)
        button18.grid(row=9, column=1)
        button19.grid(row=10, column=0)
        button20.grid(row=10, column=1)
        button21.grid(row=11, column=0)
        button22.grid(row=11, column=1)
        button23.grid(row=12, column=0)

class CP10(tk.Frame):
    def __init__(self,parent, controller):

        ButtonName= ['Ch - Answerpter 10 Problem 1',
                        'Ch - Answerpter 10 Problem 1 - Answer',
                        'Ch - Answerpter 10 Problem 3',
                        'Ch - Answerpter 10 Problem 3 - Answer',
                        'Ch - Answerpter 10 Problem 4',
                        'Ch - Answerpter 10 Problem 4 - Answer',
                        'Ch - Answerpter 10 Problem 13',
                        'Ch - Answerpter 10 Problem 13 - Answer',
                        'Ch - Answerpter 10 Problem 15',
                        'Ch - Answerpter 10 Problem 15 - Answer',
                        'Ch - Answerpter 10 Problem 19',
                        'Ch - Answerpter 10 Problem 19 - Answer',
                        'Ch - Answerpter 10 Problem 22',
                        'Ch - Answerpter 10 Problem 22 - Answer',
                        'Ch - Answerpter 10 Problem 25',
                        'Ch - Answerpter 10 Problem 25 - Answer',
                        'Ch - Answerpter 10 Problem 29',
                        'Ch - Answerpter 10 Problem 29 - Answer',
                        'Ch - Answerpter 10 Problem 33',
                        'Ch - Answerpter 10 Problem 33 - Answer',
                        'Ch - Answerpter 10 Problem 41',
                        'Ch - Answerpter 10 Problem 41 - Answer',
                        'Ch - Answerpter 10 Problem 50',
                        'Ch - Answerpter 10 Problem 50 - Answer']

        Filename = ['HMM\C10P1Q.png',
                    'HMM\C10P1A.png',
                    'HMM\C10P3Q.png',
                    'HMM\C10P3A.png',
                    'HMM\C10P4Q.png',
                    'HMM\C10P4A.png',
                    'HMM\C10P13Q.png',
                    'HMM\C10P13A.png',
                    'HMM\C10P15Q.png',
                    'HMM\C10P15A.png',
                    'HMM\C10P19Q.png',
                    'HMM\C10P19A.png',
                    'HMM\C10P22Q.png',
                    'HMM\C10P22A.png',
                    'HMM\C10P25Q.png',
                    'HMM\C10P25A.png',
                    'HMM\C10P29Q.png',
                    'HMM\C10P29A.png',
                    'HMM\C10P33Q.png',
                    'HMM\C10P33A.png',
                    'HMM\C10P41Q.png',
                    'HMM\C10P41A.png',
                    'HMM\C10P50Q.png',
                    'HMM\C10P50A.png'
]


        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Assignment 7: Ch 10", font=controller.title_font)
        label.grid(row=0, column=0, sticky=E)

        button1 = tk.Button(self, text=ButtonName[0], width=24,
                            command=lambda img=Image.open(Filename[0]): img.show())
        button2 = tk.Button(self, text=ButtonName[1], width=24,
                            command=lambda img=Image.open(Filename[1]): img.show())
        button3 = tk.Button(self, text=ButtonName[2], width=24,
                            command=lambda img=Image.open(Filename[2]): img.show())
        button4 = tk.Button(self, text=ButtonName[3], width=24,
                            command=lambda img=Image.open(Filename[3]): img.show())
        button5 = tk.Button(self, text=ButtonName[4], width=24,
                            command=lambda img=Image.open(Filename[4]): img.show())
        button6 = tk.Button(self, text=ButtonName[5], width=24,
                            command=lambda img=Image.open(Filename[5]): img.show())
        button7 = tk.Button(self, text=ButtonName[6], width=24,
                            command=lambda img=Image.open(Filename[6]): img.show())
        button8 = tk.Button(self, text=ButtonName[7], width=24,
                            command=lambda img=Image.open(Filename[7]): img.show())
        button9 = tk.Button(self, text=ButtonName[8], width=24,
                            command=lambda img=Image.open(Filename[8]): img.show())
        button10 = tk.Button(self, text=ButtonName[9], width=24,
                             command=lambda img=Image.open(Filename[9]): img.show())
        button11 = tk.Button(self, text=ButtonName[10], width=24,
                             command=lambda img=Image.open(Filename[10]): img.show())
        button12 = tk.Button(self, text=ButtonName[11], width=24,
                             command=lambda img=Image.open(Filename[11]): img.sow())
        button13 = tk.Button(self, text=ButtonName[12], width=24,
                             command=lambda img=Image.open(Filename[12]): img.show())
        button14 = tk.Button(self, text=ButtonName[13], width=24,
                             command=lambda img=Image.open(Filename[13]): img.show())
        button15 = tk.Button(self, text=ButtonName[14], width=24,
                             command=lambda img=Image.open(Filename[14]): img.show())
        button16 = tk.Button(self, text=ButtonName[15], width=24,
                             command=lambda img=Image.open(Filename[15]): img.show())
        button17 = tk.Button(self, text=ButtonName[16], width=24,
                             command=lambda img=Image.open(Filename[16]): img.show())
        button18 = tk.Button(self, text=ButtonName[17], width=24,
                             command=lambda img=Image.open(Filename[17]): img.show())
        button19 = tk.Button(self, text=ButtonName[18], width=24,
                             command=lambda img=Image.open(Filename[18]): img.show())
        button20 = tk.Button(self, text=ButtonName[19], width=24,
                             command=lambda img=Image.open(Filename[19]): img.show())
        button21 = tk.Button(self, text=ButtonName[20], width=24,
                             command=lambda img=Image.open(Filename[20]): img.show())
        button22 = tk.Button(self, text=ButtonName[21], width=24,
                             command=lambda img=Image.open(Filename[21]): img.show())
        button23 = tk.Button(self, text=ButtonName[22], width=24,
                             command=lambda img=Image.open(Filename[22]): img.show())
        button24 = tk.Button(self, text=ButtonName[23], width=24,
                             command=lambda img=Image.open(Filename[23]): img.show())
        button25 = tk.Button(self, text="Go to the First page", width=24,
                             command=lambda: controller.show_frame("StartPage"))



        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=3, column=0)
        button6.grid(row=3, column=1)
        button7.grid(row=4, column=0)
        button8.grid(row=4, column=1)
        button9.grid(row=5, column=0)
        button10.grid(row=5, column=1)
        button11.grid(row=6, column=0)
        button12.grid(row=6, column=1)
        button13.grid(row=7, column=0)
        button14.grid(row=7, column=1)
        button15.grid(row=8, column=0)
        button16.grid(row=8, column=1)
        button17.grid(row=9, column=0)
        button18.grid(row=9, column=1)
        button19.grid(row=10, column=0)
        button20.grid(row=10, column=1)
        button21.grid(row=11, column=0)
        button22.grid(row=11, column=1)
        button23.grid(row=12, column=0)
        button24.grid(row=12, column=1)
        button25.grid(row=13, column=0)

class CP913(tk.Frame):
    def __init__(self,parent, controller):

        ButtonName= [
            'Chapter 9 Problem 76',
            'Chapter 9 Problem 76 - Answer',
            'Chapter 9 Problem 78',
            'Chapter 9 Problem 78 - Answer',
            'Chapter 9 Problem 79',
            'Chapter 9 Problem 79 - Answer',
            'Chapter 9 Problem 107',
            'Chapter 9 Problem 107 - Answer',
            'Chapter 9 Problem 113',
            'Chapter 9 Problem 113 - Answer',
            'Chapter 9 Problem 127',
            'Chapter 9 Problem 127 - Answer',
            'Chapter 13 Problem 2',
            'Chapter 13 Problem 2 - Answer',
            'Chapter 13 Problem 3',
            'Chapter 13 Problem 3 - Answer',
            'Chapter 13 Problem 4',
            'Chapter 13 Problem 4 - Answer',
            'Chapter 13 Problem 8',
            'Chapter 13 Problem 8 - Answer',
            'Chapter 13 Problem 9',
            'Chapter 13 Problem 9 - Answer',
            'Chapter 13 Problem 30',
            'Chapter 13 Problem 30 - Answer'
        ]

        Filename = ['HMM\C9P76A.png',
                    'HMM\C9P76Q.png',
                    'HMM\C9P78A.png',
                    'HMM\C9P78Q.png',
                    'HMM\C9P79A.png',
                    'HMM\C9P79Q.png',
                    'HMM\C9P107A.png',
                    'HMM\C9P107Q.png',
                    'HMM\C9P113A.png',
                    'HMM\C9P113Q.png',
                    'HMM\C9P127A.png',
                    'HMM\C9P127Q.png',
                    'HMM\C13P2A.png',
                    'HMM\C13P2Q.png',
                    'HMM\C13P3A.png',
                    'HMM\C13P3Q.png',
                    'HMM\C13P4A.png',
                    'HMM\C13P4Q.png',
                    'HMM\C13P8A.png',
                    'HMM\C13P8Q.png',
                    'HMM\C13P9A.png',
                    'HMM\C13P9Q.png',
                    'HMM\C13P30A.png',
                    'HMM\C13P30Q.png'
                    ]


        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Assignment 8: Ch 9&13", font=controller.title_font)
        label.grid(row=0, column=0, sticky=E)

        button1 = tk.Button(self, text=ButtonName[0], width=24,
                            command=lambda img=Image.open(Filename[0]): img.show())
        button2 = tk.Button(self, text=ButtonName[1], width=24,
                            command=lambda img=Image.open(Filename[1]): img.show())
        button3 = tk.Button(self, text=ButtonName[2], width=24,
                            command=lambda img=Image.open(Filename[2]): img.show())
        button4 = tk.Button(self, text=ButtonName[3], width=24,
                            command=lambda img=Image.open(Filename[3]): img.show())
        button5 = tk.Button(self, text=ButtonName[4], width=24,
                            command=lambda img=Image.open(Filename[4]): img.show())
        button6 = tk.Button(self, text=ButtonName[5], width=24,
                            command=lambda img=Image.open(Filename[5]): img.show())
        button7 = tk.Button(self, text=ButtonName[6], width=24,
                            command=lambda img=Image.open(Filename[6]): img.show())
        button8 = tk.Button(self, text=ButtonName[7], width=24,
                            command=lambda img=Image.open(Filename[7]): img.show())
        button9 = tk.Button(self, text=ButtonName[8], width=24,
                            command=lambda img=Image.open(Filename[8]): img.show())
        button10 = tk.Button(self, text=ButtonName[9], width=24,
                             command=lambda img=Image.open(Filename[9]): img.show())
        button11 = tk.Button(self, text=ButtonName[10], width=24,
                             command=lambda img=Image.open(Filename[10]): img.show())
        button12 = tk.Button(self, text=ButtonName[11], width=24,
                             command=lambda img=Image.open(Filename[11]): img.sow())
        button13 = tk.Button(self, text=ButtonName[12], width=24,
                             command=lambda img=Image.open(Filename[12]): img.show())
        button14 = tk.Button(self, text=ButtonName[13], width=24,
                             command=lambda img=Image.open(Filename[13]): img.show())
        button15 = tk.Button(self, text=ButtonName[14], width=24,
                             command=lambda img=Image.open(Filename[14]): img.show())
        button16 = tk.Button(self, text=ButtonName[15], width=24,
                             command=lambda img=Image.open(Filename[15]): img.show())
        button17 = tk.Button(self, text=ButtonName[16], width=24,
                             command=lambda img=Image.open(Filename[16]): img.show())
        button18 = tk.Button(self, text=ButtonName[17], width=24,
                             command=lambda img=Image.open(Filename[17]): img.show())
        button19 = tk.Button(self, text=ButtonName[18], width=24,
                             command=lambda img=Image.open(Filename[18]): img.show())
        button20 = tk.Button(self, text=ButtonName[19], width=24,
                             command=lambda img=Image.open(Filename[19]): img.show())
        button21 = tk.Button(self, text=ButtonName[20], width=24,
                             command=lambda img=Image.open(Filename[20]): img.show())
        button22 = tk.Button(self, text=ButtonName[21], width=24,
                             command=lambda img=Image.open(Filename[21]): img.show())
        button23 = tk.Button(self, text=ButtonName[22], width=24,
                             command=lambda img=Image.open(Filename[22]): img.show())
        button24 = tk.Button(self, text=ButtonName[23], width=24,
                             command = lambda img=Image.open(Filename[23]): img.show())
        button25 = tk.Button(self, text="Go to the First page", width=24,
                             command=lambda: controller.show_frame("StartPage"))


        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=3, column=0)
        button6.grid(row=3, column=1)
        button7.grid(row=4, column=0)
        button8.grid(row=4, column=1)
        button9.grid(row=5, column=0)
        button10.grid(row=5, column=1)
        button11.grid(row=6, column=0)
        button12.grid(row=6, column=1)
        button13.grid(row=7, column=0)
        button14.grid(row=7, column=1)
        button15.grid(row=8, column=0)
        button16.grid(row=8, column=1)
        button17.grid(row=9, column=0)
        button18.grid(row=9, column=1)
        button19.grid(row=10, column=0)
        button20.grid(row=10, column=1)
        button21.grid(row=11, column=0)
        button22.grid(row=11, column=1)
        button23.grid(row=12, column=0)
        button24.grid(row=12, column=1)
        button25.grid(row=13, column=0)

class QQ(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Lib: Quizzes", font=controller.title_font)
        label.grid(row=0, column=0, sticky=N)

        button1 = tk.Button(self, text="Quiz 1", width=18,
                            command=lambda img=Image.open('HMM\QUIZ1.png'): img.show())
        button2 = tk.Button(self, text="Quiz 2", width=18,
                            command=lambda img =Image.open('HMM\QUIZ2.png'): img.show())
        button3 = tk.Button(self, text="Quiz 3", width=18,
                            command=lambda img=Image.open('HMM\QUIZ3.png'): img.show())
        button4 = tk.Button(self, text="Quiz 4", width=18,
                            command=lambda img=Image.open('HMM\QUIZ4.png'): img.show())
        button5 = tk.Button(self, text="Quiz 5", width=18,
                            command=lambda img=Image.open('HMM\QUIZ5.png'): img.show())
        button6 = tk.Button(self, text="Quiz 6", width=18,
                            command=lambda img=Image.open('HMM\QUIZ6.png'): img.show())
        button7 = tk.Button(self, text="Quiz 7", width=18,
                            command=lambda img=Image.open('HMM\QUIZ7.png'): img.show())
        button8 = tk.Button(self, text="Quiz 8", width=18,
                            command=lambda img=Image.open('HMM\QUIZ8.png'): img.show())
        button9 = tk.Button(self, text="Go to the start page", width=18,
                            command=lambda: controller.show_frame("StartPage"))

        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=3, column=0)
        button6.grid(row=3, column=1)
        button7.grid(row=4, column=0)
        button8.grid(row=4, column=1)
        button9.grid(row=5, column=0)

class ETM(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Lib: Exams", font=controller.title_font)
        label.grid(row=0, column=0, sticky=N)



        button1 = tk.Button(self, text="MidTerm 1", width=18,
                            command=lambda img=Image.open('HMM\MID1.png'): img.show())

        button2 = tk.Button(self, text="MidTerm 2", width=18,
                            command=lambda img =Image.open('HMM\MID2.png'): img.show())
        button3 = tk.Button(self, text="Old_MidTerm 1", width=18,
                            command=lambda img=Image.open('HMM\Old_MID1.png'): img.show())

        button4 = tk.Button(self, text="Old_MidTerm 2", width=18,
                            command=lambda img=Image.open('HMM\Old_MID2.png'): img.show())
        button5 = tk.Button(self, text="Old_Final", width=18,
                            command=lambda img=Image.open('HMM\Old_Final.png'): img.show())
        button6 = tk.Button(self, text="Go to the start page", width=18,
                            command=lambda: controller.show_frame("StartPage"))

        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=3, column=0)
        button6.grid(row=3, column=1)

class RC(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Related Links!", font=controller.title_font)
        label.grid(row=0, column=0, sticky=N)
        button1 = tk.Button(self, text="Professor Profile", width=18,
                            command=lambda: webbrowser.open_new('https://www.rider.edu/ridermagazine/spring-2015/people/faculty/dr-john-bochanski'))
        button2 = tk.Button(self, text="Spark Notes", width=18,
                            command=lambda: webbrowser.open_new('http://www.sparknotes.com/physics/'))
        button3 = tk.Button(self, text="Khan Academy", width=18,
                            command=lambda: webbrowser.open_new('https://www.khanacademy.org/science/physics'))
        button4 = tk.Button(self, text="Youtube - Yale", width=18,
                            command=lambda: webbrowser.open_new('https://www.youtube.com/watch?v=KOKnWaLiL8w&list=PL561F7ACE736068D5'))

        button5 = tk.Button(self, text="Go to the start page", width=18,
                            command=lambda: controller.show_frame("StartPage"))


        button1.grid(row=1, column=0)
        button2.grid(row=2, column=0)
        button3.grid(row=3, column=0)
        button4.grid(row=4, column=0)
        button5.grid(row=5, column=0)


class LTFun(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Here Have some Fun!", font=controller.title_font)
        label.grid(row=0, column=0, sticky=N)

        #Not submitting the game as it need more of work.
        button1 = tk.Button(self, text="Korean Double Rock Scissors Paper Game", width=50,
                            command=lambda: runpy.run_path('DoubleRCP2_Edited.pyc'))


        button1.grid(row = 1, column = 0)
        button2 = tk.Button(self, text="Go to the start page", width=50,
                            command=lambda: controller.show_frame("StartPage"))
        button2.grid(row=2, column=0)





root = Tk()
lf = LoginFrame(root)
root.mainloop()
