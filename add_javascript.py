#!/usr/bin/env python3
import os
import re

# JavaScript dari index.html
javascript_code = '''  <script>
    // ── Mobile menu ──────────────────────────────────────────
    var mobiToggle = document.getElementById('mobiToggle');
    var mobiClose  = document.getElementById('mobiClose');
    var mobiPanel  = document.getElementById('SiteHeaderMobilePanel');

    if (mobiToggle && mobiPanel) {
      mobiToggle.addEventListener('click', function () {
        mobiPanel.classList.add('open');
        mobiToggle.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden';
      });
    }

    if (mobiClose && mobiPanel) {
      mobiClose.addEventListener('click', function () {
        mobiPanel.classList.remove('open');
        mobiToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    }

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mobiPanel && mobiPanel.classList.contains('open')) {
        mobiPanel.classList.remove('open');
        if (mobiToggle) mobiToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });

    // ── Scroll reveal ────────────────────────────────────────
    var revealEls = document.querySelectorAll('.revealable');
    if (revealEls.length > 0 && 'IntersectionObserver' in window) {
      var observer  = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.08 });

      revealEls.forEach(function (el) { observer.observe(el); });
    }
  </script>'''

# List semua file HTML yang perlu diupdate
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

        # Cek apakah sudah ada mobile menu script
        if 'Mobile menu' in content and 'mobiToggle' in content:
            print(f"  ✓ {filename} sudah memiliki JavaScript")
            continue

        # Cari </body>
        body_end = content.rfind('</body>')
        if body_end == -1:
            print(f"  ❌ Tag </body> tidak ditemukan")
            continue

        # Sisipkan JavaScript sebelum </body>
        new_content = content[:body_end] + '\n' + javascript_code + '\n\n' + content[body_end:]

        # Simpan file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  ✅ {filename} JavaScript ditambahkan")

    except Exception as e:
        print(f"  ❌ Error: {str(e)}")

print("\n🎉 Selesai! JavaScript telah ditambahkan ke semua halaman")
