import json
import os

DOSYA = "turnuvalar.json"


def turnuvalari_yukle():
    if os.path.exists(DOSYA):
        with open(DOSYA, "r", encoding="utf-8") as dosya:
            return json.load(dosya)

    return []


def turnuvalari_kaydet(turnuvalar):
    with open(DOSYA, "w", encoding="utf-8") as dosya:
        json.dump(
            turnuvalar,
            dosya,
            ensure_ascii=False,
            indent=4
        )


def turnuva_olustur(takimlar, turnuvalar):
    print("\n🏆 TURNUVA OLUŞTUR")

    turnuva_adi = input("Turnuva adı (geri dönmek için 0): ").strip()

    if turnuva_adi == "0":
        print("↩️ Ana menüye dönülüyor...")
        return

    if not turnuva_adi:
        print("❌ Turnuva adı boş olamaz.")
        return

    tarih = input("Turnuva tarihi (geri dönmek için 0): ").strip()

    if tarih == "0":
        print("↩️ Ana menüye dönülüyor...")
        return

    if not tarih:
        print("❌ Turnuva tarihi boş olamaz.")
        return

    turnuva = {
        "ad": turnuva_adi,
        "tarih": tarih,
        "takimlar": []
    }

    print(f"\n✅ {turnuva_adi} oluşturuldu.")
    print(f"📅 Tarih: {tarih}")

    if not takimlar:
        print("\n❌ Henüz kayıtlı takım yok.")
    else:
        print("\n🏀 KAYITLI TAKIMLAR")

        for sira, takim in enumerate(takimlar, start=1):
            print(f"{sira}. {takim}")

        print("\nTakım eklemek için numara gir.")
        print("Bitirmek için 0 yaz.")

        while True:
            secim_takim = input("\nTakım numarası: ").strip()

            if secim_takim == "0":
                break

            if not secim_takim.isdigit():
                print("❌ Lütfen bir sayı gir.")
                continue

            takim_numarasi = int(secim_takim)

            if 1 <= takim_numarasi <= len(takimlar):
                secilen_takim = takimlar[takim_numarasi - 1]

                if secilen_takim in turnuva["takimlar"]:
                    print("⚠️ Bu takım zaten eklenmiş.")
                else:
                    turnuva["takimlar"].append(secilen_takim)
                    print(f"✅ {secilen_takim} turnuvaya eklendi.")

            else:
                print("❌ Geçersiz takım numarası.")

    turnuvalar.append(turnuva)
    turnuvalari_kaydet(turnuvalar)

    print("\n🏆 Turnuva kaydedildi!")
    print(f"📋 Turnuva: {turnuva['ad']}")
    print(f"📅 Tarih: {turnuva['tarih']}")
    print(f"🏀 Takım sayısı: {len(turnuva['takimlar'])}")


def turnuvalari_listele(turnuvalar):
    print("\n🏆 TURNUVALAR")

    if not turnuvalar:
        print("Henüz turnuva oluşturulmadı.")
        return

    for sira, turnuva in enumerate(turnuvalar, start=1):
        print(f"\n{sira}. {turnuva['ad']}")
        print(f"📅 Tarih: {turnuva['tarih']}")
        print(f"🏀 Takım sayısı: {len(turnuva['takimlar'])}")

        print("🏀 Takımlar:")

        for takim in turnuva["takimlar"]:
            print(f"   - {takim}")


def turnuva_sil(turnuvalar, maclar):
    print("\n🗑️ TURNUVA SİL")

    if not turnuvalar:
        print("❌ Henüz turnuva oluşturulmadı.")
        return

    for sira, turnuva in enumerate(turnuvalar, start=1):
        print(f"{sira}. {turnuva['ad']} - {turnuva['tarih']}")

    secim = input(
        "\nSilmek istediğin turnuva numarası (0 = geri): "
    ).strip()

    if secim == "0":
        print("↩️ Ana menüye dönülüyor...")
        return

    if not secim.isdigit():
        print("❌ Lütfen bir sayı gir.")
        return

    numara = int(secim)

    if not 1 <= numara <= len(turnuvalar):
        print("❌ Geçersiz turnuva numarası.")
        return

    turnuva = turnuvalar[numara - 1]

    onay = input(
        f"⚠️ '{turnuva['ad']}' turnuvası silinsin mi? (E/H): "
    ).strip().lower()

    if onay != "e":
        print("↩️ Silme işlemi iptal edildi.")
        return

    turnuva_adi = turnuva["ad"]

    turnuvalar.pop(numara - 1)
    turnuvalari_kaydet(turnuvalar)

    maclar[:] = [
        mac for mac in maclar
        if mac["turnuva"] != turnuva_adi
    ]

    from maclar import maclari_kaydet
    maclari_kaydet(maclar)

    print(f"🗑️ '{turnuva_adi}' turnuvası silindi.")
    print("🧹 Bu turnuvaya ait maçlar da silindi.")