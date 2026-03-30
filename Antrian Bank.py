import heapq
import os
from gtts import gTTS
from playsound import playsound


class Antrian:
    def __init__(self):
        self.heap = []
        self.nomor_berikutnya = []
        self.maksimal_antrian = 5
        self.counter = {
            "Bisnis": 0,
            "Personal": 0
        }

    def AddAudio(self, text):
        tts = gTTS(text, lang='id')
        tts.save("panggilan.mp3")
        playsound("panggilan.mp3")
        os.remove("panggilan.mp3")

    def tambah_antrian(self, nama, jenis):
        if len(self.heap) >= self.maksimal_antrian:
            print("Antrian penuh. Maksimal 5 antrian.")
            self.AddAudio("Antrian penuh. Maksimal 5 antrian.")
            return

        if jenis not in self.counter:
            print("Jenis antrian tidak dikenali")
            return

        self.counter[jenis] += 1
        kode = "B" if jenis == "Bisnis" else "P"
        nomor = f"{nama} {kode}{self.counter[jenis]:03d}"
        prioritas = 0 if jenis == "Bisnis" else 1
        urutan_datang = sum(self.counter.values())

        heapq.heappush(self.heap, (prioritas, urutan_datang, nomor))
        self.nomor_berikutnya.append(nomor)
        print(f"{nomor} berhasil ditambahkan.")
        self.AddAudio(f"Antrian {nomor} berhasil ditambahkan.")

    def panggil(self, meja=1):
        if self.heap:
            _, _, nomor = heapq.heappop(self.heap)
            self.nomor_berikutnya.remove(nomor)
            print(f" Memanggil: {nomor} ke meja {meja}")
            self.AddAudio(f"Silakan, {nomor}, ke meja {meja}")
            return nomor
        else:
            print(" Tidak ada antrian.")
            self.AddAudio("Tidak ada antrian")
            return None

    def tampilkan_semua(self):
        print("\n--- Daftar Antrian Saat Ini (berdasarkan prioritas) ---")
        self.AddAudio("Daftar antrian saat ini.")
        if not self.heap:
            print("Belum ada antrian.")
            self.AddAudio("Belum ada antrian.")
        else:
            urutan = sorted(self.heap)
            for i, (_, _, nomor) in enumerate(urutan, 1):
                print(f"{i}. {nomor}")
                self.AddAudio(f"{i}. {nomor}")
        print("------------------------------------------------------\n")


def tampilkan_menu():
    print("\n=== APLIKASI BANKQU ===")
    print("1. Tambah Antrian Bisnis")
    print("2. Tambah Antrian Personal")
    print("3. Meja 1 Memanggil")
    print("4. Meja 2 Memanggil")
    print("5. Tampilkan Semua Antrian")
    print("6. Keluar")


def main():
    antrian = Antrian()
    meja1 = "-"
    meja2 = "-"

    while True:
        tampilkan_menu()
        print(f"\nMeja 1: {meja1}")
        print(f"Meja 2: {meja2}")
        print("Nomor Selanjutnya:", " ".join(antrian.nomor_berikutnya[:3]))
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            nama = input("Masukkan nama nasabah: ")
            antrian.tambah_antrian(nama, "Bisnis")

        elif pilihan == "2":
            nama = input("Masukkan nama nasabah: ")
            antrian.tambah_antrian(nama, "Personal")

        elif pilihan == "3":
            nomor = antrian.panggil(meja=1)
            if nomor:
                meja1 = nomor

        elif pilihan == "4":
            nomor = antrian.panggil(meja=2)
            if nomor:
                meja2 = nomor

        elif pilihan == "5":
            antrian.tampilkan_semua()

        elif pilihan == "6":
            print("Terima kasih telah menggunakan aplikasi BANK QU.")
            antrian.AddAudio("Terima kasih telah menggunakan aplikasi BANK QU.")
            break


        else:
            print("Pilihan tidak valid.")
            antrian.AddAudio("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
