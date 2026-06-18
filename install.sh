#!/usr/bin/env bash

echo "Installing Pipe Dream Factory..."

mkdir -p vault/AI
mkdir -p vault_refined/AI
mkdir -p vault_chapters
mkdir -p vault_books
mkdir -p ~/bin

if command -v pip3 >/dev/null 2>&1; then
    pip3 install -r requirements.txt
fi

if [ ! -f vault/AI/sample_note.md ]; then
    cp examples/sample_note.md vault/AI/
fi

cat > ~/bin/pdf <<'EOC'
#!/usr/bin/env bash
cd "$(dirname "$(realpath "$0")")" >/dev/null 2>&1
cd ~/projects/pipe-dreams || exit 1
python3 pipeline.py
EOC

chmod +x ~/bin/pdf

echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc 2>/dev/null

echo ""
echo "================================="
echo " Pipe Dream Factory Installed "
echo "================================="
echo ""
echo "Run:"
echo "  python3 pipeline.py"
echo ""
