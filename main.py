from category import Category

if __name__ == "__main__":
    
    cat = Category(name="Filmes", description="Categoria de filmes em geral")
    print("Categoria criada:", cat.to_dict())

    data = cat.to_dict()
    new_cat = Category.from_dict(data)
    print("Reconstruída a partir do dict:", new_cat.to_dict())

    cat.update(name="Filmes e Séries", description="Filmes e séries populares")

    cat.deactivate()
    cat.activate()

    print("\nEventos disparados:")
    for event in cat.events:
        print(event)