#!/usr/bin/env python3
import os
import re

# Baca index.html sebagai template
with open('/tmp/cc-agent/63900732/project/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract header (dari <header> sampai </header>)
header_start = index_html.find('<header class="site-header">')
header_end = index_html.find('</header>') + len('</header>')
header_html = index_html[header_start:header_end]

# Extract footer (dari <footer> sampai </footer>)
footer_start = index_html.find('<footer>')
footer_end = index_html.find('</footer>') + len('</footer>')
footer_html = index_html[footer_start:footer_end]

# Extract head section (fonts dan style)
head_start = index_html.find('  <!-- Fonts -->')
head_end = index_html.find('</head>')
head_section = index_html[head_start:head_end].strip()

print("✓ Template extracted from index.html")
print(f"  Header: {len(header_html)} chars")
print(f"  Footer: {len(footer_html)} chars")
print(f"  Head: {len(head_section)} chars\n")

# Pages to update dengan content placeholder
pages_content = {
    'contact.html': '''
      <section class="c-one-col--text revealable">
        <h2>Get in touch with us</h2>
      </section>

      <section class="c-tout-overlay c-tout-overlay--dimmed revealable"
               style="background-image:url('https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg?auto=compress&cs=tinysrgb&w=1200');">
        <div class="container">
          <h2 class="h1">Contact Us</h2>
          <p>Visit us at 358 East Main St., Ashland, OR 97520 or call (541) 488-5493</p>
          <a href="mailto:info@pieandvine.co" class="btn btn-brand-alt">Email Us</a>
        </div>
      </section>
''',
    'menus.html': '''
      <section class="c-one-col--text revealable">
        <h2>Influenced by regional traditions of Italy and the flavors of the West Coast</h2>
      </section>

      <section class="c-tout-overlay c-tout-overlay--dimmed revealable"
               style="background-image:url('https://images.pexels.com/photos/1907228/pexels-photo-1907228.jpeg?auto=compress&cs=tinysrgb&w=1200');">
        <div class="container">
          <h2 class="h1">Our Menus</h2>
          <p>Fresh pasta, wood-fired pizza, and authentic Italian cuisine</p>
          <a href="#" class="btn btn-brand-alt">View Full Menu</a>
        </div>
      </section>
''',
    'our-story.html': '''
      <section class="c-split revealable">
        <div class="c-split__col c-split__col--dimmed">
          <div class="c-split__col-inner">
            <div class="c-split__image"
                 style="background-image:url('https://images.pexels.com/photos/1435904/pexels-photo-1435904.jpeg?auto=compress&cs=tinysrgb&w=1200');"></div>
            <div class="c-split__content">
              <img src="accounts/f8db619de6ceee5540be4875cb5cfe3f/media/images/Vine_Yard-Logo_w-1000-fit-max-auto-compress-format-h-1000.png"
                   alt="Vine + Yard Logo" style="width:240px;"
                   onerror="this.outerHTML='<p style=\\'font-family:Playfair Display,serif;font-size:2.2rem;color:#fff;font-style:italic;\\'>Vine + Yard</p>'">
              <a href="#" class="btn btn-brand-alt">Our Story</a>
            </div>
          </div>
        </div>

        <div class="c-split__col c-split__col--dimmed">
          <div class="c-split__col-inner">
            <div class="c-split__image"
                 style="background-image:url('https://images.pexels.com/photos/1260968/pexels-photo-1260968.jpeg?auto=compress&cs=tinysrgb&w=1200');"></div>
            <div class="c-split__content">
              <img src="accounts/f8db619de6ceee5540be4875cb5cfe3f/media/images/PieVine-Logo1_w-1000-fit-max-auto-compress-format-h-1000.png"
                   alt="Pie + Vine Logo" style="width:240px;"
                   onerror="this.outerHTML='<p style=\\'font-family:Playfair Display,serif;font-size:2.2rem;color:#fff;font-style:italic;\\'>Pie + Vine</p>'">
              <a href="#" class="btn btn-brand-alt">Our Restaurant</a>
            </div>
          </div>
        </div>
      </section>

      <section class="c-one-col--text revealable">
        <h2>We are passionate about all things food!</h2>
      </section>
''',
    'sustainability.html': '''
      <section class="c-one-col--text revealable">
        <h2>Committed to sustainability and local sourcing</h2>
      </section>

      <section class="c-tout-overlay c-tout-overlay--dimmed revealable"
               style="background-image:url('https://images.pexels.com/photos/1435904/pexels-photo-1435904.jpeg?auto=compress&cs=tinysrgb&w=1200');">
        <div class="container">
          <h2 class="h1">Sustainability</h2>
          <p>We believe in sustainable practices and supporting local farmers</p>
          <a href="our-story/" class="btn btn-brand-alt">Learn More</a>
        </div>
      </section>
''',
    'store.html': '''
      <section class="c-split revealable">
        <div class="c-split__col c-split__col--dimmed">
          <div class="c-split__col-inner">
            <div class="c-split__image"
                 style="background-image:url('https://images.pexels.com/photos/1169084/pexels-photo-1169084.jpeg?auto=compress&cs=tinysrgb&w=1200');"></div>
            <div class="c-split__content">
              <h2 style="font-family:var(--font-display);font-size:2.5rem;color:#fff;font-style:italic;">Our Wines</h2>
              <a href="#" class="btn btn-brand-alt">Shop Now</a>
            </div>
          </div>
        </div>

        <div class="c-split__col c-split__col--dimmed">
          <div class="c-split__col-inner">
            <div class="c-split__image"
                 style="background-image:url('https://images.pexels.com/photos/34426/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=1200');"></div>
            <div class="c-split__content">
              <h2 style="font-family:var(--font-display);font-size:2.5rem;color:#fff;font-style:italic;">Vineyard</h2>
              <a href="our-story/" class="btn btn-brand-alt">Our Story</a>
            </div>
          </div>
        </div>
      </section>
''',
    'press-listing.html': '''
      <section class="c-one-col--text revealable">
        <h2>Press & Media</h2>
      </section>

      <section class="c-tout-overlay c-tout-overlay--dimmed revealable"
               style="background-image:url('https://images.pexels.com/photos/941861/pexels-photo-941861.jpeg?auto=compress&cs=tinysrgb&w=1200');">
        <div class="container">
          <h2 class="h1">In the News</h2>
          <p>See what people are saying about Pie + Vine</p>
          <a href="contact/" class="btn btn-brand-alt">Contact Press</a>
        </div>
      </section>
''',
}

# JavaScript dari index.html
javascript = '''  <script>
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

base_path = '/tmp/cc-agent/63900732/project/'

for filename, content_html in pages_content.items():
    filepath = os.path.join(base_path, filename)

    if not os.path.exists(filepath):
        print(f"⚠️  {filename} tidak ditemukan")
        continue

    print(f"🔧 Rebuilding {filename}...")

    # Get title dari filename
    page_titles = {
        'contact.html': 'Contact | Pie + Vine & Vine + Yard',
        'menus.html': 'Menus | Pie + Vine & Vine + Yard',
        'our-story.html': 'Our Story | Pie + Vine & Vine + Yard',
        'sustainability.html': 'Sustainability | Pie + Vine & Vine + Yard',
        'store.html': 'Our Wines | Pie + Vine & Vine + Yard',
        'press-listing.html': 'Press | Pie + Vine & Vine + Yard',
    }

    # Build complete HTML
    new_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>{page_titles.get(filename, 'Pie + Vine & Vine + Yard')}</title>
  <link rel="canonical" href="https://www.pieandvine.co/{filename.replace('.html', '')}/" />
  <meta name="description" content="Main Street patio & bright dining room specializing in Italian pastas & pizza.">

{head_section}
</head>

<body>

  <a href="#main-content" class="skip">Skip to main content</a>
  <div class="site-notifications"></div>

{header_html}

  <!-- ===== MAIN CONTENT ===== -->
  <div class="site-content">
    <main id="main-content">
{content_html}
    </main>

    <!-- MOBILE STICKY FOOTER -->
    <aside class="mobi-footer mobi-footer--sticky">
      <ul class="mobi-footer__list">
        <li class="mobi-footer__item">
          <a href="tel:541-488-5493" class="btn btn-brand btn-block">Call Us</a>
        </li>
        <li class="mobi-footer__item">
          <a href="../order-now/" class="btn btn-brand btn-block">Order Now</a>
        </li>
        <li class="mobi-footer__item">
          <a href="mailto:info@pieandvine.co" class="btn btn-brand btn-block">Email Us</a>
        </li>
      </ul>
    </aside>
  </div>

{footer_html}

{javascript}

</body>
</html>'''

    # Save file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"  ✅ {filename} - REBUILT dengan struktur index.html")

print("\n🎉 SELESAI! Semua halaman telah di-rebuild dengan struktur yang sama seperti index.html")
print("Navbar, konten, dan footer sekarang rapi di semua halaman!")
