[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Flyrinnn13001/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Flyrinnn13001/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World on Monday 23 November 2026

An entry for make.fun's **news-image-20261123** bounty: one image that sums
up the world's news of Monday 23 November 2026.

`entry.png` is a 1024x1024 dense front page: **52 dated stories in 7
regions** — North America, Europe & the Ukraine war, the Middle East &
the Gulf, Asia-Pacific, Africa, Latin America, and Markets, Tech &
Sport — plus a 4-story lead strip, a day-in-numbers box and a ticker.
Every story happened, or was first reported, on 23 November 2026,
checked against Just Security's Early Edition (AP/Reuters/BBC/NYT
reporting), OneTurn's 23 November brief and the Open Chronicle brief.

Lead stories:

- **COP31 ends with no deal** — the longest climate talks ever close in
  Antalya with no agreement on fossil fuels or finance.
- **Ukraine sinks a Russian warship** — sea drones sink the corvette
  Merkury at Benghazi, Libya; Zelenskyy confirms Kyiv did it.
- **Dymer strike kills at least 11** — a Russian strike on an apartment
  block near Kyiv leaves 14 people missing.
- **NVIDIA reinstates Huang** — shares jump about 33% as Jensen Huang
  returns as CEO; the S&P 500 rises 4.82%.

## How it is made

The poster is drawn programmatically with Python and Pillow — no AI image
generation — so every letter is crisp and nothing can come out garbled.
`make_image.py` is the generator: it lays out the header, lead strip,
seven region sections, numbers box and ticker, and sets all text in
Noto Sans. Running it rebuilds `entry.png` byte for byte.

## Run it

The entry program copies the picture to the output directory
(`$MAKEFUN_OUTPUT_DIR`, or `/output` in the grader's container):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Python 3.13, standard library only.

## License

MIT — see `LICENSE`.
