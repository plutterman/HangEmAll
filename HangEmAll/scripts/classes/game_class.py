"""
Payton Lutterman and Karma Chandia
HangEmAll
Last Updated 10-6

"""

from scripts.settings import *
from scripts.classes.display_class import *

class Game():
    def __init__(self):
        self.root = self.setup_root()
        self.load_data = self.load_data()
        self.pg = pg
        self.sfx_list = []
        self.load_sfx()
        self.word = ""
        self.word_sofar = "?"*len(self.word)
        self.guess = ""
        self.hint = ""
        self.trys = -1
        self.picked_letter = ""
        self.diff = "Easy"
        self.word_lbl_list = []
        self.load_images()
        self.create_widgets()
        self.setup_game()
        self.pg.mixer.music.play(loops=-1)



    def setup_game(self, trash=None):
        self.diff_select.config(state=NORMAL)
        for bttn in self.button_list:
            bttn.config(state=NORMAL)
        self.guess = ""
        self.trys = -2
        self.picked_letter = ""
        self.diff = self.diff_select.get()
        self.update_display()

        if self.diff == "Easy":
            num = random.randint(0,len(self.easy_words)-1)
            self.word = self.easy_words[num]
            self.hint = self.easy_hints[num]
        elif self.diff == "Medium":
            num = random.randint(0, len(self.med_words) - 1)
            self.word = self.med_words[num]
            self.hint = self.med_hints[num]
        else:
            num = random.randint(0, len(self.hard_words) - 1)
            self.word = self.hard_words[num]
            self.hint = self.hard_hints[num]
        self.word_sofar = "?" * len(self.word)
        self.hint_lbl.config(text = self.hint)
        self.update_word_lbl()
        self.update_display()

    def load_data(self):
        try:
            file = open("assets/text/wordbank.txt","r")
        except:
            messagebox.showerror("No","Could Not Load Word Bank")
        temp_list = file.readlines()
        file.close()
        clean_list = []
        for e in temp_list:
            clean_list.append(e.strip("\n"))
        word_list = []
        hint_list = []
        for i in clean_list:
            word,hint = i.split(":",2)
            word_list.append(word)
            hint_list.append(hint)
        self.hard_words = []
        self.hard_hints = []
        self.med_words = []
        self.med_hints = []
        self.easy_words = []
        self.easy_hints = []
        for i in range(len(word_list)):
            if len(word_list[i]) <=4:
                self.easy_words.append(word_list[i])
                self.easy_hints.append(hint_list[i])
            elif len(word_list[i]) <=8:
                self.med_words.append(word_list[i])
                self.med_hints.append(hint_list[i])
            else:
                self.hard_words.append(word_list[i])
                self.hard_hints.append(hint_list[i])


    def update_display(self):
        self.trys +=1
        self.display.config(image=self.img_list[self.trys])

    def update_word_lbl(self):
        for lbl in self.word_lbl_list:
            lbl.destroy()
        self.word_lbl_list = []
        col = 0
        for letter in self.word_sofar:
            x = Label(self.letter_display,text=letter)
            x.pack(side=LEFT)
            col +=1
            self.word_lbl_list.append(x)

    def load_sfx(self):
        paths = ["assets/sfx/background-music.mp3",
                 "assets/sfx/right-answer.mp3",
                 "assets/sfx/wrong-answer.wav"]
        for name in paths:
            self.sfx_list.append(pg.mixer.Sound(name))
        self.pg.mixer.music.load("assets/sfx/background-music.mp3")

    def load_images(self):
        self.img_list = []
        for i in range(11):
            self.img_list.append(PhotoImage(file=str.format("assets/img/{}.png", i+1)))

    def create_widgets(self):
        frame_font = font.Font(family="Poor Richard",size=20,weight="bold")
        self.window = Frame(self.root,width=WIDTH,height=HEIGHT, background="violetred4")
        self.diff_select = ttk.Combobox(self.window, values=["Easy", "Medium","Hard"], font=frame_font)
        self.diff_select.current(0)
        self.diff_select.bind("<<ComboboxSelected>>", self.setup_game)
        self.display = Label(self.window,image=self.img_list[0],justify=CENTER)
        self.hint_lbl = Label(self.window,text = "hint",font=frame_font)
        self.letter_display = Frame(self.window)
        col = 0
        for letter in self.word_sofar:
            x = Label(self.letter_display,text=letter)
            x.pack(side=LEFT)
            col +=1
            self.word_lbl_list.append(x)
        self.word_entry = Entry(self.window)
        self.guess_bttn = Button(self.window,text="Guess Word",command = self.guess_word)
        self.bttn_frame = Frame(self.window)
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.button_list = []
        col = 0
        row = 0
        index = 0
        for l in self.letters:
            x=Button(self.bttn_frame, text=l,
                   command = lambda id= index:self.guess_letter(id))
            x.grid(row=row,column=col,padx=5,pady=5,ipadx=5,ipady=5)
            self.button_list.append(x)
            index += 1
            col += 1
            if col > 12:
                row += 1
                col = 0

        # Place Widgets

        # Row 0
        self.diff_select.grid(row=0, column=0, columnspan=3, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)

        # Row 1
        self.display.grid(row=1, column=0, columnspan=3, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)

        # Row 2
        self.hint_lbl.grid(row=2, column=0, columnspan=3, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)

        # Row 3
        self.letter_display.grid(row=3, column=0, columnspan=3, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)

        # Row 4
        self.word_entry.grid(row=4, column=0, columnspan=2, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)
        self.guess_bttn.grid(row=4, column=2, columnspan=1, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)

        # Row 5
        self.bttn_frame.grid(row=5, column=0, columnspan=3, sticky=NSEW, padx=5, pady=5, ipadx=5, ipady=5)

        self.window.pack()

    def guess_letter (self, id = None):
        self.diff_select.config(state=DISABLED)
        if id != None:
            x = self.letters[id]
            self.button_list[id].config(state=DISABLED)

            self.guess = self.letters[id]
        temp = ""
        if self.guess.upper() in self.word.upper():
            pg.mixer.Sound.play(self.sfx_list[1])
            for i in range(len(self.word)):
                if self.guess.upper() == self.word[i].upper():
                    temp += self.word[i]
                else:
                    temp += self.word_sofar[i]
            self.word_sofar = temp
            self.update_word_lbl()
        else:
            pg.mixer.Sound.play(self.sfx_list[2])
            if self.trys < len(self.img_list)-1:
                self.update_display()
            else:
                answer = messagebox.askyesno("Game Over","Play Again")
                if answer:
                    # Call Game Setup
                    pass
                else:
                    self.root.destroy()

        if self.word == self.word_sofar:
            answer = messagebox.askyesno("U Won Dawg", "Play Again")
            if answer:
                # Call Game Setup
                self.setup_game()
            else:
                self.root.destroy()

    def guess_word(self):
        guess_word = self.word_entry.get()
        if guess_word == self.word:
            pg.mixer.Sound.play(self.sfx_list[1])
            self.word_sofar = guess_word
        else:
            self.guess = "~"
            pg.mixer.Sound.play(self.sfx_list[2])
            self.trys = len(self.img_list)-1
        self.guess_letter()

    def setup_root(self):
        root = Tk()
        root.geometry(geoString)
        root.title(TITLE)
        root.iconbitmap(icon_path)
        root.resizable(0,0)

        return root

    def play(self):
        self.root.mainloop()