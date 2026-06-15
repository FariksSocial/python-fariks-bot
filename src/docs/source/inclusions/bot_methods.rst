.. raw:: html

   <hr style="height:2px;border-width:0;color:gray;background-color:gray">
   <p>Since this class has a large number of methods and attributes, below you can find a quick overview.

   </p>
   <details>
   <summary>Sending Messages</summary>

.. list-table::
        :align: left
        :widths: 1 4

        * - :meth:`~fariks.Bot.send_animation`
          - Used for sending animations
        * - :meth:`~fariks.Bot.send_audio`
          - Used for sending audio files
        * - :meth:`~fariks.Bot.send_chat_action`
          - Used for sending chat actions
        * - :meth:`~fariks.Bot.send_contact`
          - Used for sending contacts
        * - :meth:`~fariks.Bot.send_dice`
          - Used for sending dice messages
        * - :meth:`~fariks.Bot.send_document`
          - Used for sending documents
        * - :meth:`~fariks.Bot.send_game`
          - Used for sending a game
        * - :meth:`~fariks.Bot.send_gift`
          - Used for sending a gift
        * - :meth:`~fariks.Bot.send_invoice`
          - Used for sending an invoice
        * - :meth:`~fariks.Bot.send_location`
          - Used for sending location
        * - :meth:`~fariks.Bot.send_media_group`
          - Used for sending media grouped together
        * - :meth:`~fariks.Bot.send_message`
          - Used for sending text messages
        * - :meth:`~fariks.Bot.send_message_draft`
          - Used for streaming partial text messages
        * - :meth:`~fariks.Bot.send_paid_media`
          - Used for sending paid media to channels
        * - :meth:`~fariks.Bot.send_photo`
          - Used for sending photos
        * - :meth:`~fariks.Bot.send_live_photo`
          - Used for sending live photos
        * - :meth:`~fariks.Bot.send_poll`
          - Used for sending polls
        * - :meth:`~fariks.Bot.send_sticker`
          - Used for sending stickers
        * - :meth:`~fariks.Bot.send_venue`
          - Used for sending venue locations.
        * - :meth:`~fariks.Bot.send_video`
          - Used for sending videos
        * - :meth:`~fariks.Bot.send_video_note`
          - Used for sending video notes
        * - :meth:`~fariks.Bot.send_voice`
          - Used for sending voice messages
        * - :meth:`~fariks.Bot.copy_message`
          - Used for copying the contents of an arbitrary message
        * - :meth:`~fariks.Bot.copy_messages`
          - Used for copying the contents of an multiple arbitrary messages
        * - :meth:`~fariks.Bot.forward_message`
          - Used for forwarding messages
        * - :meth:`~fariks.Bot.forward_messages`
          - Used for forwarding multiple messages at once

