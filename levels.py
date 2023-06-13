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
        background_image_path="assets/backrounds/default.jpg",
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
        background_image_path="assets/backrounds/default.jpg",
        character=pygame.image.load("assets/characters/priest.png"),
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



]
