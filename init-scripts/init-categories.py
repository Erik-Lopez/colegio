from categories.models import Category

categories = [
    {
        'name': "Evento",
        'color': 
    }
    {
        'name': "Noticia"
        'color': 
    }
    {
        'name': "Presentación"
        'color': 
    }
    {
        'name': "Reportaje/Opinión"
        'color': 
    }
    {
        'name': "Entrevista"
        'color': 
    }
]

for category in categories:
    Category.objects.create(
        name = category.name,
        color = category.color
    )
