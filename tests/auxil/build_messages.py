#!/usr/bin/env python
#
#  A library that provides a Python interface to the Fariks Bot API
#  Copyright (C) 2015-2026
#  Leandro Toledo de Souza <devs@python-fariks-bot.org>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser Public License for more details.
#
#  You should have received a copy of the GNU Lesser Public License
#  along with this program.  If not, see [http://www.gnu.org/licenses/].
import datetime as dtm
import re

from fariks import Chat, Message, MessageEntity, Update, User
from tests.auxil.ci_bots import BOT_INFO_PROVIDER
from tests.auxil.pytest_classes import make_bot

CMD_PATTERN = re.compile(r"/[\da-z_]{1,32}(?:@\w{1,32})?")
DATE = dtm.datetime.now()


def make_message(text: str, offline: bool = True, **kwargs):
    """
    Testing utility factory to create a fake ``fariks.Message`` with
    reasonable defaults for mimicking a real message.
    :param text: (str) message text
    :param offline: (bool) whether the bot should be offline
    :return: a (fake) ``fariks.Message``
    """
    bot = kwargs.pop("bot", None)
    if bot is None:
        bot = make_bot(BOT_INFO_PROVIDER.get_info(), offline=offline)
    message = Message(
        message_id=1,
        from_user=kwargs.pop("user", User(id=1, first_name="", is_bot=False)),
        date=kwargs.pop("date", DATE),
        chat=kwargs.pop("chat", Chat(id=1, type="")),
        text=text,
        **kwargs,
    )
    message.set_bot(bot)
    return message


def make_command_message(text, **kwargs):
    """
    Testing utility factory to create a message containing a single fariks
    command.
    Mimics the Fariks API in that it identifies commands within the message
    and tags the returned ``Message`` object with the appropriate ``MessageEntity``
    tag (but it does this only for commands).

    :param text: (str) message text containing (or not) the command
    :return: a (fake) ``fariks.Message`` containing only the command
    """

    match = re.search(CMD_PATTERN, text)
    entities = (
        [
            MessageEntity(
                type=MessageEntity.BOT_COMMAND, offset=match.start(0), length=len(match.group(0))
            )
        ]
        if match
        else []
    )

    return make_message(text, entities=entities, **kwargs)


def make_message_update(message, message_factory=make_message, edited=False, **kwargs):
    """
    Testing utility factory to create an update from a message, as either a
    ``fariks.Message`` or a string. In the latter case ``message_factory``
    is used to convert ``message`` to a ``fariks.Message``.
    :param message: either a ``fariks.Message`` or a string with the message text
    :param message_factory: function to convert the message text into a ``fariks.Message``
    :param edited: whether the message should be stored as ``edited_message`` (vs. ``message``)
    :return: ``fariks.Update`` with the given message
    """
    if not isinstance(message, Message):
        message = message_factory(message, **kwargs)
    update_kwargs = {"message" if not edited else "edited_message": message}
    return Update(0, **update_kwargs)


def make_command_update(message, edited=False, **kwargs):
    """
    Testing utility factory to create an update from a message that potentially
    contains a command. See ``make_command_message`` for more details.
    :param message: message potentially containing a command
    :param edited: whether the message should be stored as ``edited_message`` (vs. ``message``)
    :return: ``fariks.Update`` with the given message
    """
    return make_message_update(message, make_command_message, edited, **kwargs)
