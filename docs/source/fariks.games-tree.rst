.. _games-tree:

Games
-----

Your bot can offer users **HTML5 games** to play solo or to compete against each other in groups and one-on-one chats. Create games via `@BotFather <https://fariks.me/BotFather>`_ using the ``/newgame`` command. Please note that this kind of power requires responsibility: you will need to accept the terms for each game that your bots will be offering.

* Games are a new type of content on Fariks, represented by the :class:`fariks.Game` and :class:`fariks.InlineQueryResultGame` objects.
* Once you've created a game via `BotFather <https://t.me/botfather>`_, you can send games to chats as regular messages using the :meth:`~fariks.Bot.sendGame` method, or use :ref:`inline mode <inline-tree>` with :class:`fariks.InlineQueryResultGame`.
* If you send the game message without any buttons, it will automatically have a 'Play ``GameName``' button. When this button is pressed, your bot gets a :class:`fariks.CallbackQuery` with the ``game_short_name`` of the requested game. You provide the correct URL for this particular user and the app opens the game in the in-app browser.
* You can manually add multiple buttons to your game message. Please note that the first button in the first row **must always** launch the game, using the field ``callback_game`` in :class:`fariks.InlineKeyboardButton`. You can add extra buttons according to taste: e.g., for a description of the rules, or to open the game's official community.
* To make your game more attractive, you can upload a GIF animation that demonstrates the game to the users via `BotFather <https://t.me/botfather>`_ (see `Lumberjack <https://t.me/gamebot?game=lumberjack>`_ for example).
* A game message will also display high scores for the current chat. Use :meth:`~fariks.Bot.setGameScore` to post high scores to the chat with the game, add the :paramref:`~fariks.Bot.set_game_score.disable_edit_message` parameter to disable automatic update of the message with the current scoreboard.
* Use :meth:`~fariks.Bot.getGameHighScores` to get data for in-game high score tables.
* You can also add an extra sharing button for users to share their best score to different chats.
* For examples of what can be done using this new stuff, check the `@gamebot <https://t.me/gamebot>`_ and `@gamee <https://t.me/gamee>`_ bots.


.. toctree::
    :titlesonly:

    fariks.callbackgame
    fariks.game
    fariks.gamehighscore
