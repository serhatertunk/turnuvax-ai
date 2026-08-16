import json
import os

print("🏀 TURNUVAX AI")
print("=" * 30)

DOSYA = "takimlar.json"


def takimlari_yukle():
    if os.path.exists(DOSYA):
        with open(DOSYA, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    return []


def takimlari_kaydet(takimlar):
    with open(DOSYA, "w", encoding="utf-8") as dosya:
        json.dump(takimlar, dosya, ensure_ascii=False, indent=4)


takimlar = takimlari_yukle()

while True:
    print("\n1 - Takım ekle")
    print("2 - Takımları listele")
    print("3 - Turnuva oluştur")
    print("4 - Çıkış")

    secim = input("\nSeçimin: ")

    if secim == "1":
        takim = input("Takım adı: ")

        if takim:
            takimlar.append(takim)
            takimlari_kaydet(takimlar)
            print(f"✅ {takim} takımı eklendi ve kaydedildi.")
        else:
            print("❌ Takım adı boş olamaz.")

    elif secim == "2":
        print("\n🏀 TAKIMLAR")

        if len(takimlar) == 0:
            print("Henüz takım eklenmedi.")
        else:
            for sira, takim in enumerate(takimlar, start=1):
                print(f"{sira}. {takim}")

    elif secim == "3":
        print("\n🏆 TURNUVA OLUŞTUR")

        turnuva_adi = input("Turnuva adı: ")
        tarih = input("Turnuva tarihi: ")

        print(f"\n✅ {turnuva_adi} oluşturuldu.")
        print(f"📅 Tarih: {tarih}")

    elif secim == "4":
        print("👋 Turnuvax AI kapatılıyor...")
        break

    else:
        print("❌ Geçersiz seçim!")
        