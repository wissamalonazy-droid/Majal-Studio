# --- محرك لغة مَجال العالمي (Majal Universal Engine) ---

memory = {}

def majal_interpreter(code_text):
    lines = code_text.strip().split('\n')
    results = []

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"): continue
        
        # دعم العربي والإنجليزي (عرف / define)
        if line.startswith("عرف") or line.lower().startswith("define"):
            content = line.replace("عرف", "").replace("define", "").replace(" ", "")
            name, val = content.split("=")
            memory[name] = int(val)
            results.append(f"✔️ [Majal]: Registered '{name}' = {val}")

        # دعم العربي والإنجليزي (اطبع / print)
        elif line.startswith("اطبع") or line.lower().startswith("print"):
            var_name = line.replace("اطبع", "").replace("print", "").strip()
            val = memory.get(var_name, "Error: Not Found!")
            results.append(f"📄 [Output]: {val}")

        # دعم الحساب (احسب / calculate)
        elif line.startswith("احسب") or line.lower().startswith("calculate"):
            expr = line.replace("احسب", "").replace("calculate", "").strip()
            # تبسيط العمليات الحسابية
            for op in ['+', '-', '*', '/']:
                if op in expr:
                    parts = expr.split(op)
                    v1 = memory.get(parts[0].strip(), int(parts[0].strip()) if parts[0].strip().isdigit() else 0)
                    v2 = int(parts[1].strip())
                    res = eval(f"{v1} {op} {v2}")
                    results.append(f"📊 [Calc]: {res}")
                    break
    return "\n".join(results)

# تجربة المحرك باللغتين
test_code = """
عرف السعر = 1000
define discount = 200
احسب السعر - 200
print السعر
"""
print(majal_interpreter(test_code))
