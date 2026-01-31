def analice():
    genero = input("Cual es su genero favotito?").lower()

    generos = {
        "progresivo": ["Pink Floyd", "Yes", "Genesis", "King Crimson", "The Mars Volta"],
        "rock": ["Queen", "Nirvana", "Guns N' Roses", "The Beatles"],
        "pop": ["Taylor Swift", "Ariana Grande", "Dua Lipa", "Ed Sheeran"],
        "hip hop": ["Kendrick Lamar", "Drake", "J. Cole", "Travis Scott"],
        "jazz": ["Miles Davis", "John Coltrane", "Ella Fitzgerald", "Louis Armstrong"],
        "classical": ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Frédéric Chopin"]
    }
    
    if genero in generos:
        print("Te recomiendo esto:")
        for artista in generos[genero]:
            print("- " + artista)
    else:
        print("Lo siento, no tengo recomendaciones para ese género.")

analice()





