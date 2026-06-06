import requests

# 1. ضع مفتاح الـ Token المجاني الخاص بك هنا
HF_TOKEN = "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"

# نستخدم نموذج Stable Diffusion XL السريع والقوي والمجاني
API_URL = (
    "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
)
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# 2. نص الوصف ومواصفات الصورة
payload = {
    "inputs": "A beautiful cinematic cyberpunk city at sunset, highly detailed, 4k",
    "parameters": {
        "width": 512,
        "height": 512,
    },
}

print("⏳ جاري الاتصال بسيرفرات Hugging Face وتوليد الصورة مجاناً...")

try:
    # إرسال طلب POST مباشرة للسيرفر
    response = requests.post(API_URL, headers=headers, json=payload)

    # إذا كان السيرفر يستيقظ من النوم (تحميل النموذج لأول مرة)، سيعود برمز 503 ويخبرك بالانتظار ثوانٍ
    if response.status_code == 200:
        # 3. حفظ الصورة المستلمة (تأتي كملف باينري مباشر)
        with open("huggingface_image.png", "wb") as f:
            f.write(response.content)
        print("🎯 نجاح باهر! تم توليد الصورة وحفظها باسم: huggingface_image.png")

    elif response.status_code == 503:
        print(
            "🔄 السيرفر يستعد الآن (يتم تحميل النموذج)، يرجى إعادة تشغيل السكريبت بعد 20 ثانية..."
        )
        print(response.json())
    else:
        print(f"❌ فشل التوليد. رمز الخطأ: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"❌ حدث خطأ غير متوقع: {e}")