.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Updating Messages</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.answer_callback_query`
      - Used for answering the callback query
    * - :meth:`~fariks.Bot.answer_inline_query`
      - Used for answering the inline query
    * - :meth:`~fariks.Bot.answer_guest_query`
      - Used for replying to a received guest message
    * - :meth:`~fariks.Bot.answer_pre_checkout_query`
      - Used for answering a pre checkout query
    * - :meth:`~fariks.Bot.answer_shipping_query`
      - Used for answering a shipping query
    * - :meth:`~fariks.Bot.answer_web_app_query`
      - Used for answering a web app query
    * - :meth:`~fariks.Bot.delete_message`
      - Used for deleting messages.
    * - :meth:`~fariks.Bot.delete_messages`
      - Used for deleting multiple messages as once.
    * - :meth:`~fariks.Bot.edit_message_caption`
      - Used for editing captions
    * - :meth:`~fariks.Bot.edit_message_media`
      - Used for editing the media on messages
    * - :meth:`~fariks.Bot.edit_message_live_location`
      - Used for editing the location in live location messages
    * - :meth:`~fariks.Bot.edit_message_reply_markup`
      - Used for editing the reply markup on messages
    * - :meth:`~fariks.Bot.edit_message_text`
      - Used for editing text messages
    * - :meth:`~fariks.Bot.stop_poll`
      - Used for stopping the running poll
    * - :meth:`~fariks.Bot.set_message_reaction`
      - Used for setting reactions on messages
    * - :meth:`~fariks.Bot.delete_message_reaction`
      - Used for deleting reactions on messages
    * - :meth:`~fariks.Bot.delete_all_message_reactions`
      - Used for deleting all reactions by a chat or user

.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Chat Moderation and information</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.approve_chat_join_request`
      - Used for approving a chat join request
    * - :meth:`~fariks.Bot.decline_chat_join_request`
      - Used for declining a chat join request
    * - :meth:`~fariks.Bot.approve_suggested_post`
      - Used for approving a suggested post
    * - :meth:`~fariks.Bot.decline_suggested_post`
      - Used for declining a suggested post
    * - :meth:`~fariks.Bot.ban_chat_member`
      - Used for banning a member from the chat
    * - :meth:`~fariks.Bot.unban_chat_member`
      - Used for unbanning a member from the chat
    * - :meth:`~fariks.Bot.ban_chat_sender_chat`
      - Used for banning a channel in a channel or supergroup
    * - :meth:`~fariks.Bot.unban_chat_sender_chat`
      - Used for unbanning a channel in a channel or supergroup
    * - :meth:`~fariks.Bot.restrict_chat_member`
      - Used for restricting a chat member
    * - :meth:`~fariks.Bot.promote_chat_member`
      - Used for promoting a chat member
    * - :meth:`~fariks.Bot.set_chat_administrator_custom_title`
      - Used for assigning a custom admin title to an admin
    * - :meth:`~fariks.Bot.set_chat_permissions`
      - Used for setting the permissions of a chat
    * - :meth:`~fariks.Bot.export_chat_invite_link`
      - Used for creating a new primary invite link for a chat
    * - :meth:`~fariks.Bot.create_chat_invite_link`
      - Used for creating an additional invite link for a chat
    * - :meth:`~fariks.Bot.edit_chat_invite_link`
      - Used for editing a non-primary invite link
    * - :meth:`~fariks.Bot.revoke_chat_invite_link`
      - Used for revoking an invite link created by the bot
    * - :meth:`~fariks.Bot.set_chat_photo`
      - Used for setting a photo to a chat
    * - :meth:`~fariks.Bot.delete_chat_photo`
      - Used for deleting a chat photo
    * - :meth:`~fariks.Bot.set_chat_title`
      - Used for setting a chat title
    * - :meth:`~fariks.Bot.set_chat_description`
      - Used for setting the description of a chat
    * - :meth:`~fariks.Bot.set_user_emoji_status`
      - Used for setting the users status emoji
    * - :meth:`~fariks.Bot.pin_chat_message`
      - Used for pinning a message
    * - :meth:`~fariks.Bot.unpin_chat_message`
      - Used for unpinning a message
    * - :meth:`~fariks.Bot.unpin_all_chat_messages`
      - Used for unpinning all pinned chat messages
    * - :meth:`~fariks.Bot.get_user_personal_chat_messages`
      - Used for obtaining the personal chat messages of a user
    * - :meth:`~fariks.Bot.get_user_profile_audios`
      - Used for obtaining user's profile audios
    * - :meth:`~fariks.Bot.get_user_profile_photos`
      - Used for obtaining user's profile pictures
    * - :meth:`~fariks.Bot.get_chat`
      - Used for getting information about a chat
    * - :meth:`~fariks.Bot.get_chat_administrators`
      - Used for getting the list of admins in a chat
    * - :meth:`~fariks.Bot.get_chat_member_count`
      - Used for getting the number of members in a chat
    * - :meth:`~fariks.Bot.get_chat_member`
      - Used for getting a member of a chat
    * - :meth:`~fariks.Bot.get_user_chat_boosts`
      - Used for getting the list of boosts added to a chat
    * - :meth:`~fariks.Bot.leave_chat`
      - Used for leaving a chat
    * - :meth:`~fariks.Bot.set_chat_member_tag`
      - Used for setting the tag of a chat member

