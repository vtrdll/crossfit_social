from WOD.models import Movement, MOVEMENT_TYPE_CHOICES


def populate_movements():
    for category, movements in MOVEMENT_TYPE_CHOICES:
        for value, label in movements:
            
            obj, created = Movement.objects.get_or_create(
                name=label,  
                type=category,
                defaults={"description": f"Movimento do tipo {category.lower()}"}
            )
            if created:
                print(f" Criado: {label} ({category})")
            else:
                print(f"Já existia: {label} ({category})")

populate_movements()