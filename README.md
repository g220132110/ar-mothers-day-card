# 🎁 AR 母親節卡片

使用 WebAR 技術製作的互動式母親節卡片，無需安裝 App，只要手機瀏覽器就能體驗 AR 效果！

## ✨ 特色

- 📱 **無需安裝 App** - 直接用手機瀏覽器掃描
- 🎬 **播放影片** - 掃描卡片圖片後自動播放影片
- 🔄 **可自訂** - 輕鬆替換標記圖片和影片內容
- 🆓 **完全免費** - 使用開源技術 (MindAR + A-Frame)
- 📱 **跨平台** - 支援 iOS Safari 和 Android Chrome

## 🚀 快速開始

### 線上體驗

👉 **[點擊這裡體驗 AR 效果](你的GitHub-Pages網址/ar-card.html)** 

*(部署後請更新此連結)*

### 如何使用

1. 用手機瀏覽器開啟上方連結
2. 允許相機權限
3. 將相機對準卡片上的標記圖片
4. 享受 AR 驚喜！

## 📦 專案結構

```
ar-mothers-day-card/
├── ar-card.html              # AR 主程式
├── targets.mind              # AR 標記圖片訓練檔
├── video.mp4                 # 播放的影片
├── example_marker.jpg        # 範例標記圖片
├── generate_marker.py        # 標記圖片生成輔助工具
└── README.md                 # 說明文件
```

## 🛠️ 自己製作

### 需求

- 標記圖片（建議高對比度、清晰的圖案）
- 影片檔案（MP4 格式，建議 < 50MB）
- 網頁伺服器（用於測試和部署）

### 步驟

1. **生成 AR 標記檔案**
   - 前往：https://hiukim.github.io/mind-ar-js-doc/tools/compile
   - 上傳你的標記圖片
   - 下載生成的 `targets.mind`

2. **準備影片**
   - 將影片重新命名為 `video.mp4`
   - 確保格式為 H.264 編碼的 MP4

3. **本地測試**
   ```bash
   # 啟動簡單伺服器
   python3 -m http.server 8000
   
   # 用手機瀏覽器開啟
   # http://你的電腦IP:8000/ar-card.html
   ```

4. **部署到 GitHub Pages**
   - 上傳所有檔案到此 Repository
   - 前往 Settings → Pages
   - Source 選擇 `main` branch
   - 儲存後等待 1-2 分鐘
   - 取得你的 GitHub Pages 網址

### 替換標記圖片

每次更換標記圖片時：

1. 準備新的標記圖片
2. 到線上工具重新生成 `targets.mind`
3. 替換 `targets.mind` 檔案
4. 重新部署

### 替換影片

直接替換 `video.mp4` 檔案即可，不需要重新生成 `targets.mind`。

## 📱 製作實體卡片

1. **印出標記圖片**（彩色列印，高品質）
2. **製作 QR Code**（連結到你的 GitHub Pages 網址）
3. **組合卡片**：
   - 將標記圖片貼在卡片上
   - 加上 QR Code
   - 寫上使用說明

### 使用說明範例

```
🎁 母親節快樂！

請用手機掃描 QR Code
然後將相機對準這張圖片
會有驚喜喔！💝
```

## 🔧 技術棧

- **[MindAR](https://hiukim.github.io/mind-ar-js-doc/)** - WebAR 圖像追蹤
- **[A-Frame](https://aframe.io/)** - WebVR 框架
- **HTML5** - Video & Camera API

## 📖 詳細文檔

查看 [完整使用說明](./docs/README.md)（如果有的話）

## ⚠️ 注意事項

- 手機需要允許相機權限
- 需要在光線充足的環境下使用
- 標記圖片要印得清晰（避免模糊或反光）
- 不能直接雙擊 HTML 開啟，必須使用網頁伺服器
- 建議使用 Chrome (Android) 或 Safari (iOS)

## 🐛 常見問題

**Q: 掃不到標記圖片？**
- 增加環境光線
- 調整手機距離（20-40cm）
- 確認標記圖片清晰無反光

**Q: 影片無法播放？**
- 檢查 video.mp4 是否存在
- 確認影片格式為 H.264 MP4
- 清除瀏覽器快取重試

**Q: 可以用其他圖片格式嗎？**
- 標記圖片：JPG 或 PNG
- 3D 模型：GLTF/GLB
- 音訊：MP3

## 📄 授權

MIT License - 自由使用和修改

## 🙏 致謝

- [MindAR](https://github.com/hiukim/mind-ar-js) by hiukim
- [A-Frame](https://aframe.io/) by Mozilla

## 💝 獻給所有偉大的母親

願這個小小的專案能幫助你表達對媽媽的愛！

---

**⭐ 如果這個專案對你有幫助，請給一個 Star！**

有問題或建議？歡迎開 Issue 討論！
