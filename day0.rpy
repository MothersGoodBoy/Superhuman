label intro:
    "Are you 18 or over?"
    menu:
        "Yes":
            jump canplaysuperhuman
        "No":
            jump cannotplaysuperhuman

    label cannotplaysuperhuman:
    "Then you're out of here."
    $ MainMenu(confirm=False)()

    label canplaysuperhuman:
    "Alright then. Forgive the early game art, I'll update it over time. Anyway, let's get started."
    play music "audio/ambientpark.mp3"
    scene white with dissolve
    You "Ugh… I feel sick… "
    scene parkblurry1 with dissolve
    You "my head is killing me."
    show wake with dissolve
    You "Why is it so bright… goddamn. Wait, where am I?"
    scene parkblurry1 with dissolve
    show parkblurry2 with dissolve
    show parkday with dissolve
    hide wake
    "My eyes slowly adjust to the light and I take a look around"
    You "(Bill's Park... I used to come here with my dad when mum was alive.)"
    show wake with dissolve
    hide parkday
    You "(But why the hell am I waking up here?)"
    You "What happened last night?"
    "I push myself up slowly, trying not to aggravate my aching head."
    stop music fadeout 1.0
    play sound "audio/dogbark.mp3"
    Unknown "*bark* *bark*"
    show parkday
    show dog
    with dissolve
    "I look up and see a dog approaching me. It's large and shaggy, with a pure black coat of fur. "
    You "Hey there boy, calm down..."
    show sniffhand with dissolve
    hide parkblurry1
    "I resist the urge to sprint in the opposite direction and hold my hand out for it to smell."
    "It starts sniffing me and after a few seconds seems to accept me as a friend."
    "I reach out to give it a pat on the head."
    show parkblurry1 with hpunch
    You "Arrrgh!!!"
    "As my hand makes contact with the dog my head starts spinning and a rush of stray thoughts enter my mind."
    scene black with dissolve
    "Intense smells of all kinds stronger than I've ever experienced and a black and white sequences of a beautiful young woman caring for me."
    "The sudden onrush of memories causes me to fall back on my ass and groan in pain, my headache twice renewed."
    You "Ugh, What the fuck just happened?"
    Unknown "Hey, are you alright?"
    You "Huh?"
    play music "audio/park.mp3"
    show emilyw sad with dissolve
    "I look up to find a woman looking down on me, the same woman I saw in my memories a moment ago."
    You "(Do I know her?)"
    show emilyw sadt with dissolve
    Unknown "You ok?"
    show emilyw sad with dissolve
    "She feels so familiar... and yet the only memory I can find of her is the one I recalled a few seconds ago..."
    Unknown "You're not hurt, are you?"
    You "(It's the strangest thing, for some reason I feel safe with her near me, who is this girl?)"
    Unknown "Uh, hello?"
    "Shocked out of my thoughts I realize she's talking to me"
    You "Oh, sorry. I kind of zoned out a bit there. What were you saying?"
    show emilyw nt with dissolve
    Unknown "Uh, no problem. I was just asking if you're alright. I saw you on the ground with my dog circling you and, uh.... "
    Unknown "She didn't attack you, did she?"
    show emilyw n with dissolve
    You "Hm? Oh, no. I just had a dizzy spell or something. I've had this killer headache since I woke up."
    show emilyw nt with dissolve
    Unknown "Phew... That's good..."
    Unknown "Not about your headache obviously, I'm just glad Shadow isn't causing me more trouble. Damn dog runs off every chance she gets."
    show emilyw n with dissolve
    You "(Shadow huh? So that's the dog's name, at least she seems friendly.)"
    You "Excuse me, um, have we met before? You seem really familiar."
    show emilyw qt with dissolve
    Unknown "Uhhhhh I don't think so? I've never seen you before at least."
    show emilyw q with dissolve
    "No surprise there, I don't even know her name. But then, what is this feeling? What was that memory?"
    You "Do you mind if I ask you your name?"
    show emilyw qt with dissolve
    Emily "Emily, why?"
    show emilyw q with dissolve
    You "Huh, doesn't ring a bell."
    show emilyw nt with dissolve
    Emily "Thought as much, maybe I just look like someone you know."
    show emilyw n with dissolve
    You "(With an appearance like hers? Not likely.)"
    You "Hmmm, maybe."
    "I reach out my hand so that she can help me up and after a moment of hesitation, she grabs it."
    show shakehands with dissolve
    "Another wave of dizziness comes over me as she pulls me to my feet, but I focus hard on suppressing it and manage to get it under control."
    You "Well, my name is"
    $ name = renpy.input("What is your name?")
    $ name = name.strip()
    $ persistent.protagonist_male_name = name
    $ sname = renpy.input("And what's your family name too while I'm asking.")
    $ sname = sname.strip()
    $ persistent.protagonist_sur_name = sname
    $ familynamegiven = True
    You "[name]."
    You "(She's shorter than I thought she was.)"
    Emily "[name] huh? Well good to meet you, I guess."
    You "(She seems a lot less interested in me now that she knows her dog didn't accost me.)"
    Emily "Well anyway, I should be heading home, so I'll see ya around. Kay?"
    "She walks past me, her dog following close behind."
    show armstretch1 with dissolve
    stop music fadeout 1.0
    You "Hang on, wait!"
    "Unable to shake this feeling that I know her, I reach out my arm and- "
    play sound "audio/stretch.mp3"
    show armstretch2 with dissolve
    You "Wha!?"
    "My arm actually stretches out! It's almost like I've dislocated it from my socket and am waving it about. But this length... that's not natural."
    You "(What the fuck is this!?)"
    "Just before my outstretched arm touches Emily's shoulder I pull it back, and... it shortens back into its normal length."
    play sound "audio/stretch.mp3"
    hide armstretch2 with dissolve
    You "What in the world..."
    You "I've got to get home!"
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    play music "audio/walk.mp3"
    show walkhome with dissolve
    "I keep stretching my arms in and out as I walk home. Surprisingly it's fairly easy to repeat and the lengths I can to are pretty incredible."
    "I got as far as about 10 meters before I saw someone across the street and had to pull it back."
    show walkhome b
    show mcb n at left2
    with dissolve
    You "Just what is going on with me?"
    Unknown "That's what I would like to know."
    show mcb ans with hpunch
    You "Waaaaagggghhh!"
    "The voice scares the crap out of me, did they see what I was doing?"
    show mcb nt flip
    show amber nt at right2
    with dissolve
    Amber "Jeeze, what's up your butt?"
    show amber n with dissolve
    show mcb n flip with dissolve
    You "(Phew, it's just Amber, an old high school classmate. But... did she see anything?)"
    show mcb nt flip with dissolve
    You "Yo Amber, it's been a while. How's it going?"
    show amber nt with dissolve
    show mcb n flip with dissolve
    Amber "Not bad. You're looking... big."
    show amber n with dissolve
    You "(Big? Shit, does she mean my arms? Did she see them?)"
    show mcb nt flip with dissolve
    You "Um... big?"
    show amber st with dissolve
    show mcb n flip with dissolve
    Amber "Yeah, that's some growth spurt you've had. It hasn't even been a couple months since I last saw you."
    show mcb nt flip with dissolve
    You "Growth spurt?"
    "I look down at my body."
    show black
    with dissolve
    You "(Holy shit!)"
    "My arms, even without stretching them, are too long for the sleeves of my hoodie. Likewise, my ankles are completely bare, my jeans barely covering my shins."
    You "(Earlier I had thought Amber was looking a little shorter than usual, but it was me that's grown! Can I grow any part of my body? Is that what's happening?)"
    hide black
    show amber nt
    with dissolve
    Amber "Anyway let's go. I was just about to head to your place."
    show amber n flip with dissolve
    hide amber with moveoutright
    "Amber takes off in the direction of my house, expecting me to follow."
    scene walkhomeamber 1 with dissolve
    You "What? Uh, my place?"
    show walkhomeamber 1t with dissolve
    Amber "Yeah? The three of us agreed to train it to college together. Remember?"
    show walkhomeamber 1 with dissolve
    You "Huh? College?"
    You "(Shit! What day is it?)"
    show walkhomeamber 2t with dissolve
    Amber "Yeah? Jeeze how drunk did you get last night? We told you not to get too fucked up, it's your first friggin day of college and you smell of booze."
    You "(Last night?)"
    scene bar
    show deryl celeb flip at left4
    show daryl n flip behind jordan at left2
    show jordan n flip at left
    show mc n at right3
    with hpunch
    You "(That's right, we were celebrating my 18th birthday, how could I forget!!!)"
    You "(We drank and we-)"
    Amber "[name]! Where are you zoning off to?"
    scene walkhomeamber 2 with dissolve
    You "Huh? What? Nowhere."
    show walkhomeamber 1t with dissolve
    Amber "Uhuh, well Liz isn't coming. She's got a meeting with some big shot, so it'll just be the two of us."
    show walkhomeamber 1 with dissolve
    You "(Shit, I did promise to go with her. But with what's happening to my body I really don't have time for it, or college for that matter.)"
    You "Listen Amber..."
    show walkhomeamber 2a with dissolve
    Amber "I don't want to hear it! You're coming! I'm not going through my first day of college alone with Deryl just because you've got a hangover! It's bad enough that Liz is ditching me."
    You "(*sigh* I've been a pretty shit friend to Amber lately. Ever since Liz shot me down I've been avoiding the two of them, barely even just texting.)"
    show walkhomeamber 2 with dissolve
    You "Fine, fine. I'll come. But I'll need to take a different train. I've got to deal with some stuff at home first. Take a shower, change my clothes and all that."
    show walkhomeamber 1t with dissolve
    Amber "Hmph, fine, I guess you do need a change of clothes. Try and find something your own size at least."
    You "(Shit, she's right, my old clothes are too small for me now. I wonder if I can take some of Dad's stuff...)"
    show walkhomeamber 2t with dissolve
    Amber "Anyway, I'm heading to the train station."
    Amber "First class starts in an hour and a half; I better see you there."
    "With that Amber heads off to the train station and I continue on home"
    scene black with dissolve
    You "What's going on with me? First my arms and now my whole body? It all started this morning at the park... or was it before even that?"
    stop music fadeout 1.0
    "As I continue my walk home, I cast my mind back to last night"
    You "(Think [name], think. What exactly happened last night?)"
    play music "audio/club.mp3"
    scene bar with dissolve
    show bar b
    show deryl n flip at left4
    show daryl n flip behind jordan at left2
    show jordan n flip at left
    show mc n at right2
    with dissolve
    You "I went out drinking to celebrate my 18th birthday."
    show deryl celeb flip with dissolve
    Deryl "Woooo! 18 at last! Congrats buddy!"
    show deryl n flip at left4
    show mc nt
    with dissolve
    You "What do you mean “at last”? You guys only turned 18 a couple of weeks ago."
    show mc n
    show deryl nt flip
    with dissolve
    Deryl "And we’ve been drinking every night since, haha!!"
    show deryl n flip
    show jordan nt flip
    with dissolve
    Jordan "You guys are lucky, it’s gonna be another 5 months til my eighteenth."
    show daryl nt
    show jordan n flip
    with dissolve
    Daryl "Yet here you are drinking with us."
    show jordan ant flip
    show daryl n
    with dissolve
    Jordan "Not so loud dude! I don’t wanna get tossed outa here."
    scene black with dissolve
    "Yeah, that’s right. I was with my buddies Jordan, Deryl and Daryl. We’re kind of a weird bunch, but we know how to have a good time with each other."
    scene bar b
    show deryl n flip at left4
    show daryl n flip behind jordan at left2
    show jordan n flip at left
    show mc n at right2
    with dissolve
    Deryl "So college huh? Man how time flies…"
    show jordan nt flip
    show deryl n flip
    with dissolve
    Jordan "Can’t come soon enough if you ask me, I fucking hated our school, right [name]?"
    menu:
        "It was't so bad":
            call AintSoBad from _call_AintSoBad
        "Yeah it sucked":
            call YeahItSucks from _call_YeahItSucks
        "Meh":
            call Meh from _call_Meh

    show deryl nt at left4
    show daryl n flip behind jordan at left2
    show jordan nt flip at left
    show mc n at right2
    with dissolve
    Deryl "Welp it'll be a new start for you guys, college soon. Man, I can't wait!"
    show deryl nt
    show jordan nt flip
    with dissolve
    Jordan "Yeah, sucks you and [name] aren't with us though."
    show jordan n flip
    show mc nt
    with dissolve
    You "Yeah, I know. We'll be breaking the team up."
    show mc n
    show jordan nt flip
    with dissolve
    Jordan "Hey you could have come with us, but you had to go to a fancy school."
    show jordan n flip
    show mc nt
    with dissolve
    You "Not like I got a say in the matter."
    show mc n
    show deryl nt flip
    with dissolve
    Deryl "Don't be such a downer, it's the best college in the country, maybe even the world. The kinda tech that's come outta that place... Man, it's gonna be awesome! I mean who wouldn't want to go to the university that literally cured cancer?"
    show deryl n flip
    show mc nt
    with dissolve
    You "Me?"
    show mc n
    show daryl st flip
    with dissolve
    Daryl "How'd you even get in anyway? I mean I get this freak making it in, people being calling my bro a genius since we were like 4 years old."
    show daryl nt flip
    with dissolve
    Daryl "But you dude? I mean your grades are good and all, don't get me wrong, but you ain't a genius; and you ain't that rich either."
    show daryl n flip
    show mc nt
    with dissolve
    You "*sigh* it was my dad, I told you he does some weird shit for the government right? He pulled some strings and got me in."
    show mc n
    show jordan nt flip
    with dissolve
    Jordan "Damn, sounds nice."
    show jordan nt flip
    show mc ant
    with dissolve
    You "Not really, I don't even get to choose my own college."
    show mc n
    show deryl nt flip
    with dissolve
    Deryl "Relax dude, I'm sure we'll have a great time. Rubbing shoulders with all the rich kids."
    show deryl laugh flip
    Deryl "Maybe even land ourselves a sugarmomma!"

    menu:
       "If you say so":
           call ifyousayso from _call_ifyousayso
       "Sounds terrible":
           call soundsterrible from _call_soundsterrible

    show deryl nt flip at left4
    show daryl nt flip behind jordan at left2
    show jordan n flip at left
    show mc n at right2
    with dissolve
    Daryl "Well, college aside, look who's finally here"
    show daryl n flip
    show ellaintro
    with dissolve
    "I look behind me and spot my pal Dave with a dark-haired babe on his arm."
    You "Damn, who's that?"

    Daryl "Ella, Dave's new girl."
    show black with dissolve
    with dissolve
    "That's right! Dave brought his crazy girlfriend out with us!"
    hide black
    with dissolve

    Jordan "Woah, that’s Ella? I thought he just made her up."

    Deryl "Damn, she's hot."

    Jordan "What's she doing with friggin Dave?"

    You "Don't ask me."

    Deryl "Shut up, they’re coming this way."
    hide ellaintro
    show deryl m flip
    show mc n flip at right4
    show daryl nt flip
    with dissolve
    Daryl "Yo Dave, what’s going on?"
    show daryl n flip
    show dave nt at right
    show ella h at right2
    with dissolve
    Dave "Hey guys, I see you started without me. Sorry I’m late."
    show dave n
    show daryl nt flip
    with dissolve
    Daryl "I see you’ve brought someone"
    show daryl n flip
    show dave nt
    Dave "Ha, yep. Let me introduce you to Ella."
    show dave n
    show ella nt
    Ella "Hey guys, nice to meetcha. Hi [name]..."
    "How does she know my name?"
    You "Uh..."

    menu:
       "Hi":
           call Hi from _call_Hi
       "Do we know each other?":
           call Wtf from _call_Wtf

    ".............."
    show dave nt
    Dave "Soooo, what was up with that?"
    show dave n
    show daryl nt flip
    Daryl "You know her [name]?"
    show daryl n flip
    show mc nt flip
    You "Not at all, at least as far as I can remember."
    show deryl nt flip
    show mc n flip
    Deryl "Damn, and here I thought you had a thing with her, she was giving you that look."
    show deryl sadt flip
    Deryl "Uh, no offense Dave."
    show deryl sad flip
    show dave s
    Dave "Hm?"
    show dave st
    Dave "Oh, don't worry about it. To be honest I don't think we're going anywhere, she's too fucking weird for me."
    show deryl s flip
    show dave s
    show mc nt flip
    You "What do you mean?"
    show mc n flip
    show dave st
    Dave "Well get this, you know all those Satanist nutjobs who worship the devil and like kill goats and shit? Well, she's into all that."
    show dave s
    show deryl qt flip
    Deryl "Damn, seriously?"
    show deryl n flip
    show dave st
    Dave "Oh yeah, I found cut up animal body parts and weird symbols and shit at her place while we were hangin out. She didn't even try to hide it man, it was messed up."
    show dave s
    show daryl nt flip
    Daryl "Then why'd you bring her here?"
    show dave nt
    show daryl n flip
    Dave "Haha... well, when I told her I was going out to celebrate [name]'s birthday she got really excited and insisted on coming. Said she wanted to 'meet my friends'."
    Dave "I wasn't gonna bring her at first but she uh, made a really convincing argument."
    Dave "But yeah, I gotta get outta this thing before she ends up asking me to sacrifice a goat and have sex on top of it or something. *shudder*"
    Dave "Actually, do you wanna take her off me hands [name]? Deryl's right, she did seem kinda into you."
    menu:
       "What? No!":
           call whatno from _call_whatno
       "Well...":
           call well from _call_well

    show ella nt at right2 with moveinright
    Ella "Hey guys! I got us a couple of jugs, let’s go crazy!!"
    "All the guys look at me."
    "Jeeze, what a weird situation."
    You "Uh, yeah, let's drink!!!"
    show black with dissolve
    "The next few hours were a blur."
    hide black
    show mcdrink
    with dissolve
    "I drank"
    "I drank a lot..."
    show ellakissdave with dissolve
    "I remember Ella making out with Dave…"
    Deryl "Haha, now it’s a party!"
    hide ellakissdave
    show ellakissmc2
    with dissolve
    "And with me..."
    "Oh shit."
    show ellakissmc1 with dissolve
    You "What are you-"
    Ella "Dave told me you were into me"
    You "Hang on, I-"
    show ellakissmc with dissolve
    You "Mmmph"
    "She kisses me again, but this time I feel her push something small into my mouth, and before I can even register what it was, I swallow it instinctively."
    hide ellakissmc1
    show ellakissmc1
    with dissolve
    You "*cough* *hack* What the fuck was that?"
    Ella "Haha, just a little something to make this party even more fun. Trust me, you’ll thank me later."
    show black with dissolve
    "That’s right!!! She fucking roofied me or something! That crazy bitch! Godammit, I’ve gotta try and remember, what happened next? What did she do to me?"
    hide black with dissolve
    Ella "C'mon, come with me a sec."
    "Ella drags me off to a remote corner of the club."
    stop music fadeout 1.0
    scene barback with dissolve
    show mc nt at right3
    show ella h at left3
    show barback b
    with dissolve
    You "Hey, hang on a second"
    show ella st flip
    show mc n
    with dissolve
    "Ella let's go of my hand and turns around"
    Ella "So how're you feeling?"
    show mc nt
    show ella s flip
    with dissolve
    You "Uh... fine?"
    show ella st flip
    show mc n
    with dissolve
    Ella "No headaches? No urge toooo... cough up blood?"
    show mc nt
    show ella s flip
    with dissolve
    You "What? No?"
    show ella laugh flip
    show mc n
    with dissolve
    Ella "Perfect!!!"
    show ella ht flip with dissolve
    Ella "I knew you were the one!!!"
    show ella sigh flip with dissolve
    Ella "At last..."
    "She's looking incredibly pleased with herself."
    show mc nt
    show ella s flip
    with dissolve
    You "Why are you aski-"
    show mc ans
    with hpunch
    You "Wait, is this about that pill you gave me!?"
    show mc n
    show ella ss flip
    with dissolve
    Ella "Huh? No, not at all, I'm just uuuuhhh, making sure you're healthy!"
    show ella ht flip with dissolve
    Ella "Hehe"
    "I don't like the way she's looking at me, she's obviously up to something. Dave was right, she's a nutjob."
    show mc nt
    show ella n flip
    with dissolve
    You "Uhuh, I'm going to the bathroom."
    show mc n
    show ella st flip
    with dissolve
    Ella "Hm? Ok, I'll wait here for you."
    show mc nt
    show ella s flip
    with dissolve
    You "You don't have to-"
    show mc n
    show ella ht flip
    with dissolve
    Ella "I know, I'll wait here for you"
    show mc n
    show ella h flip
    with dissolve
    "..........."
    show mc nt
    show ella h flip
    with dissolve
    You "*sigh* Alright, do what you want."
    show mc n
    show ella ht flip
    with dissolve
    Ella "I always do."

    scene clubbathroom with dissolve

    "I sit on the can thinking about the events of tonight"
    You "Dave you fucker, trying to dump this chick on me."

    menu:
       "She's pretty hot though":
           call shesprettyhotthough from _call_shesprettyhotthough
       "I gotta try and stay away from her":
           call igottatrytostayawayfromher from _call_igottatrytostayawayfromher

    You "*sigh* I guess I better head back, she's waiting for me."

    scene barback
    with dissolve
    play music "audio/fight.mp3"
    Unknown "Hey babe, c'mon back with us. We'll show you a really good time"
    Ella "Dream on dickwipe, besides, I'm already here with someone."
    show barback b
    show bargang at right
    show ella an at right1
    with dissolve
    Unknown "Chill honey, I guarantee you'll have a better time if you leave with us. Or maybe just a quick trip to the bathroom?"
    "Looks like a few meatheads are harrassing Ella"
    "Should I help her out, or..."
    menu:
       "Help her out":
           call helpherout from _call_helpherout
       "Leave her":
           call leaveher from _call_leaveher

