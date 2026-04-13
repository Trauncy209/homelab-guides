---
layout: default
title: Homelab Guides
---

<p class="eyebrow">Homelab notes</p>
<h1>Homelab Guides</h1>
<p class="muted">Short, practical notes for people who want their home server to do something useful without turning into a full-time hobby.</p>

<div class="stack">
  <section class="card">
    <h2 class="section-title">Start here</h2>
    <ul class="clean">
      {% for post in site.posts limit:2 %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <div class="muted">{{ post.date | date: "%b %d, %Y" }}</div>
      </li>
      {% endfor %}
    </ul>
  </section>

  <section class="card">
    <h2 class="section-title">What this site is for</h2>
    <p>One quiet server, one useful service, and a few notes that save you time later.</p>
  </section>

  <section class="card">
    <h2 class="section-title">Recent posts</h2>
    <ul class="clean">
      {% for post in site.posts limit:5 %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <div class="muted">{{ post.date | date: "%b %d, %Y" }}</div>
      </li>
      {% endfor %}
    </ul>
  </section>
</div>
