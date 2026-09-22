import sqlite3

from flask import current_app, g


def get_db():
    """Mevcut uygulama için SQLite bağlantısını oluşturur."""
    if "db" not in g:
        database_url = current_app.config.get(
            "DATABASE_URL",
            "sqlite:///turnuvax.db"
        )

        if database_url.startswith("sqlite:///"):
            database_path = database_url.replace(
                "sqlite:///",
                "",
                1
            )
        else:
            database_path = "turnuvax.db"

        g.db = sqlite3.connect(database_path)
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(exception=None):
    """İstek sonunda açık veritabanı bağlantısını kapatır."""
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db(app):
    """Leads tablosunu oluşturur ve gerekli sütunları ekler."""
    with app.app_context():
        db = get_db()

        # Tablo yoksa oluştur.
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                mail TEXT,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # Eski tabloda mail sütunu yoksa ekle.
        columns = db.execute(
            "PRAGMA table_info(leads)"
        ).fetchall()

        column_names = [column["name"] for column in columns]

        if "mail" not in column_names:
            db.execute(
                "ALTER TABLE leads ADD COLUMN mail TEXT"
            )

        db.commit()

    app.teardown_appcontext(close_db)


def lead_ekle(isim, mail, telefon, mesaj):
    """Yeni iletişim kaydı oluşturur."""
    db = get_db()

    cursor = db.execute(
        """
        INSERT INTO leads (isim, mail, telefon, mesaj)
        VALUES (?, ?, ?, ?)
        """,
        (isim, mail, telefon, mesaj)
    )

    db.commit()

    return cursor.lastrowid


def tum_leadler():
    """Lead kayıtlarını yeniden eskiye doğru getirir."""
    db = get_db()

    cursor = db.execute(
        """
        SELECT id, isim, mail, telefon, mesaj, tarih
        FROM leads
        ORDER BY tarih DESC, id DESC
        """
    )

    return cursor.fetchall()
