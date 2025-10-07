
import os
import logging
from celery import shared_task
from Social.models import Story
from django.utils import timezone
from django.core.files.storage import default_storage



logger = logging.getLogger(__name__)

@shared_task
def delete_old_media():
    # Seleciona apenas stories expiradas
    expired_stories = Story.objects.all()

    for story in expired_stories:

        # Deleta as imagens associadas
        for media in story.story_images.all():
            try:
                if media.story_image and default_storage.exists(media.story_image.name):
                    logger.info(f"Deletando arquivo de imagem: {media.story_image.name}")
                    default_storage.delete(media.story_image.name)

                media.delete()
                logger.info(f"Registro da imagem deletado: ID {media.id}")
            except Exception as e:
                logger.error(f"Erro ao deletar imagem ID {media.id}: {e}")

        # Deleta os vídeos associados
        for media in story.story_videos.all():
            try:
                if media.story_video and default_storage.exists(media.story_video.name):
                    logger.info(f"Deletando arquivo de vídeo: {media.story_video.name}")
                    default_storage.delete(media.story_video.name)

                media.delete()
                logger.info(f"Registro do vídeo deletado: ID {media.id}")
            except Exception as e:
                logger.error(f"Erro ao deletar vídeo ID {media.id}: {e}")

        # Deleta a story
        story.delete()
        logger.info(f"Story deletada: ID {story.id}")

    logger.info("Tarefa de limpeza de stories concluída.")