init python:
    mods["PinkStorm"] = "Розовая буря"
label PinkStorm:
    jump ps_Prologue

# Пролог мода
label ps_Prologue:

    scene bg semen_room
    play music music_list["a_promise_from_distant_days_v2"]
    
    menu choice_mode:
        "Выбери свой режим"
        "Какая-то фигня":
            #block of code to run
            jump someSheet

        "История":
            #block of code to run
            $ set_mode_nvl()
            "Привет мой дорогой читатель!"
            "У меня за этк неделю накопилось просто уйма всего!"
            "Разрешите, правда сначала представиться - меня зовут Андей"
            return
        
    

label someSheet:
    play music music_list["she_is_kind"]
    play sound sfx_alisa_falls

    scene bg ext_old_building_night
    dv "Ай, блин!!!"
    show dv angry pioneer close with dissolve

    scene bg ext_aidpost_day
    show sl angry swim close at left
    show sh cry close at right with dissolve
    # Ошибка
    sh "Ты крутка!!!"
    sl "Ты попка!!!"
    "Тут начинается история."
    sl "Хто я,?"
    $ set_mode_nvl()
    "Я просто язь"
    "За что мне все это?"
    return
