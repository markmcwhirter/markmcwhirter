#!/usr/bin/env python3
"""Generates the static site (index.html, about.html, posts/*.html) from POSTS data.
Run: python3 generate.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

POSTS = [
    {
        "slug": "stopped-chasing-productivity-hacks",
        "title": "Why I Stopped Chasing Productivity Hacks",
        "date": "August 12, 2026",
        "tag": "Reflections",
        "excerpt": "I spent two years trying every app, method, and morning routine I could find. Here's what actually changed when I stopped optimizing and just started working.",
        "content": [
            "For a while, my search history was basically a productivity graveyard: time-blocking apps, the latest note-taking system, a color-coded calendar that took longer to maintain than the tasks it tracked. Every new method felt like the one that would finally fix how scattered I felt.",
            "The truth is none of them fixed anything, because the problem was never the system. It was that I was using the search for a better method as a way to avoid starting the actual work in front of me. Research feels productive. It rarely is.",
            "What changed things wasn't a new app. It was a short list on an index card: three things that mattered that day, written by hand before I opened my laptop. No categories, no priorities ranked by urgency versus importance, just three things.",
            "&ldquo;Simple enough to remember, small enough to finish.&rdquo; That's the whole method now. It's not glamorous, and it won't make a great newsletter headline, but it's the first system I've kept using for longer than a month.",
            "If you're circling the productivity aisle right now, my only suggestion is to try going smaller before you try going more sophisticated. The friction is rarely the tool.",
        ],
    },
    {
        "slug": "weekend-without-my-phone",
        "title": "A Weekend Without My Phone",
        "date": "July 28, 2026",
        "tag": "Slow Living",
        "excerpt": "I left my phone in a drawer for 48 hours out of curiosity more than discipline. It was uncomfortable in ways I didn't expect, and useful in ways I really didn't expect.",
        "content": [
            "The first few hours were the hardest, not because I missed anything specific, but because my hand kept reaching for a pocket that wasn't there. That reflex alone told me something worth paying attention to.",
            "By Saturday afternoon, the itch had mostly faded, replaced by a strange sense of extra time. I don't think the weekend was actually longer. It just felt that way because nothing was fragmenting it into five-minute pieces.",
            "I read most of a book I'd been meaning to finish for months. I also got bored, properly bored, in a way I hadn't in a long time. It turns out boredom is where a lot of my better ideas quietly show up, if I give them the room.",
            "I'm not going to pretend I've sworn off my phone forever. Monday morning I was back to checking it before I'd even had coffee. But I've started keeping it in another room on weekend mornings, just to buy myself that first hour back.",
        ],
    },
    {
        "slug": "slow-morning-coffee",
        "title": "The Joy of a Slow Morning Coffee",
        "date": "July 9, 2026",
        "tag": "Rituals",
        "excerpt": "Ten minutes with a kettle, a grinder, and no phone in sight has become the one part of my day I refuse to rush, and it's changed how the rest of the morning goes.",
        "content": [
            "There's nothing efficient about grinding beans by hand instead of pressing a button. That's rather the point. The extra ninety seconds gives me a reason to stand still before the day starts moving.",
            "I used to drink coffee on the way out the door, which meant I barely noticed it. Now I sit at the table, no screen, and just watch the pour. It sounds precious written down, but it doesn't feel precious in practice. It feels like the one unhurried thing before everything else asks for my attention.",
            "&ldquo;A ritual doesn't have to be complicated to be a ritual. It just has to be repeated on purpose.&rdquo;",
            "If your mornings feel like they start already behind, I'd gently suggest picking one small, slightly inefficient thing and doing it the slow way anyway. Ten minutes is a small price for a calmer first hour.",
        ],
    },
    {
        "slug": "keeping-a-paper-journal",
        "title": "Notes on Keeping a Paper Journal",
        "date": "June 21, 2026",
        "tag": "Writing",
        "excerpt": "After years of digital notes I can never find again, I went back to a plain notebook. Six months in, here's what's stuck and what hasn't.",
        "content": [
            "I've tried nearly every note-taking app that promised to be the last one I'd ever need. Each time, the notes piled up somewhere I never revisited them. Searchable isn't the same as memorable.",
            "A paper journal forces a kind of editing that typing doesn't. Handwriting is slower, so I only write down what actually feels worth the effort. The result is fewer notes, but the ones I keep matter more.",
            "It's not all upside. I've genuinely lost track of a few good ideas because they live in a notebook and not in a searchable database. I've made peace with that trade. Some things are allowed to be a little inefficient if they're also enjoyable.",
            "My current habit: one page most nights, no more than a few minutes, mostly about what actually happened that day rather than what I planned to do. It's a small thing, but I look forward to it more than I expected to.",
        ],
    },
    {
        "slug": "learning-to-say-no",
        "title": "Learning to Say No",
        "date": "June 3, 2026",
        "tag": "Reflections",
        "excerpt": "For most of my twenties, saying yes felt like the safe choice. It took a genuinely overwhelming year to teach me that it usually wasn't.",
        "content": [
            "I used to think that turning something down meant closing a door that might not open again. So I said yes to almost everything: extra projects, favors, plans I didn't really want to make. It felt generous. Mostly it just left me tired.",
            "The shift happened gradually, then all at once during a stretch where I had said yes to more than I could actually deliver on. Nothing dramatic happened. I just quietly did a worse job at all of it, and nobody was better off for my agreeableness.",
            "&ldquo;A yes given out of guilt isn't really a gift to anyone, including yourself.&rdquo;",
            "These days I try to leave a day or two before answering anything that isn't urgent. Most of the time, the extra pause is enough to tell whether I actually want to do the thing, or whether I just didn't want to feel like the kind of person who says no.",
            "I still say yes to plenty. I just trust the yeses more now, because I know they're not the default.",
        ],
    },
]

SITE_TITLE = "Quiet Notes"
SITE_TAGLINE = "Small, unhurried thoughts on slow living, simple tools, and paying attention."

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="{css_path}styles.css">
</head>
<body>
"""

