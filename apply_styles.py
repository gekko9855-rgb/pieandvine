#!/usr/bin/env python3
import re
import os

# Definisi halaman dan JS yang sesuai
pages = {
    'reservations.html': 'home.js',
    'sustainability.html': 'about.js',
    'store.html': 'menu.js',
    'jobs.html': 'home.js',
    'order-now.html': 'home.js',
    'press-listing.html': 'about.js',
}

base_path = '/tmp/cc-agent/63900732/project/'

css_insert = '''	<!-- Custom Styles -->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
	<link rel="stylesheet" href="../assets/css/global.css">
	<link rel="stylesheet" href="../assets/css/mobile-menu.css">
	<link rel="stylesheet" href="../assets/css/{}.css">'''

js_insert = '''    <!-- Custom Scripts -->
    <script src="../assets/js/global.js"></script>
    <script src="../assets/js/{}"></script>'''

for filename, js_file in pages.items():
    filepath = os.path.join(base_path, filename)

    if not os.path.exists(filepath):
        print(f"❌ {filename} tidak ditemukan")
        continue

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Tentukan CSS file berdasarkan JS file
        if js_file == 'home.js':
            css_file = 'home'
        elif js_file == 'about.js':
            css_file = 'about'
        elif js_file == 'menu.js':
            css_file = 'menu'
        elif js_file == 'contact.js':
            css_file = 'contact'
        else:
            css_file = 'home'

        # Cek apakah sudah ada custom styles
        if '<!-- Custom Styles -->' in content:
            print(f"✓ {filename} sudah memiliki custom styles")
            continue

        # Tambahkan CSS setelah stylesheet utama
        css_pattern = r'(<link rel="stylesheet" href="\.\.\/stylesheet\/[^"]+\.scss"\/>\s*)'
        if re.search(css_pattern, content):
            content = re.sub(
                css_pattern,
                r'\1' + css_insert.format(css_file) + '\n',
                content,
                count=1
            )

        # Tambahkan JS sebelum </body></html>
        if '</body></html>' in content and '<!-- Custom Scripts -->' not in content:
            content = content.replace(
                '</body></html>',
                js_insert.format(js_file) + '\n</body></html>'
            )

        # Simpan file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ {filename} berhasil diupdate")

    except Exception as e:
        print(f"❌ Error processing {filename}: {str(e)}")

print("\n🎉 Selesai! Semua halaman telah diupdate dengan style baru.")
