import json
from pathlib import Path

cfg = json.loads(Path("book_config.json").read_text())
title = cfg.get("title", "Generated Book")
subtitle = cfg.get("subtitle", "")
author = cfg.get("author", "Justin Kyu")

Path("vault_books").mkdir(exist_ok=True)

chapters = sorted(Path("vault_chapters").rglob("*.md"))
out = Path("vault_books") / f"{title.replace(' ', '_')}.md"

parts = [
    f"# {title}",
    f"## {subtitle}",
    f"**Author:** {author}",
    "",
    "# Table of Contents",
    ""
]

for i, ch in enumerate(chapters, 1):
    parts.append(f"{i}. {ch.stem.replace('_', ' ').title()}")

parts.append("\n---\n")

for i, ch in enumerate(chapters, 1):
    text = ch.read_text(encoding="utf-8").strip()
    if not text.startswith("#"):
        text = f"# Chapter {i}: {ch.stem.replace('_', ' ').title()}\n\n{text}"
    parts.append(text)
    parts.append("\n\\pagebreak\n")

out.write_text("\n".join(parts), encoding="utf-8")
print(f"Book generated: {out}")
