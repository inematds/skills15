#!/usr/bin/env python3
"""Monta guia/index.html (PT), guia/en/ e guia/es/ a partir de catalogo*.json e dos textos abaixo.
CSS = o do template projetos-landing-guia (amarelo #FACC15 do kit inema-design V1). Uso: python3 scripts/build_guia.py"""
import html, json, os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.expanduser("~/.claude/skills/projetos-landing-guia/assets/template.html")
REPO = "https://github.com/inematds/skills15"
BASE = "https://inematds.github.io/skills15/guia/"
VIDEOS = json.load(open(os.path.join(RAIZ, "videos.json"))) if os.path.exists(os.path.join(RAIZ, "videos.json")) else {}

css = re.search(r"<style>(.*?)</style>", open(TPL).read(), re.S).group(1)
css = (css.replace("--amb:#E2A23B; --amb2:#f0c070", "--amb:#FACC15; --amb2:#fde68a")
          .replace("--amb:#b9791d; --amb2:#a16207", "--amb:#a16207; --amb2:#854d0e")
          .replace("rgba(226,162,59,", "rgba(250,204,21,")
          .replace(".chip{display:inline-block;font-size:.72rem", ".chip{display:inline-block;font-size:.75rem"))
css += """
  .idx{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:22px}
  @media(max-width:820px){.idx{grid-template-columns:repeat(3,1fr)}} @media(max-width:480px){.idx{grid-template-columns:1fr 1fr}}
  .idx a{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px;color:var(--txt);font-family:Sora;font-weight:600;font-size:.9rem}
  .idx a:hover{border-color:var(--amb)} .idx a b{display:block;color:var(--amb);font-size:1.3rem;font-weight:800}
  .idx a small{display:block;color:var(--mut);font-family:Inter;font-weight:400;font-size:.8rem}
  .sk{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:28px;padding:34px 0;border-top:1px solid var(--line);scroll-margin-top:70px}
  @media(max-width:860px){.sk{grid-template-columns:minmax(0,1fr)}}
  .sk p,.sk li{overflow-wrap:anywhere}
  .sk figure{margin:0;border-radius:14px;overflow:hidden;border:1px solid var(--line);align-self:start}
  .sk figure img{width:100%;display:block}
  .sk .pos{font-family:Sora;font-weight:800;font-size:2.4rem;color:var(--amb);line-height:1}
  .sk h3{font-size:1.45rem;margin:.2em 0 .35em}
  .sk .meta{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}
  .sk .meta span{border:1px solid var(--line);border-radius:999px;padding:.2em .7em;font-size:.78rem;color:var(--mut)}
  .sk h4{font-family:Sora;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:var(--amb);margin:16px 0 4px}
  .sk p,.sk li{color:var(--txt);font-size:.96rem;margin:.2em 0}
  .sk ol{margin:.2em 0;padding-left:1.3em}
  .sk .exq{background:var(--bg2);border-left:3px solid var(--amb);border-radius:8px;padding:10px 14px;margin:6px 0}
  .sk .exq p{margin:.25em 0} .sk .exq b{font-family:Sora;font-size:.82rem;color:var(--mut)}
  .sk .warn{border-left-color:#ef4444}
  .sk .refs a{margin-right:14px;font-weight:600}
  .chart{margin:0;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 18px 10px;overflow-x:auto}
  .chart svg{width:100%;min-width:520px;display:block} .chart figcaption{color:var(--mut);font-size:.82rem;margin-top:8px}
  .chart .mk{fill:var(--amb)} .chart .hit{fill:transparent} .chart .bar:hover .mk{opacity:.8} .chart .bar:hover .lb{fill:var(--txt);font-weight:600}
  .chart .lb{fill:var(--mut);font:13px Inter,sans-serif} .chart .vl{fill:var(--txt);font:600 13px Sora,sans-serif}
  .tbl{margin-top:12px;color:var(--mut);font-size:.9rem} .tbl summary{cursor:pointer;color:var(--amb)} .tbl table{border-collapse:collapse;margin-top:8px}
  .tbl td,.tbl th{border-bottom:1px solid var(--line);padding:4px 14px 4px 0;text-align:left}
  .vid{display:grid;grid-template-columns:1.4fr .6fr;gap:18px} @media(max-width:760px){.vid{grid-template-columns:1fr}}
  .vid iframe{width:100%;aspect-ratio:16/9;border:0;border-radius:14px} .vid .v916 iframe{aspect-ratio:9/16}
"""

