define a = Character('Aureliene', color="#c8ffc8")
define r = Character('Ren', color="#c8c8ff")
define l = Character('Lucien', color="#ffc8c8")
define m = Character('Morgan', color="#ffffc8")
define ar = Character('Arden', color="#ffffff")
define abc = Character('???', color="#ffb6c1")

label start:

    scene bg room_day
    "It was raining heavily. The sound of raindrops hitting the window filled the room."
    "Aureliene sat by the window, staring out at the gray sky."
    "A knock came at the door."

menu:
    "Open the door":
        jump ye_path
    "Stay in bed":
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
    l "Good. I have a task for you."
    "She was curious as to what her father was going to ask of her."
    l "There have been"







    scene bg ballroom_night
    "That evening, the grand ballroom was filled with nobles and dignitaries from across the kingdom."
    "Aureliene entered the room, Ren at her side. He went to go stand near another entrance, taking the position of aother guard who had recently left."
    abc "Aureliene! It's been too long!"
    "Aureliene turned to find a familiar face- that one of Morgan, a close childhood friend."
    a "Morgan? I had no idea you were coming."
    "Morgan smiled sheepishly."
    m "I wanted to surprise you. It's been ages since I last saw you... and thought it would be a pleaseant surprise."
    "Aureliene smiled warmly."
    a "I'm glad you're here now, though. I thought I'd just have to mingle with drunken nobles like always."
    "Morgan laughed."
    m "Not anymore! Now that I'm here, we can catch up. It's been forever!"
    m "Do you want to go on a walk? I could use some fresh air after all this chaos."

    menu:
        "Go on a walk":
            jump walk_morgan
        "Stay and mingle":
            jump stay_mingle
    
label walk_morgan:
    a "Sure, let's go for a walk."
    "Aureliene gave Ren a look in the corner, who gave a slight nod. He feel into step a few paces behind them."
    m "And who are you?"
    r "Her guardsman. Who are you?"
    "Morgan scoffed."
    m "A friend."
    a "Ren... it's alright. I promise. I know Morgan very well."
    "Ren seemed wary, but he hid it."
    r "As you wish, my lady."
    "They walked out into the gardens, the rain having stopped. The air was fresh and cool."
    "Ren trailed a few paces behind them, mindful of the surroundings."
    m "So, how have you been? It's been so long since we last saw each other."
    a "I've been well. Its been a "
jump end_menu

label stay_mingle:
    "Aureliene smiled apologetically."
    a "Sorry, Morgan. I think I'll stay here for some time. But you're more than welcome to stay with me. I'll be a lot less bored."
    "Morgan laughed."
    m "No worries. I'll stay here with you. Mind telling me what's been going on?"
    a "Well. I'm to "
jump end_menu

label end_menu:
    scene bg ballroom_night
    "Meanwhile, Ren's eyes scanned the area, ever vigilant."
    abc "My lord! Please, you must hurry!"
    "Ren's eyes darted to Aureliene and Morgan, before turning to the othe guardsman."
    r "What troubles you?"
    abc "It's the king! He's been poisoned!"

return