HEADER = """<header class="site-header">
  <div class="wrap">
    <a class="site-title" href="{root}index.html">Quiet<span class="dot">.</span>Notes</a>
    <nav class="site-nav">
      <a href="{root}index.html">Home</a>
      <a href="{root}about.html">About</a>
    </nav>
  </div>
</header>
"""

FOOTER = """<footer class="site-footer">
  <div class="wrap">
    &copy; 2026 Quiet Notes. Written slowly, published simply.
  </div>
</footer>
</body>
</html>
"""


def render_index():
    cards = []
    for p in POSTS:
        cards.append(f"""      <a class="panel" href="posts/{p['slug']}.html">
        <div class="meta">
          <span class="tag">{p['tag']}</span>
          <span>{p['date']}</span>
        </div>
        <h2>{p['title']}</h2>
        <p>{p['excerpt']}</p>
        <span class="read-more">Read more <span class="arrow">&rarr;</span></span>
      </a>""")

    html = HEAD.format(
        title=f"{SITE_TITLE} &mdash; a simple blog",
        description=SITE_TAGLINE,
        css_path="",
    )
    html += HEADER.format(root="")
    html += f"""  <main>
    <section class="hero wrap">
      <h1>Small notes on living a little slower.</h1>
      <p>{SITE_TAGLINE}</p>
    </section>
    <section class="panel-grid wrap">
{chr(10).join(cards)}
    </section>
  </main>
"""
    html += FOOTER
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(html)


def render_about():
    html = HEAD.format(
        title=f"About &mdash; {SITE_TITLE}",
        description="A little about Quiet Notes.",
        css_path="",
    )
    html += HEADER.format(root="")
    html += """  <main class="page-content wrap">
    <h1>About</h1>
    <div class="article-content">
      <p>Quiet Notes is a small, simple blog about slowing down: fewer notifications, plainer routines, and paying closer attention to ordinary things. Nothing here is trying to sell you a system.</p>
      <p>Posts go up whenever there's something worth saying, not on a schedule. Thanks for reading.</p>
    </div>
  </main>
"""
    html += FOOTER
    with open(os.path.join(ROOT, "about.html"), "w") as f:
        f.write(html)


def render_post(p):
    paragraphs = "\n".join(
        f"        <p>{para}</p>" if not para.startswith("&ldquo;")
        else f"        <blockquote>{para}</blockquote>"
        for para in p["content"]
    )
    html = HEAD.format(
        title=f"{p['title']} &mdash; {SITE_TITLE}",
        description=p["excerpt"],
        css_path="../",
    )
    html += HEADER.format(root="../")
    html += f"""  <main class="article wrap">
    <a class="back-link" href="../index.html">&larr; Back to all notes</a>
    <div class="meta">
      <span class="tag">{p['tag']}</span>
      <span>{p['date']}</span>
    </div>
    <h1>{p['title']}</h1>
    <div class="article-content">
{paragraphs}
    </div>
  </main>
"""
    html += FOOTER
    with open(os.path.join(ROOT, "posts", f"{p['slug']}.html"), "w") as f:
        f.write(html)


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "posts"), exist_ok=True)
    render_index()
    render_about()
    for p in POSTS:
        render_post(p)
    print(f"Generated index.html, about.html, and {len(POSTS)} post pages.")
