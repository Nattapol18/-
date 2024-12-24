import re

def find_duplicate_names(names):
    """
    คัดแยกรายชื่อที่ซ้ำและไม่ซ้ำ
    
    Parameters:
    names (list): รายชื่อทั้งหมด
    
    Returns:
    dict: พจนานุกรมที่มีชื่อที่ซ้ำเป็นคีย์ และจำนวนครั้งที่ปรากฏเป็นค่า
    """
    # นับจำนวนครั้งที่แต่ละชื่อปรากฏ
    name_counts = {}
    for name in names:
        # ทำให้ชื่อเป็นตัวพิมพ์เล็กทั้งหมดเพื่อการเปรียบเทียบที่แม่นยำ
        normalized_name = name.strip().lower()
        name_counts[normalized_name] = name_counts.get(normalized_name, 0) + 1
    
    # กรองเอาเฉพาะชื่อที่ซ้ำ (ปรากฏมากกว่าหนึ่งครั้ง)
    duplicates = {name: count for name, count in name_counts.items() if count > 1}
    
    # กรองเอาเฉพาะชื่อที่ไม่ซ้ำ (ปรากฏเพียงครั้งเดียว)
    unique_names = {name for name, count in name_counts.items() if count == 1}
    
    return duplicates, unique_names

def detect_duplicate_honorific(names):
    """
    ตรวจจับคำนำหน้าชื่อที่ซ้ำและไม่ซ้ำ
    
    Parameters:
    names (list): รายชื่อทั้งหมด
    
    Returns:
    dict: พจนานุกรมที่มีคำนำหน้าชื่อที่ซ้ำเป็นคีย์ และจำนวนครั้งที่ปรากฏ
    """
    honorifics = ['น.', 'นาง', 'นางสาว', 'พล.ร.อ.', 'พล.ร.ท.', 'พล.ร.ต.', 'น.อ.', 'น.ท.', 'น.ต.', 
                  'ร.อ.', 'ร.ท.', 'ร.ต.', 'พ.จ.อ.', 'พ.จ.ท.', 'พ.จ.ต.', 'จ.อ.', 'จ.ท.', 'จ.ต.', 'พลฯ']
    
    # ใช้ regex เพื่อหาคำนำหน้าในชื่อ
    honorific_counts = {honorific: 0 for honorific in honorifics}
    
    for name in names:
        for honorific in honorifics:
            if re.search(r'\b' + re.escape(honorific) + r'\b', name.lower()):
                honorific_counts[honorific] += 1
                break  # เจอคำนำหน้าแล้วไม่ต้องตรวจจับต่อ
    
    # กรองเอาเฉพาะคำนำหน้าที่ซ้ำ (ปรากฏมากกว่าหนึ่งครั้ง)
    duplicates_honorific = {honorific: count for honorific, count in honorific_counts.items() if count > 1}
    
    # กรองเอาเฉพาะคำนำหน้าที่ไม่ซ้ำ (ปรากฏเพียงครั้งเดียว)
    unique_honorifics = {honorific for honorific, count in honorific_counts.items() if count == 1}
    
    return duplicates_honorific, unique_honorifics

def main():
    print("โปรแกรมค้นหารายชื่อและคำนำหน้าที่ซ้ำและไม่ซ้ำ")
    print("ใส่ชื่อทีละชื่อ กด Enter หลังใส่ชื่อ พิมพ์ 'done' เมื่อต้องการสิ้นสุดการป้อนชื่อ")
    
    # เก็บรายชื่อ
    names = []
    
    while True:
        name = input("ป้อนชื่อ: ").strip()
        
        # ตรวจสอบการสิ้นสุดการป้อนชื่อ
        if name.lower() == 'done':
            break
        
        # ตรวจสอบว่าป้อนชื่อมาหรือไม่
        if name:
            names.append(name)
    
    # ค้นหารายชื่อที่ซ้ำและไม่ซ้ำ
    duplicate_results, unique_results = find_duplicate_names(names)
    duplicate_honorific_results, unique_honorific_results = detect_duplicate_honorific(names)
    
    # แสดงผลลัพธ์
    print("\n==================== รายชื่อที่ซ้ำกัน ====================")
    if duplicate_results:
        for name, count in duplicate_results.items():
            print(f"  {name}: {count} ครั้ง")
    else:
        print("  ไม่พบชื่อซ้ำ")
    
    print("\n==================== รายชื่อที่ไม่ซ้ำกัน ====================")
    if unique_results:
        for name in unique_results:
            print(f"  {name}")
    else:
        print("  ไม่พบชื่อที่ไม่ซ้ำ")
    
    print("\n==================== คำนำหน้าที่ซ้ำกัน ====================")
    if duplicate_honorific_results:
        for honorific, count in duplicate_honorific_results.items():
            print(f"  {honorific}: {count} ครั้ง")
    else:
        print("  ไม่พบคำนำหน้าซ้ำ")
    
    print("\n==================== คำนำหน้าที่ไม่ซ้ำกัน ====================")
    if unique_honorific_results:
        for honorific in unique_honorific_results:
            print(f"  {honorific}")
    else:
        print("  ไม่พบคำนำหน้าที่ไม่ซ้ำ")

# เรียกใช้ฟังก์ชันหลัก
if __name__ == "__main__":
    main()
