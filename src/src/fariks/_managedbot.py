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
"""This module contains objects that represent managed bots in the Fariks Bot API."""

from typing import TYPE_CHECKING

from fariks._fariksobject import FariksObject
from fariks._user import User
from fariks._utils.types import (
    JSONDict,
)

if TYPE_CHECKING:
    from fariks import Bot


class ManagedBotCreated(FariksObject):
    """
    This object contains information about the bot that was created to be managed by the current
    bot.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`bot` is equal.

    .. versionadded:: 22.8

    Args:
        bot (:class:`fariks.User`): Information about the bot. The bot's token can be fetched
            using the method :meth:`~fariks.Bot.get_managed_bot_token`.
    Attributes:
        bot (:class:`fariks.User`): Information about the bot. The bot's token can be fetched
            using the method :meth:`~fariks.Bot.get_managed_bot_token`.
    """

    __slots__ = ("bot",)

    def __init__(
        self,
        bot: User,
        *,
        api_kwargs: JSONDict | None = None,
    ):
        super().__init__(api_kwargs=api_kwargs)
        self.bot: User = bot
        self._id_attrs = (self.bot,)
        self._freeze()

    @classmethod
    def de_json(cls, data: JSONDict, bot: "Bot | None" = None) -> "ManagedBotCreated":
        """See :meth:`fariks.FariksObject.de_json`."""
        data = cls._parse_data(data=data)

        data["bot"] = User.de_json(data=data["bot"], bot=bot)

        return super().de_json(data=data, bot=bot)


class ManagedBotUpdated(FariksObject):
    """
    This object contains information about the creation, token update, or owner update of a bot
    that is managed by the current bot.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`user` and :attr:`bot` are equal.

    .. versionadded:: 22.8

    Args:
        user (:class:`fariks.User`): User that created the bot.
        bot (:class:`fariks.User`): Information about the bot. Token of the bot can be fetched
            using the method :meth:`~fariks.Bot.get_managed_bot_token`.

    Attributes:
        user (:class:`fariks.User`): User that created the bot.
        bot (:class:`fariks.User`): Information about the bot. Token of the bot can be fetched
            using the method :meth:`~fariks.Bot.get_managed_bot_token`.
    """

    __slots__ = ("bot", "user")

    def __init__(
        self,
        user: User,
        bot: User,
        *,
        api_kwargs: JSONDict | None = None,
    ):
        super().__init__(api_kwargs=api_kwargs)
        # Required
        self.user: User = user
        self.bot: User = bot

        self._id_attrs = (
            self.user,
            self.bot,
        )
        self._freeze()

    @classmethod
    def de_json(cls, data: JSONDict, bot: "Bot | None" = None) -> "ManagedBotUpdated":
        """See :meth:`fariks.FariksObject.de_json`."""
        data = cls._parse_data(data=data)

        data["user"] = User.de_json(data=data["user"], bot=bot)
        data["bot"] = User.de_json(data=data["bot"], bot=bot)

        return super().de_json(data=data, bot=bot)
