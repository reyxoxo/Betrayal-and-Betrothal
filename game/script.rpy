define a = Character('Aureliene', color="#c8ffc8")
define r = Character('Ren', color="#c8c8ff")
define l = Character('Lucien', color="#ffc8c8")
define mr = Character('Morgan', color="#ffffc8")
define ar = Character('Arden', color="#ffffff")
define abc = Character('???', color="#ffb6c1")
define v = Character('Vidir', color="#ffa500")
define t = Character('Thomas', color="#d3d3d3")
define j = Character('Jane', color="#d3d3d3" )
define c = Character('Celia', color="#d453d3" )

#Story is an epic in the language of Caerwyn, translated to out modern day english

label start:
    scene bg stairs_night
    "The halls of Silvercrest castle were dimly lit with torches, light from the flickering torches bouncing off the stones."
    "Aureliene snuck down the stairs leading to the south entrance of the palace. It was unguarded mostly, because little to no one knew of the passage."
    "At least, it was unguarded most of the time."
    "A figure smiled halfheartedly from where he was. Aureliene sighed."
    a "Ren... why are you here?"
    r "My lady. I must ask you the same thing."
    "Aureliene sighed."
    a "You are incorrigible."
    "He laughed a bit."
    r "And you, my lady, are very persistent."
    a "Why are you here anyways?"
    "Ren smiled dryly."
    "His Majesty has suspicions you'd try to sneak out. He ordered me to guard the bottom gate."
    "Aureliene groaned."
    a "And here I was, thinking that I'd finally be able to see the city for myself."
    r "You will. In due time."
    "Ren looked at her, from where she was at the top of the stairs."
    r "But now, go sleep."
    a "I refuse."
    "She went down the stairs, looking up at Ren defiantly."
    a "I command you let me pass."
    "He sighed."
    r "My lady, I cannot-"
    a "As princess to the kingdom of Elysumme, I demand you let me pass."
    "Ren sighed."
    r "Why... do you want to go so badly, anyways?"
    a "I want to know what is outside."
    "It was a simple answer, really, but it was exactly what she wanted to do."
    "Aureliene's mother had died long after she was born, and her father kept her within the palace to be protected."
    r "My lady."
    "She gave him a pleading look."
    a "Please..."
    r "I will be defying the king's orders for this. The king. You father."
    "Aureliene hesitated. She didn't want to defy her father... but she also wanted to see the world outside. How the villages were."
    "She wanted to see the people she would one day rule over."
    a "Just once. I won't ask again. I'll take the blame if someone finds us. You wont get in trouble. I swear it."
    "Ren pursed his lips once. Oh, she was so stubborn."
    "He turned to hold open the door to the south entrnce."
    r "After you, My lady."


    scene bg market_night
    "Aureliene gazed at the lights in the market. She was in awe."
    a "It's... beautiful..."
    "Ren had left his armor in the palace as well- so now he looked like an ordinary village-goer."
    r "It really is."
    "Aureliene smiled, but felt a tugging on her dress."
    abc "Would you be interested in trying a stuffed bun? It's a copper piece each!"
    "She looked down to see a child, barely seven to eight years in age. She smiled."
    a "Of course."
    "She gave the child a copper piece, and she gave her a warm bun. Aureliene bit into it, savoring the flavor of the cheese and meat within the bun."
    abc "Would your husband like one as well?"
    "Aureliene nearly choked."
    "Ren let out a quiet laugh, bending down to ruffle the child's hair."
    "I would love to try one. And she's not my wife... just a friend."
    "The child laughed, giving him a bun as well. He paid an extra copper as well. She gawked at him. Ren smiled."
    r "Keep it. The bun is delicious."
    "She looked at him in wonder." 
    abc "Really?"
    r "Of course. What's your name, little one?"
    abc "My name is Celia!"
    a "What a pretty name. I'm... Anna."
    "She heard Ren sigh in relief behind her."
    a "Do you make these buns yourself?"
    c "No, mother makes them, and I sell them."
    "Celia pointed to a figure standing near a stall."
    c "She's over there!"
    "Celia and her mother wee"


    scene bg room_day
    "It was raining heavily. The sound of raindrops hitting the window filled the room."
    "Aureliene sat by the window, staring out at the gray sky. A little notebook sat in her lap, filled with sketches of the world otutside."
    "She sighed, feeling trapped within the palace walls. She could go out, yes- but rarely. And when she did, it was always with the king and queen by her side, or with a guardsman watching her every move."
    "Her only confidante was Ren, her personal guardsman. He was always by her side, protecting her from any potential threats. He was more... tolerable than the other guardsmen. At least he offered her some sort of freedom to be by herself at times."
    "Aureliene continued drawing, sketching the city outside. The carriages, cobblestone paths, and the libraries and shops she longed to visit."
    "While she was deep in thought, a knock came at the door."

menu:
    "Open the door":
        jump yes_path
    "Stay in bed":
        jump no_path

label no_path:
    "The knock came again, more insistent this time."

