define img_size = 300

$ artist2 = "Artist Name"
$ handle2 = "@handle"

label enter_gallery2:
    "You enter Gallery 2 and see a bunch of offshooting hallways. You browse the artist name plaque overhead each one."

    if guide == e:
        e "Take a look around, sugar."
    if guide == h:
        h "I trust thy gaze to discern art of the highest echelon."

    menu:
            "Abigail Davis":
                define artist2 = "Abigail Davis"
                define handle2 = "@bananaslugshuffle on Instagram. Shop at bananaslugshuff.redbubble.com"
                jump abby

            "Go back to the reception area":
                jump ask

label abby:

    #show the menu with Abigail Davis's arts
    call screen imenu2("images/minds_eye.png", "images/oat_milk_framed.png", "images/debut.png") # add many images as many as you want...
    
    jump abbyquestions

#questions for abby's art
label abbyquestions:
    if guide == e:
        show eyve at left with move
    if guide == h:
        show tin-can-nibal at left with move

    #use menu selection to pick a piece to show
    if _return == 0:
        $ title = "Minds Eye"
        image e = "images/minds_eye.png"
        show e at center:
            yalign 0
            fit "contain"
            ysize(743)
        
    elif _return == 1: # 2nd image is picked
        $ title = "Oat Milk"
        image f = "images/oat_milk_framed.png"
        show f at center:
            yalign 0
            fit "contain"
            ysize(743)
        

    elif _return == 2: # 3rd image is picked
        $ title = "Debut"
        image g = "images/debut.png"
        show g at center:
            yalign 0
            fit "contain"
            ysize(743)

    menu:
            "What is the title of this piece?":
                jump titleQ2
    
            "She looks familiar." if _return == 0:
                jump familiarQ

            "What’s it made of?" if _return == 0:
                jump madeofQ
                
            "Why is it called \"Oat Milk\"?" if _return == 1:
                jump oatmilkQ
            
            "It’s not very colorful, is it?" if _return == 1:
                jump colorfulQ
            
            "What does it mean?" if _return == 2:
                jump meaningQ
            
            "Who are those people?" if _return == 2:
                jump whoareQ

            "Let me check out another piece.":
                hide e
                hide f
                hide g
                if guide == e:
                    show eyve at center with move
                if guide == h:
                    show tin-can-nibal at center with move
                jump abby

$ title = ""
label titleQ2:
    if artist2 == "Abigail Davis":
        if _return == 0: # represents that the first image is picked...
            $ title = "\"Mind’s Eye\" (2023), analog collage."
        elif _return == 1: # 2nd image is picked
            $ title = "\"Oat Milk\" (2023), analog collage."
        elif _return == 2: # 3rd image is picked
            $ title = "\"Debut\" (2023), analog collage."
        guide "The title of this piece is %(title)s"
        jump abbyquestions

label familiarQ:
    if guide == e:
        guide "Oh stop sweetness, I’m turning red! Ah, I remember when we had these made..."
    if guide == h:        
        guide "A mind such as thyself should recognize the insightful Eyve in her early days. Tis the counterpart to her partner’s much-lauded portrait."
    jump abbyquestions

label madeofQ:
    if guide == e:
        guide "Well, there’s a piece of the morning paper to go with your sweet tea, some lovely little flowers, and of course that pretty young thing on the left in nuthin but her creation suit!"
    if guide == h:        
        guide "Note thy Edenic foliage, harvested in full bloom, pressed and dried for precisely two weeks, and encased in resin. Note the precisely spaced blue circles and rigid rows of text, which rival my finest battalion in their discipline."
    jump abbyquestions

label oatmilkQ:
    if guide == e:
        guide "Reminds me of a nice cozy frothy vegan chai–with extra sugar, of course!"
    if guide == h:        
        guide "My soldiers, grown from the earth of their homeland, shall rise in vast rows to defend and conquer!"
    jump abbyquestions

label colorfulQ:
    if guide == e:
        guide "Honey, you know me, I couldn’t stand all this sad beige. I guess the military man likes it, tho. Ya know, gray is his faaaavorite color. I bet it’s on account of them elephants and such."
    if guide == h:        
        guide "Do not underestimate the power of uniformity and coordination. Your victory may one day rest on the nuance of shades."
    jump abbyquestions

label meaningQ:
    if guide == e:
        guide "Prying eyes, sweetness, prying eyes."
    if guide == h:        
        guide "When the hierarchy of man in all his opulence confronts thee, how shall you navigate the world."
    jump abbyquestions

label whoareQ:
    if guide == e:
        guide "That’s my apple-picking buddy! Man, when we get together, we make a mean cobbler. And we aint bad to look at either ;)."
    if guide == h:        
        guide "Thy grand lady resides in mine same mountainous neighborhood. And those men are mere ants, with not a face to remember or threat to regard."
    jump abbyquestions

screen imenu2(*imgs):
    text artist2 size 100 xalign 0.5 yalign 0 color"#000000"
    text handle2 size 50 xalign 0.5 yalign 0.1 color"#000000"
    vbox xalign 0.5 yalign 0.5 spacing 300:
        hbox xalign 0.5 yalign 0.5 spacing (1920-(len(imgs))*img_size)/len(imgs):
            for i, img in enumerate(imgs):
                imagebutton:
                    idle im.Scale(img, img_size,img_size)
                    action Return(i)
        hbox xalign 0.5 yalign 0.5:
            imagebutton:
                    idle im.Scale(img, img_size,100)
                    action Jump("enter_gallery2")
    