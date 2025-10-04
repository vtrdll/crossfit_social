
import os
import logging
from celery import shared_task
from Social.models import Story, StoryMedia
from django.utils import timezone




logger = logging.getLogger(__name__)
@shared_task
def delete_old_media():
    expired_stories = Story.objects.all()  # FK reverso: related_name='media'

    for story in expired_stories:

        
        for media in story.media.all():
            print(media)
            try:
                if media.document and os.path.exists(media.document.path):
                    print(f"Deletando arquivo: {media.document.path}")
                    print(f"Existe arquivo? {os.path.exists(media.document.path)}")
                    os.remove(media.document.path)
                    logger.info(f'Arquivo deletado: {media.document.path}')

                media.delete()
                logger.info(f'Registro do banco deletado: photo ID {media.id}')
                
            except Exception as e:
                logger.error(f'Erro ao deletar media ID {media.id}: {e}')

        story.delete()

    logger.info('Tarefa de limpeza de imagens concluída.')

