from categories.models import Category

categories = [
    {
        'name': "Evento",
        'color': "#a48166"
    },
    {
        'name': "Noticia",
        'color': "#534439"
    },
    {
        'name': "Presentación",
        'color': "#baa89b"
    },
    {
        'name': "Reportaje/Opinión",
        'color': "#689177"
    },
    {
        'name': "Entrevista",
        'color': "#386e46"
    }
]

for category in categories:
    Category.objects.create(
        name = category["name"],
        color = category["color"]
    )
