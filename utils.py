import os

def unique_filename(folder, filename):

    base = filename.replace(".md", "")
    candidate = filename

    count = 2

    while os.path.exists(
        os.path.join(folder, candidate)
    ):

        candidate = (
            f"{base}_{count}.md"
        )

        count += 1

    return candidate


def vault_stats(vault):

    stats = {}

    total = 0

    for category in os.listdir(vault):

        path = os.path.join(
            vault,
            category
        )

        if os.path.isdir(path):

            count = len(
                [
                    f
                    for f in os.listdir(path)
                    if f.endswith(".md")
                ]
            )

            stats[category] = count

            total += count

    return stats, total
