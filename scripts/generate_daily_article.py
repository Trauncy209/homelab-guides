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

openers = [
    'The easiest way to make a homelab useful is to give it one job that matters.',
    'If the server is noisy, overcomplicated, or hard to trust, you will stop using it.',
    'I like homelabs that quietly replace something annoying in daily life.'
]
core = [
    ('One useful service', 'Pick one thing you will actually use this week: DNS filtering, file sync, backups, or a simple dashboard.'),
    ('Keep recovery easy', 'Snapshots and backups matter more than fancy hardware. If something breaks, you want the fix to be boring.'),
    ('Don\'t overbuild', 'A small machine that stays on beats a big machine that becomes a project.')
]
lead = random.choice(openers)
first, second, third = random.sample(core, 3)
content = f'''---
layout: post
title: "{keyword.title()}"
date: {today} 09:00:00 -0400
---

{lead}

## {first[0]}
{first[1]}

## {second[0]}
{second[1]}

## {third[0]}
{third[1]}

What I would do first: install a stable base, keep the network simple, and add one service that saves time instead of just looking clever.
'''
post.write_text(content, encoding='utf-8')
print(post)
