from django.core.mail import EmailMessage
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def enviar_correo_registro(inscrito):
    logger.info(f"=== INICIANDO ENVÍO DE CORREO ===")
    logger.info(f"Destinatario: {inscrito.correo_electronico}")
    logger.info(f"Código inscrito: {inscrito.codigo}")
    
    if not inscrito.correo_electronico:
        logger.warning(f"Inscrito {inscrito.codigo} sin correo electrónico")
        return
    
    # Verificar configuración
    logger.info(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    logger.info(f"EMAIL_HOST: {settings.EMAIL_HOST}")
    logger.info(f"EMAIL_PORT: {settings.EMAIL_PORT}")
    
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
    
    # Adjuntar QR desde Cloudinary
    if inscrito.qr_image:
        try:
            logger.info(f"Adjuntando QR desde: {inscrito.qr_image.url}")
            filename = f"qr_{inscrito.codigo}.png"
            
            inscrito.qr_image.open('rb')
            qr_content = inscrito.qr_image.read()
            inscrito.qr_image.close()
            
            email.attach(filename, qr_content, 'image/png')
            logger.info(f"✅ QR adjuntado correctamente")
            
        except Exception as e:
            logger.error(f"❌ Error al adjuntar QR: {str(e)}")
    else:
        logger.warning("⚠️ No hay imagen QR para adjuntar")
    
    # Enviar email
    try:
        logger.info("📧 Intentando enviar correo...")
        email.send(fail_silently=False)
        logger.info(f"✅ Correo enviado exitosamente a {inscrito.correo_electronico}")
    except Exception as e:
        logger.error(f"❌ ERROR AL ENVIAR CORREO: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        raise
