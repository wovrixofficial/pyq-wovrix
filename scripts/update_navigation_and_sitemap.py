import os
import re

DRAWER_ITEM = '''      <a href="/derivations/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">
        <span class="drawer-nav-icon">📐</span>
        <div>
          <div>Derivations & Formulas</div>
          <span class="drawer-nav-desc">CBSE 12 step marking & formula sheets</span>
        </div>
      </a>
'''

FOOTER_ITEM = '          <li><a href="/derivations/">Derivations & Formulas</a></li>\n'

TARGET_DIRS = [
    '.', 'about', 'contact', 'paper-maker', 'practice', 'privacy', 
    'repeated', 'saved', 'syllabus', 'takedown', 'cbse-12', 'jee', 'neetug'
]

def update_html_files():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    updated_drawer_count = 0
    updated_footer_count = 0

    for rel_dir in TARGET_DIRS:
        full_dir = os.path.join(root_dir, rel_dir)
        if not os.path.exists(full_dir):
            continue
        for file in os.listdir(full_dir):
            if not file.endswith('.html'):
                continue
            path = os.path.join(full_dir, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            new_content = content
            changed = False

            # Update drawer nav if needed
            if 'drawer-nav' in new_content and '/derivations/' not in new_content:
                if '<a href="/repeated/" class="drawer-nav-item"' in new_content:
                    new_content = new_content.replace(
                        '<a href="/repeated/" class="drawer-nav-item"',
                        DRAWER_ITEM + '      <a href="/repeated/" class="drawer-nav-item"'
                    )
                    changed = True
                    updated_drawer_count += 1
                elif '<a href="/syllabus/" class="drawer-nav-item"' in new_content:
                    new_content = new_content.replace(
                        '<a href="/syllabus/" class="drawer-nav-item"',
                        DRAWER_ITEM + '      <a href="/syllabus/" class="drawer-nav-item"'
                    )
                    changed = True
                    updated_drawer_count += 1

            # Update footer links if needed
            if 'Platform Hubs</h4>' in new_content and '/derivations/' not in new_content:
                if '<li><a href="/practice/?exam=cbse">CBSE 12 Practice Hub</a></li>' in new_content:
                    new_content = new_content.replace(
                        '<li><a href="/practice/?exam=cbse">CBSE 12 Practice Hub</a></li>',
                        '<li><a href="/practice/?exam=cbse">CBSE 12 Practice Hub</a></li>\n' + FOOTER_ITEM.rstrip()
                    )
                    changed = True
                    updated_footer_count += 1

            if changed and new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

    print(f"Updated drawer navigation in {updated_drawer_count} HTML files.")
    print(f"Updated footer links in {updated_footer_count} HTML files.")

def update_sitemap():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sitemap_path = os.path.join(root_dir, 'sitemap.xml')
    if not os.path.exists(sitemap_path):
        print("sitemap.xml not found!")
        return

    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'https://learnosha.in/derivations/' in content:
        print("derivations URL already present in sitemap.xml")
        return

    new_entry = '''  <url>
    <loc>https://learnosha.in/derivations/</loc>
    <lastmod>2026-11-11</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
'''
    # Insert right before </urlset>
    if '</urlset>' in content:
        content = content.replace('</urlset>', new_entry + '</urlset>')
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully added https://learnosha.in/derivations/ to sitemap.xml")

if __name__ == '__main__':
    update_html_files()
    update_sitemap()
