# -*- coding: utf-8 -*-
from celery import shared_task

from metro.parser import provider


@shared_task
def load_metro():
    provider.download_all()
