from pathlib import Path
import datetime as dt
import json
import random

base = Path(__file__).resolve().parents[1]
keywords = [line.strip() for line in (base / 'content' / 'keywords.txt').read_text(encoding='utf-8').splitlines() if line.strip()]
if not keywords:
    raise SystemExit('No keywords found')
keyword = keywords[dt.date.today().toordinal() % len(keywords)]
today = dt.date.today().isoformat()
slug = keyword.lower().replace(' ', '-').replace('/', '-')[:80]
post = base / '_posts' / f'{today}-{slug}.md'
research_file = base / 'research' / 'daily-headlines.json'
research = json.loads(research_file.read_text(encoding='utf-8')) if research_file.exists() else {}
headlines = research.get('feeds', {}).get('tech_news', [])[:5]
if post.exists():
    print(f'already exists: {post.name}')
    raise SystemExit(0)
lead = random.choice([
    'This week in tech feels less like a product parade and more like a systems story: AI, capital, energy, education, and trust all keep colliding.',
    'Useful tech coverage should explain what the announcement means for the next decision, not just repeat the headline.',
    'The real story is not the press release. It is the second-order effect: who has to change plans because of it.'
])
body = [
    '---',
    'layout: post',
    f'title: "{keyword.title()}"',
    f'date: {today} 09:00:00 -0400',
    '---',
    '',
    lead,
    '',
    '## Research snapshot',
    'Today\'s feed check pulled these recent headlines into view:',
]
for headline in headlines:
    body.append(f'- {headline}')
body += [
    '',
    '## What changed',
    'The pattern across the day\'s headlines is simple: AI is no longer a side topic, energy and infrastructure are now part of the tech conversation, and companies are being judged less on novelty than on whether their systems can survive real-world use. That shift matters because it changes how people buy, build, and plan.',
    '',
    '## Why it matters',
    'When a funding round, a product launch, or a policy argument shows up, the obvious takeaway is usually too shallow. The deeper takeaway is whether the new move lowers friction for ordinary users or just creates a nicer demo. For example, AI tools that are useful inside a company are usually not the flashiest ones; they are the ones that reduce repetitive work, surface information quickly, and do not require a new workflow every week.',
    '',
    '## Education and AI',
    'The education angle keeps coming back because classrooms expose all the weak points in a technology. If a model is unreliable, students can spot it. If a policy is unclear, teachers feel it immediately. If the interface is confusing, everyone loses time. That is why ChatGPT and similar tools keep generating tension: they are genuinely useful, but they also force institutions to decide what skill they are actually trying to teach. Memorization, reasoning, editing, and judgment are not the same thing, and AI makes that distinction harder to ignore.',
    '',
    '## Capital, hardware, and execution',
    'Funding stories are only interesting when they translate into concrete execution. A company can raise a huge round and still fail if it cannot ship, scale, or support the product. That is why hardware and infrastructure matter more than they used to. If the stack cannot handle more usage, the narrative falls apart. So when a startup gets money or a platform gets a new AI feature, the real question is whether the underlying systems—compute, storage, model routing, and support—can carry the load.',
    '',
    '## Trust is becoming the product',
    'The more capable the tools become, the more people care about reliability and honesty. An AI model that is confident but wrong is not a premium feature; it is a liability. A platform that changes rules without explanation does not gain loyalty just because the feature list is long. This is why product quality increasingly means predictable behavior, clear limitations, and fewer surprises.',
    '',
    '## What to watch next',
    'Over the next few weeks, I would watch for three signals. First, whether AI tools move closer to daily workflows instead of one-off demos. Second, whether energy and infrastructure constraints start shaping the next wave of products. Third, whether education, business, and consumer software teams get more serious about transparency and practical utility. Those are the things that separate a temporary headline from a real trend.',
    '',
    '### Sources used today',
]
for headline in headlines:
    body.append(f'- {headline}')
body += [
    '',
    'If you want the shortest possible summary: the tech market is rewarding systems that are useful, durable, and understandable, not just loud.',
]
post.write_text("\n".join(body) + "\n", encoding='utf-8')
print(post)
