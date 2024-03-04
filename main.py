import customtkinter
import tkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Траслитерация текста')
        self.geometry('500x400')
        self.resizable(False, False)

        self.in_label = customtkinter.CTkLabel(self, width=50, height=20, text='Ввод:')
        self.in_label.place(x=10,y=10)
        self.input_text = customtkinter.CTkTextbox(self, width=300, height=150)
        self.input_text.place(x=10,y=30)

        self.out_label = customtkinter.CTkLabel(self, width=50, height=20, text='Вывод:')
        self.out_label.place(x=10,y=210)
        self.output_text = customtkinter.CTkTextbox(self, width=300, height=150)
        self.output_text.place(x=10,y=230)

        self.button_transl = customtkinter.CTkButton(self, width=100, height=30, text='Траслитерация', command=self.transliterate)
        self.button_transl.place(x=350,y=150)

        self.symbol_var = tkinter.BooleanVar()
        self.symbol_var.set(False)
        customtkinter.CTkLabel(self, text='Специальные символы: ').place(x=350, y=400)
        customtkinter.CTkRadioButton(self, text='En => Ru', variable=self.symbol_var, value=False).place(x=350, y=50)
        customtkinter.CTkRadioButton(self, text='Ru => En', variable=self.symbol_var, value=True).place(x=350, y=80)

    def transliterate(self):
        
        self.output_text.delete(0.0, tkinter.END)

        dict = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
        'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
        'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
        'ц':'c','ч':'cz','ш':'sh','щ':'scz','ъ':'','ы':'y','ь':'','э':'e',
        'ю':'u','я':'ja', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E',
        'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
        'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
        'Ц':'C','Ч':'CZ','Ш':'SH','Щ':'SCH','Ъ':'"','Ы':'y','Ь':"'",'Э':'E',
        'Ю':'U','Я':'YA', ' ':' ', '\n':' '}

        dict_reverse = {'a':'а','b':'б','v':'в','g':'г','d':'д','e':'е','e':'ё',
        'zh':'ж','z':'з','i':'и','k':'к','l':'л','m':'м','n':'н',
        'o':'о','p':'п','r':'р','s':'с','t':'т','u':'у','f':'ф','h':'х',
        'c':'ц','cz':'ч','sh':'ш','scz':'щ','y':'ы','e':'э','ja':'я', 
        'A':'А','B':'Б','V':'В','G':'Г','D':'Д','E':'Е','E':'Ё',
        'ZH':'Ж','Z':'З','I':'И','I':'Й','K':'К','L':'Л','M':'М','N':'Н',
        'O':'О','P':'П','R':'Р','S':'С','T':'Т','U':'У','F':'Ф','H':'Х',
        'C':'Ц','CZ':'Ч','SH':'Ш','SCH':'Щ','Y':'Ы','E':'Э','JA':'Я', '"':'ъ',"'":'ь',
        '':'э','u':'ю','ya':'я',' ':' ', '\n':' '}
        
        if self.symbol_var.get():
            text = self.input_text.get('0.0', 'end')
            for i in text:
                text = text.replace(i, dict[i])
            self.output_text.insert(tkinter.END, text)
            
        else:
            text = self.input_text.get('0.0', 'end')
            for i in text:
                text = text.replace(i, dict_reverse[i])
            self.output_text.insert(tkinter.END, text)
        

if __name__ == '__main__':
    app = App()
    app.mainloop()