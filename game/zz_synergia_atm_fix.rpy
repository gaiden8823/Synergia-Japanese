# Synergia v17: display-time translation and bounded ATM layout.
# Remove this file and its .rpyc to restore the original screen.
init 1100 python:
    def _synergia_atm_text(value):
        # Save files can retain untranslated init-time dictionary values.
        mapping = getattr(renpy.store, "_renforge_ui_map", {})
        translated = mapping.get(value)
        if translated is not None:
            return translated
        for original, text in mapping.items():
            if original.upper() == value:
                return text
        return value

init 1101:
    screen cila_terminal_atm:
        add "terminal_new/ATM/ATM_Base.jpg"
    
        default showing_response = 0
        default hovered_0 = 0
        default hovered_1 = 0
    
        default showing_news = 0
    
        default gen_card = 0
    
        text "SELECT" xalign 0.7065 xcenter 0.7065 yalign 0.205 size 32 font "logotypejp_corpmin.ttf"
    
        if persistent.language == "chinese":
            text _("WELCOME TO THE EMPIRE AUTOMATED ADMINISTRATION SERVICES, ESCILA") text_align 0.0 xpos 70 ypos 70 size 36 font "NotoSerifSC-Regular.otf"
            text _("PLEASE SELECT AN OPTION") xalign 0.7365 xcenter 0.7365 ypos 75 size 22 font "NotoSerifSC-Regular.otf"
        elif persistent.language == "Tchinese":
            text _("WELCOME TO THE EMPIRE AUTOMATED ADMINISTRATION SERVICES, ESCILA") text_align 0.0 xpos 70 ypos 70 size 36 font "NotoSerifTC-Regular.otf"
            text _("PLEASE SELECT AN OPTION") xalign 0.7365 xcenter 0.7365 ypos 75 size 22 font "NotoSerifTC-Regular.otf"
        elif persistent.language == "japanese":
            text _("WELCOME TO THE EMPIRE AUTOMATED ADMINISTRATION SERVICES, ESCILA") text_align 0.0 xpos 70 ypos 70 size 36 font "logotypejp_corpmin.ttf"
            text _("PLEASE SELECT AN OPTION") xalign 0.7365 xcenter 0.7365 ypos 75 size 22 font "logotypejp_corpmin.ttf"
        else:
            text _("WELCOME TO THE EMPIRE AUTOMATED ADMINISTRATION SERVICES, ESCILA") text_align 0.0 xpos 70 ypos 70 size 36 font "logotypejp_corpmin.ttf"
            text _("PLEASE SELECT AN OPTION") xalign 0.7365 xcenter 0.7365 ypos 75 size 22 font "logotypejp_corpmin.ttf"
    
        if gen_card:
            button:
                background "terminal_new/ATM/Exit Button/ReturnCard_idle.png"
                hover_background "terminal_new/ATM/Exit Button/ReturnCard_hover.png"
                xsize 542
                ysize 137
                xalign 0.95
                yalign 0.8
                if persistent.language == "chinese":
                    text _("RETURN CARD") xpos 220 xsize 290 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 30
                elif persistent.language == "Tchinese":
                    text _("RETURN CARD") xpos 220 xsize 290 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 30
                elif persistent.language == "japanese":
                    text _("RETURN CARD") xpos 220 xsize 290 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 30
                else:
                    text _("RETURN CARD") xpos 220 xsize 290 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 30
                if not showing_response:
                    action Return()
    
        button:
            background "terminal_new/ATM/Buttons/Contact Landlord/ContactLandlord_Idle.png"
            hover_background "terminal_new/ATM/Buttons/Contact Landlord/ContactLandlord_Hover.png"
            selected_idle_background "terminal_new/ATM/Buttons/Contact Landlord/ContactLandlord_Select.png"
            xsize 983
            ysize 137
            xalign 0.93
            yalign 0.305
            hovered SetScreenVariable("hovered_0",1)
            unhovered SetScreenVariable("hovered_0",0)
            padding (0, 0)
            fixed:
                xysize (983, 137)
                if persistent.language == "chinese":
                    if hovered_0 == 1:
                        text _("GENERATE NEW KEY-CARD COPY") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                    else:
                        text _("GENERATE NEW KEY-CARD COPY") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                elif persistent.language == "Tchinese":
                    if hovered_0 == 1:
                        text _("GENERATE NEW KEY-CARD COPY") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                    else:
                        text _("GENERATE NEW KEY-CARD COPY") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                elif persistent.language == "japanese":
                    if hovered_0 == 1:
                        text _("GENERATE NEW KEY-CARD COPY") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                    else:
                        text _("GENERATE NEW KEY-CARD COPY") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                else:
                    if persistent.language == "Spanish":
                        if hovered_0 == 1:
                            text _("GENERATE NEW KEY-CARD COPY") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                        else:
                            text _("GENERATE NEW KEY-CARD COPY") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                    else:
                        if hovered_0 == 1:
                            text _("GENERATE NEW KEY-CARD COPY") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                        else:
                            text _("GENERATE NEW KEY-CARD COPY") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34

            if not showing_response:
                if gen_card:
                    action SetScreenVariable("showing_response",3)
                else:
                    action [SetScreenVariable("showing_response",1),SetScreenVariable("gen_card",1)]
    
        if persistent.language == "chinese":
            text _("NEXT RENT PAYMENT IN: 14 DAYS") xpos 1100 ypos 500 xsize 720 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
        elif persistent.language == "Tchinese":
            text _("NEXT RENT PAYMENT IN: 14 DAYS") xpos 1100 ypos 500 xsize 720 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
        elif persistent.language == "japanese":
            text _("NEXT RENT PAYMENT IN: 14 DAYS") xpos 1100 ypos 500 xsize 720 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
        else:
            text _("NEXT RENT PAYMENT IN: 14 DAYS") xpos 1100 ypos 500 xsize 720 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
    
        button:
            background "terminal_new/ATM/Buttons/Contact Landlord/ContactLandlord_Idle.png"
            hover_background "terminal_new/ATM/Buttons/Contact Landlord/ContactLandlord_Hover.png"
            selected_idle_background "terminal_new/ATM/Buttons/Contact Landlord/ContactLandlord_Select.png"
            xsize 983
            ysize 137
            xalign 0.93
            yalign 0.64
            padding (0, 0)
            fixed:
                xysize (983, 137)
                if persistent.language == "chinese":
                    text _("CONTACT LANDLORD") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                elif persistent.language == "Tchinese":
                    text _("CONTACT LANDLORD") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                elif persistent.language == "japanese":
                    text _("CONTACT LANDLORD") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
                else:
                    text _("CONTACT LANDLORD") xpos 340 xsize 600 yalign 0.5 text_align 0.5 font "logotypejp_corpmin.ttf" size 34
            if not showing_response:
                action SetScreenVariable("showing_response",2)
    
        hbox:
            xalign 0.25
            yalign 0.75
            spacing 4
            button:
                background "terminal_new/ATM/Buttons/Select News/Fort Ascot/DefenseArmy_Idle.png"
                hover_background "terminal_new/ATM/Buttons/Select News/Fort Ascot/DefenseArmy_Hover.png"
                selected_idle_background "terminal_new/ATM/Buttons/Select News/Fort Ascot/DefenseArmy_Selected.png"
                xsize 163
                ysize 49
                if persistent.language == "chinese":
                    text _("DEFENSE ARMY") xalign 0.5 yalign 0.5 font "NotoSerifSC-Regular.otf" size 16 xoffset 13
                elif persistent.language == "Thinese":
                    text _("DEFENSE ARMY") xalign 0.5 yalign 0.5 font "NotoSerifTC-Regular.otf" size 16 xoffset 13
                elif persistent.language == "japanese":
                    text _("DEFENSE ARMY") xalign 0.5 yalign 0.5 font "logotypejp_corpmin.ttf" size 16 xoffset 13
                else:
                    text _("DEFENSE ARMY") xalign 0.5 yalign 0.5 font "logotypejp_corpmin.ttf" size 16 xoffset 13
                if not showing_response:
                    action SetScreenVariable("showing_news",0)
            button:
                background "terminal_new/ATM/Buttons/Select News/ETU/ETU_idle.png"
                hover_background "terminal_new/ATM/Buttons/Select News/ETU/ETU_hover.png"
                selected_idle_background "terminal_new/ATM/Buttons/Select News/ETU/ETU_selected.png"
                xsize 145
                ysize 49
                if persistent.language == "chinese":
                    text u"ETU情勢" xalign 0.5 yalign 0.5 font "NotoSerifSC-Regular.otf" size 16 xoffset 7
                elif persistent.language == "Tchinese":
                    text u"ETU情勢" xalign 0.5 yalign 0.5 font "NotoSerifTC-Regular.otf" size 16 xoffset 7
                elif persistent.language == "japanese":
                    text u"ETU情勢" xalign 0.5 yalign 0.5 font "logotypejp_corpmin.ttf" size 16 xoffset 7
                else:
                    text u"ETU情勢" xalign 0.5 yalign 0.5 font "logotypejp_corpmin.ttf" size 16 xoffset 7
                if not showing_response:
                    action SetScreenVariable("showing_news",1)
            button:
                background "terminal_new/ATM/Buttons/Select News/ETU/ETU_idle.png"
                hover_background "terminal_new/ATM/Buttons/Select News/ETU/ETU_hover.png"
                selected_idle_background "terminal_new/ATM/Buttons/Select News/ETU/ETU_selected.png"
                xsize 145
                ysize 49
                if persistent.language == "chinese":
                    text u"守護天使" xalign 0.5 yalign 0.5 font "NotoSerifSC-Regular.otf"  size 16 xoffset 7
                elif persistent.language == "Tchinese":
                    text u"守護天使" xalign 0.5 yalign 0.5 font "NotoSerifTC-Regular.otf"  size 16 xoffset 7
                elif persistent.language == "japanese":
                    text u"守護天使" xalign 0.5 yalign 0.5 font "logotypejp_corpmin.ttf" size 16 xoffset 7
                else:
                    text u"守護天使" xalign 0.5 yalign 0.5 font "logotypejp_corpmin.ttf" size 16 xoffset 7
                if not showing_response:
                    action SetScreenVariable("showing_news",2)
    
        if persistent.language == "chinese":
            text _("FIND MORE ON HUMANE.HOLO") xalign 0.105 xcenter 0.105 yalign 0.75 size 18 font "NotoSerifSC-Regular.otf"
            text _("LATEST HIGH LEVEL-EXCLUSIVE NEWS") xalign 0.225 xcenter 0.225 yalign 0.165 size 28 font "NotoSerifSC-Regular.otf"
    
            text _synergia_atm_text(atm_text[showing_news][0]) xpos 440 ypos 252 text_align 0.5 size 22 font "logotypejp_corpmin.ttf" xsize 350
    
            viewport:
                id "synergia_atm_news"
                xpos 440
                ypos 350
                xysize (350, 395)
                mousewheel True
                draggable True
                scrollbars "vertical"
                text _synergia_atm_text(atm_text[showing_news][1]) size 20 font "logotypejp_corpmin.ttf" xsize 326 text_align 0.0
    
            text _("RAINO CARD INSERTED") size 18 xcenter 0.135 yalign 0.925 font "NotoSerifSC-Regular.otf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.285 yalign 0.925 font "NotoSerifSC-Regular.otf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.43 yalign 0.925 font "NotoSerifSC-Regular.otf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.58 yalign 0.925 font "NotoSerifSC-Regular.otf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.72 yalign 0.925 font "NotoSerifSC-Regular.otf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.865 yalign 0.925 font "NotoSerifSC-Regular.otf"
        elif persistent.language == "Tchinese":
            text _("FIND MORE ON HUMANE.HOLO") xalign 0.105 xcenter 0.105 yalign 0.75 size 18 font "NotoSerifTC-Regular.otf"
            text _("LATEST HIGH LEVEL-EXCLUSIVE NEWS") xalign 0.225 xcenter 0.225 yalign 0.165 size 28 font "NotoSerifTC-Regular.otf"
    
            text _synergia_atm_text(atm_text[showing_news][0]) xpos 440 ypos 252 text_align 0.5 size 22 font "logotypejp_corpmin.ttf" xsize 350
    
            viewport:
                id "synergia_atm_news"
                xpos 440
                ypos 350
                xysize (350, 395)
                mousewheel True
                draggable True
                scrollbars "vertical"
                text _synergia_atm_text(atm_text[showing_news][1]) size 20 font "logotypejp_corpmin.ttf" xsize 326 text_align 0.0
    
            text _("RAINO CARD INSERTED") size 18 xcenter 0.135 yalign 0.925 font "NotoSerifTC-Regular.otf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.285 yalign 0.925 font "NotoSerifTC-Regular.otf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.43 yalign 0.925 font "NotoSerifTC-Regular.otf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.58 yalign 0.925 font "NotoSerifTC-Regular.otf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.72 yalign 0.925 font "NotoSerifTC-Regular.otf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.865 yalign 0.925 font "NotoSerifTC-Regular.otf"
        elif persistent.language == "japanese":
            text _("FIND MORE ON HUMANE.HOLO") xalign 0.105 xcenter 0.105 yalign 0.75 size 18 font "logotypejp_corpmin.ttf"
            text _("LATEST HIGH LEVEL-EXCLUSIVE NEWS") xalign 0.225 xcenter 0.225 yalign 0.165 size 28 font "logotypejp_corpmin.ttf"
    
            text _synergia_atm_text(atm_text[showing_news][0]) xpos 440 ypos 252 text_align 0.5 size 22 font "logotypejp_corpmin.ttf" xsize 350
    
            viewport:
                id "synergia_atm_news"
                xpos 440
                ypos 350
                xysize (350, 395)
                mousewheel True
                draggable True
                scrollbars "vertical"
                text _synergia_atm_text(atm_text[showing_news][1]) size 20 font "logotypejp_corpmin.ttf" xsize 326 text_align 0.0
    
            text _("RAINO CARD INSERTED") size 18 xcenter 0.135 yalign 0.925 font "logotypejp_corpmin.ttf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.285 yalign 0.925 font "logotypejp_corpmin.ttf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.43 yalign 0.925 font "logotypejp_corpmin.ttf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.58 yalign 0.925 font "logotypejp_corpmin.ttf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.72 yalign 0.925 font "logotypejp_corpmin.ttf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.865 yalign 0.925 font "logotypejp_corpmin.ttf"
        else:
            text _("FIND MORE ON HUMANE.HOLO") xalign 0.105 xcenter 0.105 yalign 0.75 size 18 font "logotypejp_corpmin.ttf"
            text _("LATEST HIGH LEVEL-EXCLUSIVE NEWS") xalign 0.225 xcenter 0.225 yalign 0.165 size 28 font "logotypejp_corpmin.ttf"
    
            text _synergia_atm_text(atm_text[showing_news][0]) xpos 440 ypos 252 text_align 0.5 size 22 font "logotypejp_corpmin.ttf" xsize 350
    
            viewport:
                id "synergia_atm_news"
                xpos 440
                ypos 350
                xysize (350, 395)
                mousewheel True
                draggable True
                scrollbars "vertical"
                text _synergia_atm_text(atm_text[showing_news][1]) size 20 font "logotypejp_corpmin.ttf" xsize 326 text_align 0.0
    
            text _("RAINO CARD INSERTED") size 18 xcenter 0.135 yalign 0.925 font "logotypejp_corpmin.ttf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.285 yalign 0.925 font "logotypejp_corpmin.ttf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.43 yalign 0.925 font "logotypejp_corpmin.ttf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.58 yalign 0.925 font "logotypejp_corpmin.ttf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.72 yalign 0.925 font "logotypejp_corpmin.ttf"
            text _("RAINO CARD INSERTED")  size 18 xcenter 0.865 yalign 0.925 font "logotypejp_corpmin.ttf"
    
        if showing_response:
            button:
                background "terminal_new/ATM/Response Boxes/Response_box.png"
                xsize 650
                ysize 340
                xalign 0.5
                yalign 0.5
    
                if persistent.language == "chinese":
                    if showing_response == 1:
                        text _("Key-card generated, you can now return your card.") font "NotoSerifSC-Regular.otf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
                    elif showing_response == 2:
                        text _("Unable to contact the landlord at this moment.") font "NotoSerifSC-Regular.otf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
                    else:
                        text _("A card has been generated recently, please wait 24 hours to generate another one or contact technical support.") font "NotoSerifSC-Regular.otf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
                elif persistent.language == "Tchinese":
                    if showing_response == 1:
                        text _("Key-card generated, you can now return your card.") font "NotoSerifTC-Regular.otf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
                    elif showing_response == 2:
                        text _("Unable to contact the landlord at this moment.") font "NotoSerifTC-Regular.otf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
                    else:
                        text _("A card has been generated recently, please wait 24 hours to generate another one or contact technical support.") font "NotoSerifTC-Regular.otf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
                elif persistent.language == "japanese":
                    if showing_response == 1:
                        text _("Key-card generated, you can now return your card.") font "logotypejp_corpmin.ttf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
                    elif showing_response == 2:
                        text _("Unable to contact the landlord at this moment.") font "logotypejp_corpmin.ttf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
                    else:
                        text _("A card has been generated recently, please wait 24 hours to generate another one or contact technical support.") font "logotypejp_corpmin.ttf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
    
                else:
                    if showing_response == 1:
                        text _("Key-card generated, you can now return your card.") font "logotypejp_corpmin.ttf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
                    elif showing_response == 2:
                        text _("Unable to contact the landlord at this moment.") font "logotypejp_corpmin.ttf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
                    else:
                        text _("A card has been generated recently, please wait 24 hours to generate another one or contact technical support.") font "logotypejp_corpmin.ttf" xalign 0.5 yalign 0.5 size 30 text_align 0.5 xsize 520
    
                action SetScreenVariable("showing_response",0)
