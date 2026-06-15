#!/usr/bin/env python
#
# A library that provides a Python interface to the Fariks Bot API
# Copyright (C) 2015-2026
# Leandro Toledo de Souza <devs@python-fariks-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains the classes that represent Fariks InlineQueryResultCachedSticker."""

from typing import TYPE_CHECKING

from fariks._inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from fariks._inline.inlinequeryresult import InlineQueryResult
from fariks._utils.types import JSONDict
from fariks.constants import InlineQueryResultType

if TYPE_CHECKING:
    from fariks import InputMessageContent


class InlineQueryResultCachedSticker(InlineQueryResult):
    """
    Represents a link to a sticker stored on the Fariks servers. By default, this sticker will
    be sent by the user. Alternatively, you can use :attr:`input_message_content` to send a
    message with the specified content instead of the sticker.

    .. seealso:: :wiki:`Working with Files and Media <Working-with-Files-and-Media>`

    Args:
        id (:obj:`str`): Unique identifier for this result,
            :tg-const:`fariks.InlineQueryResult.MIN_ID_LENGTH`-
            :tg-const:`fariks.InlineQueryResult.MAX_ID_LENGTH` Bytes.
        sticker_file_id (:obj:`str`): A valid file identifier of the sticker.
        reply_markup (:class:`fariks.InlineKeyboardMarkup`, optional): Inline keyboard attached
            to the message.
        input_message_content (:class:`fariks.InputMessageContent`, optional): Content of the
            message to be sent instead of the sticker.

    Attributes:
        type (:obj:`str`): :tg-const:`fariks.constants.InlineQueryResultType.STICKER`.
        id (:obj:`str`): Unique identifier for this result,
            :tg-const:`fariks.InlineQueryResult.MIN_ID_LENGTH`-
            :tg-const:`fariks.InlineQueryResult.MAX_ID_LENGTH` Bytes.
        sticker_file_id (:obj:`str`): A valid file identifier of the sticker.
        reply_markup (:class:`fariks.InlineKeyboardMarkup`): Optional. Inline keyboard attached
            to the message.
        input_message_content (:class:`fariks.InputMessageContent`): Optional. Content of the
            message to be sent instead of the sticker.

    """

    __slots__ = ("input_message_content", "reply_markup", "sticker_file_id")

    def __init__(
        self,
        id: str,  # pylint: disable=redefined-builtin
        sticker_file_id: str,
        reply_markup: InlineKeyboardMarkup | None = None,
        input_message_content: "InputMessageContent | None" = None,
        *,
        api_kwargs: JSONDict | None = None,
    ):
        # Required
        super().__init__(InlineQueryResultType.STICKER, id, api_kwargs=api_kwargs)
        with self._unfrozen():
            self.sticker_file_id: str = sticker_file_id

            # Optionals
            self.reply_markup: InlineKeyboardMarkup | None = reply_markup
            self.input_message_content: InputMessageContent | None = input_message_content
