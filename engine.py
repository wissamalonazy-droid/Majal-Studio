import re

class MajalEngine:
    def __init__(self):
        # ذاكرة النظام الفولاذية
        self.variables = {}
        self.last_calc = 0

    def run(self, code):
        lines = code.strip().split('\n')
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            
            try:
                self.execute(line)
            except Exception as e:
                print(f"❌ خطأ في محرك مَجال (سطر {line_num}): {e}")

    def execute(self, line):
        # 1. نظام التعريف (Variable Assignment)
        if "عرف" in line:
            # استخدام Regex لضمان دقة استخراج الأسماء والقيم
            match = re.match(r"عرف\s+(\w+)\s*=\s*(.*)", line)
            if match:
                var_name = match.group(1)
                var_value = eval(self.prepare_expression(match.group(2)))
                self.variables[var_name] = var_value
                return

        # 2. نظام المنطق (Conditional Logic)
        if line.startswith("لو"):
            condition = line.replace("لو", "").replace(":", "").strip()
            if eval(self.prepare_expression(condition)):
                # هنا يمكن تطوير النظام ليدعم البلوكات البرمجية لاحقاً
                pass

        # 3. نظام الحساب (Math Core)
        if line.startswith("احسب"):
            expr = line.replace("احسب", "").strip()
            self.last_calc = eval(self.prepare_expression(expr))
            print(f"📊 [CORE_MATH]: {self.last_calc}")
            return

        # 4. نظام الطباعة (Output Interface)
        if line.startswith("اطبع"):
            content = line.replace("اطبع", "").strip()
            # دعم كلمة "الحسبة" للربط مع المحرك الحسابي
            content = content.replace("الحسبة", str(self.last_calc))
            result = eval(self.prepare_expression(content))
            print(f"📄 [MAJAL_OUT]: {result}")

    def prepare_expression(self, expr):
        """تجهيز التعبير البرمجي باستبدال متغيرات مَجال بقيمها الحقيقية"""
        for var, val in self.variables.items():
            # استبدال دقيق لضمان عدم تداخل الأسماء
            expr = re.sub(r'\b' + var + r'\b', str(repr(val) if isinstance(val, str) else val), expr)
        return expr

# --- تشغيل تجريبي للنواة الصلبة ---
engine = MajalEngine()
majal_code = """
# تأسيس قوي لمحرك مَجال
عرف المستخدم = "وسام"
عرف رصيد_البداية = 5000
عرف المشتريات = 1250

احسب رصيد_البداية - المشتريات
اطبع "مرحباً يا " + المستخدم
اطبع "رصيدك المتبقي حالياً هو: " + str(الحسبة)
"""

engine.run(majal_code)
