#!/usr/bin/env python3
"""
AR 標記圖片生成工具
用於將你的圖片轉換成 AR 可辨識的 .mind 檔案

使用方法:
1. 安裝套件: pip install opencv-python pillow --break-system-packages
2. 準備你的標記圖片（建議: 高對比度、清晰、獨特的圖案）
3. 執行: python3 generate_marker.py 你的圖片.jpg
"""

import sys
import os
import subprocess

def check_dependencies():
    """檢查必要的套件"""
    try:
        import cv2
        from PIL import Image
        return True
    except ImportError as e:
        print(f"❌ 缺少必要套件: {e}")
        print("\n請執行以下指令安裝:")
        print("pip install opencv-python pillow --break-system-packages")
        return False

def prepare_image(image_path, output_path="marker.jpg"):
    """準備標記圖片 - 調整大小和品質"""
    try:
        from PIL import Image
        
        # 開啟圖片
        img = Image.open(image_path)
        
        # 轉換為 RGB（如果是 PNG 或其他格式）
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # 調整大小到適合的尺寸（MindAR 建議 480-1024px）
        max_size = 800
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        
        # 儲存優化後的圖片
        img.save(output_path, 'JPEG', quality=95)
        
        print(f"✅ 圖片已優化: {output_path}")
        print(f"   尺寸: {img.size}")
        return output_path
        
    except Exception as e:
        print(f"❌ 圖片處理失敗: {e}")
        return None

def generate_mind_file(image_path):
    """使用 MindAR compiler 生成 .mind 檔案"""
    
    print("\n" + "="*50)
    print("🎯 AR 標記圖片生成工具")
    print("="*50 + "\n")
    
    # 檢查圖片是否存在
    if not os.path.exists(image_path):
        print(f"❌ 找不到圖片: {image_path}")
        return False
    
    print(f"📷 使用圖片: {image_path}")
    
    # 準備圖片
    optimized_image = prepare_image(image_path, "D:/Downloads/ar-card/marker_optimized.jpg")
    if not optimized_image:
        return False
    
    print("\n" + "-"*50)
    print("📝 需要使用線上工具生成 .mind 檔案")
    print("-"*50)
    print("\n請按照以下步驟操作:\n")
    print("1. 前往: https://hiukim.github.io/mind-ar-js-doc/tools/compile")
    print("2. 點擊 'Upload Image' 上傳你的圖片: marker_optimized.jpg")
    print("3. 點擊 'Start' 開始編譯")
    print("4. 下載生成的 'targets.mind' 檔案")
    print("5. 將 targets.mind 放在與 ar-card.html 同一個資料夾")
    
    print("\n" + "="*50)
    print("💡 圖片選擇建議:")
    print("="*50)
    print("✓ 使用高對比度的圖案")
    print("✓ 避免純色或漸層背景")
    print("✓ 包含明顯的特徵點（邊角、圖案等）")
    print("✓ 避免模糊或反光的照片")
    print("✓ 建議尺寸: 500x500 到 1000x1000 像素")
    
    return True

def main():
    #if len(sys.argv) < 2:
    #    print("使用方法: python3 generate_marker.py 你的圖片.jpg")
    #    print("\n範例: python3 generate_marker.py mom_photo.jpg")
    #    sys.exit(1)
    
    # 檢查依賴套件
    if not check_dependencies():
        sys.exit(1)
    
    #image_path = sys.argv[1]
    image_path="D:/Downloads/ar-card/mothercard.jpg"
    generate_mind_file(image_path)

if __name__ == "__main__":
    main()
