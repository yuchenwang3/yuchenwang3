"""Render the profile's self-contained, theme-aware terminal header."""
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def terminal_svg(dark=False):
    palette = (
        dict(bg="#0d1117", bar="#161b22", border="#30363d", ink="#e6edf3", muted="#9da7b3", accent="#79d2b0")
        if dark else
        dict(bg="#ffffff", bar="#f6f8fa", border="#d1d9e0", ink="#1f2328", muted="#59636e", accent="#1a7f37")
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="220" viewBox="0 0 800 220" role="img" aria-labelledby="terminal-title terminal-desc">
<title id="terminal-title">Yuchen (Ean) Wang — agentic post-training and ML systems</title>
<desc id="terminal-desc">A terminal prompt reads yuchen@github:~$ whoami. The output is Yuchen (Ean) Wang, agentic post-training / ML systems, followed by data to train to eval to ship.</desc>
<rect x="0.5" y="0.5" width="799" height="219" rx="8" fill="{palette['bg']}" stroke="{palette['border']}"/>
<path d="M8.5 1H791.5A7.5 7.5 0 0 1 799 8.5V36H1V8.5A7.5 7.5 0 0 1 8.5 1Z" fill="{palette['bar']}"/>
<path d="M1 36.5H799" stroke="{palette['border']}"/>
<g font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
<path d="m19 14 5 4-5 4m9 0h7" fill="none" stroke="{palette['accent']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<text x="47" y="23" fill="{palette['muted']}" font-size="12">~/profile</text>
<text x="774" y="23" fill="{palette['muted']}" font-size="12" text-anchor="end">README.md</text>
<text x="28" y="70" font-size="15"><tspan fill="{palette['accent']}">yuchen@github:~$</tspan><tspan fill="{palette['ink']}"> whoami</tspan></text>
<text x="28" y="113" fill="{palette['ink']}" font-size="29" font-weight="600" letter-spacing="-0.8">Yuchen (Ean) Wang</text>
<text x="28" y="143" fill="{palette['muted']}" font-size="18">agentic post-training / ML systems</text>
<text x="28" y="189" font-size="16"><tspan fill="{palette['muted']}">data</tspan><tspan fill="{palette['accent']}"> → </tspan><tspan fill="{palette['muted']}">train</tspan><tspan fill="{palette['accent']}"> → </tspan><tspan fill="{palette['muted']}">eval</tspan><tspan fill="{palette['accent']}"> → </tspan><tspan fill="{palette['muted']}">ship</tspan><tspan fill="{palette['accent']}"> _</tspan></text>
</g>
</svg>
'''


if __name__ == "__main__":
    for dark in (False, True):
        theme = "dark" if dark else "light"
        (ROOT / "assets" / f"terminal-{theme}.svg").write_text(terminal_svg(dark))
