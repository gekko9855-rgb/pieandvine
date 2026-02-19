#!/usr/bin/env python3
import os

files = {
    'menus.html': 'menu.js',
    'reservations.html': 'home.js',
    'jobs.html': 'home.js',
    'order-now.html': 'home.js',
}

base_path = '/tmp/cc-agent/63900732/project/'

for filename, js_file in files.items():
    filepath = os.path.join(base_path, filename)

    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!-- Custom Scripts -->' in content:
        print(f"✓ {filename} sudah ada custom scripts")
        continue

    # Tambahkan JS sebelum </body></html>
    if '</body></html>' in content:
        js_insert = f'''    <!-- Custom Scripts -->
    <script src="../assets/js/global.js"></script>
    <script src="../assets/js/{js_file}"></script>
</body></html>'''

        content = content.replace('</body></html>', js_insert)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ {filename} JS added")

print("\n✅ Selesai!")