T = {
 "pt": {"lang": "pt-BR", "cat": "catalogo.json", "pfx": "", "dir": "",
   "title": "skills15 — as 15 skills para o Claude que valem a pena",
   "desc": "As 15 skills para Claude Code que valem a pena: problema que cada uma resolve, como funciona, exemplo, comando de instalação e link do projeto original.",
   "nav": ["As 15", "Como escolher", "Instalar", "Vídeos"],
   "chip": "Catálogo · 15 skills para o Claude",
   "h1": 'As 15 skills que <span class="amb">valem a pena</span>',
   "lead": "Existem mais de um milhão de skills. Estas 15 resolvem problemas de verdade: gastar menos limite, responder direto, desenhar, fazer vídeo, programar com método e ver por dentro de qualquer app.",
   "cta1": "Ver as 15", "cta2": "Ver no GitHub", "alt": "As 15 melhores skills",
   "rchip": "Em resumo",
   "resumo": "O skills15 é um catálogo grátis das 15 skills para agentes de IA (Claude Code e outros) que mais valem a pena hoje. Para cada uma você vê o problema que ela resolve, como funciona por dentro, o comando oficial de instalação, um exemplo de pedido e o link para o projeto original. Serve para quem usa o Claude e quer escolher a skill certa para a dor de hoje, sem instalar tudo. Não precisa programar: basta colar o link no Claude Code e pedir para instalar.",
   "oq_chip": "O que é", "oq_h": "Um mapa, não uma pilha de skills", "oq_sub": "Este repositório não copia o código de ninguém: aponta para o projeto original e explica, em português simples, quando cada skill vale a pena.",
   "cards": [("🎯", "Uma dor, uma skill", "Cada ficha começa pelo problema. Você acha a sua dor e chega na skill."),
             ("🔗", "Sempre a fonte", "Link para o repositório original, estrelas contadas em 18/10/2026 e a licença de cada um."),
             ("⚠️", "Com os cuidados", "Avisos honestos: o que não é oficial, que número é só do autor e o que pode quebrar.")],
   "idx_chip": "As 15", "idx_h": "Da 15ª à 1ª", "idx_sub": "Clique para ir direto à ficha. A ordem segue a contagem regressiva: a melhor fica no fim.",
   "esc_chip": "Como escolher", "esc_h": "Não instale todas", "esc_sub": "Cada skill a mais é contexto que o agente carrega e pode disparar sem você querer. O caminho:",
   "flow": ["sua dor de hoje", "a ficha", "instale uma", "teste numa tarefa real", "ficou ou apague"],
   "h_prob": "O problema", "h_faz": "O que faz", "h_como": "Como funciona", "h_inst": "Como instalar", "h_ex": "Exemplo",
   "h_pede": "Você pede", "h_volta": "Volta", "h_cuid": "Cuidado", "h_ref": "Referência",
   "fonte": "Projeto original", "inema": "No INEMA", "estr": "★ em 18/10/2026", "lic": "licença", "sem_repo": "post do Reddit (sem repositório)",
   "ins_chip": "Instalar", "ins_h": "Um jeito para todas", "ins_sub": "Funciona com qualquer uma das 15.",
   "steps": [("Copie o link e peça", "Cole o link do repositório no Claude Code e diga: instale isso para mim. Ele lê o README e faz o resto.", None),
             ("Ou use o instalador deste repo", "Ele só mostra os comandos oficiais; roda apenas com --executar.",
              "git clone https://github.com/inematds/skills15.git && cd skills15\n./scripts/instalar.sh          # lista as 15\n./scripts/instalar.sh 12       # mostra como instalar a #12\n./scripts/instalar.sh 12 --executar"),
             ("Teste numa tarefa real", "Faça a mesma tarefa com e sem a skill. Não melhorou? Desinstale.", None)],
   "vid_chip": "Vídeos", "vid_h": "As 15 explicadas", "vid_sub": "O vídeo completo detalha cada uma; o curto cita as 15 em menos de um minuto.",
   "g_chip": "Em números", "g_h": "Estrelas no GitHub", "g_sub": "Quantas estrelas cada projeto tinha em 18/10/2026 (a #11 é um post do Reddit e fica de fora). Estrela mede popularidade, não qualidade.", "g_tab": "Ver como tabela", "g_c1": "Skill", "g_c2": "Estrelas", "g_nota": "Passe o mouse ou toque numa barra para ver o número exato.",
   "foot": "catálogo grátis · textos MIT, cada skill com a licença do projeto original"},
 "en": {"lang": "en", "cat": "catalogo.en.json", "pfx": "../", "dir": "en/",
   "title": "skills15 — the 15 Claude skills worth installing",
   "desc": "The 15 Claude Code skills worth installing: the problem each one solves, how it works, an example, the install command and a link to the original project.",
   "nav": ["The 15", "How to choose", "Install", "Videos"],
   "chip": "Catalog · 15 skills for Claude",
   "h1": 'The 15 skills <span class="amb">worth it</span>',
   "lead": "There are over a million skills out there. These 15 solve real problems: use less of your limit, get straight answers, draw diagrams, make videos, code with a method and look inside any app.",
   "cta1": "See the 15", "cta2": "View on GitHub", "alt": "The 15 best skills",
   "rchip": "In short",
   "resumo": "skills15 is a free catalog of the 15 AI agent skills (for Claude Code and others) that are most worth it today. For each one you get the problem it solves, how it works inside, the official install command, an example request and a link to the original project. It is for anyone who uses Claude and wants to pick the right skill for today's pain, without installing everything. No coding needed: paste the link into Claude Code and ask it to install it.",
   "oq_chip": "What it is", "oq_h": "A map, not a pile of skills", "oq_sub": "This repository copies nobody's code: it points to the original project and explains, in plain language, when each skill is worth it.",
   "cards": [("🎯", "One pain, one skill", "Every entry starts with the problem. Find your pain and you find the skill."),
             ("🔗", "Always the source", "Link to the original repository, stars counted on 10/18/2026 and each license."),
             ("⚠️", "With the caveats", "Honest warnings: what is unofficial, which numbers are the author's own and what may break.")],
   "idx_chip": "The 15", "idx_h": "From #15 to #1", "idx_sub": "Click to jump to an entry. It's a countdown: the best one comes last.",
   "esc_chip": "How to choose", "esc_h": "Don't install them all", "esc_sub": "Every extra skill is context the agent carries and may trigger when you don't want it. The path:",
   "flow": ["today's pain", "the entry", "install one", "test on a real task", "keep it or remove it"],
   "h_prob": "The problem", "h_faz": "What it does", "h_como": "How it works", "h_inst": "How to install", "h_ex": "Example",
   "h_pede": "You ask", "h_volta": "You get", "h_cuid": "Caveat", "h_ref": "Reference",
   "fonte": "Original project", "inema": "At INEMA", "estr": "★ on 10/18/2026", "lic": "license", "sem_repo": "Reddit post (no repository)",
   "ins_chip": "Install", "ins_h": "One way for all of them", "ins_sub": "Works with any of the 15.",
   "steps": [("Copy the link and ask", "Paste the repository link into Claude Code and say: install this for me. It reads the README and does the rest.", None),
             ("Or use this repo's installer", "It only shows the official commands; it runs them only with --executar.",
              "git clone https://github.com/inematds/skills15.git && cd skills15\n./scripts/instalar.sh          # lists the 15\n./scripts/instalar.sh 12       # shows how to install #12\n./scripts/instalar.sh 12 --executar"),
             ("Test it on a real task", "Do the same task with and without the skill. No better? Uninstall it.", None)],
   "vid_chip": "Videos", "vid_h": "The 15 explained (in Portuguese)", "vid_sub": "The full video details each one; the short one names all 15 in under a minute.",
   "g_chip": "By the numbers", "g_h": "GitHub stars", "g_sub": "How many stars each project had on 10/18/2026 (#11 is a Reddit post and is left out). Stars measure popularity, not quality.", "g_tab": "Show as a table", "g_c1": "Skill", "g_c2": "Stars", "g_nota": "Hover or tap a bar to see the exact number.",
   "foot": "free catalog · text MIT, each skill under its original project's license"},
 "es": {"lang": "es", "cat": "catalogo.es.json", "pfx": "../", "dir": "es/",
   "title": "skills15 — las 15 skills para Claude que valen la pena",
   "desc": "Las 15 skills para Claude Code que valen la pena: el problema que resuelve cada una, cómo funciona, un ejemplo, el comando de instalación y el enlace al proyecto original.",
   "nav": ["Las 15", "Cómo elegir", "Instalar", "Videos"],
   "chip": "Catálogo · 15 skills para Claude",
   "h1": 'Las 15 skills que <span class="amb">valen la pena</span>',
   "lead": "Hay más de un millón de skills. Estas 15 resuelven problemas reales: gastar menos límite, respuestas directas, dibujar diagramas, hacer videos, programar con método y ver por dentro cualquier app.",
   "cta1": "Ver las 15", "cta2": "Ver en GitHub", "alt": "Las 15 mejores skills",
   "rchip": "En resumen",
   "resumo": "skills15 es un catálogo gratis de las 15 skills para agentes de IA (Claude Code y otros) que más valen la pena hoy. De cada una ves el problema que resuelve, cómo funciona por dentro, el comando oficial de instalación, un ejemplo de pedido y el enlace al proyecto original. Sirve para quien usa Claude y quiere elegir la skill correcta para el dolor de hoy, sin instalarlo todo. No hace falta programar: pega el enlace en Claude Code y pídele que la instale.",
   "oq_chip": "Qué es", "oq_h": "Un mapa, no una pila de skills", "oq_sub": "Este repositorio no copia el código de nadie: apunta al proyecto original y explica, en lenguaje simple, cuándo vale la pena cada skill.",
   "cards": [("🎯", "Un dolor, una skill", "Cada ficha empieza por el problema. Encuentras tu dolor y llegas a la skill."),
             ("🔗", "Siempre la fuente", "Enlace al repositorio original, estrellas contadas el 18/10/2026 y la licencia de cada uno."),
             ("⚠️", "Con los cuidados", "Avisos honestos: qué no es oficial, qué número es solo del autor y qué puede romperse.")],
   "idx_chip": "Las 15", "idx_h": "De la 15.ª a la 1.ª", "idx_sub": "Haz clic para ir a la ficha. Es una cuenta regresiva: la mejor queda al final.",
   "esc_chip": "Cómo elegir", "esc_h": "No las instales todas", "esc_sub": "Cada skill de más es contexto que el agente carga y que puede activarse sin que quieras. El camino:",
   "flow": ["tu dolor de hoy", "la ficha", "instala una", "pruébala en una tarea real", "se queda o la borras"],
   "h_prob": "El problema", "h_faz": "Qué hace", "h_como": "Cómo funciona", "h_inst": "Cómo instalar", "h_ex": "Ejemplo",
   "h_pede": "Tú pides", "h_volta": "Recibes", "h_cuid": "Cuidado", "h_ref": "Referencia",
   "fonte": "Proyecto original", "inema": "En INEMA", "estr": "★ al 18/10/2026", "lic": "licencia", "sem_repo": "post de Reddit (sin repositorio)",
   "ins_chip": "Instalar", "ins_h": "Una forma para todas", "ins_sub": "Funciona con cualquiera de las 15.",
   "steps": [("Copia el enlace y pide", "Pega el enlace del repositorio en Claude Code y di: instálame esto. Lee el README y hace el resto.", None),
             ("O usa el instalador de este repo", "Solo muestra los comandos oficiales; los ejecuta únicamente con --executar.",
              "git clone https://github.com/inematds/skills15.git && cd skills15\n./scripts/instalar.sh          # lista las 15\n./scripts/instalar.sh 12       # muestra cómo instalar la #12\n./scripts/instalar.sh 12 --executar"),
             ("Pruébala en una tarea real", "Haz la misma tarea con y sin la skill. ¿No mejoró? Desinstálala.", None)],
   "vid_chip": "Videos", "vid_h": "Las 15 explicadas (en portugués)", "vid_sub": "El video completo detalla cada una; el corto nombra las 15 en menos de un minuto.",
   "g_chip": "En números", "g_h": "Estrellas en GitHub", "g_sub": "Cuántas estrellas tenía cada proyecto el 18/10/2026 (la #11 es un post de Reddit y queda fuera). Las estrellas miden popularidad, no calidad.", "g_tab": "Ver como tabla", "g_c1": "Skill", "g_c2": "Estrellas", "g_nota": "Pasa el mouse o toca una barra para ver el número exacto.",
   "foot": "catálogo gratis · textos MIT, cada skill con la licencia de su proyecto original"},
}
IMG = {"notebooklm-py": "g15-notebooklm", "i-have-adhd": "g14-adhd", "billion-context": "g13-billion", "find-skills": "g12-skillssh",
       "de-ai-writing": "g11-wikipedia", "archify": "g10-archify", "nanoclaw": "g09-nanoclaw", "karpathy-claude-md": "g08-karpathy",
       "hyperframes": "g07-hyperframes", "mattpocock-skills": "g06-pocock", "career-ops": "g05-careerops", "graphify": "g04-graphify",
       "ai-website-cloner": "g03-cloner", "anatomy": "g02-anatomy-readme", "rea": "g01-rea"}