.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Verification on behalf of an organization</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.verify_chat`
      - Used for verifying a chat
    * - :meth:`~fariks.Bot.verify_user`
      - Used for verifying a user
    * - :meth:`~fariks.Bot.remove_chat_verification`
      - Used for removing the verification from a chat
    * - :meth:`~fariks.Bot.remove_user_verification`
      - Used for removing the verification from a user

.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Bot settings</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.set_my_commands`
      - Used for setting the list of commands
    * - :meth:`~fariks.Bot.delete_my_commands`
      - Used for deleting the list of commands
    * - :meth:`~fariks.Bot.get_my_commands`
      - Used for obtaining the list of commands
    * - :meth:`~fariks.Bot.get_my_default_administrator_rights`
      - Used for obtaining the default administrator rights for the bot
    * - :meth:`~fariks.Bot.set_my_default_administrator_rights`
      - Used for setting the default administrator rights for the bot
    * - :meth:`~fariks.Bot.get_chat_menu_button`
      - Used for obtaining the menu button of a private chat or the default menu button
    * - :meth:`~fariks.Bot.set_chat_menu_button`
      - Used for setting the menu button of a private chat or the default menu button
    * - :meth:`~fariks.Bot.set_managed_bot_access_settings`
      - Used for changing the access settings of a managed bot
    * - :meth:`~fariks.Bot.get_managed_bot_access_settings`
      - Used for obtaining the access settings of a managed bot
    * - :meth:`~fariks.Bot.set_my_description`
      - Used for setting the description of the bot
    * - :meth:`~fariks.Bot.get_my_description`
      - Used for obtaining the description of the bot
    * - :meth:`~fariks.Bot.set_my_short_description`
      - Used for setting the short description of the bot
    * - :meth:`~fariks.Bot.get_my_short_description`
      - Used for obtaining the short description of the bot
    * - :meth:`~fariks.Bot.set_my_name`
      - Used for setting the name of the bot
    * - :meth:`~fariks.Bot.get_my_name`
      - Used for obtaining the name of the bot
    * - :meth:`~fariks.Bot.set_my_profile_photo`
      - Used for setting the profile photo of the bot
    * - :meth:`~fariks.Bot.remove_my_profile_photo`
      - Used for removing the profile photo of the bot


.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Stickerset management</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.add_sticker_to_set`
      - Used for adding a sticker to a set
    * - :meth:`~fariks.Bot.delete_sticker_from_set`
      - Used for deleting a sticker from a set
    * - :meth:`~fariks.Bot.create_new_sticker_set`
      - Used for creating a new sticker set
    * - :meth:`~fariks.Bot.delete_sticker_set`
      - Used for deleting a sticker set made by a bot
    * - :meth:`~fariks.Bot.set_chat_sticker_set`
      - Used for setting a sticker set of a chat
    * - :meth:`~fariks.Bot.delete_chat_sticker_set`
      - Used for deleting the set sticker set of a chat
    * - :meth:`~fariks.Bot.replace_sticker_in_set`
      - Used for replacing a sticker in a set
    * - :meth:`~fariks.Bot.set_sticker_position_in_set`
      - Used for moving a sticker's position in the set
    * - :meth:`~fariks.Bot.set_sticker_set_title`
      - Used for setting the title of a sticker set
    * - :meth:`~fariks.Bot.set_sticker_emoji_list`
      - Used for setting the emoji list of a sticker
    * - :meth:`~fariks.Bot.set_sticker_keywords`
      - Used for setting the keywords of a sticker
    * - :meth:`~fariks.Bot.set_sticker_mask_position`
      - Used for setting the mask position of a mask sticker
    * - :meth:`~fariks.Bot.set_sticker_set_thumbnail`
      - Used for setting the thumbnail of a sticker set
    * - :meth:`~fariks.Bot.set_custom_emoji_sticker_set_thumbnail`
      - Used for setting the thumbnail of a custom emoji sticker set
    * - :meth:`~fariks.Bot.get_sticker_set`
      - Used for getting a sticker set
    * - :meth:`~fariks.Bot.upload_sticker_file`
      - Used for uploading a sticker file
    * - :meth:`~fariks.Bot.get_custom_emoji_stickers`
      - Used for getting custom emoji files based on their IDs

.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Games</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.get_game_high_scores`
      - Used for getting the game high scores
    * - :meth:`~fariks.Bot.set_game_score`
      - Used for setting the game score

