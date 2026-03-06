import datetime
import random
import os
import platform

def mega_robot():
    print("========================================")
    print("      🚀 MEGA CHATBOT v2.1 AKTIF")
    print("      Gelistirici: 10 Yasindaki Hacker")
    print("========================================")
    
    isim = input("Bot: Hey! Benim adim Bot, senin adin ne? ")
    print(f"Bot: Hos geldin {isim}! Sana yardimci olmaya hazirim.")

    while True:
        print("\n" + "-"*20)
        soru = input(f"{isim}: ").lower()

        # --- YENI ÖZELLIK: YARDIM MENÜSÜ ---
        if "neler sorabilirim" in soru or "yardim" in soru or "ne yapabilirsin" in soru:
            print("Bot: Iste yapabildiklerim:")
            print("1. Selamlasabiliriz (Merhaba/Selam)")
            print("2. Saat ve Tarihi söylerim (Saat/Tarih)")
            print("3. Senin için zar atarim (Zar at)")
            print("4. Yazi-Tura oynarim (Yazi tura)")
            print("5. Sistem bilgilerini gösteririm (Sistem/Bilgisayar)")
            print("6. Nerede oldugumuzu söylerim (Dosyalar/Nerdeyim)")
            print("7. Hayatin anlamini tartisirim (Hayatin anlami)")
            print("8. Programi kapatabilirim (Kapat/Exit)")

        elif "merhaba" in soru or "selam" in soru:
            print("Bot: Selam dostum! Kodlarim bugün senin icin yaniyor.")

        elif "saat" in soru or "tarih" in soru:
            zaman = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Bot: Su anki zaman dilimi: {zaman}")

        elif "sistem" in soru or "bilgisayar" in soru:
            print(f"Bot: Su an {platform.system()} üzerinde kosuyorum.")

        elif "zar at" in soru:
            zar = random.randint(1, 6)
            print(f"Bot: Zari attim... 🎲 Sonuç: {zar}")

        elif "yazi tura" in soru:
            sonuc = random.choice(["Yazi", "Tura"])
            print(f"Bot: Parayi firlattim... Sonuc: {sonuc}")

        elif "hayatin anlami" in soru:
            print("Bot: Bence hayatin anlami Python yazmaktir!")

        elif "dosyalar" in soru or "nerdeyim" in soru:
            dizin = os.getcwd()
            print(f"Bot: Su an bu klasördeyim: {dizin}")

        elif "kapat" in soru or "baybay" in soru or "exit" in soru:
            print(f"Bot: Görüsürüz {isim}!")
            break

        else:
            print("Bot: Bu soruyu henüz anlamadim. 'Yardim' yazarak neler yapabildigime bakabilirsin.")

    input("\nProgrami kapatmak icin Enter'a bas...")

if __name__ == "__main__":
    mega_robot()