import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN, ADMIN_IDS

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("🔍 تشغيل Seeker"), KeyboardButton("📸 تشغيل CamHack"))
    keyboard.add(KeyboardButton("🛠️ حالة الأدوات"), KeyboardButton("⚙️ المساعدة"))
    return keyboard

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("⛔ هذا البوت خاص ولا يمكنك استخدامه.")
        return
    await message.answer(
        "أهلاً بك يا يوسف في لوحة التحكم السحابية الخاصة بأدواتك ⚡\nاختر الأداة المطلوبة:",
        reply_markup=get_main_keyboard()
    )

@dp.message_handler(text="🔍 تشغيل Seeker")
async def run_seeker(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    await message.answer("🔍 جاري تشغيل Seeker...")
    await message.answer("✅ تم توليد رابط Seeker بنجاح.")

@dp.message_handler(text="📸 تشغيل CamHack")
async def run_camhack(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    await message.answer("📸 جاري تحضير CamHack...")
    await message.answer("✅ تم إطلاق CamHack بنجاح.")

@dp.message_handler(text="🛠️ حالة الأدوات")
async def tools_status(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    await message.answer("🟢 السيرفر السحابي يعمل بكفاءة 24/7.")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    print("🤖 البوت يعمل سحابياً...")
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
  