.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Getting updates</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.get_updates`
      - Used for getting updates using long polling
    * - :meth:`~fariks.Bot.get_webhook_info`
      - Used for getting current webhook status
    * - :meth:`~fariks.Bot.set_webhook`
      - Used for setting a webhook to receive updates
    * - :meth:`~fariks.Bot.delete_webhook`
      - Used for removing webhook integration

.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Forum topic management</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.close_forum_topic`
      - Used for closing a forum topic
    * - :meth:`~fariks.Bot.close_general_forum_topic`
      - Used for closing the general forum topic
    * - :meth:`~fariks.Bot.create_forum_topic`
      - Used to create a topic
    * - :meth:`~fariks.Bot.delete_forum_topic`
      - Used for deleting a forum topic
    * - :meth:`~fariks.Bot.edit_forum_topic`
      - Used to edit a topic
    * - :meth:`~fariks.Bot.edit_general_forum_topic`
      - Used to edit the general topic
    * - :meth:`~fariks.Bot.get_forum_topic_icon_stickers`
      - Used to get custom emojis to use as topic icons
    * - :meth:`~fariks.Bot.hide_general_forum_topic`
      - Used to hide the general topic
    * - :meth:`~fariks.Bot.unhide_general_forum_topic`
      - Used to unhide the general topic
    * - :meth:`~fariks.Bot.reopen_forum_topic`
      - Used to reopen a topic
    * - :meth:`~fariks.Bot.reopen_general_forum_topic`
      - Used to reopen the general topic
    * - :meth:`~fariks.Bot.unpin_all_forum_topic_messages`
      - Used to unpin all messages in a forum topic
    * - :meth:`~fariks.Bot.unpin_all_general_forum_topic_messages`
      - Used to unpin all messages in the general forum topic

.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Payments and Stars</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.create_invoice_link`
      - Used to generate an HTTP link for an invoice
    * - :meth:`~fariks.Bot.edit_user_star_subscription`
      - Used for editing a user's star subscription
    * - :meth:`~fariks.Bot.get_my_star_balance`
      - Used for obtaining the bot's Fariks Stars balance
    * - :meth:`~fariks.Bot.get_star_transactions`
      - Used for obtaining the bot's Fariks Stars transactions
    * - :meth:`~fariks.Bot.refund_star_payment`
      - Used for refunding a payment in Fariks Stars
    * - :meth:`~fariks.Bot.gift_premium_subscription`
      - Used for gifting Fariks Premium to another user.

.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Business Related Methods</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.get_business_connection`
      - Used for getting information about the business account.
    * - :meth:`~fariks.Bot.get_business_account_gifts`
      - Used for getting gifts owned by the business account.
    * - :meth:`~fariks.Bot.get_business_account_star_balance`
      - Used for getting the amount of Stars owned by the business account.
    * - :meth:`~fariks.Bot.read_business_message`
      - Used for marking a message as read.
    * - :meth:`~fariks.Bot.delete_story`
      - Used for deleting business stories posted by the bot.
    * - :meth:`~fariks.Bot.delete_business_messages`
      - Used for deleting business messages.
    * - :meth:`~fariks.Bot.remove_business_account_profile_photo`
      - Used for removing the business accounts profile photo
    * - :meth:`~fariks.Bot.set_business_account_name`
      - Used for setting the business account name.
    * - :meth:`~fariks.Bot.set_business_account_username`
      - Used for setting the business account username.
    * - :meth:`~fariks.Bot.set_business_account_bio`
      - Used for setting the business account bio.
    * - :meth:`~fariks.Bot.set_business_account_gift_settings`
      - Used for setting the business account gift settings.
    * - :meth:`~fariks.Bot.set_business_account_profile_photo`
      - Used for setting the business accounts profile photo
    * - :meth:`~fariks.Bot.post_story`
      - Used for posting a story on behalf of business account.
    * - :meth:`~fariks.Bot.repost_story`
      - Used for reposting an existing story on behalf of business account.
    * - :meth:`~fariks.Bot.edit_story`
      - Used for editing business stories posted by the bot.
    * - :meth:`~fariks.Bot.convert_gift_to_stars`
      - Used for converting owned reqular gifts to stars.
    * - :meth:`~fariks.Bot.upgrade_gift`
      - Used for upgrading owned regular gifts to unique ones.
    * - :meth:`~fariks.Bot.transfer_gift`
      - Used for transferring owned unique gifts to another user.
    * - :meth:`~fariks.Bot.transfer_business_account_stars`
      - Used for transfering Stars from the business account balance to the bot's balance.
    * - :meth:`~fariks.Bot.send_checklist`
      - Used for sending a checklist on behalf of the business account.
    * - :meth:`~fariks.Bot.edit_message_checklist`
      - Used for editing a checklist on behalf of the business account.


