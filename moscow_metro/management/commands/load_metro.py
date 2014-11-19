# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from moscow_metro.models import load


class Command(BaseCommand):
    def handle(self, *args, **options):
        load()
