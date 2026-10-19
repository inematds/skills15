#!/usr/bin/env python3
"""Gera as fichas (skills/NN-slug.md) e a tabela do README a partir do catalogo.json.
Uso: python3 scripts/gerar.py   (rode na raiz do repo; idempotente)"""
import json, os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = json.load(open(os.path.join(RAIZ, "catalogo.json")))

# comandos de terminal (o que o instalar.sh executa); [] = passo manual dentro do Claude
SHELL = {
    "notebooklm-py": ['uv tool install "notebooklm-py[browser]"', "notebooklm login", "notebooklm skill install"],
    "i-have-adhd": ["claude plugin marketplace add ayghri/i-have-adhd", "claude plugin install i-have-adhd@i-have-adhd"],
    "billion-context": ["claude plugin marketplace add ranxianglei/billion-context", "claude plugin install billion-context@billion-context"],
    "find-skills": ["npx skills add vercel-labs/skills --skill find-skills"],
    "de-ai-writing": ["claude plugin marketplace add blader/humanizer", "claude plugin install humanizer@humanizer"],
    "archify": ["npx skills add tt-a1i/archify -g"],
    "nanoclaw": [],
    "karpathy-claude-md": ["claude plugin marketplace add forrestchang/andrej-karpathy-skills", "claude plugin install andrej-karpathy-skills@karpathy-skills"],
    "hyperframes": ["claude plugin marketplace add heygen-com/hyperframes", "claude plugin install hyperframes@hyperframes"],
    "mattpocock-skills": ["claude plugin install mattpocock-skills@claude-plugins-official"],
    "career-ops": ["npx @santifer/career-ops init"],
    "graphify": ["uv tool install graphifyy", "graphify install"],
    "ai-website-cloner": [],
    "anatomy": ["npx skills add wheresryan22/anatomy -g -a claude-code"],
    "rea": ["npx rea-agents setup"],
}
# conteúdo próprio do INEMA sobre a skill
INEMA = {
    "rea": ("Guia completo do REA no INEMA (testes de verdade, vídeos)", "https://inematds.github.io/rea-engenharia-reversa/guia/"),
    "mattpocock-skills": ("trio-skills: Pocock + Addy + pstack organizados", "https://inematds.github.io/trio-skills/guia/"),
    "hyperframes": ("explicavideos: o motor de vídeo do INEMA (usa HyperFrames)", "https://inematds.github.io/explicavideos/guia/"),
}


def mil(n):
    if n is None:
        return "—"
    return f"{n/1000:.1f} mil".replace(".0 mil", " mil").replace(".", ",") if n < 100000 else f"{n//1000} mil"


def ficha(x):
    n = f"{x['pos']:02d}"
    sh = SHELL[x["slug"]]
    linhas = [f"# #{x['pos']} · {x['nome']}", "",
              f"**Categoria:** {x['categoria']} · **Estrelas (18/10/2026):** {mil(x['estrelas'])} · **Licença:** {x['licenca'] or '—'}", "",
              f"**Fonte:** <{x['url']}>", "",
              "## O problema", "", x["problema"], "",
              "## O que faz", "", x["o_que_faz"], "",
              "## Como funciona", ""] + [f"{i}. {p}" for i, p in enumerate(x["como_funciona"], 1)] + [
              "", "## Como instalar", "", x["instalar"], ""]
    if sh:
        linhas += ["No terminal (ou `./scripts/instalar.sh " + str(x["pos"]) + " --executar`):", "", "```bash", *sh, "```", ""]
    else:
        linhas += ["Este é um passo manual (dentro do Claude Code ou interativo). `./scripts/instalar.sh " + str(x["pos"]) + "` mostra o passo.", ""]
    linhas += ["## Exemplo", "", f"**Você pede:** {x['exemplo_pedido']}", "", f"**Volta:** {x['exemplo_resultado']}", ""]
    if x.get("cuidado"):
        linhas += ["## Cuidado", "", x["cuidado"], ""]
    if x["slug"] in INEMA:
        t, u = INEMA[x["slug"]]
        linhas += ["## No INEMA", "", f"[{t}]({u})", ""]
    linhas += ["---", "", "Projetos e cursos gratuitos: https://inema.club", ""]
    p = os.path.join(RAIZ, "skills", f"{n}-{x['slug']}.md")
    open(p, "w").write("\n".join(linhas))
    return f"| {x['pos']} | [{x['nome']}](skills/{n}-{x['slug']}.md) | {x['categoria']} | {mil(x['estrelas'])} | {x['problema']} |"


if __name__ == "__main__":
    os.makedirs(os.path.join(RAIZ, "skills"), exist_ok=True)
    for x in CAT:
        x["instalar_shell"] = SHELL[x["slug"]]
        if x["slug"] in INEMA:
            x["inema"] = {"titulo": INEMA[x["slug"]][0], "url": INEMA[x["slug"]][1]}
    tab = ["| # | Skill | Para quê | ★ 18/10 | Problema que resolve |", "|---|---|---|---|---|"] + [ficha(x) for x in CAT]
    json.dump(CAT, open(os.path.join(RAIZ, "catalogo.json"), "w"), ensure_ascii=False, indent=1)
    rd = os.path.join(RAIZ, "README.md")
    if os.path.exists(rd):
        s = open(rd).read()
        s = re.sub(r"<!-- tabela -->.*<!-- /tabela -->", "<!-- tabela -->\n" + "\n".join(tab) + "\n<!-- /tabela -->", s, flags=re.S)
        open(rd, "w").write(s)
    print(len(CAT), "fichas")
