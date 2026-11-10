import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

SUITE_DIR = os.path.dirname(os.path.abspath(__file__))
FRAMES_DIR = os.path.join(SUITE_DIR, 'temp_frames')
OUTPUT_DIR = os.path.join(SUITE_DIR, 'output_reels')

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 1080, 1920

def create_slide_1_hook(title, subject, repeats, years):
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#090d16')
    draw = ImageDraw.Draw(img)

    # Ambient glow
    for r in range(400, 0, -8):
        draw.ellipse([540 - r*1.3, 350 - r, 540 + r*1.3, 350 + r], fill=(15 + int(35*(1-r/400)), 20 + int(45*(1-r/400)), 50 + int(90*(1-r/400))))

    # Brand badge top
    draw.rounded_rectangle([340, 160, 740, 230], radius=12, fill='#1e293b', outline='#3b82f6', width=2)
    draw.text((375, 180), 'WOVRIX / PYQ', fill='#60a5fa')

    # Warning alert pill
    draw.rounded_rectangle([200, 420, 880, 510], radius=16, fill='#7f1d1d', outline='#ef4444', width=2)
    draw.text((250, 445), f'🚨 {repeats.upper()} RECURRENCE', fill='#fecaca')

    # Main viral hook headline
    hook_text = f"DO NOT SKIP THIS\nIN CBSE 12 {subject.upper()}!"
    draw.text((120, 620), hook_text, fill='#ffffff')

    # Subtitle
    sub = f"Repeated in {years} Board Papers\nOfficial Step Marking Scheme Inside"
    draw.text((120, 820), sub, fill='#94a3b8')

    # Concept Highlight Card
    draw.rounded_rectangle([100, 1050, 980, 1350], radius=24, fill='#0f172a', outline='#334155', width=2)
    draw.text((140, 1100), "⭐ EXAM ARCHETYPE:", fill='#38bdf8')
    draw.text((140, 1160), title, fill='#f8fafc')
    draw.text((140, 1260), "Watch next slide for the official 3-step rubric ➔", fill='#94a3b8')

    # Bottom footer CTA
    draw.text((280, 1720), "Swipe / Watch till end ⬇️", fill='#64748b')

    path = os.path.join(FRAMES_DIR, 'slide1.png')
    img.save(path)
    return path

def create_slide_2_question(title, question_text, marks):
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#090d16')
    draw = ImageDraw.Draw(img)

    # Header
    draw.rounded_rectangle([100, 160, 480, 230], radius=12, fill='#1e293b', outline='#3b82f6', width=2)
    draw.text((140, 180), f"⚡ {marks} MARK QUESTION", fill='#60a5fa')

    draw.text((100, 300), "The Official Question:", fill='#ffffff')
    
    # Question Card Box
    draw.rounded_rectangle([100, 380, 980, 1150], radius=24, fill='#0f172a', outline='#38bdf8', width=2)
    
    # Question text (wrap manually)
    lines = []
    words = question_text.split()
    cur = ""
    for w in words:
        if len(cur + " " + w) < 32:
            cur += " " + w
        else:
            lines.append(cur.strip())
            cur = w
    if cur:
        lines.append(cur.strip())

    y = 440
    for l in lines:
        draw.text((140, y), l, fill='#f1f5f9')
        y += 55

    # Bottom hint
    draw.rounded_rectangle([100, 1250, 980, 1500], radius=20, fill='#1e1b4b', outline='#6366f1', width=1)
    draw.text((140, 1290), "⚠️ 78% of students lose 1 mark here:", fill='#a5b4fc')
    draw.text((140, 1360), "Missing the circuit diagram or waveform labels!", fill='#e0e7ff')

    draw.text((280, 1720), "Next: Official CBSE Marking Key ➔", fill='#64748b')

    path = os.path.join(FRAMES_DIR, 'slide2.png')
    img.save(path)
    return path

