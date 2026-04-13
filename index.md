---
layout: default
title: TECH NEWS
---

<section class="hero">
  <p class="eyebrow">Daily tech briefing</p>
  <h1>TECH NEWS</h1>
  <p class="muted">Practical daily coverage of the trends people actually buy, deploy, and argue about: local AI, privacy, homelabs, infrastructure, and the hardware that keeps it all moving.</p>
  <div>
    <a class="btn" href="{{ '/thanks/' | relative_url }}">Support the site</a>
    <a class="btn" style="margin-left:10px" href="{{ '/donations/' | relative_url }}">Monero donations</a>
  </div>
</section>

<div class="split" style="margin-top:20px;">
  <section class="card highlight">
    <span class="tag">Trending</span><span class="tag">AI</span><span class="tag">Hardware</span>
    <h2>Latest posts</h2>
    <ul class="clean">
      {% for post in site.posts limit:5 %}
      <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a><div class="muted">{{ post.date | date: "%b %d, %Y" }}</div></li>
      {% endfor %}
    </ul>
  </section>
  <section class="card">
    <h2>Why this site exists</h2>
    <p>News is useful when it helps you decide what to do next. Each post ends with the practical angle: what changed, why it matters, and what is worth watching tomorrow.</p>
    <p class="muted">If you like the coverage, the donation page has a Monero address and a simple thank-you page for supporters.</p>
  </section>
</div>
