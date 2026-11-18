init python:
    import random 
    jp_words = {
        "猫": ["кот", "кошка"],
        "火": ["огонь"],
        "水": ["вода"],
        "本": ["книга"],
    }

label start:
    scene astory:
        fit "cover"
    # Создаём список всех ключей (японских слов) и перемешиваем их
    $ words_pool = list(jp_words.keys())
    $ random.shuffle(words_pool)

    # Счётчик правильных ответов и общее количество слов 
    $ level_score = 0
    $ total_level_words = len(words_pool)

# Цикл игры 
label game_loop:
    if len(words_pool) > 0:

        $ current_jp = words_pool.pop(0)
        
        $ valid_answers = jp_words[current_jp]

        $ player_answer = renpy.input("Как переводится слово: [current_jp]?").strip().lower()


        # Проверяем, есть ли ответ игрока в списке правильных вариантов
        if player_answer in valid_answers:
            $ level_score += 1
            "Правильно!"
        else:
            $ correct_show = valid_answers[0]
            "Неверно. Правильный ответ: [correct_show]."

        jump game_loop
    else:
        jump level_results

label level_results:
    "Тест завершён! Правильных ответов: [level_score] из [total_level_words]."
    return