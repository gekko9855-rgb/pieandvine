# Panduan Implementasi Style Baru

## Overview

Saya telah membuat sistem styling yang profesional dan terpisah untuk website Pie + Vine. File-file ini menggunakan arsitektur modern dengan CSS dan JavaScript yang dipisahkan per halaman.

## Struktur File

```
/project
├── assets/
│   ├── css/
│   │   ├── global.css      # CSS global untuk semua halaman
│   │   ├── home.css        # CSS khusus untuk homepage
│   │   ├── contact.css     # CSS khusus untuk halaman contact
│   │   ├── about.css       # CSS khusus untuk halaman about/our-story
│   │   └── menu.css        # CSS khusus untuk halaman menu
│   └── js/
│       ├── global.js       # JavaScript global
│       ├── home.js         # JavaScript untuk homepage
│       ├── contact.js      # JavaScript untuk contact page
│       ├── about.js        # JavaScript untuk about page
│       └── menu.js         # JavaScript untuk menu page
├── index-new.html          # Template baru untuk homepage
└── contact-new.html        # Template baru untuk contact page
```

## Fitur-Fitur Style Baru

### 1. **Design System yang Konsisten**
   - Warna yang harmonis (coklat, krem, dan aksen emas)
   - Typography hierarchy yang jelas
   - Spacing system 8px (xs, sm, md, lg, xl, xxl)
   - Border radius dan shadow yang konsisten

### 2. **Responsive Design**
   - Mobile-first approach
   - Breakpoint di 768px
   - Grid layout yang fleksibel
   - Navigation mobile yang smooth

### 3. **Animasi dan Interaksi**
   - Fade-in animations saat scroll
   - Hover effects pada buttons dan cards
   - Smooth scrolling
   - Loading screen
   - Lightbox untuk galeri

### 4. **Komponen yang Siap Pakai**
   - Hero sections dengan background overlay
   - Feature cards dengan icons
   - Gallery grid dengan overlay
   - Contact form dengan validasi
   - Testimonial cards
   - Call-to-action sections

## Cara Implementasi

### Opsi 1: Gunakan File Template Baru (RECOMMENDED)

1. Buka `index-new.html` dan `contact-new.html`
2. File ini sudah siap pakai dengan semua styling yang terpisah
3. Copy konten dari file lama ke template baru jika diperlukan
4. Gunakan file ini sebagai halaman utama

### Opsi 2: Integrasi ke File yang Ada

Tambahkan di `<head>` section setiap file HTML:

```html
<!-- Font -->
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;600;700&family=Muli:wght@200;300;400;600&display=swap" rel="stylesheet">

<!-- Font Awesome untuk icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- CSS Files -->
<link rel="stylesheet" href="assets/css/global.css">
<link rel="stylesheet" href="assets/css/home.css"> <!-- Sesuaikan dengan halaman -->
```

Tambahkan sebelum `</body>`:

```html
<!-- JavaScript Files -->
<script src="assets/js/global.js"></script>
<script src="assets/js/home.js"></script> <!-- Sesuaikan dengan halaman -->
```

## Komponen HTML yang Bisa Digunakan

### 1. Hero Section

```html
<section class="home-hero">
    <div class="home-hero__content">
        <h1 class="home-hero__title">Your Title</h1>
        <p class="home-hero__subtitle">Your Subtitle</p>
        <div class="home-hero__buttons">
            <a href="#" class="btn">Primary Button</a>
            <a href="#" class="btn btn-outline">Secondary Button</a>
        </div>
    </div>
</section>
```

### 2. Feature Cards

```html
<div class="features__grid">
    <div class="feature-card fade-in">
        <div class="feature-card__icon">
            <i class="fas fa-fire"></i>
        </div>
        <h3 class="feature-card__title">Feature Title</h3>
        <p class="feature-card__text">Feature description</p>
    </div>
</div>
```

### 3. Gallery Grid

```html
<div class="gallery-grid">
    <div class="gallery-item fade-in">
        <img src="image.jpg" alt="Description">
        <div class="gallery-item__overlay">
            <h3 class="gallery-item__title">Image Title</h3>
        </div>
    </div>
</div>
```

### 4. Contact Form

```html
<form>
    <div class="form-group">
        <label for="name" class="form-label">Name *</label>
        <input type="text" id="name" class="form-control" required>
    </div>
    <button type="submit" class="btn">Submit</button>
</form>
```

## Customization

### Mengubah Warna

Edit di `assets/css/global.css`:

```css
:root {
  --color-primary: #8B4513;     /* Warna utama */
  --color-secondary: #2C1810;   /* Warna sekunder */
  --color-accent: #D4A574;      /* Warna aksen */
  --color-light: #F5F1E8;       /* Background terang */
}
```

### Mengubah Font

Edit di `assets/css/global.css`:

```css
:root {
  --font-primary: 'Raleway', sans-serif;
  --font-secondary: 'Muli', sans-serif;
}
```

### Mengubah Spacing

Edit di `assets/css/global.css`:

```css
:root {
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 32px;
  --spacing-xl: 48px;
  --spacing-xxl: 64px;
}
```

## Gambar dari Pexels

Semua gambar menggunakan Pexels API dengan URL format:
```
https://images.pexels.com/photos/[ID]/pexels-photo-[ID].jpeg?auto=compress&cs=tinysrgb&w=[WIDTH]
```

Contoh kategori yang digunakan:
- Pizza & Pasta: ID 1260968, 1907228, 1633578
- Restaurant Interior: ID 1435904, 941861
- Wine: ID 1169084
- Desserts: ID 2097090

## Browser Support

- Chrome (terbaru)
- Firefox (terbaru)
- Safari (terbaru)
- Edge (terbaru)
- Mobile browsers

## Performance Tips

1. **Lazy Loading**: Gambar akan di-load saat diperlukan
2. **CSS Minification**: Untuk production, minify CSS files
3. **JavaScript Async**: Script sudah di-load dengan defer
4. **Image Optimization**: Gunakan format WebP jika memungkinkan

## Troubleshooting

### Animasi tidak berjalan
- Pastikan `assets/js/global.js` sudah di-load
- Cek console browser untuk error

### Style tidak muncul
- Pastikan path ke CSS files benar
- Cek apakah file CSS sudah ter-upload
- Clear browser cache

### Mobile menu tidak berfungsi
- Pastikan `assets/js/global.js` sudah di-load
- Cek apakah class `nav-toggle-btn` ada di HTML

## Next Steps

1. ✅ Test semua halaman di berbagai device
2. ✅ Sesuaikan konten dengan kebutuhan
3. ✅ Ganti gambar placeholder dengan gambar asli
4. ✅ Test form functionality
5. ✅ Optimize untuk SEO
6. ✅ Setup Google Analytics jika diperlukan

## Support

Jika ada pertanyaan atau masalah, dokumentasi lengkap ada di:
- CSS Variables: `assets/css/global.css`
- Component Examples: `index-new.html` dan `contact-new.html`
- JavaScript Functions: Comment di setiap file `.js`

---

**Note**: File-file lama (index.html, contact.html, dll) tetap ada dan tidak diubah. File baru menggunakan suffix `-new` agar tidak mengganggu sistem yang sudah ada.
