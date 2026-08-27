# TurnuvaX AI

Basketbol turnuvaları için yapay zekâ destekli asistan ve lead toplama sistemi.

## Proje Hakkında

TurnuvaX AI; basketbol tutkunları, kulüpler ve organizatörlerin
turnuvalar hakkında bilgi almasını sağlayan yapay zekâ destekli
bir web uygulamasıdır.

Kullanıcılar yapay zekâya soru sorabilir ve iletişim bilgilerini
bırakarak kayıt oluşturabilir.

## Temel Özellikler

- Yapay zekâ ile Türkçe sohbet
- Groq API entegrasyonu
- Kullanıcı adı ve telefon bilgilerinin alınması
- Lead kayıtlarının SQLite veritabanında tutulması
- Yönetim panelinde lead kayıtlarının görüntülenmesi
- REST API
- Wix Velo frontend entegrasyonu
- Render üzerinde canlı backend

## Teknolojiler

- Python
- Flask
- SQLite
- Groq API
- Wix Velo
- Render
- GitHub

## Mimari

Proje sorumlulukların ayrılığı prensibine göre modüler olarak
tasarlanmıştır.

```text
turnuvax-ai/
├── run.py
├── config.py
├── requirements.txt
├── .gitignore
├── render.yaml
└── app/
    ├── __init__.py
    ├── database.py
    ├── routes.py
    ├── services/
    │   ├── __init__.py
    │   └── ai_service.py
    └── templates/
        ├── index.html
        └── dashboard.html
