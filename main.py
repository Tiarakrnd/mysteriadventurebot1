import time
import random

def tampil(teks):
    print(teks)
    time.sleep(0.5)

sword_art = r"""
             /| ________________
 O|===|* >________________>
             \
"""

skull_art = r'''
                 _.--"""""--._
             .'  _     _  '.
            /   (o)   (o)   \
         |  ,           ,  |
         |  \`.       .`/  |
            \  '.`'---'`.'  /
             '.  `'-----'`  .'
                 '-._______.-'
'''

def game_utama():
    tampil("--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu? ")

    while True:
        nyawa = 100
        tampil(f"Selamat datang, {nama}! Nyawamu: {nyawa}")

        tampil("Kamu berdiri di persimpangan. Pilih jalurmu:")
        tampil("1) Lembah Coding")
        tampil("2) Gunung Bug")
        pilihan = input("Ketik 1 atau 2: ").strip()

        if pilihan == "1":
            roll = random.randint(1, 100)
            if roll <= 80:
                tampil("Keberuntungan memihakmu! Kamu menaklukkan teka-teki coding.")
                tampil(sword_art)
                tampil("Hadiah: reputasi coder + cerita epik.")
            else:
                nyawa -= 20
                tampil("Sebuah bug tersembunyi menyerang proyekmu!")
                tampil(f"Kamu kehilangan 20 nyawa. Sisa nyawa: {nyawa}")
                if nyawa <= 0:
                    tampil(skull_art)
                    tampil("Nyawamu habis. Permainan berakhir.")

        elif pilihan == "2":
            roll = random.randint(1, 100)
            if roll <= 50:
                tampil("Pendakian berbahaya, namun kamu berhasil menundukkan Gunung Bug.")
                tampil(sword_art)
                tampil("Kamu menemukan artefak debugging kuno.")
            else:
                nyawa -= 20
                tampil("Bug raksasa menyerang di puncak!")
                tampil(f"Kamu kehilangan 20 nyawa. Sisa nyawa: {nyawa}")
                if nyawa <= 0:
                    tampil(skull_art)
                    tampil("Nyawamu habis. Permainan berakhir.")

        else:
            nyawa -= 20
            tampil("Pilihan tidak valid! Kamu tersesat dan kehilangan nyawa.")
            tampil(f"Sisa nyawa: {nyawa}")

        lagi = input("Main lagi? (y/n): ").strip().lower()
        if lagi != 'y':
            tampil("Terima kasih telah bermain!")
            break

if __name__ == "__main__":
    game_utama()