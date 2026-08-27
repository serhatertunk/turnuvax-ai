import requests

from config import Config


class AIServiceError(Exception):
    """Yapay zekâ servisindeki hataları temsil eder."""
    pass


class AIService:
    """Groq üzerinden yapay zekâ yanıtları üretir."""

    MODEL = "openai/gpt-oss-120b"
    API_URL = "https://api.groq.com/openai/v1/chat/completions"

    def _sistem_talimati(self):
        """Yapay zekânın sistem talimatını config'den alır."""
        return Config.BUSINESS_CONTEXT

    def yanit_uret(self, mesaj, gecmis=None):
        """Kullanıcı mesajına Groq üzerinden yanıt üretir."""

        if gecmis is None:
            gecmis = []

        api_key = Config.GROQ_API_KEY

        # API anahtarı yoksa uygulama çökmek yerine demo modunda çalışır.
        if not api_key:
            return (
                "Demo modu aktif. "
                "Groq API anahtarı bulunamadığı için gerçek "
                "yapay zekâ yanıtı üretilemiyor."
            )

        # Önce sistem talimatı, sonra geçmiş mesajlar,
        # en son yeni kullanıcı mesajı gönderilir.
        messages = [
            {
                "role": "system",
                "content": self._sistem_talimati()
            }
        ]

        messages.extend(gecmis)

        messages.append(
            {
                "role": "user",
                "content": mesaj
            }
        )

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.MODEL,
            "messages": messages,
            "temperature": 0.7
        }

        try:
            response = requests.post(
                self.API_URL,
                headers=headers,
                json=data,
                timeout=30
            )

            response.raise_for_status()

            sonuc = response.json()

            return sonuc["choices"][0]["message"]["content"]

        except requests.RequestException as hata:
            # API hatasını kullanıcıya güvenli şekilde bildir.
            if getattr(hata, "response", None) is not None:
                durum = hata.response.status_code
                detay = hata.response.text[:300]

                raise AIServiceError(
                    f"Groq API hatası ({durum}): {detay}"
                ) from hata

            raise AIServiceError(
                "Yapay zekâ servisine şu anda ulaşılamıyor."
            ) from hata

        except (KeyError, IndexError, TypeError, ValueError) as hata:
            raise AIServiceError(
                "Yapay zekâ servisinden geçersiz yanıt alındı."
            ) from hata


# Uygulamanın kullanacağı tek AIService örneği.
ai_service = AIService()
