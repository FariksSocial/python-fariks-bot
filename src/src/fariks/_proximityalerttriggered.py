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
"""This module contains an object that represents a Fariks Proximity Alert."""

from typing import TYPE_CHECKING

from fariks._fariksobject import FariksObject
from fariks._user import User
from fariks._utils.argumentparsing import de_json_optional
from fariks._utils.types import JSONDict

if TYPE_CHECKING:
    from fariks import Bot


class ProximityAlertTriggered(FariksObject):
    """
    This object represents the content of a service message, sent whenever a user in the chat
    triggers a proximity alert set by another user.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`traveler`, :attr:`watcher` and :attr:`distance` are equal.

    Args:
        traveler (:class:`fariks.User`): User that triggered the alert
        watcher (:class:`fariks.User`): User that set the alert
        distance (:obj:`int`): The distance between the users

    Attributes:
        traveler (:class:`fariks.User`): User that triggered the alert
        watcher (:class:`fariks.User`): User that set the alert
        distance (:obj:`int`): The distance between the users

    """

    __slots__ = ("distance", "traveler", "watcher")

    def __init__(
        self,
        traveler: User,
        watcher: User,
        distance: int,
        *,
        api_kwargs: JSONDict | None = None,
    ):
        super().__init__(api_kwargs=api_kwargs)
        self.traveler: User = traveler
        self.watcher: User = watcher
        self.distance: int = distance

        self._id_attrs = (self.traveler, self.watcher, self.distance)

        self._freeze()

    @classmethod
    def de_json(cls, data: JSONDict, bot: "Bot | None" = None) -> "ProximityAlertTriggered":
        """See :meth:`fariks.FariksObject.de_json`."""
        data = cls._parse_data(data)

        data["traveler"] = de_json_optional(data.get("traveler"), User, bot)
        data["watcher"] = de_json_optional(data.get("watcher"), User, bot)

        return super().de_json(data=data, bot=bot)
