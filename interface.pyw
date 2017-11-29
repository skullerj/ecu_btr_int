# -*- coding: latin-1 -*-
import Tkinter as tk
import tkFont  as tkfont
import control

servo = control.ServoMove()

class SampleApp(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.attributes('-fullscreen',True)
        self.resizable(width=False, height=False)
        self.title_font = tkfont.Font(family='Helvetica', size=18)
        self.button_font = tkfont.Font(family='Helvetica', size=14)
        self.number_button_font = tkfont.Font(family='Helvetica', size=18)
        self.input_font = tkfont.Font(family='Helvetica', size=16)
        self.id = tk.StringVar()
        container = tk.Frame(self)
        container.pack(anchor='center', fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, DigitPage, ControlPage, FinalPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Bienvenido!", font=controller.title_font)
        label.place(x=50,y=100,anchor='nw')
        button1 = tk.Button(self, text="Iniciar",
                            command=lambda: controller.show_frame("DigitPage"),
                            width=10,
                            font=controller.button_font)
        button1.place(x=50,y=150)


class DigitPage(tk.Frame):



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.message=tk.StringVar()

        label = tk.Label(self, text="Ingresa tu cedula", font=controller.button_font)
        label.grid(columnspan=3,row=0,pady=10)
        messageLabel = tk.Label(self, textvariable=self.message,fg='#D50000')
        messageLabel.grid(columnspan=3,row=1)
        id = self.controller.id
        entry = tk.Entry(self,textvariable=id,justify='center',state='readonly')
        entry.grid(columnspan=2,row=2,sticky='wens')
        delButton=tk.Button(self,text='<-',height=1,command=lambda:id.set(id.get()[:-1]))
        delButton.grid(row=2,column=2)
        # Add buttons from 0 to 9
        button0=tk.Button(self,text='0',font=controller.number_button_font,height=1,command=lambda:id.set(id.get()+'0'))
        button0.grid(row=6,column=1,sticky='wens')
        button1=tk.Button(self,text='1',font=controller.number_button_font,height=1,command=lambda:id.set(id.get()+'1'))
        button1.grid(row=3,column=0,sticky='wens')
        button2=tk.Button(self,text='2',font=controller.number_button_font,height=1,command=lambda:id.set(id.get()+'2'))
        button2.grid(row=3,column=1,sticky='wens')
        button3=tk.Button(self,text='3',font=controller.number_button_font,height=1,command=lambda:id.set(id.get()+'3'))
        button3.grid(row=3,column=2,sticky='wens')
        button4=tk.Button(self,text='4',font=controller.number_button_font,height=1,command=lambda:id.set(id.get()+'4'))
        button4.grid(row=4,column=0,sticky='wens')
        button5=tk.Button(self,text='5',font=controller.number_button_font,height=1,command=lambda:id.set(id.get()+'5'))
        button5.grid(row=4,column=1,sticky='wens')
        button6=tk.Button(self,text='6',font=controller.number_button_font,height=1,command=lambda:id.set(id.get()+'6'))
        button6.grid(row=4,column=2,sticky='wens')
        button7=tk.Button(self,text='7',font=controller.number_button_font,height=1,command=lambda:id.set(id.get()+'7'))
        button7.grid(row=5,column=0,sticky='wens')
        button8=tk.Button(self,text='8',font=controller.number_button_font,height=1,command=lambda:id.set(id.get()+'8'))
        button8.grid(row=5,column=1,sticky='wens')
        button9=tk.Button(self,text='9',font=controller.number_button_font,height=1,command=lambda:id.set(id.get()+'9'))
        button9.grid(row=5,column=2,sticky='wens')
        clear=tk.Button(self,text='Borrar',height=1,command=lambda:id.set(''))
        clear.grid(row=6,column=0)
        continueBut=tk.Button(self,text='Continuar',font=controller.button_font,command=self.nextPage)
        continueBut.grid(row=7,columnspan=3,rowspan=2,sticky='wens')
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=3)
        self.grid_rowconfigure(3, weight=3)
        self.grid_rowconfigure(4, weight=3)
        self.grid_rowconfigure(5, weight=3)
        self.grid_rowconfigure(6, weight=2)
        self.grid_rowconfigure(7, weight=2)
        self.grid_rowconfigure(7, weight=2)
        self.columnconfigure(0, minsize=75)
        self.columnconfigure(1, minsize=75)
        self.columnconfigure(2, minsize=75)

    def nextPage(self):
        #validar que la cedula sea correcta
        if(len(self.controller.id.get())<10):
            return self.showError()
        else:
            self.controller.show_frame("ControlPage")


    def showError(self):

        self.message.set('Cedula invalida')


class ControlPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.value = tk.StringVar()
        self.value.set('0')
        self.statusMessage = tk.StringVar()
        self.statusLabel = tk.Label(self,textvariable=self.statusMessage);
        self.statusLabel.grid(columnspan=3,row=1,pady=10,sticky='wens')

        idLabel = tk.Label(self, textvariable=self.controller.id, font=controller.title_font)
        idLabel.grid(columnspan=3,row=0,column=0,pady=10,sticky='wens')
        scanButton = tk.Button(self, text="Escanear",
                           command=self.predict)
        scanButton.grid(columnspan=3,row=2,pady=10,sticky='wens')

        totalLabel = tk.Label(self,text='Total: $',font=controller.title_font,pady=10)
        totalLabel.grid(column=0,row=3,rowspan=2)
        totalValueLabel = tk.Label(self,textvariable=self.value,font=controller.title_font,pady=10)
        totalValueLabel.grid(column=1,row=3,columnspan=2,rowspan=2)

        backButton = tk.Button(self, text="Atrás",command=self.back)
        backButton.grid(column=0,row=5)
        finishButton = tk.Button(self, text="Finalizar",command=self.finish)
        finishButton.grid(column=2,row=5)

    def predict(self):
		self.showSuccess('Escanenando...')
        self.controller.update()
		result,value = control.request_validation(self.controller.id.get())
		if(result):
			newTotal = float(self.value.get())+value
			self.value.set("{0:.2f}".format(round(newTotal,2)))
			self.showSuccess('Botella recibida!')
			servo.accept()
		else:
			self.showError('No reconocemos tu botella :(')
			servo.reject()

    def showSuccess(self,message):
        self.statusLabel.config(fg='#00C853')
        self.statusMessage.set(message)

    def showError(self,message):
        self.statusLabel.config(fg='#D50000')
        self.statusMessage.set(message)

    def finish(self):
        self.controller.id.set('')
        self.statusMessage.set('')
        self.value.set('0')
        self.controller.show_frame('FinalPage')

    def back(self):
        self.statusMessage.set('')
        self.value.set('0')
        self.controller.show_frame('DigitPage')

class FinalPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        label = tk.Label(self, text="Felicidades y Gracias por ayudar a tu planeta :)", font=controller.title_font,wraplength=200)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Regresar al Inicio",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()
