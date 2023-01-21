import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("URL Cutter")
root.configure(bg="#27263D")
url = StringVar()
url_adress = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_adress.set(url_short)

def copyurl():
    url_short = url_adress.get()
    pyperclip.copy(url_short)

Label(root, text="Сокращенная ссылка", font="poppins", bg="#8B7AA8").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5, fill=X)
Button(root, text="Сгенерировать", command=urlshortener, bg="#7AA899").pack(pady=7)
Entry(root, textvariable=url_adress).pack(pady=5, fill=X)
Button(root, text="Скопировать URL", command=copyurl, bg="#7AA899").pack(pady=5)

root.mainloop()