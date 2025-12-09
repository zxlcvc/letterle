import customtkinter as ctk, mss, pytesseract, random
from PIL import Image, ImageFilter, ImageTk
from collections import Counter

#pytesseract.pytesseract.tesseract_cmd = r'IGNORE\\IGNORE\\USER'

class LetterLe:
    def __init__(self):
        self.win = ctk.CTk()
        self.win.title("LetterLe")
        self.win.geometry("450x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.words = set()
        try:
            f = open('words.txt','r',encoding='utf-8')
            for w in f:
                w = w.strip().lower()
                if len(w)>2: self.words.add(w)
            f.close()
        except: pass

     
        self.bg_frame = ctk.CTkFrame(self.win, fg_color="#1e1e1e", corner_radius=15)
        self.bg_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.lbl = ctk.CTkLabel(self.bg_frame, text="LetterLe", font=("Segoe UI",24,"bold"), text_color="#FF5555")
        self.lbl.pack(pady=15)

        self.entry = ctk.CTkEntry(self.bg_frame, placeholder_text="letters here", font=("Segoe UI",12), border_width=1, border_color="#FF5555")
        self.entry.pack(pady=8, padx=10, fill="x")

        self.btnc = ctk.CTkButton(self.bg_frame, text="CAPTURE", fg_color="#FF5555", hover_color="#AA0000", command=self.capture)
        self.btnc.pack(pady=6, padx=10, fill="x")

        self.btnf = ctk.CTkButton(self.bg_frame, text="FIND WORDS", fg_color="#FF5555", hover_color="#AA0000", command=self.find_manual)
        self.btnf.pack(pady=6, padx=10, fill="x")

        self.txt = ctk.CTkTextbox(self.bg_frame, font=("Segoe UI",12), fg_color="#2a2a2a", text_color="#FF5555", border_width=1, border_color="#FF5555")
        self.txt.pack(pady=10, padx=10, fill="both", expand=True)

    def capture(self):
        self.txt.delete("1.0","end")
        try:
            with mss.mss() as sct:
                mon = sct.monitors[1]
                shot = sct.grab(mon)
                img = Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")
                img = img.filter(ImageFilter.GaussianBlur(2))
            text = pytesseract.image_to_string(img)
            letters = ''.join([c for c in text if c.isalpha()])
            self.txt.insert("1.0", letters.upper()+"\n")
            if letters:
                self.find_words(letters)
        except:
            self.txt.insert("1.0","ERROR CAPTURING SCREEN")

    def find_manual(self):
        letters = self.entry.get().strip()
        self.txt.delete("1.0","end")
        if letters:
            self.find_words(letters)
        else:
            self.txt.insert("1.0","ENTER LETTERS")

    def find_words(self, letters):
        letters = letters.lower()
        counts = Counter(letters)
        matches=[]
        for w in self.words:
            wc = Counter(w)
            good=True
            for c in wc:
                if counts.get(c,0)<wc[c]:
                    good=False
                    break
            if good: matches.append(w)
        matches.sort(key=lambda x:-len(x))
        for w in matches[:20]:
            self.txt.insert("end", w.upper()+"\n")

    def run(self):
        self.win.mainloop()

if __name__=="__main__":
    app = LetterLe()
    app.run()