E = html.escape


def mil(n, lang):
    if n is None:
        return "—"
    s = f"{n/1000:.1f}" if n < 100000 else f"{n//1000}"
    return (s.replace(".", ",") if lang != "en" else s).replace(",0", "").replace(".0", "") + (" mil" if lang != "en" else "k")


def ficha(x, t, l):
    p = t["pfx"]
    estr = f'<span>{mil(x["estrelas"], l)} {t["estr"]}</span>' if x["estrelas"] else f'<span>{t["sem_repo"]}</span>'
    lic = f'<span>{t["lic"]}: {E(x["licenca"])}</span>' if x["licenca"] else ""
    como = "".join(f"<li>{E(c)}</li>" for c in x["como_funciona"])
    sh = "\n".join(E(c) for c in x.get("instalar_shell") or [])
    pre = f'<pre><span class="k">{sh}</span></pre>' if sh else ""
    cuid = f'<h4>{t["h_cuid"]}</h4><div class="exq warn"><p>{E(x["cuidado"])}</p></div>' if x.get("cuidado") else ""
    refs = f'<a href="{E(x["url"])}" target="_blank" rel="noopener">{t["fonte"]} ↗</a>'
    if x.get("inema"):
        refs += f'<a href="{E(x["inema"]["url"])}" target="_blank" rel="noopener">{t["inema"]}: {E(x["inema"]["titulo"])} ↗</a>'
    return f'''<article class="sk" id="s{x["pos"]}">
  <figure><img src="{p}assets/{IMG[x["slug"]]}.jpg" alt="{E(x["nome"])}" loading="lazy"></figure>
  <div>
    <div class="pos">#{x["pos"]}</div><h3>{E(x["nome"])}</h3>
    <div class="meta"><span>{E(x["categoria"])}</span>{estr}{lic}</div>
    <h4>{t["h_prob"]}</h4><p>{E(x["problema"])}</p>
    <h4>{t["h_faz"]}</h4><p>{E(x["o_que_faz"])}</p>
    <h4>{t["h_como"]}</h4><ol>{como}</ol>
    <h4>{t["h_inst"]}</h4><p>{E(x["instalar"])}</p>{pre}
    <h4>{t["h_ex"]}</h4><div class="exq"><p><b>{t["h_pede"]}:</b> {E(x["exemplo_pedido"])}</p><p><b>{t["h_volta"]}:</b> {E(x["exemplo_resultado"])}</p></div>
    {cuid}
    <h4>{t["h_ref"]}</h4><p class="refs">{refs}</p>
  </div>
</article>'''


