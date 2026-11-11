import os
import shutil
import re

def remove_derivations():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 1. Delete derivations directory
    deriv_dir = os.path.join(root_dir, 'derivations')
    if os.path.exists(deriv_dir):
        shutil.rmtree(deriv_dir)
        print("Deleted derivations/ directory.")

    # 2. Revert drawer and footer links in all HTML files
    reverted_drawer = 0
    reverted_footer = 0

    drawer_snippet = '''      <a href="/derivations/" class="drawer-nav-item" onclick="toggleMobileDrawer(false)">
        <span class="drawer-nav-icon">📐</span>
        <div>
          <div>Derivations & Formulas</div>
          <span class="drawer-nav-desc">CBSE 12 step marking & formula sheets</span>
        </div>
      </a>
'''

    footer_snippet = '          <li><a href="/derivations/">Derivations & Formulas</a></li>\n'

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '.vercel', 'q', 'scratch', 'graphify-out']]
        for file in files:
            if not file.endswith('.html'):
                continue
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            new_content = content
            if drawer_snippet in new_content:
                new_content = new_content.replace(drawer_snippet, '')
                reverted_drawer += 1

            if footer_snippet in new_content:
                new_content = new_content.replace(footer_snippet, '')
                reverted_footer += 1

            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

    print(f"Cleaned up {reverted_drawer} drawer navigation links and {reverted_footer} footer links.")

    # 3. Clean up practice/index.html banner if present
    practice_path = os.path.join(root_dir, 'practice', 'index.html')
    if os.path.exists(practice_path):
        with open(practice_path, 'r', encoding='utf-8') as f:
            p_content = f.read()

        p_new = re.sub(r'\s*<div id="cbseDerivationsBanner".*?</div>\s*', '\n', p_content, flags=re.DOTALL)
        p_new = p_new.replace("const banner = document.getElementById('cbseDerivationsBanner');\n      if (banner) banner.style.display = isCbse ? 'flex' : 'none';", "")

        if p_new != p_content:
            with open(practice_path, 'w', encoding='utf-8') as f:
                f.write(p_new)
            print("Cleaned banner from practice/index.html.")

    # 4. Clean up syllabus/index.html banner if present
    syllabus_path = os.path.join(root_dir, 'syllabus', 'index.html')
    if os.path.exists(syllabus_path):
        with open(syllabus_path, 'r', encoding='utf-8') as f:
            s_content = f.read()

        s_new = re.sub(r'\s*<!-- Derivations & Formulas Vault Banner for CBSE 12 -->\s*<div id="cbseDerivVaultBanner".*?</div>\s*', '\n', s_content, flags=re.DOTALL)
        s_new = s_new.replace("const derivBanner = document.getElementById('cbseDerivVaultBanner');\n      if (derivBanner) derivBanner.style.display = currentTrack === 'cbse12' ? 'flex' : 'none';", "")

        if s_new != s_content:
            with open(syllabus_path, 'w', encoding='utf-8') as f:
                f.write(s_new)
            print("Cleaned banner from syllabus/index.html.")

    # 5. Clean up sitemap.xml
    sitemap_path = os.path.join(root_dir, 'sitemap.xml')
    if os.path.exists(sitemap_path):
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            sm_content = f.read()

        sm_new = re.sub(r'\s*<url>\s*<loc>https://learnosha\.in/derivations/</loc>.*?</url>\s*', '\n', sm_content, flags=re.DOTALL)
        if sm_new != sm_content:
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(sm_new)
            print("Removed derivations URL from sitemap.xml.")

if __name__ == '__main__':
    remove_derivations()
