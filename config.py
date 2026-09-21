import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "dev-secret-key"
    )

    DATABASE_URL = os.environ.get(
        "DATABASE_URL",
        "sqlite:///turnuvax.db"
    )

    GROQ_API_KEY = os.environ.get(
        "GROQ_API_KEY",
        ""
    )

    AI_PROVIDER = os.environ.get(
        "AI_PROVIDER",
        "groq"
    )

    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        """Sen TurnuvaX AI'nin basketbol turnuvaları asistanısın.

Cevaplarını Türkçe ve kısa ver.
Genellikle 1-3 cümle kullan.
Mümkünse 250 karakteri geçme.
Markdown tablo kullanma.
Markdown başlık kullanma.
Yatay çizgi kullanma.
Gereksiz açıklama ve tekrar yapma.
Kullanıcıya doğrudan ve anlaşılır cevap ver."""
    )

    CORS_ORIGINS = os.environ.get(
        "CORS_ORIGINS",
        "*"
    )


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


configurations = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