label barfightbranch:
    "As I'm about to ask her for details I see Deryl walking up to us."
    show ella h flip at left
    show mc n flip at left2
    show deryl nt at right
    with dissolve
    Deryl "Hey you two, you've been gone a while, whatcha been up to?"
    show deryl n with dissolve
    You "(By the way he's grinning at me I'd say his fucked up imaginations got a few ideas.)"
    show deryl nt with dissolve
    Deryl "Hate to interrupt but Daryl made me come and get you, Dave's passed out so we're gonna take him home."
    show deryl n
    show ella sigh flip
    with dissolve
    Ella "*sigh* Dave's not much of a drinker, is he?"
    show ella s flip
    show mc nt flip
    with dissolve
    You "Nope."
    show mc n flip with dissolve
    show mc nt flip with dissolve
    You "Alright Deryl, we'll head out with you."

    scene black
    with dissolve

    play music "audio/walk.mp3"
    scene outsidebar behind deryl with dissolve
    show outsidebarb behind deryl
    show ella n at right
    show deryl n flip at left4
    show daryl n flip behind jordan at left2
    show jordan n flip at left
    show mc n at right3
    with dissolve
    show daryl nt flip at left2 with dissolve
    Daryl "Alright guys, me and Deryl are gonna take Dave home, I think he's had a bit too much. You guys good?"
    show daryl n
    show deryl n
    show mc n
    with dissolve
    show ella n
    show jordan nt flip
    with dissolve
    Jordan "Actually you mind if I catch the cab back with you? I'm gonna crash at my dad's place today, he lives close to Dave."
    show jordan n flip
    show deryl nt
    with dissolve
    Deryl "No prob. "
    show deryl nt flip
    with dissolve
    Deryl "What are you two gonna do?"
    show daryl n flip
    show deryl n flip
    show mc nt
    show ella n
    show jordan n flip
    with dissolve
    You "My place is the other way, so I'll call another taxi."
    show mc n
    show ella nt
    with dissolve
    Ella "Me too."
    show ella n
    show deryl mt flip
    with dissolve
    Deryl "Oh yeah? You guys should totally taxi together!"
    show deryl m flip
    with dissolve
    "Deryl slips you a sly smile."
    show ella ht
    with dissolve
    Ella "That sounds like a great idea!"
    show deryl nt flip
    show ella h
    with dissolve
    Deryl "Sweet. Alright, we're heading off. Have fun."
    show deryl m flip
    with dissolve
    "Deryl gives you another quick smirk before he and Daryl carry Dave over to the taxi with Jordan following behind."
    show deryl m
    show daryl n
    show jordan n
    with dissolve
    hide deryl
    hide daryl
    hide jordan
    with moveoutleft
    show ella h at right4
    show mc n at left3
    with dissolve
    "As you watch your friends head out together you suddenly feel yourself swaying a bit."
    You "(Shit, I think I had a bit too much to drink as well. I'm having trouble standing.)"
    show ella ss
    with dissolve
    Ella "Hey, are you ok?"
    show ella s
    show mc nt flip
    with dissolve
    You "Yeah, I'm fine. Just had a bit too much to drink."
    show mc n flip
    show ella ht
    with dissolve
    Ella "Haha, yeah, I can tell... "
    "............."
    show ella s flip with dissolve
    "............."
    show ella ss flip with dissolve
    Ella "Hey, look! There's a park just across the street. "
    show ella st with dissolve
    Ella "Wanna have a lie down on the grass while we wait on our taxi?"
    show ella s with dissolve
    "A feeling of nostalgia comes over you as you look across the street."
    show black with dissolve
    show parkday with dissolve
    "Bill's Park, you used to play here a lot as a kid with your dad. Playing hide and seek in the forest, running around in the playground. Good times..."
    hide parkday with dissolve
    hide black with dissolve
    show mc nt flip with dissolve
    You "Yeah, that sounds like a good idea."
    stop music fadeout 1
    show mc n flip
    show ella st
    with dissolve
    Ella "Nice, c'mon."
    show ella n flip with dissolve
    hide mc
    hide ella
    with moveoutright
    show black with dissolve
    "Ella and I cross the street and make our way to the park. As soon as we arrive Ella dives onto the grass and does a somersault, landing on her back."
    play music "audio/ella.mp3"

    show forest ella with dissolve
    You "(I guess the liquor's finally getting to her.)"
    You "(But damn, if I tried that right now, I'd be spewing everywhere. Just watching almost had me ready to barf.)"
    "Ella pats the ground next to her"
    show forest ellacome with dissolve
    Ella "You coming?"
    You "Yeah, I'm coming"
    show forest mcella with dissolve
    "I set myself down beside her and look up at the stars."
    "............"
    show forest ellatalk with dissolve
    Ella "So... what did David tell you about me?"
    show forest mctalk with dissolve
    You "Huh? What?"
    "Looking over at Ella, I notice she's wearing a somewhat somber expression"
    show forest ellatalk with dissolve
    Ella "He's been trying to dump me on you all night. It was pretty obvious. "
    show forest ellatalktomc with dissolve
    Ella "Not that I mind, though."
    show forest ellatalk with dissolve
    Ella "I bet he wasn't even really passed out. That's why your friends insisted that they be the ones to take him home, right?"
    You "(That does sound about right to be honest.)"
    show forest mctalk with dissolve
    You "Umm..."
    show forest ellatalk with dissolve
    Ella "Don't sweat it, I'm not mad or anything, I could already tell he was starting to lose interest in me. I'm just curious what he told you..."
    show forest mctalk with dissolve
    You "Well... he-"

    menu:
       "Said you were crazy":
           call saidyouwerecrazy from _call_saidyouwerecrazy
       "Said you were hot":
           call saidyouwerehot from _call_saidyouwerehot

    scene forestmcella
    "............."
    show forest ellatalk with dissolve
    Ella "*sigh* It's a hard thing to get someone to really care about you, to love you... you know?"
    You "..."
    show forest ellatalk with dissolve
    Ella "I always thought it was all about how good you look or how much money you have. And I worked so hard to be like that, but..."
    show forest mcella with dissolve
    "................"
    show forest ellatalk with dissolve
    Ella "You hear on T.V and shit about how love should be all about what's on the inside, that it's the heart that matters... and all that sappy shit. "
    Ella "I wonder if there's any truth to that?"
    show forest ellatalktomc with dissolve
    Ella "I'm pretty hot, right? I have money now too, and yet..."
    show forest ellatalk with dissolve
    Ella "*sigh* sorry, here I am getting into all this heavy shit and I barely even know you."
    show forest mctalk with dissolve
    You "Uh, about that. When we first met, how did you know my name?"
    show forest ellatalktomc with dissolve
    Ella "Oh? Uh, Dave told me"
    show forest mctalk with dissolve
    You "Oh... ok."
    show forest ellatalktomc with dissolve
    Ella "Um, anyway, I'm going to head to the ladies room."
    stop music fadeout 1
    show forest mc with dissolve
    "Ella gets up and heads back towards the bar, leaving me sitting alone"
    play music "audio/ambientpark.mp3"
    You "(Damn, how long is this taxi gonna take? Feels like I've been lying here for ages.)"
    show parknight with dissolve
    "Feeling a little more sober after that last conversation, I decide to get up and have a little walk around."
    You "(Ella's taking her time too, damn. I'm getting a little bored."
    You "(*sigh* Should I really try and make a move on her? Dave seemed all for it, and she kissed me earlier but...)"
    "I hear grass ruffling behind me in the distance and turn around.)"
    You "Hey Ella, finall-"
    stop music fadeout 1
    show monsterintro1 with dissolve
    "Instead of seeing Ella, I am faced with the silhouettes of two extraordinarily tall individuals, they must both be at least 7 feet..."
    play music "audio/horror.mp3"
    You "What-"
    "They're coated in shadow and still not clearly visible, but a chill goes down my spine just looking at them"

    show monsterintro2 with dissolve
    You "-the fuck..."
    "I take a step back as the figures draw closer and out of the shadows, their grotesque forms coming into view. "
    "One with thick, writhing tentacles all across its body, and another with no arms and what looks like tentacles as it’s hair."
    "But what unnerves me most of all is the fact that neither of them has a face."
    You "A-a-am I losing my mind?"
    "I back away further, almost tripping over my own feet."
    "The figures draw yet nearer still, their malformed bodies looking ever more terrifying as they get closer"
    show monsterintro3 with dissolve
    You "(T-t-they're coming towards me...?)"
    "Their movements are so fluid and serene that it's difficult to tell when they're moving"
    show monsterintro4 with dissolve
    "Fear lances through my body as the darker one reaches out it's arm, its tentacles expanding, stretching out towards me."
    You "Oh shit!"
    play music "audio/suspense.mp3"
    scene parkspeed1 with hpunch
    "Suddenly a lot more sober than I was two seconds ago I turn around and sprint as fast as I can away from the two."
    You "Ha....Ha...Ha...."
    show black with dissolve
    You "*cough* *pant*"
    show parkspeed2 with dissolve
    You "Ha... Ha..."
    "My breath is ragged; trees rush past me as I sprint through the park"
    "Ordinarily I'd know this park like the back of my hand, but right now it feels like a maze, fear and confusion clouding my mind."
    "Too afraid to look behind me and see those things on my tail, I keep running aimlessly."
    scene black with dissolve
    You "Fuck... *pant* ...fuck"
    show parkspeed3 with dissolve
    "Dodging trees and stumbling over rocks. I am nicked and scratched by stray branches as I run."
    "My lungs are on fire; they haven't seen this kind of abuse in my life time. My breath goes from haggard pants to hollow wheezing."
    "I'm decently athletic, but no one can keep up a full speed sprint forever"
    You "(I'll die if don't keep running, they'll kill me for sure.)"
    show parkspeed4 with dissolve
    "Eventually I can't take it anymore and slow to a walk, nervously looking over my shoulder to make sure I've lost my pursuers."
    You "*Sigh* Alright, I don’t think they’re following me, thank Christ."
    show forestpath with dissolve
    "I continue forward and eventually find myself at the old bike track."
    You "Phew, something I recognize at last."
    You "But... do I go left or right? It’s been ages since I’ve ridden down here..."


    menu:
       "Go left":
           call GoLeft from _call_GoLeft
       "Go right":
           call GoRight from _call_GoRight

    scene parknight
    show monsterm at right3
    show monsterf at left3
    with dissolve
    "I look up to see the other monster has returned. It seems to be communicating with the one that attacked me."
    "I still can’t move but at least there aren’t tentacles assaulting me."
    You "(I have to think of something, I've got to get out of here. If I can just get back onto the road, I can get someone to-)"
    "A sudden chill runs through my body, the monsters have stopped communicating and have once again turned their attention to me, faceless heads locked on my limp form."
    "My teeth start to chatter and my body begins to sweat, their intense eyeless gaze filling me with dread..."
    "But..."
    "They don’t seem to be making any moves against me."
    "................"
    "....................................."
    "After about a minute the creatures turn away to leave, their bodies appearing to... liquify and then dissolve into nothingness."
    hide monsterm
    hide monsterf
    with dissolve
    "I look around in confusion, they're gone?"
    "A wave of relief washes over me. "
    You "Holy shit! What a nightmare, literally I hope."
    "I stand back up"
    You "(Looks like I can move again, I’ve got to get the fuck out of here!)"
    hide black
    play sound "audio/splat.mp3"
    show melt2 with hpunch
    You "Gah!"
    "As I take my first step forward, I tumble over, eating dirt once more."
    You "For fucks sake, why do I-"
    "Wait.... something doesn’t feel right."
    You "Wha----"
    show melt 1 with dissolve
    "My right leg has disappeared, melted into a puddle of blue liquid!"
    scene black with dissolve
    You "AAAAAAAAHHHH!!"
    "Terror sweeps over me."
    You "(This can't be happening!)"
    "I try to push myself up again..."
    play sound "audio/splat.mp3"
    show melt 2 with hpunch
    "Only to fall back down, my right leg gone as well"

    You "Oh fuck! Oh fuck! OH FUCK!"

    "I can see the rest of my body melting away with my legs."
    play sound "audio/splat.mp3"
    show melt 3 with hpunch
    "My hips."
    play sound "audio/splat.mp3"
    show melt 4 with hpunch
    "My stomach."
    show black with dissolve
    "I flail about, reaching out with my right arm, looking for anything that I could use to pull myself away from this cursed place…"
    You "Wait, is that...?"
    show ellahide1 with dissolve
    "A ways ahead of me, poking out from behind a tree I can spot Ella looking over at me."

    "What is she...."
    show ellahide3 with dissolve
    You "Hey! Ella! Over here, I need your help, I’m-"
    play sound "audio/splat.mp3"
    scene melt 4 with hpunch
    "Before I can finish my sentence the hand I’d been using to support myself gives out. "
    "I fall forward, my body crashing into the ground and collapsing into liquidy goo as the impact runs through it."
    scene black with dissolve
    "Everything goes black and all I can think is…"
    menu:
       "I'm going to die":
           call IGTD from _call_IGTD
       "I'm going to become one of them":
           call IGTBOOT from _call_IGTBOOT
       "Are they bringing me with them?":
           call ATBMWT from _call_ATBMWT

    scene

    scene street with hpunch
    stop music fadeout 1
    You "AAAARRRRGGGGHHHH!!!!"
    "The memories gripping me finally subside, leaving me shaking."
    You "H-H-Holy shit, *pant* *pant*"
    You "What the fuck was that!? That must have been some sort of hallucination."
    You "I bet it was Ella’s fucking pill. There’s no way something like that could actually happen."
    "I look down at my perfectly intact body"
    You "I’m certainly not a pile of goo but... my body isn't exactly normal anymore either."
    "Realizing I'm lying in the middle of the street a little way down from my house, I get up and dust myself off, groping at my perfectly solid body just in case."
    "Those memories were so engrossing, at the end there it was almost as if I was reliving them... I hadn't even realized I'd walked all the way home."
    You "Oh shit, what’s the time?"
    "I pull out my phone and check the time"
    You "7:45? Phew, alright. Only a few minutes have passed."
    play music "audio/fun.mp3"
    show home with dissolve
    "I make my way over to my house."
    "I’ve been living by myself for the past few years, ever since my mother died. Dad moves around a lot for work."
    "I'm not sure exactly what he does, something for the government is all he would tell me."
    "Living apart from him doesn’t really bother me, our relationship isn't strained or anything, but he definitely raised me to live independently."
    scene bedroom with dissolve
    "As soon as I enter my house, I head up to my room to check myself in the mirror."
    show bedroom b
    show mcb n
    with dissolve
    You "Holy shit..."
    You "(I'm at least a foot taller now, and I look wider too.)"
    "I strip down to get a better look at myself and the changes I've gone through."
    hide mcb n
    show bmc nude
    with dissolve
    You "(Woah! I've gotten jacked! I look the way I've always imagined myself looking. Even my junk...)"
    You "(The way I imagined huh...)"
    "I stretch my arm out again as a little test. It comes naturally now, like I've been doing it all my life. I can reach all the way across the room."
    You "What if..."
    "This time I focus on growing my legs."
    show stretchlegs with dissolve
    "It works exactly as I'd hoped, I get so tall my head smacks into the roof before I shrink myself back down."
    You "Hot damn!"
    show bighead with dissolve
    hide bedroom
    hide bmc
    "I start morphing my body in all kinds of ways. Making myself ripped as all hell, making myself fat, growing my head to ridiculous proportions and more."
    You "This is amazing! I can change my body however I want!"
    You "Wait, what if I change my body into someone else?"
    show bedroom b
    show bmc nude
    with dissolve
    "I give it a try, stepping in front of the mirror, picturing Daryl in my mind and willing my body to change into him."
    show bmc black with dissolve
    "......"
    You "Huh, my skin color changed but... I still look mostly the same. Like a black version of myself."
    You "Wait, is me doing this racist?"
    You "Whatever, let's have another go."
    "I close my eyes and focus really hard on the image of Daryl I have in my head and when I look at myself again-"
    show bmc daryl1 with dissolve
    You "Woah shit! I really messed up his face."
    You "Maybe I don't have a clear enough image of him in my head. Let's see..."
    "I pull out my phone and find a picture I have of Daryl."
    You "Right, ok, so his eyes are more like this, and his nose..."
    show bmc daryl2 with dissolve
    "While looking at the picture I slowly shape my body to match Daryl's. It's not perfect but I manage to get it pretty close."
    You "Damn, this is harder than I thought it would be. How long have I been doing this?"
    "I check the time on my phone."
    You "8:15!? Shit! I'm going to be late to class if I don't get a move on."
    scene black with dissolve
    "I have a quick shower and morph myself back into my original appearance."
    "Thankfully it happens pretty much instantly, without me having to micromanage specific features."
    "Seems I have a pretty clear image of myself in my head, or rather a pretty clear image of how I want to look."
    "I head over to my dad's room to grab some better fitting clothes and chuck some on."
    show bmc nude with dissolve
    show bmc n with dissolve
    You "These look alright."
    You "Thanks dad, I'm sure you won't be needing them wherever you are."
    You "Alright. I better get going."
    scene black with dissolve
    "I hop on the bus and head to my first day of college."
    call collegefirstday from _call_collegefirstday

