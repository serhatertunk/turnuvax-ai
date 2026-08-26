import json
import os

DOSYA = "takimlar.json"


def takimlari_yukle():
    if os.path.exists(DOSYA):
        with open(DOSYA, "r", encoding="utf-8") as dosya:
            return json.load(dosya)

    return []


def takimlari_kaydet(takimlar):
    with open(DOSYA, "w", encoding="utf-8") as dosya:
        json.dump(
            takimlar,
            dosya,
            ensure_ascii=False,
            indent=4
        )


def takim_ekle(takimlar):
    print("\n🏀 TAKIM EKLE")

    takim = input(
        "Takım adı (geri dönmek için 0): "
    ).strip()

    if takim == "0":
        print("↩️ Ana menüye dönülüyor...")
        return

    if not takim:
        print("❌ Takım adı boş olamaz.")
        return

    if takim in takimlar:
        print("⚠️ Bu takım zaten kayıtlı.")
        return

    takimlar.append(takim)
    takimlari_kaydet(takimlar)

    print(f"✅ {takim} takımı eklendi ve kaydedildi.")


def takimlari_listele(takimlar):
    print("\n🏀 TAKIMLAR")

    if not takimlar:
        print("Henüz takım eklenmedi.")
        return

    for sira, takim in enumerate(takimlar, start=1):
        print(f"{sira}. {takim}")


def takim_sil(takimlar):
    print("\n🗑️ TAKIM SİL")

    if not takimlar:
        print("❌ Henüz takım bulunmuyor.")
        return

    for sira, takim in enumerate(takimlar, start=1):
        print(f"{sira}. {takim}")

    secim = input(
        "\nSilmek istediğin takım numarası (0 = geri): "
    ).strip()

    if secim == "0":
        print("↩️ Ana menüye dönülüyor...")
        return

    if not secim.isdigit():
        print("❌ Lütfen bir sayı gir.")
        return

    numara = int(secim)

    if not 1 <= numara <= len(takimlar):
        print("❌ Geçersiz takım numarası.")
        return

    takim = takimlar[numara - 1]

    onay = input(
        f"⚠️ '{takim}' takımı silinsin mi? (E/H): "
    ).strip().lower()

    if onay != "e":
        print("↩️ Silme işlemi iptal edildi.")
        return

    takimlar.pop(numara - 1)
    takimlari_kaydet(takimlar)

    print(f"🗑️ '{takim}' takımı silindi.")
