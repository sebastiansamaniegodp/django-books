from django.core.management.base import BaseCommand
from ejemplo.models import Person

class Command(BaseCommand):
    help = 'Carga datos de prueba en la base de datos'

    def handle(self, *args, **options):
        # Limpiar datos existentes (opcional)
        Person.objects.all().delete()
        
        # Datos de prueba
        personas_data = [
            {'name': 'Juan Pérez', 'age': 28, 'email': 'juan.perez@email.com'},
            {'name': 'María González', 'age': 32, 'email': 'maria.gonzalez@email.com'},
            {'name': 'Carlos Rodríguez', 'age': 25, 'email': 'carlos.rodriguez@email.com'},
            {'name': 'Ana Martínez', 'age': 29, 'email': 'ana.martinez@email.com'},
            {'name': 'Luis López', 'age': 35, 'email': 'luis.lopez@email.com'},
            {'name': 'Elena Fernández', 'age': 27, 'email': 'elena.fernandez@email.com'},
            {'name': 'Pedro Sánchez', 'age': 31, 'email': 'pedro.sanchez@email.com'},
            {'name': 'Laura García', 'age': 26, 'email': 'laura.garcia@email.com'},
            {'name': 'Miguel Torres', 'age': 33, 'email': 'miguel.torres@email.com'},
            {'name': 'Carmen Ruiz', 'age': 30, 'email': 'carmen.ruiz@email.com'},
        ]
        
        # Crear los registros
        personas_creadas = []
        for data in personas_data:
            persona = Person.objects.create(**data)
            personas_creadas.append(persona)
            self.stdout.write(
                self.style.SUCCESS(f'✓ Creada: {persona.name} ({persona.age} años)')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'\n¡Seed completado! Se crearon {len(personas_creadas)} personas.')
        )
