define img_size = 300

define artist = "Artist Name"
define handle = "@handle"

label enter_gallery2:
    scene pexels-matheusnatan-2149422 with dissolve:
        fit "fill"
        xysize (1980, 1080)

    if guide == e:
        show eyve at left with dissolve: 
            fit "contain"
            ysize (743) 
    if guide == h:
        show tin-can-nibal at left with dissolve: 
            fit "contain"
            ysize (743) 
    
    "You enter Gallery 2 and see a bunch of offshooting hallways. You browse the artist name plaque overhead each one."


    guide "Which artist do you want to check out?"
    

    menu:
            "Abigail Davis":
                define artist = "Abigail Davis"
                define handle = "@bananaslugshuffle on Instagram. Shop at bananaslugshuff.redbubble.com"
                jump abby
    
            "Anna C. Wershbale":
                define artist = "Anna C. Wershbale"
                define handle = "@annatheartfairy on Instagram"
                jump annaCW

            "Go back to the reception area":
                jump ask

label abby:

    #show the menu with Abigail Davis's arts
    call screen imenu("images/minds_eye.png", "images/oat_milk_framed.png", "images/debut.png") # add many images as many as you want...
    
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
        image a = "images/minds_eye.png"
        show a at center:
            yalign 0
            fit "contain"
            ysize(743)
        
    elif _return == 1: # 2nd image is picked
        $ title = "Oat Milk"
        image b = "images/oat_milk_framed.png"
        show b at center:
            yalign 0
            fit "contain"
            ysize(743)
        

    elif _return == 2: # 3rd image is picked
        $ title = "Debut"
        #show info2 at right
        image c = "images/debut.png"
        show c at center:
            yalign 0
            fit "contain"
            ysize(743)

    menu:
            "What is the title of this piece?":
                jump abbyTitleQ
    
            "What is the context of this piece?":
                jump tbc

            "Let me check out another piece.":
                hide a
                hide b
                hide c
                if guide == e:
                    show eyve at center with move
                if guide == h:
                    show tin-can-nibal at center with move
                jump abby

$ title = ""
label abbyTitleQ:
    if _return == 0: # represents that the first image is picked...
        $ title = "Minds Eye"
    elif _return == 1: # 2nd image is picked
        $ title = "Oat Milk"
    elif _return == 2: # 3rd image is picked
        $ title = "Cupcake"
    guide "The title of this piece is %(title)s."
    jump abbyquestions
    
    


#Anna Weshbale's work
label annaCW:
    
    #show the menu with the displayed art
    call screen imenu("images/AnnaWeshbale.png") # add many images as many as you want...
    
    jump annaCWquestions

#questions for Anna C W's art
label annaCWquestions:
    if guide == e:
        show eyve at left with move
    if guide == h:
        show tin-can-nibal at left with move

    #use menu selection to pick a piece to show
    if _return == 0:
        $ title = "Our Lady of Airbags (aka Kiss of Life)"
        image a = "images/AnnaWeshbale.png"
        show a at center:
            yalign 0
            fit "contain"
            ysize(743)

    menu:
            "What is the title of this piece?":
                jump annaCWTitleQ
    
            "What is the context of this piece?":
                jump annaCWContext

            "Let me check out another piece.":
                hide a
                hide b
                hide c
                if guide == e:
                    show eyve at center with move
                if guide == h:
                    show tin-can-nibal at center with move
                jump annaCW

$ title = ""
label annaCWTitleQ:
    if _return == 0: # represents that the first image is picked...
        $ title = "Our Lady of Airbags (aka Kiss of Life)"
    guide "The title of this piece is %(title)s."
    jump annaCWquestions

screen imenu(*imgs):
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
                    idle im.Scale("images/Back_Arrow.png", img_size,100)
                    action Jump("enter_gallery2")
    