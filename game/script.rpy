define a = Character('Aureliene', color="#c8ffc8")
define r = Character('Ren', color="#c8c8ff")
define l = Character('Lucien', color="#ffc8c8")
define mr = Character('Morgan', color="#ffffc8")
define ar = Character('Arden', color="#ffffff")
define m = Character('Melinda', color="#c8ffff")
define abc = Character('???', color="#ffb6c1")
define v = Character('Vidir', color="#ffa500")

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
    "Ren looked as polished as alwyas. Shining impeccable armor, and stoic. Like he always was." 
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
    r "How about this... when these threats have been neutralized, I'll ask the king on your behalf if you can go out more often. Go beyond the kingdom walls, if you wish. How does that sound?"
    "Aureliene gasped."
    a "Beyond the walls?"   
    "Ren nodded."
    r "When I was training to be a guardsman, I traveled beyond the kingdom walls. There are many wonders out there. But many dangers too."
    "He gave her a look."
    r "Which is why you must stay within the castle's walls for now."
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
    "Aureliene turned to find a familiar face- that one of Morgan, a close childhood friend, and heir to the throne of an allied kingdom."
    a "Morgan? I had no idea you were coming."
    "Morgan smiled sheepishly."
    mr "I wanted to surprise you. It's been ages since I last saw you... and thought it would be a pleaseant surprise."
    "Aureliene smiled warmly."
    a "I'm glad you're here now, though. I thought I'd just have to mingle with drunken nobles like always."
    "Morgan laughed."
    mr "Not anymore! Now that I'm here, we can catch up. It's been forever!"
    mr "Do you want to go on a walk? I could use some fresh air after all this chaos."

    menu:
        "Go on a walk":
            jump walk_morgan
        "Stay and mingle":
            jump stay_mingle
    
label walk_morgan:
    a "Sure, let's go for a walk."
    "Aureliene gave Ren a look in the corner, who gave a slight nod. He feel into step a few paces behind them."
    mr "And who are you?"
    r "Her guardsman. Who are you?"
    "Morgan scoffed."
    mr "A friend."
    a "Ren... it's alright. I promise. I know Morgan very well."
    "Ren seemed wary, but he hid it."
    r "As you wish, my lady."
    "They walked out into the gardens, the rain having stopped. The air was fresh and cool."
    "Ren trailed a few paces behind them, mindful of the surroundings."
    mr "So, how have you been? It's been so long since we last saw each other."
    a "I've been well. Its been a busy few months, but I'm keeping up."
jump end_menu

label stay_mingle:
    "Aureliene smiled apologetically."
    a "Sorry, Morgan. I think I'll stay here for some time. But you're more than welcome to stay with me. I'll be a lot less bored."
    "Morgan laughed."
    m "No worries. I'll stay here with you. Mind telling me what's been going on?"
    a "Well. Honestly, not much. Just the usual palace drama."
jump end_menu

label end_menu:
    scene bg ballroom_night
    "Meanwhile, Ren's eyes scanned the area, ever vigilant."
    abc "My lord! Please, you must hurry!"
    "Ren's eyes darted to Aureliene and Morgan, before turning to the othe guardsman."
    r "What troubles you?"
    abc "It's the king! He's been poisoned!"



    scene bg ballroom_night
    "Panic Ensued."
    "Aureliene gasped."
    a "What?!"
    "The king, her father, was dead."
    "They all rushed inside."
    "The Guard Commander, Arden barked out an order, telling ryone to stay in the ballroom."
    "Everyone looked around, confused and scared. Panic was starting to set in."
    abc "What do you mean, I can't leave?!"
    abc "My daughter is at home! I need to see her!"
    a "Please, everyone remain calm. We need to get to the bottom of this."
    "A servant shrieked from the other side of the room."
    "The Queen! She's collapsed!"
    "Aureliene's heart pounded in her chest. She rushed over to her mother's side."
    "But when she pressed her fingers to the queen's neck, she found no pulse."
    "Aureliene's world seemed to shatter around her."
    a "Mother..."
    "Tears welled up in her eyes as she looked around at the chaos."    
    "Ren stood by her side, his expression grim."
    r "My lady. We will find out who is responsible for this."
    "She kept her composure, though inside she was breaking."
    a "We have to. For Father and Mother."
    "Arden nodded."
    ar "Escort the guests to any and all empty rooms we have. No one is to leave. Ren, stay with the princess."
    r "Yes, Commander."
    "Aureliene nodded, wiping away her tears."
    mr "Stay strong, Aureliene. We'll get through this together."
    r "You should stay down here. I'm going to take the princess to her chambers."
    "Morgan didn't seem to happy."
    mr "I insist on staying with her."
    "Ren looked almost annoyed."
    r "Commander Arden has given the order. You are to stay here."
    "Morgan wasn't willing to back down."
    mr "I will be holding you responsible if something happens to her."
    "Ren's expression didn't change."
    r "Understood. My lady, please come with me."

    scene bg room_day
    "Aureliene followed Ren up the stairs to her chambers, pressing her hands to her eyes."
    a "I can't believe this is happening..."
    r "My lady. We will find out who did this. I promise you."
    "Aureliene nodded, trying to steady her breathing."
    r "Judging from the number of people here, it will at least take a day or two to figure out a list of potential suspects."
    r "In the meantime, you should try to rest. I'll be outside your door if you need anything."
    a "Thank you..."
    r "And... My lady. One more thing."
    "Aureliene looked up at him.
    "Yes..?"
    "Ren hesitated for a moment."
    "But then, on of his hands took hers, holding it gently."
    r "If you need anything... at all... please don't hesitate to call for me."
    "Aureliene looked at him, surprised by the gesture. She turned her head to hide the faint blush on her cheeks."
    "Ren released her hand."
    "You must rest now. I assure you, we will find out who is responsible for this."
    "Aureliene nodded."
    a "Thank you."
    "Throught the corner of her eye, she caught Morgan's gaze- who was getting situated in the room across the hall."

    #Chapter One End
    #Chapter Two Begin
    
    scene bg room_day
    "Aureliene woke up the next morning, the events of the previous night weighing heavily on her mind."
    "Her thoughts were interrupted by a soft knock at the door."
    "She opened it to find both Arden and Ren standing at her door."
    a "Yes?"
    ar "Good morning, my lady. How are you today..?"
    a "As well as can be expected, Commander."
    a "What brings you here?"
    r " We have some news regarding the investigation."
    ar "Yes. We have identified a few potential suspects. We will be questioning them throughout the day."
    a "I see."
    ar "In the meantime, we need you to stay here. For your safety."
    a "No... I need to see who it is. I need to know who did this to my parents."
    "Arden sighed."
    a "As you say."
    mr "Wait, Wait!"
    "Morgan appeared at the door, looking determined."
    mr "I want to help with the investigation. I can be of assistance."
    r "My lord. With all due respect, this is a matter for the palace guards."
    mr "I insist. I will not leave Aureliene's side until we find out who did this."
    "Ren looked at Aureliene, who nodded slightly."

    scene dungeon room_day
    "Later that day, Aureliene found herself in a dimly lit dungeon room, facing one of the suspects- a servant who had been acting suspiciously. In total, there were ten of them. All were in different cells, separated by iron bars."
    "Aureliene looked at Arden."
    a "What of the others guests at the ball? Did you manage to question them all?"
    "Arden nodded."
    "Yes, My lady. We have questioned all of them. These ten individuals were the only ones who had any sort of motive or opportunity to commit the crime."
    "Aureliene thought for a moment. Everyone who had been invited to the ball was a noble or dignitary. They all had something to gain from the king's death."
    
    
    
    
    
    
    return