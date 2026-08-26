import json
import os
from itertools import combinations

DOSYA = "maclar.json"


def maclari_yukle():
    if os.path.exists(DOSYA):
        with open(DOSYA, "r", encoding="utf-8") as dosya:
            return json.load(dosya)

    return []


def maclari_kaydet(maclar):
    with open(DOSYA, "w", encoding="utf-8") as dosya:
        json.dump(
            maclar,
            dosya,
            ensure_ascii=False,
            indent=4
        )


def maclari_olustur(turnuvalar, maclar):
    print("\n🏀 MAÇLARI OLUŞTUR")

    if not turnuvalar:
        print("❌ Henüz turnuva oluşturulmadı.")
        return maclar

    for sira, turnuva in enumerate(turnuvalar, start=1):
        print(f"{sira}. {turnuva['ad']}")

    secim = input("\nTurnuva numarası: ").strip()

    if not secim.isdigit():
        print("❌ Lütfen bir sayı gir.")
        return maclar

    numara = int(secim)

    if not (1 <= numara <= len(turnuvalar)):
        print("❌ Geçersiz turnuva numarası.")
        return maclar

    turnuva = turnuvalar[numara - 1]
    takimlar = turnuva["takimlar"]
    turnuva_adi = turnuva["ad"]

    print(f"\n🏆 {turnuva_adi} - MAÇLAR")

    if len(takimlar) < 2:
        print("❌ En az 2 takım gerekli.")
        return maclar

    mevcut = [
        mac for mac in maclar
        if mac.get("turnuva") == turnuva_adi
    ]

    if mevcut:
        print("⚠️ Bu turnuvanın maçları zaten oluşturulmuş.")

        for sira, mac in enumerate(mevcut, start=1):
            print(f"\nMaç {sira}")
            print(
                f"{mac['ev_sahibi']} 🆚 "
                f"{mac['deplasman']}"
            )

            if (
                mac.get("ev_sahibi_skor") is not None
                and mac.get("deplasman_skor") is not None
            ):
                print(
                    f"📊 Skor: "
                    f"{mac['ev_sahibi_skor']} - "
                    f"{mac['deplasman_skor']}"
                )

        print(f"\n🏀 Toplam maç: {len(mevcut)}")
        return maclar

    yeni_maclar = []

    for ev_sahibi, deplasman in combinations(takimlar, 2):
        yeni_maclar.append({
            "turnuva": turnuva_adi,
            "ev_sahibi": ev_sahibi,
            "deplasman": deplasman,
            "ev_sahibi_skor": None,
            "deplasman_skor": None
        })

    maclar.extend(yeni_maclar)
    maclari_kaydet(maclar)

    for sira, mac in enumerate(yeni_maclar, start=1):
        print(f"\nMaç {sira}")
        print(
            f"{mac['ev_sahibi']} 🆚 "
            f"{mac['deplasman']}"
        )

    print(f"\n🏀 Toplam maç: {len(yeni_maclar)}")

    return maclar


def skor_gir(maclar):
    print("\n🏀 SKOR GİR")

    if not maclar:
        print("❌ Henüz maç oluşturulmadı.")
        return

    for sira, mac in enumerate(maclar, start=1):
        print(
            f"{sira}. "
            f"{mac['turnuva']} | "
            f"{mac['ev_sahibi']} 🆚 "
            f"{mac['deplasman']}"
        )

    secim = input(
        "\nSkor girmek istediğin maç numarası: "
    ).strip()

    if not secim.isdigit():
        print("❌ Lütfen bir sayı gir.")
        return

    numara = int(secim)

    if not (1 <= numara <= len(maclar)):
        print("❌ Geçersiz maç numarası.")
        return

    mac = maclar[numara - 1]

    ev_skor = input(
        f"{mac['ev_sahibi']} skoru: "
    ).strip()

    deplasman_skor = input(
        f"{mac['deplasman']} skoru: "
    ).strip()

    if not ev_skor.isdigit() or not deplasman_skor.isdigit():
        print("❌ Skorlar sadece sayı olmalı.")
        return

    mac["ev_sahibi_skor"] = int(ev_skor)
    mac["deplasman_skor"] = int(deplasman_skor)

    maclari_kaydet(maclar)

    print(
        f"✅ Skor kaydedildi: "
        f"{ev_skor} - {deplasman_skor}"
    )


def mac_sonuclari_listele(maclar, turnuvalar):
    print("\n🏀 MAÇ SONUÇLARI")

    if not turnuvalar:
        print("❌ Henüz turnuva oluşturulmadı.")
        return

    for sira, turnuva in enumerate(turnuvalar, start=1):
        print(f"{sira}. {turnuva['ad']}")

    secim = input("\nTurnuva numarası: ").strip()

    if not secim.isdigit():
        print("❌ Lütfen bir sayı gir.")
        return

    numara = int(secim)

    if not (1 <= numara <= len(turnuvalar)):
        print("❌ Geçersiz turnuva numarası.")
        return

    turnuva = turnuvalar[numara - 1]

    turnuva_maclari = [
        mac for mac in maclar
        if mac.get("turnuva") == turnuva["ad"]
    ]

    print(f"\n🏆 {turnuva['ad']} - MAÇ SONUÇLARI")

    if not turnuva_maclari:
        print("❌ Bu turnuvada maç bulunamadı.")
        return

    oynanan = 0
    bekleyen = 0

    for sira, mac in enumerate(turnuva_maclari, start=1):
        print(f"\nMaç {sira}")

        ev_skor = mac.get("ev_sahibi_skor")
        deplasman_skor = mac.get("deplasman_skor")

        if ev_skor is None or deplasman_skor is None:
            print(
                f"{mac['ev_sahibi']} 🆚 "
                f"{mac['deplasman']}"
            )
            print("⏳ Henüz oynanmadı.")
            bekleyen += 1
            continue

        oynanan += 1

        print(
            f"{mac['ev_sahibi']} "
            f"{ev_skor} - {deplasman_skor} "
            f"{mac['deplasman']}"
        )

        if ev_skor > deplasman_skor:
            print(
                f"🏆 Kazanan: {mac['ev_sahibi']}"
            )
        elif deplasman_skor > ev_skor:
            print(
                f"🏆 Kazanan: {mac['deplasman']}"
            )
        else:
            print("🤝 Berabere")

    print(f"\n🏀 Oynanan maç: {oynanan}")
    print(f"⏳ Bekleyen maç: {bekleyen}")