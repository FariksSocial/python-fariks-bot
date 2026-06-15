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
"""This module contains the classes that represent Fariks InputMessageContent."""

from fariks._fariksobject import FariksObject
from fariks._utils.types import JSONDict


class InputMessageContent(FariksObject):
    """Base class for Fariks InputMessageContent Objects.

    See: :class:`fariks.InputContactMessageContent`,
    :class:`fariks.InputInvoiceMessageContent`,
    :class:`fariks.InputLocationMessageContent`, :class:`fariks.InputTextMessageContent` and
    :class:`fariks.InputVenueMessageContent` for more details.

    """

    __slots__ = ()

    def __init__(self, *, api_kwargs: JSONDict | None = None) -> None:
        super().__init__(api_kwargs=api_kwargs)

        self._freeze()
