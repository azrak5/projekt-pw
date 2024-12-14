import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Izdavac, Autor, Knjiga
from main.factories import (
    IzdavacFactory,
    AutorFactory,
    KnjigaFactory
)

NUM_PUBLISHERS = 10
NUM_AUTHORS = 10
NUM_BOOKS = 50

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Izdavac, Autor, Knjiga]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_PUBLISHERS):
            publisher = IzdavacFactory()

        for _ in range(NUM_AUTHORS):
            author = AutorFactory()

        for _ in range(NUM_BOOKS):
            book = KnjigaFactory()