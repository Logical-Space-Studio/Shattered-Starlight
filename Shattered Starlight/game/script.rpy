image studio_logo = "assets/gui/studio_logo.png"

# CHARACTERS INITIALIZATION

image bg1 = "assets/backgrounds/bgp_01.png"

image shiina = "assets/characters/shiina.png"
image side shiina = "assets/characters/shiina_side.png"

image gigo = "assets/characters/gigo.png"
image side gigo = "assets/characters/gigo_side.png"

image kiriori = "assets/characters/kiriori.png"
image side kiriori = "assets/characters/kiriori_side.png"

image seika = "assets/characters/seika.png"
image side seika = "assets/characters/seika_side.png"

image yutsuki = "assets/characters/yutsuki.png"
image side yutsuki = "assets/characters/yutsuki_side.png"


define Shiina = Character(name = "佐佐木 诗菜", image = "shiina")
define Shiina = Character(name = "榊 义悟", image = "gigo")
define Shiina = Character(name = "榊 雾织", image = "kirioiri")
define Shiina = Character(name = "藤原 圣香", image = "seika")
define Shiina = Character(name = "浅井 优月", image = "yutsuki")


label start :
    # call common_route
    return

label common_route :

    return

label splashscreen :
    
    # Show Studio Logo before Main Menu
    scene black
    show studio_logo
    with dissolve
    pause 2.0
    hide studio_logo
    with dissolve 
    return