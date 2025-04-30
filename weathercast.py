import tkinter as tk
from tkinter import ttk
from weather import hava_durumu_getir

# hava durumunu weather.py dosyasındaki hava_durumu_getir fonksiyonunu kullanarak apiyi guiye çeker
def sorgula_hava_durumu():
    cityName = entry.get()
    sonuc = hava_durumu_getir(cityName)
    
    if sonuc is None:
        sonuc_etiketi.config(text="Şehir bulunamadı. Lütfen tekrar deneyin.")
    else:
        tarih, sehir, sicaklik = sonuc
        sonuc_etiketi.config(text=f"{tarih}\n{sehir}\nSıcaklık: {sicaklik}°C")

# Ana pencere ayarları
window = tk.Tk()
window.title("Weather Coast")
window.geometry("600x400")
window.configure(bg="#f0f0f0")

# Stil ayarları
style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 10))
style.configure("TLabel", font=('Helvetica', 12))
style.configure("TEntry", padding=5)

# Ana frame
main_frame = ttk.Frame(window, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Başlık
hosgeldinizLabel = ttk.Label(main_frame, 
                            text="Weather Cast Uygulamasına Hoşgeldiniz",
                            font=('Helvetica', 16, 'bold'))
hosgeldinizLabel.pack(pady=20)

# Giriş alanı frame'i
input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=20)

sehirGiriniz = ttk.Label(input_frame, text="Şehir Giriniz:")
sehirGiriniz.pack(side=tk.LEFT, padx=5)

entry = ttk.Entry(input_frame, width=30)
entry.pack(side=tk.LEFT, padx=5)

# Sorgula butonu
sorgula = ttk.Button(main_frame, 
                     text="Sorgula",
                     command=sorgula_hava_durumu)
sorgula.pack(pady=10)

# Sonuç etiketi
sonuc_etiketi = ttk.Label(main_frame, 
                         text="",
                         font=('Helvetica', 12),
                         wraplength=400)
sonuc_etiketi.pack(pady=20)

# Enter tuşu ile sorgulama
entry.bind('<Return>', lambda event: sorgula_hava_durumu())

window.mainloop()



   