import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, font
from PIL import Image, ImageTk
from numpy import random

class View(object):

    def __init__(self, data):
        self.data = data
        self.trans_hide = 0
    
    def get_sentence(self):
        row_num = len(self.data)
        selection = random.randint(row_num)
        french_sentence = self.data.loc[selection][1]
        translation = self.data.loc[selection][2]
        return [french_sentence, translation]

    def mainpage(self):

        window = Tk()
        sentences = self.get_sentence()
        french_sentence = tk.StringVar()
        french_sentence.set(sentences[0])
        translation = tk.StringVar()
        translation.set(sentences[1])
        
        canvas = Canvas(
            window,
            bg = "#F1E7E5",
            height = 100,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        # Move the window
        def MouseDown(event):
            global mousX
            global mousY

            mousX = event.x
            mousY = event.y
        
        def MouseMove(event):
            window.geometry(f'+{event.x_root - mousX}+{event.y_root - mousY}')
        
        # Button functions
        def translation_clicked():
            if self.trans_hide == 0:
                print('HIDE THE TRANSLATION')
                label_translation.forget()
                self.trans_hide = 1
            else:
                print('SHOW THE TRANSLATION!')
                label_translation.pack()
                self.trans_hide = 0

        def close_clicked():
            print('DESTROY THE WINDOW!')
            window.destroy()

        def next_clicked():
            sentences = self.get_sentence()
            french_sentence.set(sentences[0])
            translation.set(sentences[1])
            print('NEXT SENTENCE!')

        # Elements of the main window
        title_image_1 = Image.open("D:/Hongyang/ESSEC_CS/Python/final_project/GUI/assets/title_1.jpg")
        title_image_1 = title_image_1.resize((250, 50))
        title_image_1 = ImageTk.PhotoImage(title_image_1)
        
        button_title = Button(
            image = title_image_1,
            borderwidth = 0,
            highlightthickness = 0,
            # command = lambda : translation_clicked(),
            relief = "flat"
        )

        button_title.place(
            x = 5,
            y = 5
        )

        # Title
        line_image_1 = Image.open("D:/Hongyang/ESSEC_CS/Python/final_project/GUI/assets/line_1.jpg")
        line_image_1 = line_image_1.resize((685, 6))
        line_image_1 = ImageTk.PhotoImage(line_image_1)
        label_line_1 = Label(window, image = line_image_1)
        label_line_1.place(
            x = 15,
            y = 60
        )

        # Sentence
        label_sentence = Label(window, textvariable = french_sentence, font = ('Arial Black', 10, 'italic'), bg = '#F1E7E5')
        label_sentence.place(
            x = 30,
            y = 40
        )

        # Translation
        label_translation = Label(window, textvariable = translation, font = ('Arial Black', 10, 'italic'), bg = '#F1E7E5')
        label_translation.place(
            x = 120,
            y = 72
        )

        # Translation button
        button_image_1 = Image.open("D:/Hongyang/ESSEC_CS/Python/final_project/GUI/assets/button_1.png")
        button_image_1 = button_image_1.resize((100, 28))
        button_image_1 = ImageTk.PhotoImage(button_image_1)

        button_1 = Button(
            image = button_image_1,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda : translation_clicked(),
            relief = "flat"
        )

        button_1.place(
            x = 10,
            y = 72,
        )

        # Close Button
        button_image_2 = Image.open("D:/Hongyang/ESSEC_CS/Python/final_project/GUI/assets/close_button.jpg")
        button_image_2 = button_image_2.resize((30, 30))
        button_image_2 = ImageTk.PhotoImage(button_image_2)

        button_2 = Button(
            image = button_image_2,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda : close_clicked(),
            relief = "flat"
        )

        button_2.place(
            x = 705,
            y = 5,
        )

        # Next Button
        button_image_3 = Image.open("D:/Hongyang/ESSEC_CS/Python/final_project/GUI/assets/next_button.png")
        button_image_3 = button_image_3.resize((30, 30))
        button_image_3 = ImageTk.PhotoImage(button_image_3)

        button_3 = Button(
            image = button_image_3,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda : next_clicked(),
            relief = "flat"
        )

        button_3.place(
            x = 705,
            y = 65,
        )

        window.title("EverydayFrench")
        window.geometry("740x100+600+400")
        window.configure(bg = "#F1E7E5")
        window.overrideredirect(True)
        window.bind("<Button-1>", MouseDown)
        window.bind("<B1-Motion>", MouseMove)
        window.attributes('-alpha', 0.8)
        window.resizable(False, False)

        window.mainloop()
