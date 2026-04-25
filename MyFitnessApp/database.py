# database.py

PLATS = [
    {
        "nom": "Poulet au Curry et Riz Basmati",
        "type": "Déjeuner",
        "cal": 550,
        "macros": {"P": 40, "G": 55, "L": 12},
        "portions": {
            "Poulet": "150g",
            "Riz cru": "70g",
            "Crème légère": "30ml",
            "Brocoli": "150g"
        },
        "recette": [
            "Cuire le riz dans l'eau bouillante.",
            "Couper le poulet en dés et le faire dorer à la poêle.",
            "Ajouter le curry et la crème, puis laisser mijoter.",
            "Servir avec les brocolis vapeur."
        ]
    },
    {
        "nom": "Skyr Gourmand Framboise",
        "type": "Petit-déj",
        "cal": 320,
        "macros": {"P": 25, "G": 35, "L": 5},
        "portions": {
            "Skyr": "250g",
            "Framboises": "100g",
            "Muesli sans sucre": "40g",
            "Beurre de cacahuète": "10g"
        },
        "recette": [
            "Verser le skyr dans un bol.",
            "Ajouter les framboises fraîches.",
            "Saupoudrer de muesli et ajouter le beurre de cacahuète."
        ]
    }
]

MACHINES = ["Presse à cuisses", "Dips", "Tirage vertical", "Développé assis"]