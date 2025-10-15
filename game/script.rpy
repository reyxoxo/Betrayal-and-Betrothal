define a = Character('Aureliene', color="#c8ffc8")
define r = Character('Ren', color="#c8c8ff")
define l = Character('Lucien', color="#ffc8c8")
define a = Character('Arden', color="#ffffff")

label start:

    scene bg room_day
    "It was raining heavily. The sound of raindrops hitting the window filled the room."
    "Aureliene sat by the window, staring out at the gray sky."
    "A knock came at the door."

menu:
    "Do you want to open the door?"
    "Yes":
        jump ye_path
    "No":
        jump no_path

label no_path:
    "The knock came again, more insistent this time."


label ye_path:
     "Sighing, Aureline stood up and opened the door."
    r "My lady."
    "Her guardsman, Ren looked as polished as ever. Shining impeccable armor, and stoic as ever." 
    r "His Majesty is calling for your presence."
    a "I see. Thank you, Ren."


    scene bg throne_room_day
    "The throne room was grand, with high ceilings and ornate decorations."
    "King Lucien sat on his throne, looking as regal as ever."
    l "Aureliene, my dear. I trust you are well."
    a "Yes, Your Majesty. Thank you for asking."