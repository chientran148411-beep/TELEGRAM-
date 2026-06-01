# main.py

from telethon import TelegramClient, events

API_ID = 31284153          # Thay bằng API ID của bạn
API_HASH = "f14dca981db461bbee4e156efbc678a9" # Thay bằng API HASH của bạn

client = TelegramClient("session", API_ID, API_HASH)

welcomed_users = set()

SUPPORT_LINK = "https://t.me/Kenios_mc_bot"

PAYMENT_MESSAGE = """
🏦 THÔNG TIN THANH TOÁN

TPBANK
STK: 44413438888
Chủ tài khoản: TRẦN MINH CHIẾN

📸 QR:
https://cdn.phototourl.com/free/2026-06-01-ac99377f-3989-42ea-aca3-eca3c1735070.jpg

✅ Sau khi thanh toán vui lòng gửi bill hoặc ảnh giao dịch để xác nhận.
"""

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if not event.is_private:
        return

    sender = await event.get_sender()
    name = sender.first_name or "bạn"

    text = (event.raw_text or "").lower()

    # Chào khách lần đầu
    if sender.id not in welcomed_users:
        welcomed_users.add(sender.id)

        await event.reply(
            f"👋 Xin chào {name}!\n\n"
            "Cảm ơn bạn đã liên hệ.\n"
            "Mình sẽ hỗ trợ tiếp nhận thông tin trong thời gian sớm nhất."
        )

    # Từ khóa tư vấn
    product_keywords = [
        "mua",
        "giá",
        "gia",
        "sản phẩm",
        "san pham",
        "dịch vụ",
        "dich vu"
    ]

    if any(k in text for k in product_keywords):
        await event.reply(
            f"👋 Xin chào {name}!\n\n"
            f"Vui lòng xem thông tin tại:\n{https://t.me/Kenios_mc_bot}"
        )
        return

    # Thanh toán
    payment_keywords = [
        "stk",
        "số tài khoản",
        "so tai khoan",
        "qr",
        "thanh toán",
        "thanh toan",
        "chuyển khoản",
        "chuyen khoan",
        "bank"
    ]

    if any(k in text for k in payment_keywords):
        await event.reply(PAYMENT_MESSAGE)
        return

    # Đã thanh toán
    bill_keywords = [
        "đã chuyển",
        "da chuyen",
        "đã thanh toán",
        "da thanh toan",
        "done",
        "xong"
    ]

    if any(k in text for k in bill_keywords):
        await event.reply(
            f"👋 Cảm ơn {name}!\n\n"
            "📸 Vui lòng gửi bill hoặc ảnh giao dịch thành công để xác nhận."
        )
        return

client.start()
print("Userbot đang chạy...")
client.run_until_disconnected()
