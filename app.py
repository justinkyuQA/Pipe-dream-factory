from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

RULES_DIR = "rules"
VAULT_DIR = "vault"


def load_rules():

    rules = {}

    for filename in os.listdir(RULES_DIR):

        if filename.endswith(".txt"):

            category = filename.replace(".txt", "")

            with open(
                os.path.join(RULES_DIR, filename),
                "r",
                encoding="utf-8"
            ) as f:

                rules[category] = [
                    line.strip().lower()
                    for line in f
                    if line.strip()
                ]

    return rules


def make_filename(text):

    first_line = text.split("\n")[0]

    title = (
        first_line.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "")
        .replace(".", "")
    )

    title = "".join(
        c for c in title
        if c.isalnum() or c == "_"
    )

    title = title[:60]

    if not title:
        title = "untitled"

    return title + ".md"


@app.route("/")
def index():

    recent = []

    for root, dirs, files in os.walk(VAULT_DIR):

        for file in files:

            if file.endswith(".md"):

                recent.append(
                    os.path.join(root, file)
                )

    recent = sorted(
        recent,
        key=os.path.getmtime,
        reverse=True
    )[:20]

    return render_template(
        "index.html",
        recent=recent
    )


@app.route("/vault")
def vault():

    vault_data = {}

    for category in os.listdir(VAULT_DIR):

        path = os.path.join(
            VAULT_DIR,
            category
        )

        if os.path.isdir(path):

            vault_data[category] = sorted(
                [
                    f
                    for f in os.listdir(path)
                    if f.endswith(".md")
                ]
            )

    return render_template(
        "vault.html",
        vault=vault_data
    )


@app.route("/note/<category>/<filename>")
def note(category, filename):

    filepath = os.path.join(
        VAULT_DIR,
        category,
        filename
    )

    try:

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()

    except:

        content = "File not found."

    return render_template(
        "note.html",
        filename=filename,
        content=content
    )


@app.route("/process", methods=["POST"])
def process_text():

    raw_text = request.json.get(
        "text",
        ""
    )

    chunks = [
        chunk.strip()
        for chunk in raw_text.split("---")
        if chunk.strip()
    ]

    rules = load_rules()

    saved_files = []

    for text in chunks:

        text_lower = text.lower()

        scores = {}

        for category, keywords in rules.items():

            score = 0

            for keyword in keywords:

                if keyword in text_lower:
                    score += 1

            scores[category] = score

        top_category = max(
            scores,
            key=scores.get
        )

        if scores[top_category] == 0:
            top_category = "unsorted"

        folder_map = {
            "ai":"AI",
            "cybersecurity":"Cybersecurity",
            "linux":"Linux",
            "cloud":"Cloud",
            "business":"Business",
            "projects":"Projects",
            "writing":"Writing",
            "philosophy":"Philosophy",
            "unsorted":"Unsorted"
        }

        category_folder = folder_map[
            top_category
        ]

        os.makedirs(
            f"vault/{category_folder}",
            exist_ok=True
        )

        filename = make_filename(text)

        filepath = (
            f"vault/{category_folder}/"
            f"{filename}"
        )

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                f"# {top_category.title()} Note\n\n"
            )

            f.write(text)

        saved_files.append(filepath)

    return jsonify({
        "saved_files": saved_files,
        "count": len(saved_files)
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
