import os
import time
import subprocess
from colorama import init, Fore, Style

# ASCII sanatı
ascii_art = """
  -------------------------------
  
  
░░░░░░███████ ]▄▄▄▄▄▄▄▄
▂▄▅█████████▅▄▃▂
I███████████████████].
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...

  
  -------------------------------
 \033[92mTERMUX KURULUMUNA HOSGELDİNİZ
  -------------------------------
\033[96m|Hata, soru, öneri için: [https://t.me/weertyyyy]|
"""

# Renklendirme başlat
init(autoreset=True)

def yukle_paketler():
    python_surumleri = {"Python 2": "python2", "Python 3": "python", "Python 3 (alternatif)": "python3"}
    diger_paketler = [
        "git",
        "nano",
        "wget",
        "curl",
        "openssh",
        "zip",
        "unzip",
        "tar",
        "pkg-config",
        "clang",
        "make",
        "openssl",
        "ncurses-utils",
        "libcrypt-dev",
        "libffi-dev",
        "libxml2-dev",
        "libxslt-dev",
        "libjpeg-turbo-dev",
        "libpng-dev",
        "freetype-dev",
        "postgresql",
        "mysql"
    ]

    print(Fore.GREEN + ascii_art)
    print(Fore.GREEN + "Lütfen yüklemek istediğiniz Python sürümünü seçin:")
    for i, (surum, paket) in enumerate(python_surumleri.items(), start=1):
        print(f"{Fore.YELLOW}{i}. {surum}")

    secim = int(input(Fore.GREEN + "Seçiminizi yapın (1-3): "))

    if secim < 1 or secim > 3:
        print(Fore.RED + "Geçersiz seçim.")
        return

    secilen_python = list(python_surumleri.values())[secim - 1]

    print(Fore.GREEN + f"{secilen_python} yüklenecek ve aşağıdaki diğer paketler de yüklenecek:")

    for paket in diger_paketler:
        print(Fore.YELLOW + paket)

    onay = input(Fore.GREEN + "Devam etmek istiyor musunuz? (E/H): ")

    if onay.upper() != "E":
        print(Fore.RED + "İşlem iptal edildi.")
        return

    try:
        
        print(Fore.GREEN + "Paketler yükleniyor...")
        baslangic_zamani = time.time()

        
        install_proc = subprocess.Popen(['pkg', 'install', secilen_python, '-y'], stdout=subprocess.PIPE)
        while install_proc.poll() is None:
            print(Fore.YELLOW + "Python yükleniyor...")
            time.sleep(1)

        
        for i, paket in enumerate(diger_paketler, start=1):
            print(Fore.GREEN + f"{i}/{len(diger_paketler)} - {paket} yükleniyor...")
            subprocess.run(['pkg', 'install', paket, '-y'])

            
            yuzde = int((i / len(diger_paketler)) * 100)
            print(Fore.YELLOW + f"Yükleme: {yuzde}%")

        
        print(Fore.GREEN + "Gerekli paketler başarıyla yüklendi.")
        yukleme_suresi = round(time.time() - baslangic_zamani, 2)
        print(Fore.YELLOW + f"Toplam geçen süre: {yukleme_suresi} saniye")

    except Exception as e:
        print(Fore.RED + "Hata oluştu:")
        print(e)

if __name__ == "__main__":
    yukle_paketler()