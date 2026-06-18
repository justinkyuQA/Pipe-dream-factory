#!/data/data/com.termux/files/usr/bin/bash

echo "Installing Pipe Dream Factory..."

cd "$(dirname "$0")" || exit 1

mkdir -p vault vault_refined vault_chapters vault_books examples ~/bin

if command -v pip >/dev/null 2>&1; then
    pip install -r requirements.txt
fi

if [ -z "$(find vault -type f 2>/dev/null)" ]; then
    cp examples/sample_note.md vault/
fi

cat > ~/bin/pdf <<'EOC'
#!/data/data/com.termux/files/usr/bin/bash
cd ~/projects/pipe-dreams || exit 1
python pipeline.py
EOC

chmod +x ~/bin/pdf

grep -q 'export PATH="$HOME/bin:$PATH"' ~/.bashrc || echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc

echo "Pipe Dream Factory installed."
echo "Run: source ~/.bashrc && pdf"
