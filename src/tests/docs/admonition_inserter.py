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

"""
This module is intentionally named without "test_" prefix.
These tests are supposed to be run on GitHub when building docs.
The tests require Python 3.10+ (just like AdmonitionInserter being tested),
so they cannot be included in the main suite while older versions of Python are supported.
"""

import collections.abc

import pytest

import fariks.ext
from docs.auxil.admonition_inserter import AdmonitionInserter


@pytest.fixture(scope="session")
def admonition_inserter():
    return AdmonitionInserter()


class TestAdmonitionInserter:
    """This is a minimal-effort test to ensure that the `AdmonitionInserter`
    used for automatically inserting references in the docs works as expected.

    It does not aim to cover all links in the documentation, but rather checks that several special
    cases (which where discovered during the implementation of `AdmonitionInserter`) are handled
    correctly.
    """

    def test_admonitions_dict(self, admonition_inserter):
        # there are keys for every type of admonition
        assert len(admonition_inserter.admonitions) == len(
            admonition_inserter.ALL_ADMONITION_TYPES
        )

        # for each type of admonitions, there is at least one entry
        # ({class/method: admonition text})
        for admonition_type in admonition_inserter.ALL_ADMONITION_TYPES:
            assert admonition_type in admonition_inserter.admonitions
            assert len(admonition_inserter.admonitions[admonition_type].keys()) > 0

        # checking class admonitions
        for admonition_type in admonition_inserter.CLASS_ADMONITION_TYPES:
            # keys are fariks classes
            for cls in admonition_inserter.admonitions[admonition_type]:
                # Test classes crop up in AppBuilder, they can't come from code being tested.
                if "tests." in str(cls):
                    continue

                assert isinstance(cls, type)
                assert str(cls).startswith("<class 'fariks."), (
                    rf"Class {cls} does not belong to Fariks classes. Admonition:\n"
                    rf"{admonition_inserter.admonitions[admonition_type][cls]}"
                )

        # checking Bot method admonitions
        for admonition_type in admonition_inserter.METHOD_ADMONITION_TYPES:
            for method in admonition_inserter.admonitions[admonition_type]:
                assert isinstance(method, collections.abc.Callable)
                assert str(method).startswith("<function Bot."), (
                    f"Method {method} does not belong to methods that should get admonitions."
                    "Admonition:\n"
                    f"{admonition_inserter.admonitions[admonition_type][method]}"
                )

    @pytest.mark.parametrize(
        ("admonition_type", "cls", "link"),
        [
            (
                "available_in",
                fariks.ChatMember,
                ":attr:`fariks.ChatMemberUpdated.new_chat_member`",
            ),
            (
                "available_in",
                fariks.ChatMemberAdministrator,
                ":attr:`fariks.ChatMemberUpdated.new_chat_member`",
            ),
            (
                "available_in",
                fariks.Sticker,
                ":attr:`fariks.StickerSet.stickers`",  # tuple[fariks.Sticker]
            ),
            (
                "available_in",
                fariks.ResidentialAddress,  # mentioned on the second line of docstring of .data
                ":attr:`fariks.EncryptedPassportElement.data`",
            ),
            (
                "available_in",
                fariks.ext.JobQueue,
                ":attr:`fariks.ext.CallbackContext.job_queue`",
            ),
            (
                "available_in",
                fariks.ext.Application,
                ":attr:`fariks.ext.CallbackContext.application`",
            ),
            (
                "available_in",
                fariks.Bot,
                ":attr:`fariks.ext.CallbackContext.bot`",
            ),
            (
                "available_in",
                fariks.Bot,
                ":attr:`fariks.ext.Application.bot`",
            ),
            (
                "returned_in",
                fariks.StickerSet,
                ":meth:`fariks.Bot.get_sticker_set`",
            ),
            (
                "returned_in",
                fariks.ChatMember,
                ":meth:`fariks.Bot.get_chat_member`",
            ),
            (
                "returned_in",
                fariks.GameHighScore,
                ":meth:`fariks.Bot.get_game_high_scores`",
            ),
            (
                "returned_in",
                fariks.ChatMemberOwner,
                ":meth:`fariks.Bot.get_chat_member`",  # subclass
            ),
            (
                "returned_in",
                fariks.Message,
                ":meth:`fariks.Bot.edit_message_live_location`",  # Union[Message, bool]
            ),
            (
                "returned_in",
                fariks.ext.Application,
                ":meth:`fariks.ext.ApplicationBuilder.build`",  # <class 'types.GenericAlias'>
            ),
            (
                "shortcuts",
                fariks.Bot.edit_message_caption,
                # this method in CallbackQuery contains two return statements,
                # one of which is with Bot
                ":meth:`fariks.CallbackQuery.edit_message_caption`",
            ),
            (
                "shortcuts",
                fariks.Bot.ban_chat_member,
                # ban_member is defined on the private parent class _ChatBase
                ":meth:`fariks.Chat.ban_member`",
            ),
            (
                "shortcuts",
                fariks.Bot.ban_chat_member,
                # ban_member is defined on the private parent class _ChatBase
                ":meth:`fariks.ChatFullInfo.ban_member`",
            ),
            (
                "use_in",
                fariks.InlineQueryResult,
                ":meth:`fariks.Bot.answer_web_app_query`",  # ForwardRef
            ),
            (
                "use_in",
                fariks.InputMediaPhoto,
                ":meth:`fariks.Bot.send_media_group`",  # Sequence[Union[...]]
            ),
            (
                "use_in",
                fariks.InlineKeyboardMarkup,
                ":meth:`fariks.Bot.send_message`",  # optional
            ),
            (
                "use_in",
                fariks.Sticker,
                ":meth:`fariks.Bot.get_file`",  # .file_id with lots of piped types
            ),
            (
                "use_in",
                fariks.ext.BasePersistence,
                ":meth:`fariks.ext.ApplicationBuilder.persistence`",
            ),
            ("use_in", fariks.ext.Defaults, ":meth:`fariks.ext.ApplicationBuilder.defaults`"),
            (
                "use_in",
                fariks.ext.JobQueue,
                ":meth:`fariks.ext.ApplicationBuilder.job_queue`",  # TypeVar
            ),
            (
                "use_in",
                fariks.ext.PicklePersistence,  # subclass
                ":meth:`fariks.ext.ApplicationBuilder.persistence`",
            ),
        ],
    )
    def test_check_presence(self, admonition_inserter, admonition_type, cls, link):
        """Checks if a given link is present in the admonition of a given type for a given
        class.
        """
        admonitions = admonition_inserter.admonitions

        assert cls in admonitions[admonition_type]

        # exactly one of the lines in the admonition for this class must consist of the link
        # (this is a stricter check than just checking if the entire admonition contains the link)
        lines_with_link = [
            line
            for line in admonitions[admonition_type][cls].splitlines()
            # remove whitespaces and occasional bullet list marker
            if line.strip().removeprefix("* ") == link
        ]
        assert lines_with_link, (
            f"Class {cls}, does not have link {link} in a {admonition_type} admonition:\n"
            f"{admonitions[admonition_type][cls]}"
        )
        assert len(lines_with_link) == 1, (
            f"Class {cls}, must contain only one link {link} in a {admonition_type} admonition:\n"
            f"{admonitions[admonition_type][cls]}"
        )

    @pytest.mark.parametrize(
        ("admonition_type", "cls", "link"),
        [
            (
                "returned_in",
                fariks.ext.CallbackContext,
                # -> Application[BT, CCT, UD, CD, BD, JQ].
                # The type vars are not really part of the return value, so we don't expect them
                ":meth:`fariks.ext.ApplicationBuilder.build`",
            ),
            (
                "returned_in",
                fariks.Bot,
                # -> Application[BT, CCT, UD, CD, BD, JQ].
                # The type vars are not really part of the return value, so we don't expect them
                ":meth:`fariks.ext.ApplicationBuilder.bot`",
            ),
        ],
    )
    def test_check_absence(self, admonition_inserter, admonition_type, cls, link):
        """Checks if a given link is **absent** in the admonition of a given type for a given
        class.

        If a given class has no admonition of this type at all, the test will also pass.
        """
        admonitions = admonition_inserter.admonitions

        assert not (
            cls in admonitions[admonition_type]
            and [
                line
                for line in admonitions[admonition_type][cls].splitlines()
                # remove whitespaces and occasional bullet list marker
                if line.strip().removeprefix("* ") == link
            ]
        ), (
            f"Class {cls} is not supposed to have link {link} in a {admonition_type} admonition:\n"
            f"{admonitions[admonition_type][cls]}"
        )
