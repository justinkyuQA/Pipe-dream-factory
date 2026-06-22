import re
from pathlib import Path

def clean_markdown(text):
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"(?m)^(#{1,6})([^\s#])", r"\1 \2", text)
    text = re.sub(r"(?m)^[\*\+]\s+", "- ", text)
    return text.strip() + "\n"

if __name__ == "__main__":
    folder = Path("vault_chapters")
    for path in folder.rglob("*.md"):
        path.write_text(clean_markdown(path.read_text()), encoding="utf-8")
    print("Formatted chapters.")
