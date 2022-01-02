import os
from tkinter import *

class Aplication:
  def __init__(self):
    self.root = Tk()
    self.window()
    self.frames()
    self.automation()
    self.root.mainloop()
  
  def window(self):
    self.root.title("WhatsAutomation")
    self.root.geometry("400x600")
    self.root.resizable(True, True)
    self.root.maxsize(width=600, height=800)
    self.root.minsize(width=300, height=500)
    self.root.configure(background="#282934")

  def frames(self):
    # TEXTBOX
    self.frame_1 = Frame(self.root, bg='#45475b')
    self.frame_1.place(relx=.02, rely=.02, relwidth=.96, relheight=.4)

    # CHECKBOX | BOTÃO OPEN FILE
    self.frame_2 = Frame(self.root, bg='#45475b')
    self.frame_2.place(relx=.02, rely=.45, relwidth=.96, relheight=.1)

    # IMG
    self.frame_3 = Frame(self.root, bg='#45475b')
    self.frame_3.place(relx=.02, rely=.58, relwidth=.96, relheight=.4)

  def automation(self):
    self.root_path = os.getcwd()


if __name__ == '__main__':
  app = Aplication()