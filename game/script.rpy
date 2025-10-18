define a = Character('Aureliene', color="#c8ffc8")
define r = Character('Ren', color="#c8c8ff")
define l = Character('Lucien', color="#ffc8c8")
define m = Character('Morgan', color="#ffffc8")
define ar = Character('Arden', color="#ffffff")
define m = Character('Melinda', color="#c8ffff")
define abc = Character('???', color="#ffb6c1")

label start:

    scene bg room_day
    "It was raining heavily. The sound of raindrops hitting the window filled the room."
    "Aureliene sat by the window, staring out at the gray sky. A little notebook sat in her lap, filled with sketches of the world otutside."
    "She sighed, feeling trapped within the palace walls. She could go out, yes- but rarely. And when she did, it was always with the king and queen by her side, or with a guardsman watching her every move."
    "Her only confidante was Ren, her personal guardsman. He was always by her side, protecting her from any potential threats. He was more... tolerable than the other guardsmen. At least he offered her some sort of freedom to be by herself at times."
    "Aureliene continued drawing, sketching the city outside. The carriages, cobblestone paths, and the libraries and shops she longed to visit."
    "While she was deep in thought, a knock came at the door."

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
    "Ren looked as polished as ever. Shining impeccable armor, and stoic as ever." 
    r "His Majesty is calling for your presence."
    a "I see. Thank you, Ren."


    scene bg throne_room_day
    "The throne room was grand, with high ceilings and ornate decorations."
    "King Lucien sat on his throne, looking as regal as ever."
    l "Aureliene, my dear. I trust you are well."
    a "Yes, Your Majesty. Thank you for asking."
    l "Good. I have a task for you."
    "She was curious as to what her father was going to ask of her."
    l "There have been multiple reports of criminal activity occuring, especially in the city. I want you to stay here, and not leave the palace grounds."
    a "But Father, I-"
    l "I understand your desire to go beyond the palace. However, your safety is my top priority. As both my daughter and hair to the crown, we must keep you safe"
    m "Aureliene. Listen to your father."
    a "Mother, please... I can protect myself... and I have Ren to protect me too. I told the nobles I would be coming to-"
    m "We've already told them you can come. You mustn't go, not at this time. When we know more about these threats, neutralize them, you will be able to go wherever you wish. Just... not now."
    m "Please understand, dear. We want you safe."
    "Aureliene sighed."
    a "...I understand. I'll stay here for now."
    l "Good." 
    "Lucien clapped his hands, alerting the court."
    l "You are all dismissed."

    scene bg room_day
    "Aureliene let out a sigh of annoyance as she climbed up the stairs."
    a "I can't believe this. Stuck in the palace like a prisoner."
    "Ren spoke from ehind her."
    r "My lady. You must understand that your safety is the utmost priority."
    a "You always say that."
    "Ren smiled slightly."
    r "It's true. You are the heir of this kingdom. With these recent threats and increase in crime, it is my duty to ensure your safety."
    r "How will the people react if they find out something happened to you? They see you as a beacon of light and hope. They would be distraught."
    "His eyes met hers."
    r "After all, you matter to so many people. Your parents, your people... and to me."
    "Aureliene looked up at him. But Ren's eyes were looking stright ahead."
    a "I just... it feels like I'm being caged in. Like I can't do anything."
    "Ren was quiet for a moment."
    r "How about this... when these threats have been neutralized, I'll ask the king on your behalf if you can go out more often. Go beyond the kingdom walls, if you wish.How does that sound?"
    a "It's... acceptable, I suppose."
    "Ren looked at her, a small smile on his lips."
    "That's good. First... you get used to it. Then we can talk about going beyond the walls."
    "Aureliene gaped at him."
    a "Beyond the walls?"
    "Ren nodded."
    r "When I was training to be a guardsman, I traveled beyond the kingdom walls. There are many wonders out there. But many dangers too."
    "He gave her a look."
    r "Which is why you must stay within the castles walls for now."
    "Aureliene sighed."
    r "But once the threats are gone, we can plan a trip beyond the walls."
    a "I guess... I can wait." 
    "They stopped in front of her room."
    "My lady. You should rest now. The evening's ball will be starting soon."
    a "Alright, Ren. Thank you."







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
    a "I've been well. Its been a busy few months, but I'm keeping up."
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