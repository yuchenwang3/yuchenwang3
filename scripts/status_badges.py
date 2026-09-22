"""Small, theme-aware PR status pills for GitHub's image-only README surface."""
from html import escape


def badge_stem(pr):
    return pr['repo'].replace('/', '-') + '-' + str(pr['number'])


def render_status(pr, dark=False):
    state = pr['state']
    if state not in ('open', 'merged'):
        raise ValueError(f'Unsupported visible PR state: {state}')
    palettes = {
        ('merged', False): ('#f0edfa', '#d9d0ee', '#6746a3'),
        ('merged', True): ('#292338', '#514066', '#d2b7fa'),
        ('open', False): ('#edf7f3', '#cce6db', '#23684c'),
        ('open', True): ('#192f28', '#35584b', '#95d6b5'),
    }
    bg, border, ink = palettes[(state, dark)]
    label = f'{state} · #{pr["number"]}'
    width = 40 + len(label) * 7
    if state == 'merged':
        icon = '<path d="M4 4v8m6-8v1c0 3-6 2-6 5"/><circle cx="4" cy="3" r="2"/><circle cx="10" cy="3" r="2"/><circle cx="4" cy="13" r="2"/>'
    else:
        icon = '<path d="M4 5v6m6 0V5c0-2-1-2-3-2"/><path d="m8 1-2 2 2 2"/><circle cx="4" cy="3" r="2"/><circle cx="4" cy="13" r="2"/><circle cx="10" cy="13" r="2"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="26" viewBox="0 0 {width} 26" role="img" aria-label="{escape(label)}">
<title>{escape(label)}</title>
<rect x=".5" y=".5" width="{width-1}" height="25" rx="13" fill="{bg}" stroke="{border}"/>
<g transform="translate(10 5)" fill="{bg}" stroke="{ink}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
<text x="31" y="17" fill="{ink}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="12" font-weight="600">{escape(label)}</text>
</svg>\n'''


def status_link(pr):
    stem = './assets/prs/status/' + badge_stem(pr)
    alt = escape(f'#{pr["number"]} · {pr["state"]}')
    return (f'<a href="{escape(pr["url"], quote=True)}"><picture>'
            f'<source media="(prefers-color-scheme: dark)" srcset="{stem}-dark.svg">'
            f'<img height="26" src="{stem}-light.svg" alt="{alt}"></picture></a>')
