import sqlite3

from flask import current_app, g


def get_db():
    """Mevcut uygulama için SQLite bağlantısını oluşturur."""
    if "db" not in g:
        database_url = current_app.config.get(
            "DATABASE_URL",
            "sqlite:///turnuvax.db"
        )

        # SQLite bağlantısı için dosya yolunu belirle.
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
    """Leads tablosunu yoksa oluşturur."""
    with app.app_context():
        db = get_db()

        db.execute(
            """
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        db.commit()

    app.teardown_appcontext(close_db)


def lead_ekle(isim, telefon, mesaj):
    """Yeni bir lead kaydeder."""
    db = get_db()

    cursor = db.execute(
        """
        INSERT INTO leads (isim, telefon, mesaj)
        VALUES (?, ?, ?)
        """,
        (isim, telefon, mesaj)
    )

    db.commit()

    return cursor.lastrowid


def tum_leadler():
    """Lead kayıtlarını yeniden eskiye doğru getirir."""
    db = get_db()

    cursor = db.execute(
        """
        SELECT id, isim, telefon, mesaj, tarih
        FROM leads
        ORDER BY tarih DESC, id DESC
        """
    )

    return cursor.fetchall()
