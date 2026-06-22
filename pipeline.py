import subprocess
import sys

steps = [
    "formatter.py",
    "book_generator.py",
    "export_pdf.py"
]

for step in steps:
    print(f"\n=== Running {step} ===")
    subprocess.run([sys.executable, step], check=True)

print("\nDone. Check exports/ and vault_books/")
