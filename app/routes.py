from flask import Blueprint, jsonify, render_template, request

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import AIServiceError, ai_service


# Kullanıcıya gösterilen sayfalar için Blueprint.
pages_bp = Blueprint("pages", __name__)


# API işlemleri için Blueprint.
api_bp = Blueprint("api", __name__)


@pages_bp.route("/")
def index():
    """Ana karşılama sayfasını gösterir."""
    return render_template("index.html")


@pages_bp.route("/dashboard")
def dashboard():
    """Yönetim panelini gösterir."""
    return render_template("dashboard.html")


@api_bp.route("/sohbet", methods=["POST"])
def sohbet():
    """Kullanıcı mesajını AI servisine gönderir."""
    veri = request.get_json(silent=True) or {}

    mesaj = veri.get("mesaj", "").strip()
    gecmis = veri.get("gecmis", [])

    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj alanı boş olamaz."
        }), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)

        return jsonify({
            "basari": True,
            "cevap": cevap
        })

    except AIServiceError:
        return jsonify({
            "basari": False,
            "hata": "Yapay zekâ servisine şu anda ulaşılamıyor."
        }), 503


@api_bp.route("/leads", methods=["POST"])
def lead_olustur():
    """Yeni lead kaydı oluşturur."""
    veri = request.get_json(silent=True) or {}

    isim = veri.get("isim", "").strip()
    telefon = veri.get("telefon", "").strip()
    mesaj = veri.get("mesaj", "").strip()

    if not isim or not telefon:
        return jsonify({
            "basari": False,
            "hata": "İsim ve telefon zorunludur."
        }), 400

    try:
        lead_id = lead_ekle(isim, telefon, mesaj)

        return jsonify({
            "basari": True,
            "id": lead_id
        }), 201

    except Exception:
        return jsonify({
            "basari": False,
            "hata": "Kayıt oluşturulurken bir hata oluştu."
        }), 500


@api_bp.route("/leads", methods=["GET"])
def leadleri_getir():
    """Tüm lead kayıtlarını getirir."""
    try:
        kayitlar = tum_leadler()

        leadler = [
            {
                "id": kayit["id"],
                "isim": kayit["isim"],
                "telefon": kayit["telefon"],
                "mesaj": kayit["mesaj"],
                "tarih": kayit["tarih"]
            }
            for kayit in kayitlar
        ]

        return jsonify({
            "basari": True,
            "leadler": leadler
        })

    except Exception:
        return jsonify({
            "basari": False,
            "hata": "Kayıtlar alınırken bir hata oluştu."
        }), 500
