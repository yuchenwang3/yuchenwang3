"""GitHub-safe vector artwork. Diagrams are schematic, not benchmark plots."""
from html import escape

FONT = "system-ui, -apple-system, Segoe UI, sans-serif"
SERIF = "Georgia, Times New Roman, serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, monospace"


def palette(dark, hue="green"):
    accents = {
        "green": ("#197263", "#6ed6b6", "#edf5ef", "#162d29"),
        "blue": ("#425cbb", "#a8b8ff", "#eef1fb", "#222b43"),
        "amber": ("#95571e", "#edbc78", "#faf2e5", "#35291f"),
        "violet": ("#7355aa", "#c5adf1", "#f3eff9", "#2e253d"),
    }
    a, ad, bg, bgd = accents[hue]
    return dict(bg=bgd if dark else bg, ink="#edf0ee" if dark else "#222b2a",
                muted="#b4bdbb" if dark else "#586662", line="#46524e" if dark else "#d3ddd6",
                accent=ad if dark else a, surface="#1b211f" if dark else "#ffffff")


def text(x, y, value, size=22, fill="#222b2a", weight=400, family=FONT, **attrs):
    attr = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" {attr}>{escape(str(value))}</text>'


def rect(x, y, w, h, fill, rx=0, stroke="none"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'


def line(x1, y1, x2, y2, color, width=1, dash=""):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>'


def svg(w, h, title, desc, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>{body}</svg>\n'


def logo(x, y, size, ink, accent):
    # Official Occamy favicon geometry, Accio-Lab/occamy website/public/favicon.svg.
    return f'''<g transform="translate({x} {y}) scale({size/1800})"><g transform="translate(0 210)">
    <path fill="{ink}" d="M596 389C698 204 900 69 1110 67C1455 54 1718 312 1730 661L1727 731L1718 779C1670 862 1565 947 1425 974L1363 977L1357 972C1468 872 1518 772 1510 645C1512 440 1357 276 1150 280C998 275 856 377 800 521Q795 537 787 526C732 460 676 431 601 401Q591 398 596 389Z"/>
    <path fill="{ink}" d="M519 645C602 634 690 663 766 735C791 891 880 1001 1019 1067C1140 1110 1222 1091 1315 1046C1472 1048 1582 1007 1668 931Q1684 919 1676 937C1583 1154 1391 1308 1134 1309C784 1319 536 1057 518 742L516 680Z"/>
    <path fill="{accent}" d="M68 257Q70 247 79 256L126 304C248 414 365 412 485 433C642 457 745 529 813 679Q822 693 809 685C728 617 656 597 570 582L494 582L429 584C233 576 90 477 68 278Z"/>
    </g></g>'''


def research(name, dark=False, compact=False):
    c = palette(dark, {"occamy": "green", "cineflow": "blue", "prefill": "amber"}[name])
    a, ink, muted = c["accent"], c["ink"], c["muted"]
    w, h = (1200, 350) if name == "occamy" and not compact else (600, 390)
    b = rect(1, 1, w-2, h-2, c["bg"], 10, c["line"])
    b += line(30, 25, 68, 25, a, 3)
    if name == "occamy":
        if compact:
            b += text(30, 65, "Occamy-1.0", 42, ink, 500, SERIF)
            b += text(32, 100, "Data & agentic post-training", 20, muted)
            b += text(30, 175, "35B", 45, a, 650)
            b += text(30, 202, "total parameters", 17, muted)
            b += text(190, 175, "3B", 45, a, 650)
            b += text(190, 202, "active parameters", 17, muted)
            b += logo(350, 84, 205, ink, a)
            b += text(30, 260, "Long-horizon work. Real tools.", 23, ink, 500)
            steps = [(30, "Plan"), (168, "Act"), (286, "Recover"), (455, "Complete")]
            for x, label in steps:
                b += text(x, 313, label, 19, a, 500)
            b += line(80, 306, 150, 306, c["line"], 2)
            b += line(207, 306, 268, 306, c["line"], 2)
            b += line(369, 306, 437, 306, c["line"], 2)
            b += line(30, 339, 570, 339, c["line"])
            b += text(30, 371, "ACCIO · OPEN MODEL", 15, muted, 500, MONO)
            b += text(554, 371, "↗", 24, a)
        else:
            b += text(42, 99, "Occamy-1.0", 64, ink, 500, SERIF)
            b += text(44, 140, "Execution-grounded data & agentic post-training", 25, muted)
            b += text(44, 210, "35B", 44, a, 650)
            b += text(150, 209, "total", 19, muted)
            b += text(243, 210, "3B", 44, a, 650)
            b += text(320, 209, "active", 19, muted)
            b += text(469, 210, "Long-horizon tool use", 23, ink, 500)
            b += logo(832, 30, 290, ink, a)
            b += line(42, 252, 768, 252, c["line"])
            for x, label in [(44, "PLAN"), (224, "ACT"), (391, "RECOVER"), (622, "COMPLETE")]:
                b += text(x, 291, label, 18, a, 550, MONO)
            for x1, x2 in [(111, 203), (269, 370), (493, 600)]:
                b += line(x1, 285, x2, 285, c["line"], 2)
            b += text(44, 329, "ACCIO TEAM", 14, muted, 500, MONO, letter_spacing="2")
            b += text(1148, 324, "OPEN MODEL ↗", 17, a, 500, MONO, text_anchor="end")
        return svg(w,h,"Occamy-1.0","35B-A3B agent model. Schematic task loop: plan, act, recover, complete.",b)
    if name == "cineflow":
        b += text(30, 66, "CineFlow", 42, ink, 500, SERIF)
        b += text(31, 99, "Dependency-aware video generation", 21, muted)
        # Two parallel scene lanes; an illustration, not model-generated frames.
        b += text(30, 142, "SCENE A", 13, muted, 500, MONO)
        b += text(30, 226, "SCENE B", 13, muted, 500, MONO)
        for row in range(2):
            y = 153 + row*84
            for col in range(4):
                x = 122+col*112
                b += rect(x,y,98,64,c["surface"],4,c["line"])
                b += f'<circle cx="{x+76-col*6}" cy="{y+15+col*2}" r="6" fill="{a}" opacity=".6"/>'
                if row == 0:
                    b += f'<path d="M{x+3} {y+54}L{x+25} {y+24}L{x+44} {y+43}L{x+62} {y+21}L{x+95} {y+54}Z" fill="{a}" opacity=".25"/>'
                    b += line(x+4,y+55,x+94,y+55,a,1.5)
                    b += rect(x+10+col*14,y+43,25,9,a,2)
                    for wheel in (15,29):
                        b += f'<circle cx="{x+wheel+col*14}" cy="{y+54}" r="2" fill="{a}"/>'
                else:
                    b += f'<path d="M{x+4} {y+50}Q{x+16} {y+42} {x+28} {y+50}T{x+52} {y+50}T{x+76} {y+50}T{x+94} {y+50}" fill="none" stroke="{a}" opacity=".5"/>'
                    boat = x+13+col*14
                    b += f'<path d="M{boat} {y+42}H{boat+26}L{boat+21} {y+48}H{boat+5}Z" fill="{a}"/>'
                    b += f'<path d="M{boat+12} {y+15}V{y+40}H{boat+26}Z" fill="{a}" opacity=".65"/>'
                b += line(x+6,y+59,x+92,y+59,a,1)
                if col<3:
                    b += line(x+99,y+32,x+109,y+32,a,1.5)
        b += f'<path d="M164 218L164 228L388 228L388 237" stroke="{a}" stroke-width="1.5" fill="none"/>'
        b += line(30,327,570,327,c["line"])
        b += text(30,368,"1.7–5.5×",29,a,650)
        b += text(200,367,"reported speedup",18,muted)
        b += text(560,367,"↗",25,a)
        return svg(w,h,"CineFlow","Schematic of parallel video scenes with dependencies; reported 1.7–5.5x speedup.",b)
    b += text(30,66,"Dynamic Prefill",39,ink,500,SERIF)
    b += text(31,99,"Better packing. Less waiting.",21,muted)
    b += text(30,141,"ARRIVING PROMPTS",13,muted,500,MONO)
    b += text(344,141,"PACKED BATCH",13,muted,500,MONO)
    colors=[a,"#be8553","#e3b888","#b39b77"]
    for r, n in enumerate([5,8,3,6]):
        y=155+r*32
        for j in range(10):
            b+=rect(30+j*20,y,16,21,colors[r] if j<n else c["surface"],2,c["line"] if j>=n else "none")
    b+=f'<path d="M255 213H306M294 203L306 213L294 223" stroke="{a}" stroke-width="2" fill="none"/>'
    for r in range(3):
        for j in range(10):
            idx=r*10+j
            color=colors[0] if idx<5 else colors[1] if idx<13 else colors[2] if idx<16 else colors[3] if idx<22 else c["surface"]
            b+=rect(344+j*20,165+r*35,16,26,color,2,c["line"] if idx>=22 else "none")
    b+=text(344,289,"p95 TTFT feedback ↶",15,muted,400,MONO)
    b+=line(30,327,570,327,c["line"])
    b+=text(30,368,"↓ 20%",29,a,650)
    b+=text(151,367,"TTFT · up to, reported traces",17,muted)
    b+=text(560,367,"↗",25,a)
    return svg(w,h,"Dynamic Prefill","Illustrative token packing with p95 TTFT feedback. Up to 20% lower time to first token on reported traces.",b)


PR_DESIGN = {
    ("flashinfer-ai/flashinfer", 4984): ("FlashInfer", "KERNELS", "green", "FI", ["Calibrate FP8 attention"], "Correct K/V scales in ragged prefill"),
    ("vllm-project/vllm", 54699): ("vLLM", "INFERENCE", "blue", "vL", ["Convert MoE weights", "in place"], "Reduce conversion peak memory"),
    ("NVIDIA-NeMo/RL", 3943): ("NeMo RL", "DISTRIBUTED", "amber", "RL", ["Move references,", "not teacher payloads"], "Defer top-k transfer through Ray"),
    ("NousResearch/hermes-agent", 100693): ("Hermes Agent", "AGENT RUNTIME", "violet", "H", ["Resolve nested", "tool schemas"], "Coerce arguments through local refs"),
    ("NVIDIA-NeMo/Emerging-Optimizers", 230): ("Emerging Optimizers", "TRAINING", "green", "∇", ["Keep Muon", "scale-invariant"], "Stable small-norm Newton–Schulz"),
    ("NVIDIA/Megatron-LM", 5396): ("Megatron-LM", "KERNELS", "blue", "M", ["Fuse GDN", "Q/K normalization"], "Fold L2-norm into the delta-rule kernel"),
    ("NVIDIA/Megatron-LM", 5463): ("Megatron-LM", "MEMORY", "amber", "M", ["Recompute Mamba", "selectively"], "Extend recompute module coverage"),
    ("NousResearch/hermes-agent", 102549): ("Hermes Agent", "AGENT RUNTIME", "violet", "H", ["Make SSH reconnects", "race-safe"], "Wait for pooled-backend teardown"),
}


def render_pr(p, dark):
    project, category, hue, mark, title, detail = PR_DESIGN[(p["repo"], p["number"])]
    c=palette(dark,hue); a=c["accent"]; ink=c["ink"]; muted=c["muted"]
    b=rect(1,1,598,278,c["surface"],9,c["line"])
    b+=rect(1,1,7,278,a,3)
    b+=rect(28,26,43,43,c["bg"],8)
    b+=text(49,55,mark,22,a,650,text_anchor="middle")
    b+=text(84,54,project,22,ink,650)
    b+=text(564,85,category,12,muted,500,MONO,text_anchor="end",letter_spacing="1")
    for i,t in enumerate(title):
        b+=text(29,119+i*31,t,28,ink,600)
    b+=text(29,190,detail,18,muted)
    b+=line(28,216,572,216,c["line"])
    state=p["state"]
    status_color=("#bba0ed" if dark else "#7953ae") if state=="merged" else a if state=="open" else muted
    b+=f'<circle cx="35" cy="246" r="4" fill="{status_color}"/>'
    b+=text(49,252,state.capitalize(),16,status_color,500)
    b+=text(564,252,f'#{p["number"]} ↗',17,muted,450,MONO,text_anchor="end")
    return svg(600,296,f'{project} PR #{p["number"]}',p["title"]+"; status: "+state,b)
