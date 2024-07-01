from celery import shared_task
from .models import Question
import logging
logger = logging.getLogger(__name__)

@shared_task
def get_latest_question():
    logger.info('Logging last published question...')
    latest_questions = Question.objects.latest('pub_date')
    logger.info(f'"{latest_questions.question_text}" published by "{latest_questions.author}"')