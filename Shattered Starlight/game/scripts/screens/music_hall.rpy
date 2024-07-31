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

screen music_hall(title = "请选择音乐", author = "......", description = "......", song_image = "") :
    
    tag menu
    
    use music_hall_navigation :
            
        vbox :
            pos (30,30)

            vbox :
                spacing 20
                label _(title)
                # add song_image
                text author
                text description

screen music_hall_navigation :
    # 背景
    add "#FFFFFF"

    tag menu

    # 顶部导航条
    frame:
        pos (0, 0)
        xysize (1920, 127)
        background "#E8E8E8"

    textbutton "返回" :
        
        pos (0, 0)
        background "#FFEFDB"
        xysize(135, 104)
        action Return()

    hbox :
        xpos 1063
        ypos 0
        spacing 10

        button :
            xysize (200, 107)
            background "#FFEFDB"
        button :
            xysize (200, 107)
            background "#FFEFDB"
        button :
            xysize (200, 107)
            background "#FFEFDB"
        button :
            xysize (200, 107)
            background "#FFEFDB"

    # 按钮
    grid 2 1 :
        xpos 1145
        ypos 165
        spacing 40
        style_prefix "radio"
        for sk, info in music_info.items() :
            
            textbutton info["name"]+" - "+info["author"] :
                xysize (317, 102)
                background "#CCCCCC"
                action [
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
    
    hbox :
        pos(1145, 837)
        spacing 20
        button:
            xysize (82,61)
            background "#D6A05E"
        button:
            xysize (82,61)
            background "#fcd19d"
        button:
            xysize (270,61)
            background "#D6A05E"
        button:
            xysize (82,61)
            background "#fcd19d"
        button:
            xysize (82,61)
            background "#D6A05E"
        
    # 滑动条
    bar :
        xpos 1145
        ypos 953
        xysize (684, 33)
        value Preference("music volume")

    # 展示区域
    frame:
        xpos 25
        ypos 748
        xysize (994, 302)
        background "#FFEFDB"

        transclude
    
    frame :
        xpos 75
        ypos 840
        xysize(898, 5)
        background "#D6A05E"