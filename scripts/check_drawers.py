import os

def check():
    targets = []
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '.vercel', 'q', 'scratch', 'graphify-out']]
        for f in files:
            if f.endswith('.html'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    txt = fp.read()
                    if 'mobileNavDrawer' in txt:
                        targets.append(p)
    print(f"Total HTML with mobileNavDrawer: {len(targets)}")
    for t in targets:
        with open(t, 'r', encoding='utf-8', errors='ignore') as fp:
            has_deriv = '/derivations/' in fp.read()
        rel = os.path.relpath(t, root_dir)
        print(f"{rel}: {'HAS /derivations/' if has_deriv else 'MISSING'}")

if __name__ == '__main__':
    check()