label collegefirstday:
    show train with dissolve
    show bmc n at left4
    show train b
    with dissolve
    play music "audio/basic.mp3"
    You "(Shit, I'm going to be late.)"
    You "(*sigh* I really need to get a car. Taking the train everywhere is just not going to cut it.)"
    You "(Too bad I don't have any money or a job.)"
    You "(At least I'm staying in a dorm, I won't have to go home and back everyday.)"
    You "(But more importantly, what am I going to do about my whole shapeshifting thing? There's no way I can play with it if I've got a dorm mate lurking around.)"
    You "(And then there's Deryl. He's definitely gonna be wondering what's up with my body. No one goes through changes like this over one night.)"
    You "(I managed to dodge that bullet with Amber since I've been avoiding her and Liz over the break, but Deryl saw me just yesterday.)"
    You "(I'll have to tell him, or come up with a damn good lie.)"
    You "(Although, he's super into bio engineering and all that, maybe he can help me figure out what's going on?)"
    show train b
    show bmc s
    with hpunch
    play sound "audio/mechimpact.mp3"
    You "Woah!"
    "The train shakes wildly after hitting a particularly large bump on the track."
    play music "audio/comedy.mp3"
    show jess ss flip at right4 with moveinright
    show jess ss flip at right4 with hpunch
    play sound "audio/impact.mp3"
    "I manage to keep my balance, grabbing a nearby pole, but feel a thump on my back."
    show bmc n flip with dissolve
    hide black
    "Turning around I see a girl in what looks like some sort of cheerleading uniform trying to keep her balance while fumbling with her phone; and failing."
    menu:
       "give her a hand":
           call givehand from _call_givehand
       "Move aside":
           call moveaside from _call_moveaside

