#!/bin/bash

# Script untuk menambahkan custom CSS dan JS ke semua halaman HTML

# Fungsi untuk menambahkan script di akhir file
add_scripts() {
    local file=$1
    local js_file=$2

    # Cek apakah sudah ada custom scripts
    if grep -q "<!-- Custom Scripts -->" "$file"; then
        echo "✓ $file sudah memiliki custom scripts"
    else
        # Backup file asli
        cp "$file" "${file}.backup"

        # Hapus tag penutup
        sed -i 's|</body></html>||g' "$file"

        # Tambahkan custom scripts dan tag penutup
        cat >> "$file" << EOF
    <!-- Custom Scripts -->
    <script src="../assets/js/global.js"></script>
    <script src="../assets/js/${js_file}"></script>
</body></html>
EOF
        echo "✓ Updated $file"
    fi
}

# Update our-story.html
FILE="/tmp/cc-agent/63900732/project/our-story.html"
if [ -f "$FILE" ]; then
    add_scripts "$FILE" "about.js"
fi

# Update menus.html
FILE="/tmp/cc-agent/63900732/project/menus.html"
if [ -f "$FILE" ]; then
    add_scripts "$FILE" "menu.js"
fi

# Update reservations.html
FILE="/tmp/cc-agent/63900732/project/reservations.html"
if [ -f "$FILE" ]; then
    add_scripts "$FILE" "home.js"
fi

# Update sustainability.html
FILE="/tmp/cc-agent/63900732/project/sustainability.html"
if [ -f "$FILE" ]; then
    add_scripts "$FILE" "about.js"
fi

# Update store.html
FILE="/tmp/cc-agent/63900732/project/store.html"
if [ -f "$FILE" ]; then
    add_scripts "$FILE" "menu.js"
fi

echo ""
echo "✅ Semua file telah diupdate!"
echo ""
echo "File yang diupdate:"
echo "- index.html"
echo "- contact.html"
echo "- menus.html"
echo "- our-story.html"
echo "- reservations.html"
echo "- sustainability.html"
echo "- store.html"
