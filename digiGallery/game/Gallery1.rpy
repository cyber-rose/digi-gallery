define img_size = 300

$ artist = "Artist Name"
$ handle = "@handle"

label enter_gallery1:
    "You enter Gallery 1 and see a bunch of offshooting hallways. You browse the artist name plaque overhead each one."

    if guide == e:
        e "Take a look around, sugar."
    if guide == h:
        h "I trust thy gaze to discern art of the highest echelon."

    menu:
            "Maggie Johnson":
                $ artist = "Maggie Johnson"
                $ handle = "@jellyfisharepeopletoo on instagram"
                jump artist1
    
            "Anna C. Wershbale":
                $ artist = "Anna C. Wershbale"
                $ handle = "@annatheartfairy on instagram"
                jump artist2

            "Go back to the reception area":
                jump ask

label artist1:

    call screen imenu1("images/booferandwhippet.png", "images/dinno.png", "images/cupcake.png") # add many images as many as you want...
    
    jump questions1

label artist2:

    call screen imenu1("images/airbags.png")
    
    jump questions2

label questions1:
    if guide == e:
        show eyve at left with move
    if guide == h:
        show tin-can-nibal at left with move

    if _return == 0:
        image a = "images/booferandwhippet.png"
        show a at center:
            yalign 0
            fit "contain"
            ysize(743)
        
    elif _return == 1: # 2nd image is picked
        $ title = "Dinno"
        image b = "images/dinno.png"
        show b at center:
            yalign 0
            fit "contain"
            ysize(743)
        

    elif _return == 2: # 3rd image is picked
        $ title = "Cupcake"
        image c = "images/cupcake.png"
        show c at center:
            yalign 0
            fit "contain"
            ysize(743)

    menu:
            "What is the title of this piece?":
                jump titleQ1
    
            "Puppers! What are their names?" if _return == 0:
                jump pupperQ
            
            "Is that a baby kaiju?" if _return == 1:
                jump babyQ

            "Where did these pictures even come from?" if _return == 1:
                jump sourceQ

            "Why...?" if _return == 2:
                jump whyQ

            "This one seems out of place." if _return == 2:
                jump oopQ

            "Let me check out another piece.":
                hide a
                hide b
                hide c
                if guide == e:
                    show eyve at center with move
                if guide == h:
                    show tin-can-nibal at center with move
                jump artist1

$ title = ""
label titleQ1:
    if artist == "Maggie Johnson":
        if _return == 0: # represents that the first image is picked...
            $ title = "\"Within You, There Are Two Dogs\" (2023), made on Procreate."
        elif _return == 1: # 2nd image is picked
            $ title = "\"Godzilla’s Baby Book\" (2024), made on Procreate."
        elif _return == 2: # 3rd image is picked
            $ title = "\"Cupcake is Hungry\" (2023), made on Procreate."
        guide "The title of this piece is %(title)s"
        jump questions1
    
    if artist == "Anna C. Wershbale":
        if _return == 0:
            $ title = "\"Our Lady of Airbags (aka Kiss of Life)\" (2024), digital media collage."
        guide "The title of this piece is %(title)s"
        jump questions2
    

label pupperQ:
    if guide == e:
        guide "Oh, there’s nothin like a dog to sweeten your day! That ‘lil one that could use some under-the-table hush-hush bacon is Whippet, n’ that big ol’ boofer there is called Boofer."
    if guide == h:        
        guide "The cavalry answers to Whippet. The tank answers to Boofer. One of them stole my bacon rations, but I know not yet which."
    jump questions1

label whyQ:
    if guide == e:
        guide "Well darling, sometimes things are scary cuz they look like people but a little bit wonky…and sometimes things are scary cuz they ain’t nowhere near what people look like."
    if guide == h:        
        guide "A discerning philosopher such as thyself must recognize the alienation of the unfamiliar. Wisdom from one leader to another: do not underestimate the base hunger that drives all living things to conquer."
    jump questions1
    
label oopQ:
    if guide == e:
        guide "Us artists have layers, lovemuffin."
    if guide == h:        
        guide "The horror of war is never far from the smiles of peace, whether it be across the river...or in the hearts of man."
    jump questions1

label babyQ:
    if guide == e:
        guide "Even Godzilla was a tot once upon a time. So sweet he could rot your teeth!"
    if guide == h:        
        guide "Do not underestimate the potential of infancy. The feeblest elephant calf may one day trample Rome underfoot."
    jump questions1

label sourceQ:
    if guide == e:
        guide "Where else honey? His mama!"
    if guide == h:        
        guide "There is no bigger vulnerability than one’s kin. From thy very first breath, evidence of foolish youth and infantile feebleness are hoarded like daggers hovering above one’s crown."
    jump questions1

label questions2:
    if guide == e:
        show eyve at left with move
    if guide == h:
        show tin-can-nibal at left with move

    if _return == 0:
        image d = "images/airbags.png"
        show d at center:
            yalign 0
            fit "contain"
            ysize(743)

    menu:
            "What is the title of this piece?":
                jump titleQ1

            "What’s it about?" if _return == 0:
                jump aboutQ
            
            "What style would you call this?" if _return == 0:
                jump styleQ

            "Let me check out another piece.":
                hide d
                if guide == e:
                    show eyve at center with move
                if guide == h:
                    show tin-can-nibal at center with move
                jump artist2

label aboutQ:
    if guide == e:
        guide "Oh I just love to dance! The night starts with a melody, and it ends with a good night’s sleep. I can’t keep my eye open after waltzing ‘til daybreak."
    if guide == h:        
        guide "My military instincts are going off. This piece can only be about persistence and new beginnings. Thou would do well to learn from the philosophies of survival."
    jump questions2

label styleQ:
    if guide == e:
        guide "For some reason, I’ve always liked surrealism. Hannah Höch is one of my personal favorites."
    if guide == h:        
        guide "It takes a most capable leader to see such cacophony and harmonize it. Those modernist, neo-pop heathens have their glimmers of competence, I must admit. "
    jump questions2


screen imenu1(*imgs):
    text artist size 100 xalign 0.5 yalign 0 color"#000000"
    text handle size 50 xalign 0.5 yalign 0.1 color"#000000"
    vbox xalign 0.5 yalign 0.5 spacing 300:
        hbox xalign 0.5 yalign 0.5 spacing (1920-(len(imgs))*img_size)/len(imgs):
            for i, img in enumerate(imgs):
                imagebutton:
                    idle im.Scale(img, img_size,img_size)
                    action Return(i)
        hbox xalign 0.5 yalign 0.5:
            imagebutton:
                    idle im.Scale(img, img_size,100)
                    action Jump("enter_gallery1")