label campus:
    stop music fadeout 1
    scene school over with dissolve
    You "Whew! Here at last, at R&X itself."
    play music "audio/park.mp3"
    You "I still can't believe dad managed to get me in here."
    "Rodriguez & Xanthe's University for the exceptional, a super prestigious college that only the most talented, or the most wealthy are permitted to attend."
    "Great success for it's graduates is guaranteed, largely because it will only accept the best of the best."
    "Young prodigies, like potential Olympic athletes, math geniuses, songwriters, and other young talents of all varieties, are scouted and provided scholarships."
    "And wealthy families who want the most prestigious education for the heirs to their fortunes can also buy their way in for an enormous amount of money."
    "Success is pretty much guaranteed for these students with or without R&X, yet they still flock to this school in droves because of its reputation."
    "As the college that has cured countless deadly diseases and made incredible developments in technology, the university is almost better known as a research center than a place of education."
    "There's actually been quite a lot of complaints about how they treat their students, or so I hear."
    "What's more, the number of students that R&X actually takes in is quite small, though this of course makes all the rich families desperate to be the ones who get their children in."
    "The rich want the prestige of graduating the same university as the prodigies of this world, and the prodigies want access to the facilities the rich end up paying for."
    stop music fadeout 1
    scene school art with dissolve
    show school artb
    show bmc n
    with dissolve
    play music "audio/basic.mp3"
    You "I'm really late."
    "I feel my phone starting to buzz and see that it's Amber calling."
    show bmc pnt with dissolve
    You "Hello?"
    Amber "Where are you? Orientations already started! Even Deryl's here."
    You "Well at least you're not alone."
    Amber "Shut up, you know I can't stand Deryl."
    Deryl "Yo [name]! Where you at!?"
    Amber "Get your face away from me!"
    Deryl "*distant voice* Chill girl."
    Amber "So, where are you?"
    You "I just arrived on campus, where am I supposed to go?"
    Amber "Well all the freshman are being taken on a tour of the campus. We're at the football field down the back. But you have to sign in at the reception first, it's just the first building from the entrance."
    You "*sigh* Alright. See you soon."
    Deryl "Hurry up dude! You're missing out!"
    Amber "I told you to get away from me!"
    "The phone hangs up."
    You "I guess I better get myself signed in."
    show black with dissolve
    play music "audio/ambientcrowd.mp3"

    "After a few minutes of getting my paperwork sorted out I'm finally led to the rest of the freshmen on the tour of the university."
    scene school fieldcrowd with dissolve
    show school fieldcrowdb
    show lauren nt at left2
    with dissolve
    show bmc n at right with moveinright
    Unknown "And that leads us to the end of our tour. I hope you enjoy your time here."
    You "Shit."
    hide lauren with moveoutleft
    show amber nt flip at center
    with dissolve
    Amber "Look who finally showed up."
    You "*sigh* Looks like I missed the tour."
    show amber ant flip with dissolve
    Amber "And left me alone with Deryl all morning."
    You "C'mon Amber, he's not that bad. And you know he likes you."
    show amber sigh flip with dissolve
    Amber "Ugh."
    show amber nt with dissolve
    Amber "C'mon. We've got a general studies class next."
    show school trackb with dissolve
    You "Right, I do remember something about that. I don't suppose they told you what that class is about?"
    Amber "Oh you know, just a standard class every freshman has to take on top of their course. Teaching us how to study, how to research, how to reference, how to be polite and inclusive to everyone and all that bullshit."
    You "Sounds fun..."
    show school hallb with dissolve
    You "Where's Deryl?"
    show amber laugh with dissolve
    Amber "Idiot got hit by a stray football. He's resting in the nurse's office."
    You "Is he alright?"
    show amber nt flip with dissolve
    Amber "He's fine, it's just a football."
    Amber "Anyway, lets hurry up."
    play sound "audio/impact.mp3"
    show bmc ans at right4
    show amber ss flip
    with hpunch
    show bmc ans at right4
    show amber ss flip
    with hpunch

    You "Oooof"

    "Some guy in a rush bumps into me as he passes, pushing me into Amber."
    play sound "audio/himpact.mp3"
    show headbutt with hpunch
    "My forehead smacks right into hers and we're both sent reeling."
    You "Arrgh!"
    Amber "Arrrgh!"
    "As my head smashes into hers I'm assailed by a splitting headache, similar to what I had this morning but a thousand times worse."
    You "Nnnnnnggghhhh!!"
    "But it's not only my head aching now, my entire body is filled with a sharp, prickling pain."
    "I can feel my body start to twist and shift, just like it did several times earlier today as I stretched my arms and shaped my body."
    "I repress the feeling as best as I can, desperately trying not to give into the change that is coming over me and outing myself as a freak of nature."
    show black
    hide headbutt
    show amber sadt flip
    show bmc ans
    with dissolve
    Amber "[name]! Are you alright?"
    "I can barely hear what Amber is saying, I once again feel stray memories worm their way into my head."
    "I remember feeling disgust as I spot Deryl peeping in on me changing. I remember feeling pity as I see [name] fawn over Liz. I remember feeling frustration as Liz beats me once again."
    "My vision has gone dark and I find it difficult to maintain consciousness. I can feel myself being lead somewhere by someone, but I'm not coherent enough to observe the details."
    "Finally my consciousness fades and I fall into a troubled sleep."
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve

    You "Ugh, my head..."
    Unknown "Finally awake huh?"
    show derylwake smile with dissolve
    play music "audio/comedy.mp3"
    You "Deryl!?"
    You "What's going on!?"
    show derylwake serious with dissolve
    Deryl "That's what I wanna know [name]."
    Deryl "You are [name]... aren't you?"
    You "Huh?"
    You "(Oh shit! He's noticed how different my body looks.) "
    You "(Of course he has! He's not an idiot! No one grows a foot taller in one day!"
    You "I guess... I guess I should explain why I look like this."
    Deryl "Sounds like a really good idea. Why exactly..."
    Deryl "...Do you look exactly like Amber?"
    show amberbody change with dissolve
    You "Huh?"
    show amberbody changelook with dissolve
    You "(... tits!?)"
    "I look down at my body and rather than finding my usual masculine physique I instead find myself looking down at what appears to be an incredibly feminine form."
    You "What the fuck!"
    hide derylwake
    show derylwake serious with dissolve
    Deryl "Yep, that's what I said."
    Deryl "Amber and a teacher dragged you in here unconscious and laid you down on the bed looking like your normal self, except bigger."
    Deryl "Then about 10 minutes later you started growing tits! Before a minute more had passed you were already looking like that, the spitting image of Amber."
    Deryl "If I hadn't seen it I never would've believed it."
    You "What in the world is happening to me..."
    Deryl "My question exactly. Talk to me man, what's going on."
    hide amberbody
    show amberbody change with dissolve
    You "Shit... Alright, here's what happened..."
    "I go over the events of last night and this morning, giving Deryl every detail I could recall. Ella, the monster attack, the headaches, the dog, my stretchy arms, me transforming into his brother, all of it."
    You "So, what do you think?"
    hide derylwake
    show derylwake smile with dissolve
    Deryl "What do I think? I think this is insane, and fucking amazing!"
    Deryl "The ability to shift your own body any way you like! To expand it? To change your gender? Think about what this means!"
    Deryl "What if you can change your age? Would you be able to live forever? Could you heal wounds you have just by shifting your flesh back together? You might be immortal with this!"
    Deryl "And being able to change into a woman? I wonder if your chromosomes actually changed too. I've got to get a DNA sample!"
    You "But why is this all happening?"
    Deryl "Well, if I had to say... You were probably infected by those monsters you talked about. A lot of your symptoms seem similar to the things they did when they attacked you. Shapeshifting, turning into goo, getting into your head."
    hide amberbody
    show amberbody changelook with dissolve
    You "(He's right, it is similar. This can't be a good thing, am I going to become one of those things?)"
    show amberbody change with dissolve
    You "Wait, getting into my head? What symptoms have I had related to that?"
    hide derylwake
    show derylwake smile with dissolve
    Deryl "Well you said when you touched the dog you had a headrush or something right? "
    Deryl "And felt an inexplicable familiarity with its owner? And when you headbutted Amber, you saw things of me and her and her and Liz, things that she should know and you shouldn't, right?"
    Deryl "I'd say it seems like you can get into people's heads upon contact with their body."
    You "Hmmmm..."
    Deryl "In any case, you should practice more with these abilities. The more you understand them, the better."
    You "But what if practicing ends up causing my symptoms to worsen? I just passed out in case you've forgotten. What if I end up becoming one of those things?"
    show derylwake serious with dissolve
    Deryl "That's true, but you can't just do nothing. Even without practicing you ended up passing out right? If it were me, I'd want to at least take control with my own hands, and maybe try and master it."
    You "Hmmmm... maybe..."
    Deryl "This is good timing though."
    You "What do you mean?"
    show derylwake smile with dissolve
    Deryl "That all this happened just as we entered R&X. The research facilities here are state of the art, and this university has done more research into bio-engineering than anywhere in the world."
    You "I really don't want to end up as a science experiment for the university though, or the government."
    Deryl "Don't worry buddy, I've got your back. I'm sure we'll be able to sneak something useful out of the labs to help you."
    hide amberbody
    show amberbody change with dissolve
    You "...Thanks man."
    You "(Having friends you can count on is a good thing.)"
    You "Alright, I'm outta here, I'm busting to go to the toilet."
    Deryl "Hang on, don't you think you should-"
    show lizintro with dissolve
    "Before Deryl can even finish his sentence I've opened the door and found a familiar sight in front of me."
    You "(Liz?!)"
    Unknown "Oh, Amber? I thought you were in class?"
    You "Oh, um, I was just...."
    "Fuck! What do I do? I still look like Amber! I should've changed back."
    Deryl "She just stopped by to quickly check up on [name]."
    You "Uh, yeah, that's it!"
    You "(I've got to get out of here.)"
    Liz "Oh, me too. Where is he?"
    Deryl "Uh...."
    You "He's gone! He uh, went to check out his dorm."
    Liz "So he's alright?"
    You "Oh yeah, totally."
    Liz "*sigh* And here he's got me worked up for nothing..."
    You "A-anyway, I gotta go. Excuse me Liz- er... sis."
    "I push my way past her and sprint down the hall to the toilets."
    hide black
    show black with dissolve
    Liz "....Did she change her clothes? They looked really big on her."
    Liz "....Whatever, I need a nap."
    stop music fadeout 1
    scene school toilet with dissolve
    show school toiletb
    show amber t
    with dissolve
    You "Phew, that was close."
    You "I've really got to get this thing under control."
    hide black
    show black with dissolve
    "I head to a cubicle and let nature take its course... the female way this time."
    hide black with dissolve
    You "Phew, that's better, I don't think I could've held out much longer."
    You "Alright, lets transform back..."
    You "Although..."
    You "I've never had tits before... this could be a fun opportunity."
    menu:
       "Have a play":
           call haveaplay from _call_haveaplay
       "Forget it":
           call forgetit from _call_forgetit

    show black with dissolve

