from django.core.management.base import BaseCommand
from WOD.scripts import populate_movements

class Command(BaseCommand):
    help = "Popula os movimentos iniciais"

    def handle(self, *args, **kwargs):
        populate_movements()
        self.stdout.write(self.style.SUCCESS("Movements populados com sucesso!"))