import urllib.request

urls = [
    'https://learnosha.in/',
    'https://learnosha.in/practice/?exam=jee',
    'https://learnosha.in/repeated/?exam=jee',
    'https://learnosha.in/jee/',
    'https://learnosha.in/favicon.svg',
    'https://learnosha.in/data/jee_physics.json'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=10)
        cl = res.headers.get('Content-Length', 'chunked')
        print(f"[{res.status} OK] {u} (size: {cl})")
    except Exception as e:
        print(f"[FAIL] {u}: {e}")
