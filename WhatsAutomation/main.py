import os
from tkinter import *
from tkinter import ttk
import PIL
from PIL import ImageTk, Image
from tkinter import filedialog
import time

class Aplication:
  def __init__(self):
    self.root = Tk()

    #FUNÇÕES
    self.vars()
    self.palette()
    
    # COMPONENTES
    self.window()
    self.frames()
    self.labels()
    self.textbox()
    self.buttons()
    self.checkbox()
    self.panel()
    self.progressbar()
    self.automation()
    self.root.mainloop()

  def vars(self):
    # PATH
    self.root_path = os.getcwd()

    # GLOBAL
    self.var_ckb1 = IntVar()
    
    # SET IMAGE DEFAUT
    self.image_path = Image.open('midia.png')
    self.imagem_defaut = ImageTk.PhotoImage(self.image_path)

  def palette(self):
    self.text_color     = '#D9D9D9'
    self.textbox_color  = '#d4d4d4'
    self.buttons_color  = '#d4d4d4'
    self.checkbox_color = '#45475b'
    self.label_color    = '#45475b'
    self.frame_color    = '#45475b'
    self.bg_color       = '#282934'
      
  def window(self):
    self.root.title("WhatsAutomation")
    self.root.geometry("400x680")
    self.root.resizable(True, True)
    self.root.maxsize(width=600, height=800)
    self.root.minsize(width=300, height=500)
    self.root.configure(background=self.bg_color)

  def frames(self):
    # TEXTBOX
    self.frame_1 = Frame(self.root, bg=self.frame_color)
    self.frame_1.place(relx=.02, rely=.02, relwidth=.96, relheight=.38)

    # CHECKBOX | BOTÃO OPEN FILE
    self.frame_2 = Frame(self.root, bg=self.frame_color)
    self.frame_2.place(relx=.02, rely=.41, relwidth=.96, relheight=.06)

    # IMG
    self.frame_3 = Frame(self.root, bg=self.frame_color)
    self.frame_3.place(relx=.02, rely=.482, relwidth=.96, relheight=.35)

    # SEND IMAGE
    self.frame_4 = Frame(self.root, bg=self.frame_color)
    self.frame_4.place(relx=.02, rely=.845, relwidth=.96, relheight=.14)

  def labels(self):
    self.label_1 = Label(self.frame_1, text='Mensagem a ser enviada:', bg=self.label_color, fg=self.text_color)
    self.label_1.place(relx=.3, rely=.03)

  def textbox(self):
    self.textbox_1 = Text(self.frame_1, height=9, width=37, bg=self.textbox_color, pady=10, padx=10, font='sans-serif')
    self.textbox_1.place(relx=.04, rely=.14, relwidth=.92, relheight=.80)

  def buttons(self):
    self.button_1 = Button(self.frame_2, text='Open file', command=self.file_open, bg=self.buttons_color, state=DISABLED)
    self.button_1.place(relx=.26, rely=.16, relwidth=.2, relheight=.7)

    self.button_2 = Button(self.frame_4, text='ENVIAR')
    self.button_2.place(relx=.335, rely=.12, relwidth=.3, relheight=.3)

  def checkbox(self):
    self.checkbox_1 = Checkbutton(self.frame_2, text='Imagem',onvalue=1, offvalue=0, variable=self.var_ckb1, command=self.func_checkbox1, bg=self.checkbox_color, activebackground=self.checkbox_color, activeforeground=self.text_color)
    self.checkbox_1['fg'] = '#D9D9D9'
    self.checkbox_1.place(relx=.50, rely=.16, relheight=.7)

  def panel(self):
    self.panel_1 = Label(self.frame_3, image=self.imagem_defaut, bg='#45475b', state= DISABLED, width=200, height=200)
    self.panel_1.place(relx=.24, rely=.08, relwidth=.5, relheight=.84)

  def progressbar(self):
    self.progressbar_1 = ttk.Progressbar(self.frame_4, orient=HORIZONTAL, length=300, mode='determinate')
    self.progressbar_1.place(relx=.1, rely=.6)


  def func_checkbox1(self):
    if (self.var_ckb1.get() == 1):
      self.button_1.config(state=NORMAL)
      self.panel_1.config(state=NORMAL)
      self.checkbox_1.configure(selectcolor="green")
    elif (self.var_ckb1.get() == 0):
      self.button_1.config(state=DISABLED)
      self.panel_1.config(state=DISABLED)
      self.checkbox_1.configure(selectcolor="#D9D9D9")
    else:
      print('Valor Invalido')


  def file_open(self):
    try:
      path=filedialog.askopenfilename(initialdir='C://')
      self.new_image = ImageTk.PhotoImage(Image.open(path))
      self.panel_1.configure(image=self.new_image)      
    except AttributeError:
      print('Selecione uma imagem')
    except PIL.UnidentifiedImageError:
      print('Formato invalido')


  def automation(self):
    pass    


if __name__ == '__main__':
  app = Aplication()