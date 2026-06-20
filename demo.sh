#!/data/data/com.termux/files/usr/bin/bash

clear

echo ""
echo "=================================="
echo "PIPE DREAM FACTORY DEMO"
echo "=================================="
echo ""

sleep 2

echo "Vault Statistics"
echo "----------------"
find vault -type f | wc -l

du -sh vault

sleep 3

echo ""
echo "Sample Vault Contents"
echo "---------------------"
find vault | head -20

sleep 5

echo ""
echo "Running Pipeline..."
echo "-------------------"

sleep 2

python pipeline.py

sleep 3

echo ""
echo "Generated Books"
echo "---------------"

ls vault_books

sleep 3

echo ""
echo "Book Preview"
echo "------------"

head -40 vault_books/AI_Testing_Handbook.md

echo ""
echo "=================================="
echo "DEMO COMPLETE"
echo "=================================="

