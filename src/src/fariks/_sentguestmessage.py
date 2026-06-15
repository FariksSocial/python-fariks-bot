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
"""This module contains an object that represents a Fariks Sent Guest Message."""

from fariks._fariksobject import FariksObject
from fariks._utils.types import JSONDict


class SentGuestMessage(FariksObject):
    """Describes an inline message sent by a guest bot.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`inline_message_id` are equal.

    .. versionadded:: 22.8

    Args:
        inline_message_id (:obj:`str`): Identifier of the sent inline message.

    Attributes:
        inline_message_id (:obj:`str`): Identifier of the sent inline message.
    """

    __slots__ = ("inline_message_id",)

    def __init__(
        self,
        inline_message_id: str,
        *,
        api_kwargs: JSONDict | None = None,
    ):
        super().__init__(api_kwargs=api_kwargs)
        # Required
        self.inline_message_id: str = inline_message_id

        self._id_attrs = (self.inline_message_id,)

        self._freeze()
