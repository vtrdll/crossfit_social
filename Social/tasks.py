import logging
from celery import shared_task
from django.utils import timezone
from django.core.files.storage import default_storage
from Social.models import Story, StoryImage, StoryVideo

logger = logging.getLogger(__name__)

@shared_task(bind=False)  # bind=False permite chamar direto sem self
def delete_old_media():
    """
    Task que deleta stories expiradas e seus arquivos (imagens e vídeos) do storage.
    Funciona mesmo se não houver stories ou mídias.
    """
    try:
        # Para testes, pega todas as stories
        expired_stories = Story.objects.all()  # substitua por .filter(expires_at__lte=timezone.now()) em produção

        for story in expired_stories:

            # Combina imagens e vídeos da story
            medias = list(story.story_images.all()) + list(story.story_videos.all())

            for media in medias:
                try:
                    # Deleta imagem no storage
                    if isinstance(media, StoryImage) and media.story_image:
                        if default_storage.exists(media.story_image.name):
                            default_storage.delete(media.story_image.name)
                            logger.info(f"Imagem deletada: {media.story_image.name}")

                    # Deleta vídeo no storage
                    if isinstance(media, StoryVideo) and media.story_video:
                        if default_storage.exists(media.story_video.name):
                            default_storage.delete(media.story_video.name)
                            logger.info(f"Vídeo deletado: {media.story_video.name}")

                    # Deleta o registro no banco
                    media.delete()
                    logger.info(f"Registro de mídia deletado: {media.id}")

                except Exception as e:
                    logger.error(f"Erro deletando mídia {media.id}: {e}")

            # Deleta a story
            try:
                story.delete()
                logger.info(f"Story deletada: {story.id}")
            except Exception as e:
                logger.error(f"Erro deletando story {story.id}: {e}")

    except Exception as e:
        logger.error(f"Erro geral na task delete_old_media: {e}")
