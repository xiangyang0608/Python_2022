from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from PIL import Image, ImageTk

def MAINPAGE():

    window = Tk()

    canvas = Canvas(
        window,
        bg = "#F1E7E5",
        height = 100,
        width = 740,
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
        print('HEY!!!')

    def close_cliked():
        window.destroy()

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

    line_image_1 = Image.open("D:/Hongyang/ESSEC_CS/Python/final_project/GUI/assets/line_1.jpg")
    line_image_1 = line_image_1.resize((720, 6))
    line_image_1 = ImageTk.PhotoImage(line_image_1)
    label_line_1 = Label(window, image = line_image_1)
    label_line_1.place(
        x = 15,
        y = 65
    )

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

    button_image_2 = Image.open("D:/Hongyang/ESSEC_CS/Python/final_project/GUI/assets/close_button.jpg")
    button_image_2 = button_image_2.resize((30, 30))
    button_image_2 = ImageTk.PhotoImage(button_image_2)

    button_2 = Button(
        image = button_image_2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : close_cliked(),
        relief = "flat"
    )

    button_2.place(
        x = 705,
        y = 5,
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

MAINPAGE()
