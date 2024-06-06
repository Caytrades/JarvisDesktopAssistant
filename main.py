from customtkinter import *
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
import warnings
# import pyautogui as pag
# from voice import speechRecognition, text_to_speech

warnings.simplefilter("ignore")

root = CTk()
root.title("JARVIS")
root.attributes('-fullscreen',True)
root.state('zoomed')
root.resizable(width=False,height=False)
frame = CTkFrame(master=root, fg_color='black', corner_radius=0)
frame.pack(fill=BOTH, expand=True)

# --------------------------------------------------------------------- #

def closeApp():

    x = messagebox.askokcancel(title='Closing Jarvis', message='This will close jarvis. Do you want to close it?')
    if x:
        root.destroy()
    else:
        pass


def micOnOff():

    if micButton.cget('image') == micImg:
        micButton.configure(image=micOffImg)
    elif micButton.cget('image') == micOffImg:
        micButton.configure(image=micImg)
    else:
        print('unknown mic image error!')

# --------------------------------------------------------------------- #

labelFrame = CTkFrame(master=frame, fg_color='black', corner_radius=0, height=80)
labelFrame.pack(fill=X)
CTkLabel(master=labelFrame, text='J.A.R.V.I.S', font=('Eavm', 50), text_color='azure3').pack(side=BOTTOM)

micImg = CTkImage(light_image=Image.open(r'assets/micIconOn.png'), size=(60,60))
micOffImg = CTkImage(light_image=Image.open(r'assets/micIconOff.png'), size=(60,60))
deleteImg = CTkImage(light_image=Image.open(r'assets/delbutton.png'), size=(10,10))
chatLog = CTkImage(light_image=Image.open(r'assets/chatLogPink.png'), size=(500,600)) # 550, 650

micButton = CTkButton(master=frame, width=30, height=60, corner_radius=10, fg_color='black', text='', image=micImg, border_width=0, hover=True, hover_color="gray", command=micOnOff)
micButton.pack(side=BOTTOM, pady=40)

delButton = CTkButton(master=labelFrame, width=20, height=20, corner_radius=0, fg_color='black', text='', image=deleteImg, border_width=2, hover=True, hover_color="gray", border_color="black", command=closeApp)
delButton.pack(side=TOP, anchor=E)

chatlogFrame = CTkFrame(master=frame, fg_color='black', corner_radius=0, width=600, height=800)
chatlogFrame.pack(side=LEFT, padx=20, pady=20)

chatlogLabel = CTkLabel(master=chatlogFrame, corner_radius=0, image=chatLog, text='')

# def createJarUserLabels():

#     xAxisDefault = 120
#     jar_yAxisDefault = 70
#     user_yAxisDefault = 100
#     label_gap = 30  # Adjust the vertical gap between labels if needed

#     for i in range(8):
#         CTkLabel(master=chatlogFrame, text='Jarvis : ', text_color="white", font=('Arial', 15)).place(x=xAxisDefault, y=jar_yAxisDefault)
#         CTkLabel(master=chatlogFrame, text='User : ', text_color="white", font=('Arial', 15)).place(x=xAxisDefault, y=user_yAxisDefault)

#         jar_yAxisDefault += label_gap * 2
#         user_yAxisDefault += label_gap * 2

# createJarUserLabels()
CTkLabel(master=chatlogFrame, text='Jarvis : ', text_color="white", font=('Arial', 15)).place(x=120, y=30)
CTkLabel(master=chatlogFrame, text='User : ', text_color="white", font=('Arial', 15)).place(x=120, y=60)
chatlogLabel.pack()


# --------------------------------------------------------------------- #

def update_frame(index):
    global gif_frames
    global gif_label
    gif_label.configure(image=gif_frames[index])
    root.after(40, update_frame, (index + 1) % len(gif_frames))

gif_path = r'assets/ui6.gif' #ui, ui2, ui6, ui7
gif_image = Image.open(gif_path)
gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif_image)]

gif_label = CTkLabel(master=frame, corner_radius=0, text='')
gif_label.pack()

# --------------------------------------------------------------------- #

update_frame(0)

root.mainloop()