def puan_durumu(maclar, turnuvalar):
    print("\n🏆 PUAN DURUMU")

    if not turnuvalar:
        print("❌ Henüz turnuva oluşturulmadı.")
        return

    for sira, turnuva in enumerate(turnuvalar, start=1):
        print(f"{sira}. {turnuva['ad']}")

    secim = input("\nTurnuva numarası: ").strip()

    if not secim.isdigit():
        print("❌ Lütfen bir sayı gir.")
        return

    turnuva_numarasi = int(secim)

    if not 1 <= turnuva_numarasi <= len(turnuvalar):
        print("❌ Geçersiz turnuva numarası.")
        return

    turnuva = turnuvalar[turnuva_numarasi - 1]

    takimlar = turnuva["takimlar"]

    puanlar = {}

    for takim in takimlar:
        puanlar[takim] = {
            "O": 0,
            "G": 0,
            "M": 0,
            "A": 0,
            "Y": 0,
            "AV": 0,
            "P": 0
        }

    for mac in maclar:

        if mac["turnuva"] != turnuva["ad"]:
            continue

        ev_skor = mac["ev_sahibi_skor"]
        dep_skor = mac["deplasman_skor"]

        if ev_skor is None or dep_skor is None:
            continue

        ev = mac["ev_sahibi"]
        deplasman = mac["deplasman"]

        puanlar[ev]["O"] += 1
        puanlar[deplasman]["O"] += 1

        puanlar[ev]["A"] += ev_skor
        puanlar[ev]["Y"] += dep_skor

        puanlar[deplasman]["A"] += dep_skor
        puanlar[deplasman]["Y"] += ev_skor

        if ev_skor > dep_skor:
            puanlar[ev]["G"] += 1
            puanlar[ev]["P"] += 2

            puanlar[deplasman]["M"] += 1
            puanlar[deplasman]["P"] += 1

        elif dep_skor > ev_skor:
            puanlar[deplasman]["G"] += 1
            puanlar[deplasman]["P"] += 2

            puanlar[ev]["M"] += 1
            puanlar[ev]["P"] += 1

    for takim in puanlar:
        puanlar[takim]["AV"] = (
            puanlar[takim]["A"] - puanlar[takim]["Y"]
        )

    siralama = sorted(
        puanlar.items(),
        key=lambda x: (
            x[1]["P"],
            x[1]["AV"],
            x[1]["A"]
        ),
        reverse=True
    )

    print(f"\n🏆 {turnuva['ad']} - PUAN DURUMU")
    print("=" * 55)

    for sira, (takim, bilgi) in enumerate(siralama, start=1):
        print(f"\n{sira}. {takim}")
        print(
            f"   O: {bilgi['O']} | "
            f"G: {bilgi['G']} | "
            f"M: {bilgi['M']} | "
            f"A: {bilgi['A']} | "
            f"Y: {bilgi['Y']} | "
            f"AV: {bilgi['AV']} | "
            f"P: {bilgi['P']}"
        )