def grafico(cat, t, l):
    xs = sorted([x for x in cat if x["estrelas"]], key=lambda x: -x["estrelas"])
    W, LW, RW, BH, GAP = 760, 210, 70, 22, 8
    mx = xs[0]["estrelas"]; H = len(xs) * (BH + GAP)
    rows = []
    for i, x in enumerate(xs):
        y = i * (BH + GAP); w = max(4, (W - LW - RW) * x["estrelas"] / mx)
        full = f'{x["estrelas"]:,}'.replace(",", "." if l != "en" else ",")
        rows.append(f'<g class="bar"><title>#{x["pos"]} {E(x["nome"])}: {full} ★</title>'
                    f'<rect class="hit" x="0" y="{y}" width="{W}" height="{BH + GAP}"/>'
                    f'<text class="lb" x="{LW - 10}" y="{y + BH/2 + 5}" text-anchor="end">#{x["pos"]} {E(x["nome"].split(" (")[0][:24])}</text>'
                    f'<path class="mk" d="M{LW},{y} h{w-4} a4,4 0 0 1 4,4 v{BH-8} a4,4 0 0 1 -4,4 h-{w-4} z"/>'
                    f'<text class="vl" x="{LW + w + 8}" y="{y + BH/2 + 5}">{mil(x["estrelas"], l)}</text></g>')
    tab = "".join(f'<tr><td>#{x["pos"]} {E(x["nome"])}</td><td>{x["estrelas"]:,}</td></tr>'.replace(",", "." if l != "en" else ",") for x in xs)
    return f'''<section id="numeros"><div class="wrap"><span class="chip">{t["g_chip"]}</span><h2>{t["g_h"]}</h2><p class="sub">{E(t["g_sub"])}</p>
  <figure class="chart"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{E(t["g_h"])}">{"".join(rows)}</svg><figcaption>{E(t["g_nota"])}</figcaption></figure>
  <details class="tbl"><summary>{t["g_tab"]}</summary><table><thead><tr><th>{t["g_c1"]}</th><th>{t["g_c2"]}</th></tr></thead><tbody>{tab}</tbody></table></details>
</div></section>'''


