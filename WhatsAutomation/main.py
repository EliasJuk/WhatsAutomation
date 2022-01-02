import os
from tkinter import *

class Aplication:
  def __init__(self):
    self.root = Tk()
    self.palette()
    self.window()
    self.frames()
    self.labels()
    self.textbox()
    self.buttons()
    self.checkbox()
    self.automation()
    self.root.mainloop()

  def palette(self):
    self.text_color     = '#D9D9D9' 
    self.textbox_color  = '#d4d4d4'
    self.buttons_color  = '#d4d4d4'
    self.checkbox_color = '#d4d4d4'
    self.label_color    = '#45475b'
    self.frame_color    = '#45475b'
    self.bg_color       = '#282934'
      
  def window(self):
    self.root.title("WhatsAutomation")
    self.root.geometry("400x600")
    self.root.resizable(True, True)
    self.root.maxsize(width=600, height=800)
    self.root.minsize(width=300, height=500)
    self.root.configure(background=self.bg_color)

  def frames(self):
    # TEXTBOX
    self.frame_1 = Frame(self.root, bg=self.frame_color)
    self.frame_1.place(relx=.02, rely=.02, relwidth=.96, relheight=.4)

    # CHECKBOX | BOTÃO OPEN FILE
    self.frame_2 = Frame(self.root, bg=self.frame_color)
    self.frame_2.place(relx=.02, rely=.45, relwidth=.96, relheight=.1)

    # IMG
    self.frame_3 = Frame(self.root, bg=self.frame_color)
    self.frame_3.place(relx=.02, rely=.58, relwidth=.96, relheight=.4)

  def labels(self):
    self.label_1 = Label(self.frame_1, text='Mensagem a ser enviada:', bg=self.label_color, fg=self.text_color)
    self.label_1.place(relx=.3, rely=.03)

  def textbox(self):
    self.textbox_1 = Text(self.frame_1, height=9, width=37, bg=self.textbox_color, pady=10, padx=10, font='sans-serif')
    self.textbox_1.place(relx=.04, rely=.16, relwidth=.92, relheight=.74)

  def buttons(self):
    self.button_1 = Button(self.frame_2, text='Open file', bg=self.buttons_color)
    self.button_1.place(relx=.26, rely=.3, relwidth=.2, relheight=.4)

  def checkbox(self):
    self.checkbox_1 = Checkbutton(self.frame_2, text='Imagem', bg=self.checkbox_color, onvalue=1, offvalue=0)
    self.checkbox_1.place(relx=.50, rely=.3, relheight=.4)

  def automation(self):
    self.root_path = os.getcwd()


if __name__ == '__main__':
  app = Aplication()