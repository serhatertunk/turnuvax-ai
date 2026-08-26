import takimlar
import turnuvalar
import maclar
import puan_durumu


print("🏀 TURNUVAX AI")
print("=" * 30)


takimlar_listesi = takimlar.takimlari_yukle()
turnuvalar_listesi = turnuvalar.turnuvalari_yukle()
maclar_listesi = maclar.maclari_yukle()


while True:

    print("\n1 - Takım ekle")
    print("2 - Takımları listele")
    print("3 - Turnuva oluştur")
    print("4 - Turnuvaları listele")
    print("5 - Çıkış")
    print("6 - Maçları oluştur")
    print("7 - Skor gir")
    print("8 - Puan durumu")
    print("9 - Turnuva sil")
    print("10 - Takım sil")


    secim = input("\nSeçimin: ").strip()

    if secim == "1":
        takimlar.takim_ekle(takimlar_listesi)

    elif secim == "2":
        takimlar.takimlari_listele(
            takimlar_listesi
        )

    elif secim == "3":
        turnuvalar.turnuva_olustur(
            takimlar_listesi,
            turnuvalar_listesi
        )

    elif secim == "4":
        turnuvalar.turnuvalari_listele(
            turnuvalar_listesi
        )

    elif secim == "5":
        print("👋 Turnuvax AI kapatılıyor...")
        break

    elif secim == "6":
        maclar_listesi = maclar.maclari_olustur(
            turnuvalar_listesi,
            maclar_listesi
        )

    elif secim == "7":
        maclar.skor_gir(maclar_listesi)

    elif secim == "8":
        puan_durumu.puan_durumu(
            maclar_listesi,
            turnuvalar_listesi
        )

    elif secim == "9":
        turnuvalar.turnuva_sil(
            turnuvalar_listesi,
            maclar_listesi
        )
    elif secim == "10":
        takimlar.takim_sil(takimlar_listesi)
    else:
        print("❌ Geçersiz seçim!")