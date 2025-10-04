
import os
import logging
from celery import shared_task
from Social.models import Story, StoryMedia
from django.utils import timezone
from django.core.files.storage import default_storage



logger = logging.getLogger(__name__)
@shared_task
def delete_old_media():
    expired_stories = Story.objects.all()  # Aqui você pode filtrar por data de expiração se quiser

    for story in expired_stories:
        for media in story.media.all():
            print(media)
            try:
                # Deleta o arquivo no storage (local ou Cloudinary)
                if media.document:
                    if default_storage.exists(media.document.name):
                        print(f"Deletando arquivo no storage: {media.document.name}")
                        default_storage.delete(media.document.name)
                        logger.info(f'Arquivo deletado: {media.document.name}')

                # Deleta o registro do banco
                media.delete()
                logger.info(f'Registro do banco deletado: media ID {media.id}')
                
            except Exception as e:
                logger.error(f'Erro ao deletar media ID {media.id}: {e}')

        # Deleta a story
        story.delete()

    logger.info('Tarefa de limpeza de imagens concluída.')
