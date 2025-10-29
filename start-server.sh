#!/bin/bash
# 快速啟動 AR 卡片測試伺服器

echo "================================"
echo "🎁 AR 母親節卡片 - 測試伺服器"
echo "================================"
echo ""

# 檢查檔案
echo "📋 檢查必要檔案..."

if [ ! -f "ar-card.html" ]; then
    echo "❌ 找不到 ar-card.html"
    exit 1
fi

if [ ! -f "targets.mind" ]; then
    echo "⚠️  警告: 找不到 targets.mind"
    echo "   請先生成標記圖片訓練檔！"
    echo "   參考 README.md 的說明"
    echo ""
fi

if [ ! -f "video.mp4" ]; then
    echo "⚠️  警告: 找不到 video.mp4"
    echo "   請準備你要播放的影片"
    echo ""
fi

# 取得本機 IP
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    LOCAL_IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    LOCAL_IP=$(hostname -I | awk '{print $1}')
else
    LOCAL_IP="localhost"
fi

echo "✅ 準備啟動伺服器..."
echo ""
echo "📱 手機掃描以下網址:"
echo "   http://${LOCAL_IP}:8000/ar-card.html"
echo ""
echo "🖥️  或在電腦瀏覽器開啟:"
echo "   http://localhost:8000/ar-card.html"
echo ""
echo "⏸️  按 Ctrl+C 停止伺服器"
echo ""
echo "================================"
echo ""

# 啟動伺服器
python3 -m http.server 8000
