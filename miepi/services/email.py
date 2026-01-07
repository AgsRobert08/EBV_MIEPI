from django.core.mail import EmailMessage
from django.conf import settings
import requests
import logging

logger = logging.getLogger(__name__)

def enviar_correo_registro(inscrito):
    if not inscrito.correo_electronico:
        return

    subject = "Confirmación de registro – MIEPI"

    body = f"""
Hola {inscrito.nombre},

Tu registro ha sido realizado correctamente.
Debe presentar el QR recibido en este correo para validar 
su asistencia.

Dios te bendiga.
"""

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[inscrito.correo_electronico],
        reply_to=[settings.EMAIL_HOST_USER],
    )

    if inscrito.qr_image:
        try:
            qr_url = inscrito.qr_image.url
            response = requests.get(qr_url, timeout=10)

            if response.status_code == 200:
                content_type = response.headers.get('Content-Type', 'image/png')
                filename = f"qr_{inscrito.codigo}.png"
                email.attach(filename, response.content, content_type)
            else:
                logger.warning(f"No se pudo descargar QR ({response.status_code})")

        except Exception:
            logger.exception("Error al adjuntar QR desde Cloudinary")

    email.send(fail_silently=False)
