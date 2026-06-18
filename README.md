# Pipe Dream Factory (PDF)

## A Local-First Knowledge Refinery

Pipe Dream Factory transforms raw notes, research, ideas, transcripts, and documents into structured chapters and assembled books through an automated publishing pipeline.

Instead of storing information and forgetting it, Pipe Dream Factory continuously organizes knowledge into reusable assets.

---

## How It Works

Input:

vault/
- Notes
- Research
- Ideas
- Drafts
- Documents

Pipeline:

Vault
↓
Refinement
↓
Chapter Building
↓
Book Assembly
↓
Knowledge Assets

Output:

vault_books/
- Books
- Handbooks
- Documentation
- Knowledge Libraries

---

## Philosophy

Most note-taking systems focus on collection.

Pipe Dream Factory focuses on transformation.

Ideas become chapters.

Chapters become books.

Books become knowledge assets.

---

## Installation

Clone the repository:

git clone https://github.com/justinkyuQA/pipe-dream-factory.git

Enter the project directory:

cd pipe-dream-factory

Run the installer:

bash install.sh

---

## Usage

Run the complete publishing pipeline:

pdf

Or directly:

python pipeline.py

---

## Repository Structure

README.md

install.sh

pipeline.py

refine_vault.py

chapter_builder.py

book_assembler.py

app.py

utils.py

rules/

templates/

examples/

---

## Current Pipeline

refine_vault.py
    ↓
chapter_builder.py
    ↓
book_assembler.py

---

## Design Goals

- Local-first
- Human-readable files
- Minimal dependencies
- Automated organization
- Personal publishing workflows
- Knowledge preservation
- Reproducible outputs

---

## Example Workflow

1. Add notes to the vault.

2. Run:

pdf

3. Review generated output in:

vault_books/

---

## Status

Prototype v0.1

Current focus:

- Pipeline stability
- Book generation
- Installation experience
- Documentation
- PDF export support

---

## Pipe Dream Factory

PDF means:

- Pipe Dream Factory
- Portable Document Format
- Publish, Distill, Forge

The goal is simple:

Turn information into assets.
