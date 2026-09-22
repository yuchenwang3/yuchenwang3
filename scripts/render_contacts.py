"""Equal-size, theme-aware contact links, without a third-party badge service."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTACTS = {
    "website": ("Website", "https://yuchenwang3.github.io/"),
    "cv": ("CV", "https://yuchenwang3.github.io/CV.pdf"),
    "scholar": ("Scholar", "https://scholar.google.com/citations?user=NharhG8AAAAJ"),
    "linkedin": ("LinkedIn", "https://www.linkedin.com/in/yuchen3"),
    "email": ("Email", "mailto:yuchenwang0303@gmail.com"),
    "wechat": ("WeChat · eangyc", "https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/main/assets/wechat-qr.jpg"),
}
ICONS = {
    "website": '<circle cx="8" cy="8" r="6.5"/><ellipse cx="8" cy="8" rx="3" ry="6.5"/><path d="M1.5 8h13"/>',
    "cv": '<path d="M3 1.5h6l4 4v9H3zM9 1.5v4h4M5.5 8h5M5.5 11h4"/>',
    "scholar": '<path d="m1 6 7-4 7 4-7 4zM4 8v4c2 2 6 2 8 0V8M15 6v6"/>',
    "linkedin": '<rect x="1.5" y="1.5" width="13" height="13" rx="2"/><path d="M5 7v5M8 12V7m0 2c0-3 4-3 4 0v3M5 4.5v.2"/>',
    "email": '<rect x="1" y="3" width="14" height="10" rx="2"/><path d="m2 4 6 5 6-5"/>',
    "wechat": '<path d="M14.5 7.5a6.5 5.5 0 0 1-6.5 5.5H6l-3 1 .8-2.2A5.3 5.3 0 0 1 1.5 7.5a6.5 5.5 0 0 1 13 0Z"/><path d="M5 7h.2M8 7h.2M11 7h.2"/>',
}


def contact_svg(key, dark=False):
    label = CONTACTS[key][0]
    display = "WeChat" if key == "wechat" else label
    bg, border, ink = (("#17263d", "#3c5579", "#bad1f5") if dark
                       else ("#edf3fb", "#c8d7eb", "#315b94"))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="104" height="30" viewBox="0 0 104 30" role="img" aria-label="{escape(label)}">
<title>{escape(label)}</title>
<rect x=".5" y=".5" width="103" height="29" rx="6" fill="{bg}" stroke="{border}"/>
<g transform="translate(11 7)" fill="none" stroke="{ink}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">{ICONS[key]}</g>
<text x="36" y="19" fill="{ink}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="12" font-weight="600">{display}</text>
</svg>
'''


def contact_button(key):
    label, url = CONTACTS[key]
    stem = f'./assets/contacts/{key}'
    return (f'<a href="{escape(url, quote=True)}" title="{escape(label)}"><picture>'
            f'<source media="(prefers-color-scheme: dark)" srcset="{stem}-dark.svg">'
            f'<img width="104" height="30" src="{stem}-light.svg" alt="{escape(label)}">'
            '</picture></a>')


if __name__ == "__main__":
    destination = ROOT / 'assets/contacts'
    destination.mkdir(exist_ok=True)
    for key in CONTACTS:
        for dark in (False, True):
            (destination / f'{key}-{"dark" if dark else "light"}.svg').write_text(contact_svg(key, dark))
