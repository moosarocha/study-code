def load_knowledge(filename='knowledge.txt'):
    knowledge = []
  
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            if "=>" not in line:
                continue

            key_part, value = line.split("=>", 1)
            value = value.strip()

            keys = frozenset([key.strip() for key in key_part.split(",") if key.strip()])

    return knowledge


def krr(question):

    rules = load_knowledge()

    for rule, fact in rules.items():
        if all(question in rule for question in question):
            return fact

    return "ไม่สมารภวินิจฉัยได้"

if __name__ == "__main__":
    n = int(input("Enternumber of your case: "))

    rule = []
    for i in range(n):
        rule.append(input())

    fact = krr(rule)
ยังไม่เสร็จสมบูรณ์

# Rule System1
# facts = [
#     "เครื่องรีสตาร์ตเองเป็นระยะ",
#     "อุณหภูมิ CPU สูงกว่า 90 องศาเซลเซียส"
# ]
# # Rule 1
# if ("เครื่องรีสตาร์ตเองเป็นระยะ" in facts and
#     "อุณหภูมิ CPU สูงกว่า 90 องศาเซลเซียส" in facts):
#     facts.append("สงสัยว่าระบบระบายความร้อนของ CPU มีปัญหา")
#     print("สรุป: สงสัยว่าระบบระบายความร้อนของ CPU มีปัญหา")

# # Rule 2
# if "สงสัยว่าระบบระบายความร้อนของ CPU มีปัญหา" in facts:
#     print("คำแนะนำ: ทำความสะอาดพัดลมและเปลี่ยนซิลิโคนระบายความร้อน")


# # Rule System2

# facts = [
#     "เครื่องคอมพิวเตอร์เปิดไม่ติด",
#     "พัดลม Power Supply ไม่หมุน"
# ]
# # Rule 1
# if ("เครื่องคอมพิวเตอร์เปิดไม่ติด" in facts and
#     "พัดลม Power Supply ไม่หมุน" in facts):
#     facts.append("สงสัยว่า Power Supply ชำรุด")
#     print("สรุป: สงสัยว่า Power Supply ชำรุด")
# # Rule 2
# if "สงสัยว่า Power Supply ชำรุด" in facts:
#     print("คำแนะนำ: แนะนำให้เปลี่ยน Power Supply")
