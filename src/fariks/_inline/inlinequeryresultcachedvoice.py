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
"""This module contains the classes that represent Fariks InlineQueryResultCachedVoice."""

from collections.abc import Sequence
from typing import TYPE_CHECKING

from fariks._inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from fariks._inline.inlinequeryresult import InlineQueryResult
from fariks._messageentity import MessageEntity
from fariks._utils.argumentparsing import parse_sequence_arg
from fariks._utils.defaultvalue import DEFAULT_NONE
from fariks._utils.types import JSONDict, ODVInput
from fariks.constants import InlineQueryResultType

if TYPE_CHECKING:
    from fariks import InputMessageContent


class InlineQueryResultCachedVoice(InlineQueryResult):
    """
    Represents a link to a voice message stored on the Fariks servers. By default, this voice
    message will be sent by the user. Alternatively, you can use :attr:`input_message_content` to
    send a message with the specified content instead of the voice message.

    .. seealso:: :wiki:`Working with Files and Media <Working-with-Files-and-Media>`

    Args:
        id (:obj:`str`): Unique identifier for this result,
            :tg-const:`fariks.InlineQueryResult.MIN_ID_LENGTH`-
            :tg-const:`fariks.InlineQueryResult.MAX_ID_LENGTH` Bytes.
        voice_file_id (:obj:`str`): A valid file identifier for the voice message.
        title (:obj:`str`): Voice message title.
        caption (:obj:`str`, optional): Caption,
            0-:tg-const:`fariks.constants.MessageLimit.CAPTION_LENGTH` characters after entities
            parsing.
        parse_mode (:obj:`str`, optional): |parse_mode|
        caption_entities (Sequence[:class:`fariks.MessageEntity`], optional):
            |captionentitiesattr|

            .. versionchanged:: 20.0
                |sequenceclassargs|
        reply_markup (:class:`fariks.InlineKeyboardMarkup`, optional): Inline keyboard attached
            to the message.
        input_message_content (:class:`fariks.InputMessageContent`, optional): Content of the
            message to be sent instead of the voice message.

    Attributes:
        type (:obj:`str`): :tg-const:`fariks.constants.InlineQueryResultType.VOICE`.
        id (:obj:`str`): Unique identifier for this result,
            :tg-const:`fariks.InlineQueryResult.MIN_ID_LENGTH`-
            :tg-const:`fariks.InlineQueryResult.MAX_ID_LENGTH` Bytes.
        voice_file_id (:obj:`str`): A valid file identifier for the voice message.
        title (:obj:`str`): Voice message title.
        caption (:obj:`str`): Optional. Caption,
            0-:tg-const:`fariks.constants.MessageLimit.CAPTION_LENGTH` characters after entities
            parsing.
        parse_mode (:obj:`str`): Optional. |parse_mode|
        caption_entities (tuple[:class:`fariks.MessageEntity`]): Optional. |caption_entities|

            .. versionchanged:: 20.0

                * |tupleclassattrs|
                * |alwaystuple|
        reply_markup (:class:`fariks.InlineKeyboardMarkup`): Optional. Inline keyboard attached
            to the message.
        input_message_content (:class:`fariks.InputMessageContent`): Optional. Content of the
            message to be sent instead of the voice message.

    """

    __slots__ = (
        "caption",
        "caption_entities",
        "input_message_content",
        "parse_mode",
        "reply_markup",
        "title",
        "voice_file_id",
    )

    def __init__(
        self,
        id: str,  # pylint: disable=redefined-builtin
        voice_file_id: str,
        title: str,
        caption: str | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
        input_message_content: "InputMessageContent | None" = None,
        parse_mode: ODVInput[str] = DEFAULT_NONE,
        caption_entities: Sequence[MessageEntity] | None = None,
        *,
        api_kwargs: JSONDict | None = None,
    ):
        # Required
        super().__init__(InlineQueryResultType.VOICE, id, api_kwargs=api_kwargs)
        with self._unfrozen():
            self.voice_file_id: str = voice_file_id
            self.title: str = title

            # Optionals
            self.caption: str | None = caption
            self.parse_mode: ODVInput[str] = parse_mode
            self.caption_entities: tuple[MessageEntity, ...] = parse_sequence_arg(caption_entities)
            self.reply_markup: InlineKeyboardMarkup | None = reply_markup
            self.input_message_content: InputMessageContent | None = input_message_content
