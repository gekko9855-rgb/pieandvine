#!/usr/bin/env python3
import os
import re

# Baca style dan head section dari index.html
with open('/tmp/cc-agent/63900732/project/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract style dari index.html (baris 10-436)
style_start = index_content.find('  <!-- Fonts -->')
style_end = index_content.find('</head>')
style_block = index_content[style_start:style_end].strip()

print("✓ Style extracted from index.html")
print(f"  Length: {len(style_block)} characters\n")

# List semua file HTML yang perlu diupdate (exclude index.html dan file new)
html_files = [
    'contact.html',
    'menus.html',
    'our-story.html',
    'sustainability.html',
    'store.html',
    'press-listing.html',
]

base_path = '/tmp/cc-agent/63900732/project/'

for filename in html_files:
    filepath = os.path.join(base_path, filename)

    if not os.path.exists(filepath):
        print(f"⚠️  {filename} tidak ditemukan")
        continue

    print(f"📝 Processing {filename}...")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Cari tag </head>
        head_end = content.find('</head>')
        if head_end == -1:
            print(f"  ❌ Tag </head> tidak ditemukan")
            continue

        # Cari tag <head> start
        head_start = content.find('<head>')
        if head_start == -1:
            head_start = content.find('<head ') # Jika ada atribut

        if head_start == -1:
            print(f"  ❌ Tag <head> tidak ditemukan")
            continue

        # Ambil bagian sebelum </head>
        before_head_close = content[:head_end]
        after_head_close = content[head_end:]

        # Hapus custom styles/scripts yang sudah ada
        # Cari dan hapus <!-- Custom Styles --> sampai tag berikutnya
        before_head_close = re.sub(
            r'<!-- Custom Styles -->.*?(?=<script|</head>|$)',
            '',
            before_head_close,
            flags=re.DOTALL
        )

        # Hapus link ke assets/css/global.css dll
        before_head_close = re.sub(
            r'<link rel="stylesheet" href="\.\.\/assets\/css\/[^"]+\.css">\s*',
            '',
            before_head_close
        )
        before_head_close = re.sub(
            r'<link rel="stylesheet" href="assets\/css\/[^"]+\.css">\s*',
            '',
            before_head_close
        )

        # Tambahkan style baru sebelum </head>
        new_content = before_head_close.rstrip() + '\n\n' + style_block + '\n' + after_head_close

        # Hapus custom scripts di akhir body (jika ada)
        new_content = re.sub(
            r'<!-- Custom Scripts -->.*?</body>',
            '</body>',
            new_content,
            flags=re.DOTALL
        )

        # Simpan file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  ✅ {filename} berhasil diupdate")

    except Exception as e:
        print(f"  ❌ Error: {str(e)}")

print("\n🎉 Selesai! Semua halaman telah diupdate dengan style dari index.html")
