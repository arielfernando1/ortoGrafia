import pygame
import level

levels = [
    level.Level(
        background_image_path="assets/backrounds/baker.png",
        character=pygame.image.load("assets/characters/baker.png"),
        words=["Hay", "Ahi", "Ay!"],
        correct_word="Hay",
        dialogue="Si ? pan"
    ),
    level.Level(
        background_image_path="assets/backrounds/tuti.png",
        character=pygame.image.load("assets/characters/mom.png"),
        words=["Valla", "Vaya", "Baya"],
        dialogue="Mijo ? a comprar a la tienda",
        correct_word="Vaya"
    ),
    level.Level(
        background_image_path="assets/backrounds/street.gif",
        character=pygame.image.load("assets/characters/rocky.png"),
        words=["Haber", "A ver", "Haver"],
        dialogue="? si te atreves",
        correct_word="A ver"
    ),
    level.Level(
        background_image_path="assets/backrounds/church.jpg",
        character=pygame.image.load("assets/characters/priest.png"),
        words=["Zumo", "Sumo", "Summo"],
        correct_word = "Zumo",
        dialogue="El sacerdote se bebió el ? sagrado"
    ),
    level.Level(
        background_image_path="assets/backrounds/poema.jpg",
        character=pygame.image.load("assets/characters/poema.png"),
        words=["Bello", "Vello", "Beyo"],
        correct_word = "Bello",
        dialogue="Me leyó el poema mas ? que escuché en la vida"
    ),
    level.Level(
        background_image_path="assets/backrounds/hostia.png",
        character=pygame.image.load("assets/characters/papa.png"),
        words=["Hostia", "Ostia", "Ostea"],
        correct_word = "Hostia",
        dialogue="El sacerdote repartió la ? durante la misa"
    ),
    level.Level(
        background_image_path="assets/backrounds/estatica.jpg",
        character=pygame.image.load("assets/characters/estatica.png"),
        words=["Vello","Bello","Veyo"],
        correct_word = "Vello",
        dialogue="La estática le movía el ? de los brazos"
    ),
    level.Level(
        background_image_path="assets/backrounds/beses.jpg",
        character=pygame.image.load("assets/characters/beses.png"),
        words=["Beses","Veces","Beces"],
        correct_word = "Beses",
        dialogue="Aunque la ?, no podrás recuperar su amor"
    ),
    level.Level(
        background_image_path="assets/backrounds/abrace.jpg",
            character=pygame.image.load("assets/characters/abrace.png"),
        words=["Abrace","Abrase","Abraze"],
        correct_word = "Abrace",
        dialogue="Solo quiero que alguien me ?"
    ),
    level.Level(
        background_image_path="assets/backrounds/abracev.jpg",
        character=pygame.image.load("assets/characters/abracev.png"),
        words=["Abracé","Abrazé","Abrasé"],
        correct_word = "Abracé",
        dialogue="Cuando lo ?, me largué a llorar"
    ),
    level.Level(
        background_image_path="assets/backrounds/danza.png",
        character=pygame.image.load("assets/characters/danza.png"),
        words=["Danza","Dança","Danzza"],
        correct_word = "Danza",
        dialogue="La ? es una forma de expresión"
    ),
    level.Level(
        background_image_path="assets/backrounds/influenza.png",
        character=pygame.image.load("assets/characters/influenza.png"),
        words=["Influenza","Influensa","Influuenza"],
        correct_word = "Influenza",
        dialogue="La ? es una enfermedad viral"
    ),
    level.Level(
        background_image_path="assets/backrounds/mundial.png",
        character=pygame.image.load("assets/characters/mundial.png"),
        words=["Mundial","Mundeaal","Mundiall"],
        correct_word = "Mundial",
        dialogue="El deportista ganó el campeonato ?"
    ),
    level.Level(
        background_image_path="assets/backrounds/albahaca.png",
        character=pygame.image.load("assets/characters/albahaca.png"),
        words=["Albahaca","Alhabaca","Aplaháca"],
        correct_word = "Albahaca",
        dialogue="La ? es una planta aromática"
    ),
    level.Level(
        background_image_path="assets/backrounds/eclipse.png",
        character=pygame.image.load("assets/characters/eclipse.png"),
        words=["Eclipse","Eclipze","Eklipze"],
        correct_word = "Eclipse",
        dialogue="Anoche hubo un ? lunar"
    ),
    #     level.Level(
    #     background_image_path="assets/backrounds/clases.png",
    #     character=pygame.image.load("assets/characters/llanas01.png"),
    #     words=["Agudas", "Llanas", "Esdrújulas"],
    #     correct_word="LLanas",
    #     dialogue="Las palabras que se acentúan cuando terminan en consonante que  no sea'N' ni'S' son: "
    # ),
    level.Level(
        background_image_path="assets/backrounds/animo.png",
        character=pygame.image.load("assets/characters/animo01.png"),
        words=["Agudas", "Llana", "Esdrújula"],
        dialogue="'Ánimo' es una palabra:",
        correct_word="Esdrújula"
    ),
    # level.Level(
    #     background_image_path="assets/backrounds/complemento.png",
    #     character=pygame.image.load("assets/characters/complemento01.png"),
    #     words=["Directo", "Indirecto", "Agente"],
    #     dialogue="¿Qué complemento verbal se puede sustituir por los pronombres 'lo, la, los, las'?",
    #     correct_word="Complemento Directo"
    # ),
    # level.Level(
    #     background_image_path="assets/backrounds/paco.png",
    #     character=pygame.image.load("assets/characters/paco01.png"),
    #     words=["Ayer", "A Maria", "Flores"],
    #     dialogue="¿Cuál es el 'Complemento Directo' en esta frase? - Paco regaló flores a María ayer.", 
    #     correct_word="Flores"
    # ),

    level.Level(
        background_image_path="assets/backrounds/verdad.png",
        character=pygame.image.load("assets/characters/verdad01.png"),
        words=["Joven", "Verdad", "Imagen"],
        dialogue="¿Cual de estas palabras no lleva tilde en su plural", 
        correct_word="Verdad"
    )

]
