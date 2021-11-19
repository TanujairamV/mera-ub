# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}lock <msgs/media/sticker/gif/games/inline/polls/invites/pin/changeinfo>`
    Lock the Used Setting in Used Group.

• `{i}unlock <msgs/media/sticker/gif/games/inline/polls/invites/pin/changeinfo>`
    UNLOCK the Used Setting in Used Group.

"""
from pyUltroid.functions.admins import lock_unlock
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest

from . import eor, ultroid_cmd


@ultroid_cmd(
    pattern="lock ?(.*)",
    groups_only=True,
    admins_only=True,
    manager=True,
)
async def lockho(e):
    mat = e.pattern_match.group(1)
    if not mat:
        return await eor(e, "`Give some Proper Input..`", time=5)
    ml = lock_unlock(mat)
    if not ml:
        return await eor(e, "`Incorrect Input`", time=5)
    await e.client(EditChatDefaultBannedRightsRequest(e.chat_id, ml))
    await eor(e, f"Locked - `{mat}` ! ")


@ultroid_cmd(
    pattern="unlock ?(.*)",
    groups_only=True,
    admins_only=True,
    manager=True,
)
async def unlckho(e):
    mat = e.pattern_match.group(1)
    if not mat:
        return await eor(e, "`Give some Proper Input..`", time=5)
    ml = lock_unlock(mat, lock=False)
    if not ml:
        return await eor(e, "`Incorrect Input`", time=5)
    await e.client(EditChatDefaultBannedRightsRequest(e.chat_id, ml))
    await eor(e, f"Unlocked - `{mat}` ! ")
