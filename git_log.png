from PIL import Image, ImageDraw, ImageFont
import subprocess

# Recuperer le git log
result = subprocess.run(
    [\"git\", \"log\", \"--oneline\", \"--graph\", \"--all\"],
    capture_output=True, text=True, cwd=\"/app/projet_rattrapage\"
)
lines = result.stdout.strip().split(\"
\")

# Configuration
font_size = 16
line_height = 22
padding = 30
width = 800
height = padding * 2 + len(lines) * line_height + 40

# Creer l'image avec fond sombre (style terminal)
img = Image.new(\"RGB\", (width, height), (30, 30, 30))
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype(\"/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf\", font_size)
except:
    font = ImageFont.load_default()

# Titre
draw.text((padding, 10), \"$ git log --oneline --graph --all\", fill=(0, 255, 0), font=font)

# Contenu du log
y = 10 + line_height + 10
for line in lines:
    # Colorer les elements du graph
    color = (220, 220, 220)  # blanc par defaut
    if line.strip().startswith(\"*\"):
        # Ligne de commit
        if \"merge:\" in line:
            color = (255, 200, 100)  # orange pour merge
        elif \"feat:\" in line:
            color = (100, 200, 255)  # bleu pour feat
        elif \"fix:\" in line:
            color = (255, 100, 100)  # rouge pour fix
        elif \"init:\" in line or \"docs:\" in line:
            color = (150, 255, 150)  # vert pour init/docs
    draw.text((padding, y), line, fill=color, font=font)
    y += line_height

img.save(\"/app/projet_rattrapage/git_log.png\")
print(\"Image generee : git_log.png\")
"