def pagina(l):
    t = T[l]; p = t["pfx"]
    cat = json.load(open(os.path.join(RAIZ, t["cat"])))
    langs = {"pt": '<a class="on" href="./">PT</a><a href="en/">EN</a><a href="es/">ES</a>',
             "en": '<a href="../">PT</a><a class="on" href="./">EN</a><a href="../es/">ES</a>',
             "es": '<a href="../">PT</a><a href="../en/">EN</a><a class="on" href="./">ES</a>'}[l]
    bn = "" if l == "pt" else f"-{l}"
    idx = "".join(f'<a href="#s{x["pos"]}"><b>#{x["pos"]}</b>{E(x["nome"])}<small>{E(x["categoria"])}</small></a>' for x in cat)
    cards = "".join(f'<div class="card"><h3>{e} {E(a)}</h3><p>{E(b)}</p></div>' for e, a, b in t["cards"])
    flow = '<span class="arr">→</span>'.join(f"<span>{E(f)}</span>" for f in t["flow"])
    steps = "".join(f'<div class="step"><div class="b">{i}</div><div><h3>{E(a)}</h3><p>{E(b)}</p>' + (f"<pre>{E(c)}</pre>" if c else "") + "</div></div>" for i, (a, b, c) in enumerate(t["steps"], 1))
    vid = ""
    if VIDEOS:
        vid = f'''<section id="videos"><div class="wrap"><span class="chip">{t["vid_chip"]}</span><h2>{t["vid_h"]}</h2><p class="sub">{t["vid_sub"]}</p>
  <div class="vid"><div><iframe src="https://www.youtube-nocookie.com/embed/{VIDEOS["longo"]}" title="skills15" loading="lazy" allowfullscreen></iframe></div>
  <div class="v916"><iframe src="https://www.youtube-nocookie.com/embed/{VIDEOS["short"]}" title="skills15 short" loading="lazy" allowfullscreen></iframe></div></div></div></section>''' if VIDEOS.get("short") else f'''<section id="videos"><div class="wrap"><span class="chip">{t["vid_chip"]}</span><h2>{t["vid_h"]}</h2><p class="sub">{t["vid_sub"]}</p>
  <div><iframe style="width:100%;aspect-ratio:16/9;border:0;border-radius:14px" src="https://www.youtube-nocookie.com/embed/{VIDEOS["longo"]}" title="skills15" loading="lazy" allowfullscreen></iframe></div></div></section>'''
    nav_v = f'<a class="sec" href="#videos">{t["nav"][3]}</a>' if VIDEOS else ""
    sk = "\n".join(ficha(x, t, l) for x in cat)
    return f'''<!DOCTYPE html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(t["title"])}</title>
<meta name="description" content="{E(t["desc"])}">
<link rel="alternate" hreflang="pt-BR" href="{BASE}">
<link rel="alternate" hreflang="en" href="{BASE}en/">
<link rel="alternate" hreflang="es" href="{BASE}es/">
<meta property="og:image" content="{BASE}assets/banner{bn}.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<nav><div class="wrap">
  <a class="brand" href="#top"><span class="emoji">🧰</span> skills15</a>
  <span class="sep">|</span>
  <span class="clubpro"><a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a><span class="sep">-</span><a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a></span>
  <div class="links">
    <a class="sec" href="#indice">{t["nav"][0]}</a>
    <a class="sec" href="#escolher">{t["nav"][1]}</a>
    <a class="sec" href="#guia">{t["nav"][2]}</a>
    {nav_v}
    <span class="lang">{langs}</span>
    <button class="tgl" id="themeToggle" aria-label="Tema" title="Tema">🌙</button>
    <a class="btn" href="{REPO}" target="_blank" rel="noopener">GitHub</a>
  </div>
</div></nav>
<header class="hero" id="top"><div class="glow"></div><div class="wrap">
  <div><span class="chip">{t["chip"]}</span><h1>{t["h1"]}</h1><p class="lead">{E(t["lead"])}</p>
  <div class="cta"><a class="btn" href="#indice">{t["cta1"]}</a><a class="btn ghost" href="{REPO}" target="_blank" rel="noopener">{t["cta2"]}</a></div></div>
  <figure><img src="{p}assets/banner{bn}.jpg" alt="{E(t["alt"])}"></figure>
</div></header>
<section id="resumo" class="resumo"><div class="wrap"><span class="chip">{t["rchip"]}</span><p>{E(t["resumo"])}</p></div></section>
<section id="oque"><div class="wrap"><span class="chip">{t["oq_chip"]}</span><h2>{t["oq_h"]}</h2><p class="sub">{E(t["oq_sub"])}</p>
  <figure style="margin:0 0 26px;border-radius:16px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 80px -30px #000"><img src="{p}assets/banner-grade{bn}.jpg" alt="{E(t["alt"])}" loading="lazy" style="width:100%;display:block"></figure>
  <div class="grid g3">{cards}</div></div></section>
<section id="indice"><div class="wrap"><span class="chip">{t["idx_chip"]}</span><h2>{t["idx_h"]}</h2><p class="sub">{E(t["idx_sub"])}</p><div class="idx">{idx}</div></div></section>
{grafico(cat, t, l)}
<section id="escolher"><div class="wrap"><span class="chip">{t["esc_chip"]}</span><h2>{t["esc_h"]}</h2><p class="sub">{E(t["esc_sub"])}</p><div class="flow">{flow}</div></div></section>
<section id="skills"><div class="wrap">
{sk}
</div></section>
<section id="guia"><div class="wrap"><span class="chip">{t["ins_chip"]}</span><h2>{t["ins_h"]}</h2><p class="sub">{E(t["ins_sub"])}</p>{steps}</div></section>
{vid}
<footer><div class="wrap">
  <div class="pill">Claude Code</div><div class="pill">Agent Skills</div><div class="pill">15 skills</div>
  <p style="margin-top:18px">skills15 · {E(t["foot"])} · <a href="{REPO}">inematds/skills15</a> · <a href="https://inema.club">INEMA.CLUB</a></p>
</div></footer>
<script>
(function(){{var KEY='skills15-theme',b=document.body,t=document.getElementById('themeToggle');
try{{if(localStorage.getItem(KEY)==='light'){{b.classList.add('light');t.textContent='☀️';}}}}catch(e){{}}
t.addEventListener('click',function(){{var l=b.classList.toggle('light');t.textContent=l?'☀️':'🌙';try{{localStorage.setItem(KEY,l?'light':'dark');}}catch(e){{}}}});}})();
</script>
</body>
</html>
'''


if __name__ == "__main__":
    import sys
    for l in (sys.argv[1:] or ["pt", "en", "es"]):
        if not os.path.exists(os.path.join(RAIZ, T[l]["cat"])):
            print("sem", T[l]["cat"]); continue
        d = os.path.join(RAIZ, "guia", T[l]["dir"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(pagina(l))
        print("ok", l)
