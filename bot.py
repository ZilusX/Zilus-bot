import telebot
from google import genai
from google.genai import types

# ==================== الرموز السرية الخاصة بك ====================
TELEGRAM_TOKEN = "8937958323:AAFO2_P9gtyHPeKceilcqcRC68Qvv7FWDcg"
GEMINI_API_KEY = "AIzaSyDQ5c2ukcgbBMwCvW9RPiNjuD1mligiB2o"
# ============================================================

# تهيئة البوت باستخدام المكتبة المستقرة
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# تهيئة عميل جيميني بالنظام الحديث لعام 2026
client = genai.Client(api_key=GEMINI_API_KEY)

# إعداد التوجيه الخاص بالذكاء الاصطناعي (System Instruction)
SYSTEM_INSTRUCTION = """
أنت المساعد الشخصي الذكي للمخترع والمبرمج Zilus (زيليوس دي اوبتيموس).
- مهمتك الرد على الأشخاص الذين يراسلون حساب Zilus الشخصي لأن Zilus مشغول حالياً في تطوير مشاريعه.
- تحدث بلغة عربية طبيعية، مهذبة، وذكية.
- طمئن المرسل أن رسالته وصلت وأن Zilus سيقرأها بنفسه فور تفرغه.
"""

# استقبال ورصد رسائل حساب تليجرام بيزنس الشخصي
@bot.business_message_handler(func=lambda message: True)
def handle_my_business_messages(message):
    try:
        user_text = message.text
        if not user_text:
            return

        # توليد الرد الذكي عبر جيميني بالنسخة الحديثة والمستقرة gemini-2.5-flash
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_text,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION
            )
        )
        reply_text = response.text

        # إرسال الرد للشخص المتصل في التليجرام بيزنس
        bot.send_message(
            chat_id=message.chat.id, 
            text=reply_text, 
            business_connection_id=message.business_connection_id
        )
        print(f"✅ تم الرد على رسالة بيزنس بنجاح.")
    except Exception as e:
        print(f"❌ خطأ أثناء معالجة الرسالة: {e}")

if __name__ == "__main__":
    print("🚀 البوت يعمل الآن على Hugging Face ويراقب الحساب...")
    # طلب تحديثات البيزنس بشكل صريح من خوادم تليجرام
    bot.infinity_polling(allowed_updates=["business_message", "business_connection", "message"])