label dorm:
    stop music fadeout 1
    play music "audio/alice.mp3"
    scene school hall with dissolve

    You "Phew, what an ordeal that was."
    You "Gender bending huh? This day keeps getting weirder and weirder."

    if fjared == True:
        jump fuckedjared
    else:
        jump notfuckedjared
    label fuckedjared:
    You "I can't believe I fucked a guy."
    jump notfuckedjared
    label notfuckedjared:
    You "But these abilities, they could be useful."

    You "In a school with only geniuses and rich elites, maybe this could be my way to get ahead?"
    You "I could..."
    menu:
       "Take up sports":
           call takeupsports from _call_takeupsports
       "Get some money":
           call getsomemoney from _call_getsomemoney
       "Get some girls":
           call getsomegirls from _call_getsomegirls

    label takeupsports:
    You "I doubt I'll be able to keep up with the other kids in grades, I've never beat Deryl even once, but sports..."
    You "I don't know much about the sporting program here, but Amber and Liz got their scholarships for swimming. As I understand it all you need to be is the best of the best, it doesn't matter what the sport is..."
    You "And with a body like this a lot of sports would be easy. With my arms I could probably dunk a basketball from the other side of a court..."
    You "I'd have to be subtle about it though, I can't afford to expose myself."
    You "With Dad's connections I'll probably graduate one way or another, but I'd rather not lag behind as the slowest kid in college."
    You "With these powers though, I could wind up being the best!"
    call somanythings from _call_somanythings

    label getsomemoney:
    You "I don't need to compete with the prodigies when I could just be one of the rich kids..."
    You "If I can get a handle on these abilities making money would be a cinch."
    You "I probably won't be able to do it legally though, at least if I want the money in my immediate future..."
    You "But am I willing to turn to crime? The idea kinda make me feel like a supervillain from the old comic books I used to read."
    You "Hmmm, that has potential."
    call somanythings from _call_somanythings_1

    label getsomegirls:
    You "Who cares about school when I could be getting girls!"
    You "I can change my face and body, if I can get a handle on controlling this, I could make myself into a super-hot celebrity or something."
    You "Everyone has someone who they'll fuck right? Whether it's their boyfriends or their crushes, all I have to find out is who it is and then I'm golden!"
    You "Though it's not exactly ethical... actually is it even legal? If you impersonate a woman's husband and fuck her, do you get in trouble? I feel like I've seen a movie where that happens..."
    You "But, it's not like I could ever get caught..."
    You "Either way, I can always just make myself look like a girl's dream guy. Nothing creepy about just making yourself look better right? It's not really any different than makeup if you think about it."
    call somanythings from _call_somanythings_2

    label somanythings:
    You "Maybe these abilities are actually a blessing. As long as I don't eventually turn into one of those freakish monsters that is. But even if I did, wouldn't I just be able to transform myself back to normal anyway?"
    You "Hmmm...."
    Unknown "For the last time Alice, take that disgusting thing off!"
    You "???"
    "I walk a little way down the corridor and peek around the corner."
    show school hall flip with dissolve
    show school hallb flip
    show alice q at right2
    show lauren an flip at left2
    with dissolve
    Unknown "If you want to dress like a slut go right ahead, but you will not do so with the university's logo on your top!"
    You "(It's that teacher from earlier and- woah, who is she? Her tits are huge.)"
    show alice qt with dissolve
    Alice "This is the college's official cheerleading uniform, it's not my problem if you don't like it."
    show alice n with dissolve
    Unknown "It most certainly is not! It's a uniform you modified to reveal as much skin as possible. It's disgraceful."
    show alice nt with dissolve
    Alice "The modifications were Jess' idea, she's head cheerleader not me. So take it up with her."
    show lauren nt flip with dissolve
    Unknown "I already have, and she admitted the changes she made were not approved by the board! So that uniform is not official, get changed."
    show alice qt with dissolve
    Alice "No? I don't give a fuck if it's official or not, I wear what I want. "
    Alice "And their's no policy about how I have to dress. So how about you get off my back?"
    show alice q
    show lauren ant flip
    with dissolve
    Unknown "Watch your mouth! And regardless of policy we can't have people seeing the school brand on a uniform that leaves half your ass exposed!"
    show lauren nt flip
    with dissolve
    Unknown "Our reputation took enough of a hit when you formed your little sorority. We're supposed to be the best university in the world! People around the globe come to watch our athletes compete and win!"
    Unknown "How do you think it reflects on us when they see you and the rest of the cheerleading team prance about with your asses and tits hanging out?"
    show alice m with dissolve
    Alice "Good? That's what people like. And don't get all puritanical on me lady, you're in no place to judge given the rumors floating around about you."
    show lauren s flip with hpunch
    show lauren ant flip with hpunch
    Unknown "How dare you! Those rumors are completely baseless and if I hear you spreading them further, I'll-"
    show alice ant at right4 with hpunch
    Alice "You'll what? I think you've forgotten who you're talking to {i}Lauren{/i}. I've put up with your shit so far, but if you don't get off my back you and I are going to have a serious fucking problem."
    Alice "And believe me, that's the last fucking thing you want. So take up all your petty fucking issues with Jess. She's in charge, I honestly don't give a fuck about the uniforms either way."
    show lauren sadt flip with dissolve
    Lauren "*splutter* I- But- You can't just..."
    hide lauren
    hide alice
    show school hallb
    show bmc nt flip at right3
    with dissolve
    You "Woah, things are getting heated. I can't believe she's talking to a faculty member like that."
    show tess n flip at left3 with dissolve
    Unknown "I know right? Alice is crazy"
    show bmc nt with hpunch
    You "Woah!"
    You "I, uh, didn't see you there."
    show tess h flip with dissolve
    Unknown "*Giggle* No kidding. Eavesdropping is impolite you know?"
    You "(She's wearing the same uniform as that other girl, and her boobs are huge as well!)"
    You "Haha, yeah, I just heard all the shouting and couldn't help get curious."
    Unknown "Mhm, better not let Alice catch you though, she can get pretty unreasonable sometimes..."
    You "Oh, uh, yeah, gotcha. Thanks."
    You "I guess I'll be going now."
    show tess wink flip with dissolve
    Unknown "Mhm, bye bye cutie."
    You "Uh, yeah. Bye bye."
    hide bmc with moveoutleft
    scene black with dissolve
    "I awkwardly leave the scene and continue on my way to the dormitory."
    scene school dormhall with dissolve
    You "Alright. Now that I'm back to normal, let's see what we're working with."
    play music "audio/groovy.mp3"
    "Eager to see my new lodgings for the next 3 or so years, I head down to the college dormitories and look for my room."
    show school dormdoor with dissolve
    You "24... 25.... Ah, here we are. Room number 26, my dorm."
    show school dormday with dissolve
    "I open the door and enter my new living quarters, dropping my bag on the floor."
    show school dormdayb
    show bmc n flip
    with dissolve
    You "Pretty bare bones for a rich kids college."
    show deryl nt flip at left with dissolve
    Deryl "Hey bro!"
    show bmc nt at right3 with dissolve
    You "Deryl?"
    show deryl laugh flip with dissolve
    Deryl "I call this bed!"
    show bmc s with dissolve
    You "Wait, what? You're my dormmate?"
    show deryl n flip with dissolve
    Deryl "Yeah? Didn't you know? I asked the administration after we enrolled."
    show bmc nt with dissolve
    You "And they just said yes?"
    Deryl "Sure, why wouldn't they? Liz and Amber are dormmates too."
    show bmc ht with dissolve
    You "Huh, well that's awesome! I gotta say, I wasn't all that keen on rooming with a stranger."
    show deryl mt flip with dissolve
    Deryl "Better than that, we can examine that little problem of yours in private."
    show deryl n flip with dissolve
    Deryl "Speaking of which, I've had some thoughts on that."
    show bmc nt with dissolve
    You "Oh yeah?"
    Deryl "Yeah, I want you to try something."
    You "What?"
    Deryl "Shapeshift into me."
    You "Huh?"
    Deryl "You said you had trouble shapeshifting into my bro before, right? Try shifting into me."
    You "Uh, alright."
    hide bmc
    show derylt ugly at right3
    with dissolve
    "I give it a try. The change comes easy, but it feels a little unnatural."
    You "How's that?"
    show deryl s flip with dissolve
    Deryl "Hmm, interesting... Take a look."
    "Deryl takes a photo of me with his phone and shows it to me."
    You "Ah, shit, I messed up the face again."
    Deryl "The proportions aren't quite right either, I'm not that tall."
    You "This happened with Daryl too. I had to spend like 15 minutes micro managing the face to try and get it right."
    Deryl "Interesting... and yet you were able to change into Amber perfectly, in a few seconds, while barely conscious..."
    You "Huh, now that you mention it..."
    You "Maybe it's because you two are black? Maybe different races are harder to transform into?"
    show deryl qt flip with dissolve
    Deryl "Why would changing race be harder than changing gender?"
    You "Uh, I don't know."
    show deryl nt flip with dissolve
    Deryl "Anyway, I have a theory. Come here."
    You "What?"
    Deryl "Just do it dude."
    "I shrug my shoulders and approach him; he reaches out his hand."
    show derylt ugly at left3 with moveinright
    Deryl "Alright, now shake my hand."
    You "Hmmm, alright."
    "I do as he ask and give his hand a halfhearted shake."
    show school dormdayb with hpunch
    "A familiar dizziness comes over me as my hand meets his, but I'm prepared for it and suppress it quickly without issue."
    "No memories enter my head this time, but I do feel a unique sense of... familiarity with Deryl that I didn't a second ago."
    show deryl q flip
    show derylt ugly at center
    with dissolve
    Deryl "So? Did you get into my head?"
    You "Uh, not quite. I felt like I was about to but I managed to pull back. I might've scratched the surface a little bit."
    show deryl st flip with dissolve
    Deryl "Pulled back? Why'd you do that?"
    You "Because I don't want to faint again?"
    show deryl s flip with dissolve
    Deryl "Oh, right. Well, it looks like you can control it, at least to the degree where you can choose when and when not to use it."
    You "Yeah, but I still need some practice I think."
    Deryl "For sure."
    show deryl nt flip with dissolve
    Deryl "Well anyway, let's test out my theory. See if you can change into me now."
    You "Alright?"
    show derylt n with dissolve
    "I try once again to turn into Deryl, like before I'm able to shift my body fairly easily, but this time the transition into Deryl feels much more natural, as though I was just changing into myself."
    show deryl n flip with dissolve
    Deryl "*Whistle* Damn man, looking good. How'd you get so handsome?"
    You "It worked?"
    "He takes a picture and shows it to me."
    show deryl nt flip with dissolve
    Deryl "Perfectly, it's like I'm looking in a friggin mirror. Incredible."
    You "Huh. So, if I touch someone, I can take their form without issue..."
    Deryl "That was my theory. I figured when you entered Amber's head you were able to experience what it's like to be in her body from her point of view."
    Deryl "And by using those experiences you took from her it made assuming her form a more natural process."
    Deryl "But after you said you pulled back from my head, I didn't think you'd be able to do it with me."
    You "Hmmm, well even when I suppressed it I did feel like I took something from you, like I knew you a little better or something. It's hard to describe."
    show deryl s flip with dissolve
    Deryl "I see. So, there's degrees to which you can enter a mind. I wonder if you'd be able to push it further and do more than just see memories..."
    You "Not without fainting again I'd say."
    show deryl st flip with dissolve
    Deryl "Right, right."
    Deryl "Ok. Let's do some more tests. Orientation and General studies are the only classes freshman have today, you've already missed both of those."
    Deryl "We might as well try and get this thing of yours under control so you're at least good to function in normal society."
    hide deryl
    hide derylt
    show school dormday
    with dissolve
    stop music fadeout 1
    "We spend the next few hours practicing with my new ability."
    "By repeatedly shaking Dery's hand while focusing on staying out of his head we managed to get me to a point where I won't enter his mind unless I intend to."
    "We also tested whether it had to be skin to skin contact or if it works through clothes and hair. Clothes were a no go, but hair worked fine as long as it was attached to the body."
    show school dormnight with dissolve
    show school dormnightb
    show deryl nt flip at left3
    show bmc n at right3
    with dissolve
    Deryl "Phew, I think that's enough for today. You should be good to go about school life normally at least."
    show deryl st flip with dissolve
    Deryl "*Yawn* I'm gonna crash dude, I wanna check the campus out early morning before class. 'Night man."
    show bmc nt with dissolve
    You "Yeah, me too. Good night."
    hide deryl with dissolve
    You "(Man, I'm absolutely knackered. It's been a hell of a day; all this transforming and stuff has really taken it out of me.)"
    "Exhausted, I flop down onto my bed and drift off to sleep."
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    call day1 from _call_day1