def create_slide_3_solution(title, steps):
    img = Image.new('RGB', (WIDTH, HEIGHT), color='#090d16')
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([100, 160, 560, 230], radius=12, fill='#064e3b', outline='#10b981', width=2)
    draw.text((130, 180), "✓ CBSE OFFICIAL RUBRIC", fill='#6ee7b7')

    draw.text((100, 300), "How Evaluators Give Marks:", fill='#ffffff')

    y = 380
    for i, (step_title, mark, desc) in enumerate(steps):
        draw.rounded_rectangle([100, y, 980, y + 260], radius=20, fill='#0f172a', outline='#334155', width=1)
        draw.text((140, y + 30), f"Step {i+1}: {step_title}", fill='#38bdf8')
        draw.rounded_rectangle([780, y + 25, 940, y + 75], radius=8, fill='#1e293b')
        draw.text((800, y + 35), f"+{mark} Mark", fill='#10b981')
        draw.text((140, y + 100), desc, fill='#cbd5e1')
        y += 300

    # CTA Card at bottom
    draw.rounded_rectangle([100, 1380, 980, 1680], radius=24, fill='#1e1b4b', outline='#818cf8', width=2)
    draw.text((140, 1420), "🔥 PRACTICE 1,792 BOARD CLONES FREE", fill='#ffffff')
    draw.text((140, 1485), "• 100% Free • No Login Required\n• Verified Repeat Radar for CBSE 12 & NEET UG\n• Visit: pyq.wovrix.in (Link in Bio/Comments)", fill='#c7d2fe')

    path = os.path.join(FRAMES_DIR, 'slide3.png')
    img.save(path)
    return path

def render_video():
    # 1. Generate slides
    s1 = create_slide_1_hook(
        title="Full Wave Rectifier Working & Waveforms",
        subject="Physics",
        repeats="3 of 5 Years (9x)",
        years="2022, 2024, 2026"
    )
    s2 = create_slide_2_question(
        title="Full Wave Rectifier Working & Waveforms",
        question_text="With the help of a circuit diagram, explain the working of a full wave rectifier. Depict the input and output waveforms.",
        marks="3"
    )
    s3 = create_slide_3_solution(
        title="Full Wave Rectifier Working & Waveforms",
        steps=[
            ("Circuit Diagram", "1", "Labeled center-tap transformer, 2 diodes (D1, D2), and load resistor RL."),
            ("Working Explanation", "1", "Operation during positive and negative half-cycles with diode conduction."),
            ("Waveforms Depiction", "1", "Input AC vs Full-wave rectified pulsating DC output.")
        ]
    )

    # 2. Build 15-second video using ffmpeg
    # Slide 1: 0-4s (4 sec)
    # Slide 2: 4-9s (5 sec)
    # Slide 3: 9-15s (6 sec)
    out_video = os.path.join(OUTPUT_DIR, 'sample_reel_rectifier.mp4')
    
    cmd = [
        'ffmpeg', '-y',
        '-loop', '1', '-t', '4', '-i', s1,
        '-loop', '1', '-t', '5', '-i', s2,
        '-loop', '1', '-t', '6', '-i', s3,
        '-filter_complex', '[0:v][1:v][2:v]concat=n=3:v=1:a=0,format=yuv420p',
        '-c:v', 'libx264', '-r', '30',
        out_video
    ]
    
    print("Rendering video with ffmpeg...")
    subprocess.run(cmd, check=True)
    print(f"Video rendered successfully: {out_video}")

    # Generate ready-to-copy social captions
    caption_path = os.path.join(OUTPUT_DIR, 'sample_reel_caption.txt')
    caption_text = """🚨 3 OF 5 YEARS REPEATED: Full Wave Rectifier (CBSE Class 12 Physics)

If this derivation comes in your board paper, do NOT lose that 1 mark on waveform labeling!

CBSE 3-Step Marking Rubric:
1️⃣ Circuit Diagram with D1, D2 & Center-tap transformer [1 Mark]
2️⃣ Working during both half-cycles [1 Mark]
3️⃣ Input vs Output pulsating DC waveforms [1 Mark]

👉 Practice all 1,792 authentic CBSE board repeat clones for free (No login needed):
🔗 https://pyq.wovrix.in (Link in Bio)

#cbseclass12 #class12physics #boardexam2026 #pyq #physicsderivations #cbseboard #neet2026 #jeemains
"""
    with open(caption_path, 'w', encoding='utf-8') as f:
        f.write(caption_text)
    print(f"Caption generated: {caption_path}")

if __name__ == '__main__':
    render_video()
