from celery import shared_task
from django.utils import timezone
from django.core.files.storage import default_storage
from Social.models import Story, StoryImage, StoryVideo
import logging

logger = logging.getLogger(__name__)

@shared_task
def delete_old_media():
    """
    Task que deleta stories expiradas em lotes para evitar estouro de memória.
    """
    BATCH_SIZE = 10  # Ajuste conforme o limite de memória do Railway

    # Pega stories expiradas
    expired_stories = Story.objects.all()

    if not expired_stories.exists():
        logger.info("Nenhuma story expirada encontrada.")
        return

    # Coleta todos os IDs e caminhos de arquivos
    story_ids = []
    image_paths = []
    video_paths = []

    for story in expired_stories:
        story_ids.append(story.id)
        # Coleta imagens
        for image in story.story_images.all():
            if image.story_image:
                image_paths.append(image.story_image.name)
        # Coleta vídeos
        for video in story.story_videos.all():
            if video.story_video:
                video_paths.append(video.story_video.name)

    # Deleta arquivos do storage
    for path in image_paths + video_paths:
        try:
            if default_storage.exists(path):
                default_storage.delete(path)
                logger.info(f"Arquivo deletado: {path}")
        except Exception as e:
            logger.error(f"Erro ao deletar arquivo {path}: {e}")

    # Deleta mídias e stories do banco
    try:
        StoryImage.objects.filter(post__in=story_ids).delete()
        StoryVideo.objects.filter(post__in=story_ids).delete()
        Story.objects.filter(id__in=story_ids).delete()
        logger.info(f"Deletado lote de {len(story_ids)} stories expiradas e suas mídias.")
    except Exception as e:
        logger.error(f"Erro ao deletar lote de stories {story_ids}: {e}")

    # Reagendar a task para o próximo lote
    delete_old_media.apply_async(countdown=2)