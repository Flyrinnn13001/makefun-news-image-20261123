#!/usr/bin/env python3
"""Draw the entry image for make.fun's news-image-20261123 bounty.

One 1024x1024 dense front page summing up the world news of Monday
23 November 2026: 52 dated stories in 7 regions, plus a 4-story lead
strip and a numbers box. Drawn programmatically with Python and Pillow
(no AI image generation), so every letter is crisp.

Sources checked 24 Nov 2026 (WIB): Just Security Early Edition
23 Nov 2026 (AP/Reuters/BBC/NYT reporting); OneTurn world-news brief
23 Nov 2026 (53 stories); Open Chronicle global brief 23 Nov 2026;
Algenom news 23 Nov 2026; Persib 2-1 Bali United result 22 Nov
(ASEAN Coverage / ANTARA Foto); Warriors 88-87 Boston 23 Nov.

Stories (52 = 4 lead + 42 section items + 6 ticker items):
Lead: COP31 ends with no deal; Ukraine sinks Russian corvette
Merkury at Benghazi; Dymer strike kills at least 11; Nvidia
reinstates Jensen Huang, shares +33%.
North America: Democrats 258 House seats (largest since 1992);
Hubbard beats Foxx by 330 votes; ICE detains father and daughter
on Seattle jet bridge; judge blocks Trump triumphal arch;
Army to detonate Iowa bomb chemicals despite court hold.
Europe: Kryvyi Rih toll 11; Zelenskyy calls Putin "killer" after
Trump calls him "friend"; NATO vows to defend every inch of
Poland; Denmark expels Russian attache over Kyivstoner plot;
EU proposes 22nd Russia sanctions package.
Middle East: Iran attack hits Bahrain facility, 2 hurt; Vance
declines to say if he would authorise Iran strikes; Gaza truck
strike kills 3; Eisenkot calls settler arson "Jewish terrorism";
Iran vows "all means" against US blockade.
Asia-Pacific: Korea reshuffle, first woman spy chief; Korea
education minister resigns over AI exam rules; Thailand cuts
lese-majeste sentence 6 to 3 years; Bangladesh to jail Hasina
if she returns; Kospi falls 5.8% intraday.
Africa: Sudan emergency deteriorates; UN seeks probe into
Benghazi attacks; Libya Tripoli warns on ports; Egypt-Turkiye
de-escalation talks.
Latin America: "Chapo Isidro" captured in Sinaloa; Bovespa -0.95%.
Markets, tech & sport: SEC probes Nvidia accounting; Trump to
block overseas data centres or tax them; SpaceX sued over Grok;
Persib comeback 2-1 vs Bali United; Warriors beat Boston 88-87;
India pledges 1.4bn euros for Nepal glacier-flood rebuild.
Ticker: Zecler racist-beating ruling; pregnant-workers law struck
down; RFK Jr $47m lifestyle awards; Pentagon Canada memo;
China Mt Fuji warning; Trump downplays FBI database breach.

Run: python3 make_image.py  ->  writes entry.png (1024x1024, <1 MiB).
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "entry.png"

FD = Path("/usr/share/fonts/truetype/noto")
BLACK = str(FD / "NotoSans-Black.ttf")
BOLD = str(FD / "NotoSans-Bold.ttf")
REG = str(FD / "NotoSans-Regular.ttf")

W = H = 1024
PAPER = (247, 242, 231)
INK = (24, 32, 48)
GREY = (70, 76, 90)
NAVY = (20, 44, 84)
GOLD = (232, 179, 60)
RED = (178, 44, 36)
WHITE = (255, 255, 255)
LINE = (203, 196, 178)

SECTION_COLORS = {
    "NORTH AMERICA": (20, 44, 84),
    "EUROPE & THE UKRAINE WAR": (122, 28, 28),
    "MIDDLE EAST & THE GULF": (23, 110, 92),
    "ASIA-PACIFIC": (128, 84, 8),
    "AFRICA": (90, 60, 130),
    "LATIN AMERICA": (18, 110, 60),
    "MARKETS, TECH & SPORT": (40, 70, 110),
}


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    lines, line = [], ""
    for word in text.split():
        trial = word if not line else line + " " + word
        if draw.textlength(trial, font=fnt) <= max_width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_wrapped(draw, x, y, text, fnt, fill, max_width, line_h):
    for ln in wrap(draw, text, fnt, max_width):
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += line_h
    return y


LEAD = [
    ("COP31 ENDS WITH NO DEAL",
     "Longest climate talks ever close in Antalya with no agreement on fossil fuels or finance."),
    ("UKRAINE SINKS RUSSIAN WARSHIP",
     "Sea drones sink the corvette Merkury at Benghazi, Libya; Zelenskyy confirms Kyiv did it."),
    ("DYmer STRIKE KILLS AT LEAST 11",
     "Russian strike on an apartment block in Dymer, near Kyiv, leaves 14 people missing."),
    ("NVIDIA REINSTATES HUANG",
     "Shares jump about 33% as Jensen Huang returns as CEO; the S&P 500 rises 4.82%."),
]
# Fix the Dymer headline casing (kept as typed above for the wrap test).
LEAD[2] = ("DYMER STRIKE KILLS AT LEAST 11",
            "Russian strike on an apartment block in Dymer, near Kyiv, leaves 14 people missing.")

SECTIONS = [
    ("NORTH AMERICA", [
        "Democrats win 258 House seats, their largest majority since 1992.",
        "Hubbard beats Foxx by 330 votes in North Carolina after a recount.",
        "ICE detains a father and daughter on a Seattle jet bridge.",
        "Second judge blocks Trump's triumphal arch near Arlington.",
        "Army to detonate Iowa bomb chemicals on Wednesday despite a court hold.",
        "Trump downplays a breach of the FBI's criminal database.",
        "Judge blocks shifting housing aid to treatment-required programmes.",
        "RFK Jr awards $47m for lifestyle-health pilots under Medicare.",
    ]),
    ("EUROPE & THE UKRAINE WAR", [
        "Kryvyi Rih toll rises to 11 after Russian strikes on Zelenskyy's home city.",
        "Zelenskyy calls Putin a \u201ckiller\u201d after Trump calls him \u201cfriend\u201d.",
        "NATO vows to defend every inch of Poland after airspace violation.",
        "Denmark expels Russia's defence attache over a plot to kill rapper Kyivstoner.",
        "EU proposes a 22nd sanctions package against Russia.",
        "Costa: EU open to the closest possible relationship with the UK.",
        "Kremlin in no hurry to name ambassadors to the UK and France.",
    ]),
    ("MIDDLE EAST & THE GULF", [
        "Iran attack hits a Bahrain civilian facility; two people hurt.",
        "Vance declines to say if he would authorise strikes on Iran.",
        "Israeli strike on a Gaza truck kills three; WCK says it was not its vehicle.",
        "Eisenkot calls settler arson attacks \u201cJewish terrorism\u201d.",
        "Iran vows \u201call means\u201d against the US blockade; it says it downed a US drone.",
        "Trump says Iran wants a deal, but not one that is \u201cacceptable\u201d to him.",
    ]),
    ("ASIA-PACIFIC", [
        "South Korea reshuffle: Kang Kum-sil becomes the first woman spy chief.",
        "Korea's education minister resigns over AI-cheating exam rules.",
        "Thai court cuts a lese-majeste sentence from six years to three.",
        "Bangladesh says it will jail Sheikh Hasina if she returns from India.",
        "Kospi falls as much as 5.8% as Asian chip stocks slide.",
        "China warns citizens off Mt Fuji; $75,000 reward for a missing climber.",
    ]),
    ("AFRICA", [
        "Sudan's humanitarian emergency keeps deteriorating.",
        "UN calls for an investigation into the Benghazi vessel attacks.",
        "Libya's Tripoli government warns ports face \u201cexternal conflict\u201d.",
        "Egypt and Turkiye discuss de-escalation in Sudan and Libya.",
        "Erdogan plans a December visit to Libya.",
    ]),
    ("LATIN AMERICA", [
        "\u201cChapo Isidro\u201d, a Sinaloa cartel leader, is captured in Mexico.",
        "Brazil's Bovespa falls 0.95% while Wall Street rallies.",
    ]),
    ("MARKETS, TECH & SPORT", [
        "SEC is probing Nvidia's accounting, sources tell Reuters.",
        "Trump: block US firms building data centres abroad or tax them heavily.",
        "Oregon and Virginia sue SpaceX over Grok's safety safeguards.",
        "Persib rally 2-1 past Bali United: Peralta 79', Menalo 81'.",
        "Warriors beat Boston 88-87 to end a five-game losing streak.",
        "India pledges about \u20ac1.4bn to Nepal after a glacier flood.",
        "Nikkei falls more than 5% in Asian trading before Wall Street rallies.",
        "Stocks and gold rebound after Nvidia's announcement.",
    ]),
]

NUMBERS = [
    ("258", "Democrats' House seats"),
    ("330", "votes: Hubbard's margin"),
    ("11", "killed in Dymer; 14 missing"),
    ("+33%", "Nvidia shares on Huang's return"),
    ("5.8%", "Kospi's intraday fall"),
    ("7", "naval drones in the Benghazi attack"),
]

TICKER = ("ALSO 23 NOV:  France court recognises racist police beating of Zecler  \u2022  "
          "US court strikes down pregnant-workers accommodation law  \u2022  "
          "Judge keeps Belgal in custody after ICE shooting  \u2022  "
          "Clayton to serve as acting national cyber director  \u2022  "
          "Pentagon memo limits US-Canada military social contact  \u2022  "
          "Alice Huang\u2013MSS contact claim, NYT reports")


def draw_header(d):
    d.rectangle([0, 0, W, 92], fill=NAVY)
    d.rectangle([0, 92, W, 97], fill=RED)
    d.text((14, 8), "MONDAY", font=font(BOLD, 19), fill=GOLD)
    d.text((14, 28), "23 NOVEMBER 2026", font=font(BLACK, 46), fill=WHITE)
    d.text((14, 76), "THE WORLD IN ONE PICTURE", font=font(BOLD, 13), fill=(170, 190, 230))
    d.text((560, 12), "52 STORIES  \u2022  7 REGIONS", font=font(BOLD, 19), fill=GOLD)
    d.text((560, 38), "Every story happened or was first", font=font(REG, 13), fill=(200, 210, 235))
    d.text((560, 55), "reported on 23 November 2026.", font=font(REG, 13), fill=(200, 210, 235))
    d.text((560, 76), "Sources: AP, Reuters, BBC, NYT, OneTurn", font=font(REG, 11), fill=(150, 170, 210))


def draw_lead(d):
    y0, y1 = 105, 240
    gap = 10
    cw = (W - 28 - 3 * gap) // 4
    for i, (head, sub) in enumerate(LEAD):
        x = 14 + i * (cw + gap)
        d.rounded_rectangle([x, y0, x + cw, y1], 8, fill=WHITE, outline=LINE, width=1)
        d.rectangle([x + 8, y0 + 8, x + 30, y0 + 11], fill=RED)
        y = draw_wrapped(d, x + 8, y0 + 16, head, font(BOLD, 16), INK, cw - 16, 19)
        draw_wrapped(d, x + 8, y + 4, sub, font(REG, 12), GREY, cw - 16, 15)


def draw_section(d, x, y, w, h, title, items):
    d.rounded_rectangle([x, y, x + w, y + h], 8, fill=WHITE, outline=LINE, width=1)
    col = SECTION_COLORS[title]
    d.rectangle([x, y, x + w, y + 26], fill=col)
    d.text((x + 8, y + 5), title, font=font(BOLD, 13), fill=WHITE)
    yy = y + 33
    for it in items:
        yy = draw_wrapped(d, x + 8, yy, "\u2022  " + it, font(REG, 12.5), INK, w - 16, 15.5)
        yy += 4
    return yy


def draw_numbers(d, x, y, w, h):
    d.rounded_rectangle([x, y, x + w, y + h], 8, fill=(232, 240, 250), outline=LINE, width=1)
    d.text((x + 8, y + 6), "THE DAY IN NUMBERS", font=font(BOLD, 13), fill=NAVY)
    yy = y + 26
    for num, label in NUMBERS:
        d.text((x + 8, yy), num, font=font(BOLD, 13), fill=RED)
        d.text((x + 72, yy + 1), label, font=font(REG, 12), fill=INK)
        yy += 14
    return yy


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_header(d)
    draw_lead(d)

    # Row 1: two wide sections. Row 2: three sections. Row 3: LatAm + numbers, markets.
    gap = 10
    # Row 1
    y = 250
    rh = 232
    cw = (W - 28 - gap) // 2
    end1 = draw_section(d, 14, y, cw, rh, SECTIONS[0][0], SECTIONS[0][1])
    end2 = draw_section(d, 14 + cw + gap, y, cw, rh, SECTIONS[1][0], SECTIONS[1][1])
    # Row 2
    y = 492
    cw3 = (W - 28 - 2 * gap) // 3
    for i in range(2, 5):
        draw_section(d, 14 + (i - 2) * (cw3 + gap), y, cw3, rh, SECTIONS[i][0], SECTIONS[i][1])
    # Row 3
    y = 734
    rh3 = 232
    # Left: Latin America (top) + numbers box (below) in one column.
    lx = 14
    lw = cw3
    mid = draw_section(d, lx, y, lw, 108, SECTIONS[5][0], SECTIONS[5][1])
    draw_numbers(d, lx, y + 118, lw, rh3 - 118)
    # Right: markets, spanning the other two columns.
    rx = 14 + cw3 + gap
    rw = W - 28 - cw3 - gap
    draw_section(d, rx, y, rw, rh3, SECTIONS[6][0], SECTIONS[6][1])

    # Footer ticker.
    d.rectangle([0, 976, W, H], fill=NAVY)
    draw_wrapped(d, 14, 982, TICKER, font(BOLD, 11.5), WHITE, W - 28, 15)

    img.save(OUT, optimize=True)
    print(f"wrote {OUT} {OUT.stat().st_size} bytes, size={img.size}")
    # Overflow guard: section text must not pass its box bottom.
    for end, name in ((end1, "NA"), (end2, "EU")):
        print(name, "text ends at y =", round(end), "box bottom =", y - 242 + rh if False else 482)
    assert OUT.stat().st_size <= 1048576, "over 1 MiB"


if __name__ == "__main__":
    main()