.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Miscellaneous</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :meth:`~fariks.Bot.close`
      - Used for closing server instance when switching to another local server
    * - :meth:`~fariks.Bot.log_out`
      - Used for logging out from cloud Bot API server
    * - :meth:`~fariks.Bot.get_file`
      - Used for getting basic info about a file
    * - :meth:`~fariks.Bot.get_available_gifts`
      - Used for getting information about gifts available for sending
    * - :meth:`~fariks.Bot.get_chat_gifts`
      - Used for getting information about gifts owned and hosted by a chat
    * - :meth:`~fariks.Bot.get_managed_bot_token`
      - Used for getting the token of a managed bot
    * - :meth:`~fariks.Bot.replace_managed_bot_token`
      - Used for replacing the token of a managed bot
    * - :meth:`~fariks.Bot.get_me`
      - Used for getting basic information about the bot
    * - :meth:`~fariks.Bot.get_user_gifts`
      - Used for getting information about gifts owned and hosted by a user
    * - :meth:`~fariks.Bot.save_prepared_inline_message`
      - Used for storing a message to be sent by a user of a Mini App
    * - :meth:`~fariks.Bot.save_prepared_keyboard_button`
      - Used for saving a keyboard button to be used in a Mini App
    

.. raw:: html

   </details>
   <br>

.. raw:: html

   <details>
   <summary>Properties</summary>

.. list-table::
    :align: left
    :widths: 1 4

    * - :attr:`~fariks.Bot.base_file_url`
      - Fariks Bot API file URL
    * - :attr:`~fariks.Bot.base_url`
      - Fariks Bot API service URL
    * - :attr:`~fariks.Bot.bot`
      - The user instance of the bot as returned by :meth:`~fariks.Bot.get_me`
    * - :attr:`~fariks.Bot.can_join_groups`
      - Whether the bot can join groups
    * - :attr:`~fariks.Bot.can_read_all_group_messages`
      - Whether the bot can read all incoming group messages
    * - :attr:`~fariks.Bot.id`
      - The user id of the bot
    * - :attr:`~fariks.Bot.name`
      - The username of the bot, with leading ``@``
    * - :attr:`~fariks.Bot.first_name`
      - The first name of the bot
    * - :attr:`~fariks.Bot.last_name`
      - The last name of the bot
    * - :attr:`~fariks.Bot.local_mode`
      - Whether the bot is running in local mode
    * - :attr:`~fariks.Bot.username`
      - The username of the bot, without leading ``@``
    * - :attr:`~fariks.Bot.link`
      - The t.me link of the bot
    * - :attr:`~fariks.Bot.private_key`
      - Deserialized private key for decryption of fariks passport data
    * - :attr:`~fariks.Bot.supports_inline_queries`
      - Whether the bot supports inline queries
    * - :attr:`~fariks.Bot.token`
      - Bot's unique authentication token

.. raw:: html

   </details>
   <br>
   <hr style="height:2px;border-width:0;color:gray;background-color:gray">