label yes_path:
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
    a "Father, please... I can protect myself... and I have Ren to protect me too. I told the nobles I would be coming to-"
    l "I've already told them you can come. You mustn't go, not at this time. When we know more about these threats, neutralize them, you will be able to go wherever you wish. Just... not now."
    l "Please understand, dear. We want you safe."
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
    "Tears welled up in her eyes as she looked around at the chaos."    
    "Ren stood by her side, his expression grim."
    r "My lady. We will find out who is responsible for this."
    "She kept her composure, though inside she was breaking."
    a "We have to. For Father. And for the people."
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
    "Just as they got to the top of the stairs, the bitter smell of copper."
    "Aureliene gasped, grabbing onto Ren's arm in fear."
    "The hall was littered with dead bodies of guardsmen."
    "Ren caught her, just before she collapsed from fear."
    r "Don't look."
    "She clung to him, fear rising within her at the sight of the bodies."
    "Distantly, she could feel Ren leading her away from the carnage."

    r "Judging from the number of people here, it will at least take a day or two to figure out a list of potential suspects."
    r "In the meantime, you should try to rest. I'll be outside your door if you need anything."
    a "Thank you..."
    r "And... My lady. One more thing."
    "Aureliene looked up at him."
    a "Yes..?"
    "Ren hesitated for a moment."
    "But then, on of his hands took hers, holding it gently."
    r "If you need anything... at all... please don't hesitate to call for me."
    "Aureliene looked at him, surprised by the gesture. She turned her head to hide the faint blush on her cheeks."
    "Ren released her hand."
    r "You must rest now. I assure you, we will find out who is responsible for this."
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
    ar "Yes, My lady. We have questioned all of them. These ten individuals were the only ones who had any sort of motive or opportunity to commit the crime."
    "Aureliene thought for a moment. Everyone who had been invited to the ball was a noble or dignitary. They all had something to gain from the king's death."
    a "Very well. Let's begin."
    "The first person stepped forward- a nervous looking servant."
    ar "This is Thomas, one of the palace servants. He has been acting suspiciously since the incident."
    "Aureliene nodded."
    a "Thomas, can you tell us where you were during the ball?"
    t "I-I was in the kitchen, preparing food for the guests."
    a "Can anyone vouch for your whereabouts?"
    t "N-no... I was alone."
    "Aureliene was quiet for a moment."
    a "Okay. Let's move on."
    
    "In the cell next to Thomas's, a woman was crying, a player necklace in her hands. Her hands were clasped together as she prayed."
    a "Excuse me.."
    "The woman gasped, afraid."
    abc "M- My lady... I swear, I- I didn't do it..."
    ar "You wouldn't be here if you weren't one of the most suspicious people at the ball."
    "The lady flinched."
    abc "I- I promise- I- I didn't-"
    a 'Arden. Please, calm yourself.'
    "Aureliene looked at the woman."
    a "What is your name? And where were you at the time of the king and queen's assasination?"
    j "I- I was serving the food at the time. My n- name is Jane."
    a "If you were servin food, did you see Thomas at any time last night? Or did he see you?"
    j "N- No, your highness... I- I was in the west wing's kitchen... I- I believe he was in the south wing..."
    "She continues to sob." 
    j "P- Please don't kill me... I- I have two young children waiting for me..."
    a "I won't kill you unless you give me reason to."
    "Jane trembled, her gaze darting down, as she sobbed."
    "Aureliene looked at her sympathetically, but she new she had to move onto the next people."

    "The third and "
    

    "Aureliene paused, looking at the man in front of her."
    "He was the only one restrained by chains, unlike the others."
    "Ren moved to stand in front of her. The chained man glared at him, saying something in a language Aureliene didn't understand."
    r "What.. is he saying?"
    mr "Wait..."
    "Morgan stepped forward, his eyes widening as he recognized the language."
    mr "It's... Old Serathian. One of the languages used in Gallador."
    "Gallador- the very kingdom that Morgan was heir to."
    "Morgan asked the man a question, and the man replied in an almost sarcastic tone."
    mr "He's saying... he's innocent. That he was framed."
    "But it wasn't the language that caught Aureliene's attention. He was... different than most people Aureliene had seen."
    "What should have been te whites of his eyes were almost blue, with a faint glow to them. Veins of the same color ran along his skin, visible even through the dirt and grime covering him."
    "Not to mention, he was injured. Mustiple wounds in his legs were possibly what kept him from escaping, even from the chains as well."
    a "What... are you?"
    "The man glared at her."
    "Morgan snapped something at him in Serathian, and the man, seemed surprised. First looking at Aureliene, then Morgan."
    "The man's voice was quiet as he spoke."
    abc "Your highness... forgive me... I did not know... Caerwynn tongue is not my own...I... I do not know much... "
    a "That's okay. Can you tell us where you were during the ball?"
    abc "I was... with... lords..."
    "He looked back at Morgan, saying soemthing in Serathian. Morgan seemed surprised."
    mr "He's saying... he was with others from Gallador. His name is Vidir. He is well known among the nobles. Even I have heard his name before... but it's only today I'm meeting him."
    ar "He was also very violent. We had to chain him up numerous times. Even our best blacksmiths couldn't keep him chained. We had to sever part of his achilles tendon to keep him from escaping."
    "The man muttered something under his breath."
    a "What did he say?"
    "He said that if he was able to heal himself, this wouldn't be happening. He was... also cursing the guard commander."
    "Arden gave Vidir an angry look."
    "Aureliene looked at Vidir. The sorceror tensed."
    "Ren spoke, his voice skeptical."
    r "He is a sorcerer... yet unable to heal himself?"
    mr "That is just how magic works. It exists to help others, yet comes at the consequence of the user."
    a "Morgan.. can you tell him that we're not holding him here just solely because he's a sorceror? He was probably here due to him being in close proximity with the king, like the others here."
    "Morgan spoke to Vidir, who seemed to relax a bit."
    v "I... I am sorry. I wish you luck... to find the killer."
    "Aureliene nodded, trying to hold back her tears."
    a "We will find the killer. And bring him to justice."

    scene bg dinner_room
























































































































































































    
    
    return