from pathlib import Path
import datetime as dt
import random

base = Path(__file__).resolve().parents[1]
keywords = [line.strip() for line in (base / 'content' / 'keywords.txt').read_text(encoding='utf-8').splitlines() if line.strip()]
if not keywords:
    raise SystemExit('No keywords found')
keyword = keywords[dt.date.today().toordinal() % len(keywords)]
today = dt.date.today().isoformat()
slug = keyword.lower().replace(' ', '-').replace('/', '-')[:80]
post = base / '_posts' / f'{today}-{slug}.md'
if post.exists():
    print(f'already exists: {post.name}')
    raise SystemExit(0)
sections = [
    ('What changed', 'The big shift is not just the headline. It is the part of the market or stack that becomes hard to ignore.'),
    ('Why it matters', 'The practical effect is usually on cost, complexity, or what people choose to buy next.'),
    ('What to watch', 'The next few weeks usually reveal whether the trend is noise or something durable.'),
]
lead = random.choice([
    'This is the kind of tech story that starts as a niche conversation and then quietly becomes a default assumption.',
    'Useful tech coverage should explain the tradeoff, not just repeat the announcement.',
    'The real story is often the follow-on effect: what people will change after the headline fades.'
])
body = [f'---', 'layout: post', f'title: "{keyword.title()}"', f'date: {today} 09:00:00 -0400', '---', '', lead, '']
for heading, text in sections:
    body.append(f'## {heading}')
    body.append(text)
    body.append('')
body.append('The summary I would give a busy reader: pay attention to the part that affects cost, reliability, or workflow, and ignore the rest until it proves useful.')
post.write_text("\n".join(body) + "\n", encoding='utf-8')
print(post)
