from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from ROYEDITX import ROYX
from ROYEDITX.database import vick


@ROYX.on_callback_query()
async def cb_handler(_, query: CallbackQuery):
    if query.data == "addchat":
        user_id = query.from_user.id
        user_status = (await query.message.chat.get_member(user_id)).status
        if user_status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
            return await query.answer(
                "❖ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴇᴠᴇɴ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴏɴ'ᴛ ᴛʀʏ ᴛʜɪs ᴇxᴘʟᴏsɪᴠᴇ sʜɪᴛ !",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                await query.edit_message_text(f"❖ ᴄʜᴀᴛ-ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.")
            if is_vick:
                vick.delete_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(
                    f"❖ ɪᴅ ᴄʜᴀᴛ-ʙᴏᴛ ᴇɴᴀʙʟᴇᴅ ʙʏ ➥ {query.from_user.mention}."
                )
    if query.data == "rmchat":
        user_id = query.from_user.id
        user_status = (await query.message.chat.get_member(user_id)).status
        if user_status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
            await query.answer(
                "❖ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴇᴠᴇɴ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴏɴ'ᴛ ᴛʀʏ ᴛʜɪs ᴇxᴘʟᴏsɪᴠᴇ sʜɪᴛ !",
                show_alert=True,
            )
            return
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                vick.insert_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(
                    f"❖ ɪᴅ ᴄʜᴀᴛ-ʙᴏᴛ ᴅɪsᴀʙʟᴇᴅ ʙʏ ➥ {query.from_user.mention}."
                )
            if is_vick:
                await query.edit_message_text("❖ ɪᴅ ᴄʜᴀᴛ-ʙᴏᴛ ᴀʟʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.")
