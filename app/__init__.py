from flask import Flask, jsonify
from flask_cors import CORS

from config import configurations
from app.database import init_db
from app.routes import pages_bp, api_bp


def create_app(config_name="development"):
    """Flask uygulamasını oluşturur ve gerekli katmanları bağlar."""

    app = Flask(__name__)

    # Seçilen ortamın ayarlarını yükle.
    app.config.from_object(
        configurations.get(
            config_name,
            configurations["development"]
        )
    )

    # Frontend'in backend API'sine erişebilmesi için CORS'u aç.
    CORS(
        app,
        origins=app.config["CORS_ORIGINS"]
    )

    # Veritabanını oluştur / hazırla.
    init_db(app)

    # Sayfa ve API Blueprint'lerini kaydet.
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route("/health")
    def health():
        """Sunucunun çalıştığını kontrol eder."""
        return jsonify({
            "basari": True,
            "durum": "aktif"
        })

    return app
