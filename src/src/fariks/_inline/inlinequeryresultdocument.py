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
"""This module contains the classes that represent Fariks InlineQueryResultDocument"""

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


class InlineQueryResultDocument(InlineQueryResult):
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional
    caption. Alternatively, you can use :attr:`input_message_content` to send a message with the
    specified content instead of the file. Currently, only .PDF and .ZIP files can be sent
    using this method.

    .. seealso:: :wiki:`Working with Files and Media <Working-with-Files-and-Media>`

    .. versionchanged:: 20.5
        |removed_thumb_wildcard_note|

    Args:
        id (:obj:`str`): Unique identifier for this result,
            :tg-const:`fariks.InlineQueryResult.MIN_ID_LENGTH`-
            :tg-const:`fariks.InlineQueryResult.MAX_ID_LENGTH` Bytes.
        title (:obj:`str`): Title for the result.
        caption (:obj:`str`, optional): Caption of the document to be sent,
            0-:tg-const:`fariks.constants.MessageLimit.CAPTION_LENGTH` characters
            after entities parsing.
        parse_mode (:obj:`str`, optional): |parse_mode|
        caption_entities (Sequence[:class:`fariks.MessageEntity`], optional): |caption_entities|

            .. versionchanged:: 20.0
                |sequenceclassargs|

        document_url (:obj:`str`): A valid URL for the file.
        mime_type (:obj:`str`): Mime type of the content of the file, either "application/pdf"
            or "application/zip".
        description (:obj:`str`, optional): Short description of the result.
        reply_markup (:class:`fariks.InlineKeyboardMarkup`, optional): Inline keyboard attached
            to the message.
        input_message_content (:class:`fariks.InputMessageContent`, optional): Content of the
            message to be sent instead of the file.
        thumbnail_url (:obj:`str`, optional): URL of the thumbnail (JPEG only) for the file.

            .. versionadded:: 20.2
        thumbnail_width (:obj:`int`, optional): Thumbnail width.

            .. versionadded:: 20.2
        thumbnail_height (:obj:`int`, optional): Thumbnail height.

            .. versionadded:: 20.2


    Attributes:
        type (:obj:`str`): :tg-const:`fariks.constants.InlineQueryResultType.DOCUMENT`.
        id (:obj:`str`): Unique identifier for this result,
            :tg-const:`fariks.InlineQueryResult.MIN_ID_LENGTH`-
            :tg-const:`fariks.InlineQueryResult.MAX_ID_LENGTH` Bytes.
        title (:obj:`str`): Title for the result.
        caption (:obj:`str`): Optional. Caption of the document to be sent,
            0-:tg-const:`fariks.constants.MessageLimit.CAPTION_LENGTH` characters
            after entities parsing.
        parse_mode (:obj:`str`): Optional. |parse_mode|
        caption_entities (tuple[:class:`fariks.MessageEntity`]): Optional. |captionentitiesattr|

            .. versionchanged:: 20.0

                * |tupleclassattrs|
                * |alwaystuple|
        document_url (:obj:`str`): A valid URL for the file.
        mime_type (:obj:`str`): Mime type of the content of the file, either "application/pdf"
            or "application/zip".
        description (:obj:`str`): Optional. Short description of the result.
        reply_markup (:class:`fariks.InlineKeyboardMarkup`): Optional. Inline keyboard attached
            to the message.
        input_message_content (:class:`fariks.InputMessageContent`): Optional. Content of the
            message to be sent instead of the file.
        thumbnail_url (:obj:`str`): Optional. URL of the thumbnail (JPEG only) for the file.

            .. versionadded:: 20.2
        thumbnail_width (:obj:`int`): Optional. Thumbnail width.

            .. versionadded:: 20.2
        thumbnail_height (:obj:`int`): Optional. Thumbnail height.

            .. versionadded:: 20.2

    """

    __slots__ = (
        "caption",
        "caption_entities",
        "description",
        "document_url",
        "input_message_content",
        "mime_type",
        "parse_mode",
        "reply_markup",
        "thumbnail_height",
        "thumbnail_url",
        "thumbnail_width",
        "title",
    )

    def __init__(
        self,
        id: str,  # pylint: disable=redefined-builtin
        document_url: str,
        title: str,
        mime_type: str,
        caption: str | None = None,
        description: str | None = None,
        reply_markup: InlineKeyboardMarkup | None = None,
        input_message_content: "InputMessageContent | None" = None,
        parse_mode: ODVInput[str] = DEFAULT_NONE,
        caption_entities: Sequence[MessageEntity] | None = None,
        thumbnail_url: str | None = None,
        thumbnail_width: int | None = None,
        thumbnail_height: int | None = None,
        *,
        api_kwargs: JSONDict | None = None,
    ):
        # Required
        super().__init__(InlineQueryResultType.DOCUMENT, id, api_kwargs=api_kwargs)
        with self._unfrozen():
            self.document_url: str = document_url
            self.title: str = title
            self.mime_type: str = mime_type

            # Optionals
            self.caption: str | None = caption
            self.parse_mode: ODVInput[str] = parse_mode
            self.caption_entities: tuple[MessageEntity, ...] = parse_sequence_arg(caption_entities)
            self.description: str | None = description
            self.reply_markup: InlineKeyboardMarkup | None = reply_markup
            self.input_message_content: InputMessageContent | None = input_message_content
            self.thumbnail_url: str | None = thumbnail_url
            self.thumbnail_width: int | None = thumbnail_width
            self.thumbnail_height: int | None = thumbnail_height
