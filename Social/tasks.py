
import os
import logging
from celery import shared_task
from Social.models import Story
from django.utils import timezone
from django.core.files.storage import default_storage



logger = logging.getLogger(__name__)

@shared_task
def delete_old_media(self):
    try:
        expired_stories = Story.objects.all()  # Para teste, sem filtro
        for story in expired_stories:
            for media in getattr(story, 'story_images', []) + getattr(story, 'story_videos', []):
                try:
                    if hasattr(media, 'story_image') and media.story_image:
                        if default_storage.exists(media.story_image.name):
                            default_storage.delete(media.story_image.name)
                    if hasattr(media, 'story_video') and media.story_video:
                        if default_storage.exists(media.story_video.name):
                            default_storage.delete(media.story_video.name)
                    media.delete()
                except Exception as e:
                    logger.error(f"Erro deletando mídia {media.id}: {e}")
            try:
                story.delete()
            except Exception as e:
                logger.error(f"Erro deletando story {story.id}: {e}")
    except Exception as e:
        logger.error(f"Erro geral na task delete_old_media: {e}")