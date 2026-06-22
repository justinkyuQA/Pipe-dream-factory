import subprocess

steps = [
    "refine_vault.py",
    "chapter_builder.py",
    "book_assembler.py"
]

for step in steps:
    print(f"\n=== Running {step} ===\n")

    result = subprocess.run(["python", step])

    if result.returncode != 0:
        print(f"FAILED: {step}")
        raise SystemExit(1)

print("\n=================================")
print(" Pipe Dream Factory Complete ")
print("=================================")
print("Check vault_books for output.")

