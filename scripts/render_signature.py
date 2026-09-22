"""Compact version of the original script-letter typing signature."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def signature_svg(dark=False):
    ink = "#a3c6ff" if dark else "#426dab"
    # Preserve the original script-letter styling without a remote image service.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="430" height="52" viewBox="0 0 430 52" role="img" aria-labelledby="title">
<title id="title">Yuchen (Ean) Wang — handwritten typing signature</title>
<style>
.reveal {{ animation: write 7s linear infinite; }}
@keyframes write {{ 0% {{ width:0; }} 48%,92%,100% {{ width:420px; }} }}
@media (prefers-reduced-motion: reduce) {{ .reveal {{ animation:none; }} }}
</style>
<defs><clipPath id="writing"><rect class="reveal" width="420" height="52"/></clipPath></defs>
<text x="2" y="36" fill="{ink}" font-family="Georgia,serif" font-size="30" clip-path="url(#writing)">𝓨𝓾𝓬𝓱𝓮𝓷 (𝓔𝓪𝓷) 𝓦𝓪𝓷𝓰</text>
</svg>
'''


if __name__ == "__main__":
    for dark in (False, True):
        (ROOT / "assets" / f'signature-{"dark" if dark else "light"}.svg').write_text(signature_svg(dark))
