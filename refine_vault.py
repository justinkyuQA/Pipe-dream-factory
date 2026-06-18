import os

SOURCE = "vault/AI"
DEST = "vault_refined/AI"

os.makedirs(DEST, exist_ok=True)

GROUPS = {
    "bug_types": [
        "logical_bugs",
        "semantic_bugs",
        "structural_bugs",
        "memory_bugs",
        "behavioral_bugs",
        "factual_bugs"
    ],

    "drift_and_failure_modes": [
        "drift",
        "version_drift",
        "degradation",
        "collapse",
        "overcorrection",
        "policy_misfires"
    ],

    "exploratory_testing": [
        "heuristic",
        "observation",
        "exploration",
        "multiturn",
        "stress"
    ]
}

for output_name, keywords in GROUPS.items():

    merged = []

    for filename in os.listdir(SOURCE):

        if not filename.endswith(".md"):
            continue

        lower = filename.lower()

        if any(
            keyword in lower
            for keyword in keywords
        ):

            path = os.path.join(
                SOURCE,
                filename
            )

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                merged.append(
                    f"\n\n# {filename}\n\n"
                )

                merged.append(
                    f.read()
                )

    if merged:

        outfile = os.path.join(
            DEST,
            output_name + ".md"
        )

        with open(
            outfile,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                "\n".join(merged)
            )

        print(
            "Created:",
            outfile
        )

print("Done.")
