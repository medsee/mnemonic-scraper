# Author: medsee
# Description: Lokal test uchun mnemonic scraper

import re
import os

def create_test_file():
    """Test fayli yaratadi"""
    test_content = """
Test mnemonic phrases for wallet recovery:
abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about
zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo wrong
army van defense carry jealous true garbage claim echo media make crunch
Some random text here
another test phrase with twelve words here for testing purposes only
"""
    
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write(test_content)
    print("✅ test.txt fayli yaratildi")

def find_mnemonics_in_file(file_path):
    """Fayldan mnemonic topadi"""
    # 12-24 ta so'zli pattern (ingliz so'zlari)
    mnemonic_pattern = r'\b(?:[a-z]+\s+){11,23}[a-z]+\b'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            
        matches = re.findall(mnemonic_pattern, content)
        
        if matches:
            print(f"🟢 {file_path} faylida mnemonic topildi!")
            for i, match in enumerate(matches, 1):
                words = match.strip().split()
                if 12 <= len(words) <= 24:  # Faqat to'g'ri uzunlikdagi
                    print(f"  {i}) [{len(words)} so'z] → {' '.join(words)}")
        else:
            print(f"🔴 {file_path} faylida mnemonic topilmadi.")
            
    except Exception as e:
        print(f"❌ Xatolik: {e}")

# Asosiy kod
if __name__ == "__main__":
    print("🚀 Lokal mnemonic scraper ishga tushdi")
    
    # Agar test.txt yo'q bo'lsa, yaratadi
    if not os.path.exists('test.txt'):
        create_test_file()
    
    # Turli fayllarni tekshiradi
    files_to_check = ['test.txt', 'example.txt', 'data.txt', 'mnemonics.txt']
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            find_mnemonics_in_file(file_path)
        else:
            print(f"⚠️  {file_path} fayli topilmadi")
    
    print("\n🎯 Test tugadi!")
