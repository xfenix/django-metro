# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from metro.models import Metro, MetroLine


class Command(BaseCommand):
    def handle(self, *args, **options):
        MetroLine.objects.all().delete()
        Metro.objects.all().delete()
