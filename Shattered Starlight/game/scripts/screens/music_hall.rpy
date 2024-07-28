init python:
    import os
    # 定义音乐信息的字典
    music_info = {
        "leisure_dusk": {"name": "Leisure Dusk", "author": "Akira", "image": "bg_song1.jpg"},
        "walks": {"name": "Walks", "author": "Akira", "image": "bg_song2.jpg"},
        # 添加更多乐曲信息
    }


screen music_hall_navigation :

    tag menu
    
    use game_menu(_("音乐厅"), scroll="vbox") :
        #vbox :

        vbox :
            
            hbox :
                viewport : 
                    xinitial 0.0
                    yinitial 0.0
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    xsize 640

                    spacing 10 # 元素间留白
                    vbox :
                        label _("音乐列表")
                        style_prefix "radio"

                        $ sk0 = list(music_info.keys())[0]
                        $ info = music_info[sk0]
                        textbutton info["name"]+" - "+info["author"] action [
                            SetVariable("current_song", sk0),
                            SetVariable("info", music_info[sk0]),
                            Play("music", "assets/music/" + sk0 + ".wav"),
                            ShowMenu("info_" + sk0)
                        ]

                        $ sk1 = list(music_info.keys())[1]
                        $ info = music_info[sk1]
                        textbutton info["name"]+" - "+info["author"] action [
                            SetVariable("current_song", sk1),
                            SetVariable("info", music_info[sk1]),
                            Play("music", "assets/music/" + sk1 + ".wav"),
                            ShowMenu("info_" + sk1)
                        ]
                        
                
                vbox :
                    xsize 1280
                    
                    transclude

screen music_hall() :
    tag menu
    use music_hall_navigation :
        vbox :
            label _("请选择音乐")
            label _("作曲")
            text "......"
            label _("介绍")
            text "......"size 40


screen info_leisure_dusk() :
    tag menu
    use music_hall_navigation :
        vbox :
            label _("Leisure Dusk")
            label _("作曲")
            text "Akira"
            label _("介绍")
            text "随便乱写的"

screen info_walks() :
    tag menu
    use music_hall_navigation :
        vbox :
            label _("Walks")
            label _("作曲")
            text "Akira"
            label _("介绍")
            text "随便乱写的"