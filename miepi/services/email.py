from django.core.mail import EmailMessage
from django.conf import settings
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
            # ✅ Leer directamente del archivo (sin HTTP request)
            filename = f"qr_{inscrito.codigo}.png"
            
            # Leer el contenido del archivo desde el storage
            inscrito.qr_image.open('rb')  # Abrir en modo lectura binaria
            qr_content = inscrito.qr_image.read()
            inscrito.qr_image.close()
            
            # Adjuntar al email
            email.attach(filename, qr_content, 'image/png')
            
            logger.info(f"QR adjuntado correctamente para {inscrito.codigo}")
        except Exception as e:
            logger.exception(f"Error al adjuntar QR: {str(e)}")
    
    email.send(fail_silently=False)
