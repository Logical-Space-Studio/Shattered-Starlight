init python:
    import os
    # 定义音乐信息的字典
    music_info = {
        "leisure_dusk": {
            "name": "Leisure Dusk",
            "author": "Akira",
            "description": "",
            "image": "bg_song1.jpg"
        },
        "walks": {
            "name": "Walks",
            "author": "Akira",
            "description": "",
            "image": "bg_song2.jpg"
        },
        # 添加更多乐曲信息
    }


screen music_hall_navigation :

    tag menu
    
    use game_menu(_("音乐厅")) :
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
                    xsize 480

                    spacing 10 # 元素间留白
                    vbox :
                        label _("音乐列表")

                        style_prefix "radio"
                        for sk, info in music_info.items() :
                            
                            textbutton info["name"]+" - "+info["author"] action [
                                SetVariable("current_song", sk),
                                SetVariable("info", music_info[sk]),
                                Play("music", "assets/music/" + sk + ".wav"),
                                Return(),
                                ShowMenu(
                                    "music_hall",
                                    title = info["name"],
                                    author = info["author"],
                                    description = info["description"],
                                    song_image = info["image"]
                                )
                            ]
                        
                vbox :
                    xsize 1280
                    
                    transclude

screen music_hall(title = "请选择音乐", author = "......", description = "......", song_image = "") :
    
    tag menu
    
    use music_hall_navigation :
            
        viewport :
            xsize 960
            xinitial 0.0
            yinitial 0.0
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            
            spacing 20

            vbox :
                label _(title)
                # add song_image
                spacing 10
                label _("作曲")
                text author
                label _("介绍")
                text description