import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# ─── Configuration ──────────────────────────────────────────────────────────────
BASE_DIR     = os.path.abspath(os.path.dirname(__file__))
CSV_FILE     = os.path.join(BASE_DIR, "employee.csv")
PHOTO_DIR    = os.path.join(BASE_DIR, "photos")
LOGO_PATH    = os.path.join(BASE_DIR, "logo.png")
OUTPUT_PDF   = os.path.join(BASE_DIR, "employee_ids.pdf")

# Card dimensions (px)
ID_WIDTH, ID_HEIGHT = 800, 400

# Colors
ORANGE = (255, 102, 0)
WHITE  = (255, 255, 255)

# Layout boxes
LOGO_BOX    = (40,  40, 160, 160)          # x,y,width,height
PHOTO_BOX   = (ID_WIDTH-260,  50, 200, 240)
STRIPE_Y    = ID_HEIGHT -  80

# Text positions
COMPANY_X       = LOGO_BOX[0] + LOGO_BOX[2] + 20
COMPANY_NAME_Y  =  70
COMPANY_SUB_Y   = COMPANY_NAME_Y + 50
TITLE_Y         = PHOTO_BOX[1] + PHOTO_BOX[3] + 10
NAME_Y          = STRIPE_Y + 20

# Fonts (falls back to default if Arial not found)
def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except IOError:
        return ImageFont.load_default()

FONT_COMPANY_NAME = load_font("arialbd.ttf", 36)
FONT_COMPANY_SUB  = load_font("arial.ttf",   24)
FONT_TITLE        = load_font("arial.ttf",   22)
FONT_NAME         = load_font("arialbd.ttf", 28)

# ─── Utility to center text horizontally in a given box ─────────────────────────
def center_text(draw, text, font, container_x, container_w, y, fill):
    bbox   = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    x      = container_x + (container_w - text_w) // 2
    draw.text((x, y), text, font=font, fill=fill)

# ─── Build a single card ─────────────────────────────────────────────────────────
def make_card(name, title, photo_filename):
    # 1) Start with solid orange
    card = Image.new("RGB", (ID_WIDTH, ID_HEIGHT), ORANGE)
    draw = ImageDraw.Draw(card)

    # 2) Paste logo (if you provided logo.png)
    if os.path.isfile(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert("RGBA")
        logo = logo.resize((LOGO_BOX[2], LOGO_BOX[3]), Image.LANCZOS)
        card.paste(logo, (LOGO_BOX[0], LOGO_BOX[1]), logo)

    # 3) Company name + subtitle
    draw.text((COMPANY_X,      COMPANY_NAME_Y), "Unsolvability",   font=FONT_COMPANY_NAME, fill=WHITE)
    draw.text((COMPANY_X,      COMPANY_SUB_Y),  "Tie Enterprises", font=FONT_COMPANY_SUB,  fill=WHITE)

    # 4) Photo frame & portrait
    px, py, pw, ph = PHOTO_BOX
    draw.rectangle([px, py, px+pw, py+ph], fill=WHITE)
    photo_path = os.path.join(PHOTO_DIR, photo_filename)
    if os.path.isfile(photo_path):
        photo = Image.open(photo_path).convert("RGB")
        margin = 8
        photo = photo.resize((pw - 2*margin, ph - 2*margin), Image.LANCZOS)
        card.paste(photo, (px + margin, py + margin))

    # 5) Title under photo, centered in the photo-column
    center_text(draw, title, FONT_TITLE, px, pw, TITLE_Y, fill=WHITE)

    # 6) Bottom white stripe + name in orange
    draw.rectangle([0, STRIPE_Y, ID_WIDTH, ID_HEIGHT], fill=WHITE)
    center_text(draw, name, FONT_NAME, 0, ID_WIDTH, NAME_Y, fill=ORANGE)

    return card

# ─── Main: read CSV, generate cards, emit PDF ───────────────────────────────────
def main():
    if not os.path.isfile(CSV_FILE):
        print(f"Missing CSV: {CSV_FILE}")
        return

    df    = pd.read_csv(CSV_FILE)
    cards = []

    for _, row in df.iterrows():
        name  = row["name"].strip()
        title = row["title"].strip()
        photo = row["photo_filename"].strip()
        print(f"→ Generating card for {name}")
        cards.append(make_card(name, title, photo))

    if not cards:
        print("No cards to generate.")
        return

    # Save as multi-page PDF
    cards[0].save(
        OUTPUT_PDF,
        format="PDF",
        save_all=True,
        append_images=cards[1:],
        resolution=100.0
    )
    print(f"✅ Done! See {OUTPUT_PDF}")

if __name__ == "__main__":
    main()
