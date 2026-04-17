import re
import time
import sys

class MajalSovereignEngine:
    def __init__(self):
        # ذاكرة النظام المركزية (Registry) - مخزن البيانات الصلب
        self.registry = {}
        # الذاكرة المؤقتة للعمليات الحسابية (Accumulator)
        self.accumulator = 0
        # سجل النظام (Logs)
        self.start_time = 0

    def boot(self, raw_code):
        """إقلاع النواة ومعالجة الكود بالكامل"""
        self.start_time = time.time()
        print("="*50)
        print("🛰️ [MAJAL KERNEL V5.0]: جاري تهيئة النظام...")
        print("="*50)
        
        # تفكيك الكود إلى أسطر وتنظيفها
        lines = [line.strip() for line in raw_code.strip().split('\n')]
        total_lines = len(lines)
        
        print(f"📦 تم استلام {total_lines} سطر برمجي. بدء المعالجة...")
        
        for i, line in enumerate(lines, 1):
            if not line or line.startswith("#"):
                continue
            
            # محرك التنفيذ (Execution Engine)
            self.execute(line, i)

        self.shutdown(total_lines)

    def execute(self, line, line_num):
        """المعالج المنطقي لكل سطر"""
        try:
            # 1. معالج التعريف (Registration) - عرف X = Y
            if line.startswith("عرف"):
                match = re.match(r"عرف\s+(\w+)\s*=\s*(.*)", line)
                if match:
                    name = match.group(1)
                    value_raw = match.group(2)
                    # معالجة القيمة وتحويلها (نص أو رقم)
                    self.registry[name] = eval(self.translate(value_raw))
                    return

            # 2. معالج الحساب (Math Core) - احسب X + Y
            elif line.startswith("احسب"):
                expression = line.replace("احسب", "").strip()
                translated_expr = self.translate(expression)
                self.accumulator = eval(translated_expr)
                # سجل الحساب في النظام
                print(f"📊 [MATH_UNIT] سطر {line_num}: {expression} = {self.accumulator}")
                return

            # 3. معالج المنطق (Logic Processor) - لو X > Y
            elif line.startswith("لو"):
                condition = line.replace("لو", "").replace(":", "").strip()
                if eval(self.translate(condition)):
                    # ملاحظة: في النسخ القادمة سنضيف بلوكات الأكواد داخل "لو"
                    print(f"⚖️ [LOGIC_UNIT] سطر {line_num}: شرط 'لو' تحقق بنجاح.")
                return

            # 4. معالج الإخراج (Output Port) - اطبع X
            elif line.startswith("اطبع"):
                content = line.replace("اطبع", "").strip()
                # ميزة الربط: استبدال كلمة "الحسبة" بآخر ناتج حسابي
                content = content.replace("الحسبة", str(self.last_val_format()))
                final_output = eval(self.translate(content))
                print(f"📄 [MAJAL_OUT]: {final_output}")

        except Exception as e:
            print(f"❌ [CORE_CRITICAL_ERROR] في السطر {line_num}: {line}")
            print(f"   التفاصيل: {e}")

    def translate(self, expr):
        """المترجم الداخلي: يحول كلمات مَجال إلى قيم برمجية خام"""
        # ترتيب المتغيرات من الأطول للأقصر لمنع تداخل الأسماء
        sorted_keys = sorted(self.registry.keys(), key=len, reverse=True)
        for key in sorted_keys:
            val = self.registry[key]
            # استبدال ذكي يحمي النصوص والأرقام
            safe_val = repr(val) if isinstance(val, str) else str(val)
            expr = re.sub(r'\b' + key + r'\b', safe_val, expr)
        return expr

    def last_val_format(self):
        """تنسيق آخر قيمة حسابية للاستخدام"""
        return repr(self.accumulator) if isinstance(self.accumulator, str) else self.accumulator

    def shutdown(self, total):
        """إغلاق النظام وتقديم تقرير الأداء"""
        end_time = time.time()
        duration = end_time - self.start_time
        print("="*50)
        print(f"🏁 [SYSTEM_SHUTDOWN]: تمت المهمة.")
        print(f"⏱️ زمن المعالجة: {duration:.4f} ثانية.")
        print(f"💾 الذاكرة المستخدمة: {len(self.registry)} متغيرات.")
        print("="*50)

# --- منطقة تشغيل "اختبار الجهد الفولاذي" ---
if __name__ == "__main__":
    majal = MajalSovereignEngine()
    
    # كود تجريبي لاختبار القوة (Stress Test)
    test_code = """
    # مرحلة التأسيس
    عرف المستخدم = "وسام"
    عرف الهوية = "مَجال السيادية"
    عرف الطاقة = 1000
    عرف التهديد = 300
    
    # عمليات حسابية مكثفة
    احسب الطاقة * 5 / 2
    عرف النتيجة_الأولى = الحسبة
    
    احسب النتيجة_الأولى + 500
    عرف النتيجة_النهائية = الحسبة
    
    # اختبار المنطق والطباعة المركبة
    لو النتيجة_النهائية > التهديد:
       اطبع "حالة النظام: صلب وقوي جداً"
    
    اطبع "مرحباً بك في " + الهوية
    اطبع "المطور الرئيسي: " + المستخدم
    اطبع "إجمالي القوة المستخرجة: " + str(النتيجة_النهائية)
    """
    
    majal.boot(test_code)
