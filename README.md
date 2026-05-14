# 💃 Chika-Chan ASCII v1.0.0

<div align="center">

**Do you want Chika to dance in your terminal? No? Well I do, so I made this.**

[Download Latest Release](https://github.com/TerzicScript/chika-dance-ascii/releases) • [Report Bug](https://github.com/TerzicScript/chika-dance-ascii/issues) • [Request Feature](https://github.com/TerzicScript/chika-dance-ascii/issues)

</div>

## 🎯 Overview

**Chika-Chan ASCII** is a real-time video-to-ASCII transcoder. It processes video frames, removes green-screen backgrounds via HSV chromakeying, and renders the result directly into your terminal using 16.7 million colors. It’s essentially a low-res, text-based cinema for your CLI.

---

## 📸 Demos

<div align="center">

| Classic B&W | 24-bit TrueColor |
|:---:|:---:|
| <video src="https://github.com/user-attachments/assets/18e8cf29-4d94-464b-a037-ade7cd490adb" width="350"></video> | <video src="https://github.com/user-attachments/assets/40a56c57-2b51-4917-ac50-da9a421592f0" width="350"></video> |

</div>

---

## ⚙️ How It Works

The application acts as a digital translator between a video file and your terminal's text buffer.

1.  **Chromakeying**: The script identifies the green background and "deletes" it in real-time using HSV filtering.
2.  **Downsampling**: The $1920 \times 1080$ video is shrunken down to an 80-column grid.
3.  **ANSI Injection**: Every character is wrapped in a 24-bit ANSI color code to match the original anime frames.
4.  **Audio Sync**: Uses a temporal clock to ensure the dancing stays perfectly on beat with the music.

**Directory Structure:**
```text
Project_Folder/
├── main.py
├── maincol.py
├── chika_full.mp4
└── chika_audio2.mp3
```

---

### Why This Tool?

- Because 80 columns of best girl is peak culture. 

---

## ✨ Features

### Core Features

| Feature | Description |
|---------|-------------|
| **24-bit TrueColor** | Uses full RGB spectrum for terminal characters |
| **Real-Time Sync** | Stays perfectly in time with the background audio |
| **Chromakey Support** | Automatically removes green screens for a clean silhouette |
| **Zero-Flicker** | Optimized buffer writing to keep the animation smooth |
| **Low Latency** | Uses NumPy for high-speed matrix processing |

---

## 💾 Download & Installation

### Option 1: Run from Source

**Requirements:**
- Python 3.10 or higher
- FFmpeg (specifically ```ffplay``` for audio)

**Installation Steps:**

```bash
# Clone the repository
git clone https://github.com/TerzicScript/chika-dance-ascii.git
cd chika-dance-ascii

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

---

## 🛠 Technical Details

To keep the render fast enough for 24fps, the script uses a high-performance I/O pipeline:

- **OpenCV**: Handles the HSV color space conversion and frame extraction.
- **NumPy**: Processes the luminance mapping as a vectorized matrix operation.
- **ANSI Escape Codes**: Specifically ```\033[38;2;R;G;Bm``` for foreground TrueColor.
- **Clock Correction**: Compares ```time.time()``` against the video's frame count to prevent drift.

---

## 🚀 Quick Start Guide

### Step 1: Launch
Ensure your terminal supports TrueColor (Windows Terminal, Alacritty, or Kitty are recommended). Run ```python main.py```.

### Step 2: Sync Check
The script will automatically trigger ```ffplay``` for the audio. If you notice a delay, ensure your CPU isn't being throttled by other applications.

### Step 3: Aesthetic Tuning
Right-click your terminal header to decrease the font size. The smaller the font, the more "high-res" the ASCII art will appear!

---

## 🙏 Credits

- **OpenCV & NumPy** - For making math look like magic.
- **IQ san demo makasenasai!** - Chika Fujiwara.

---

<div align="center">

[⬆ Back to Top](#chika-dance-ascii-v100)

</div>
