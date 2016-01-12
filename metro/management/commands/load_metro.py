# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from metro.parser import provider


class Command(BaseCommand):
    def handle(self, *args, **options):
        provider.download_all()
        print('Done')
