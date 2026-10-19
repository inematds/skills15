#!/usr/bin/env bash
# Checagens do catálogo: 15 itens, ordem 15→1, fichas, links e instalador. Uso: bash tests/run.sh
cd "$(dirname "$0")/.."
ok=0; falha=0
t() { if eval "$2" >/dev/null 2>&1; then echo "OK   $1"; ok=$((ok+1)); else echo "FALHA $1"; falha=$((falha+1)); fi; }
t "catalogo.json carrega com 15 itens" "python3 -c 'import json;assert len(json.load(open(\"catalogo.json\")))==15'"
t "posições 15..1 em ordem" "python3 -c 'import json;assert [x[\"pos\"] for x in json.load(open(\"catalogo.json\"))]==list(range(15,0,-1))'"
t "slugs únicos" "python3 -c 'import json;s=[x[\"slug\"] for x in json.load(open(\"catalogo.json\"))];assert len(set(s))==15'"
t "campos obrigatórios preenchidos" "python3 -c '
import json
for x in json.load(open(\"catalogo.json\")):
  for k in (\"nome\",\"url\",\"problema\",\"o_que_faz\",\"instalar\",\"exemplo_pedido\",\"exemplo_resultado\"): assert x[k], (x[\"slug\"],k)
  assert 3<=len(x[\"como_funciona\"])<=5, x[\"slug\"]'"
t "15 fichas em skills/" "[ \$(ls skills/*.md | wc -l) -eq 15 ]"
t "toda ficha tem as seções" "for f in skills/*.md; do grep -q '## Como instalar' \$f && grep -q '## Exemplo' \$f && grep -q '## Como funciona' \$f || exit 1; done"
t "repos apontam para github.com/<repo>" "python3 -c '
import json
for x in json.load(open(\"catalogo.json\")):
  if x[\"repo\"]: assert x[\"url\"].startswith(\"https://github.com/\"+x[\"repo\"]), x[\"slug\"]'"
t "README PT/EN/ES existem e linkam entre si" "grep -q README.en.md README.md && grep -q README.es.md README.md && [ -f README.en.md ] && [ -f README.es.md ]"
t "tabela do README tem 15 linhas" "[ \$(sed -n '/<!-- tabela -->/,/<!-- \/tabela -->/p' README.md | grep -c '^| [0-9]') -eq 15 ]"
t "instalador lista as 15" "[ \$(./scripts/instalar.sh | grep -c '^ *[0-9]') -eq 15 ]"
t "instalador não executa sem --executar" "./scripts/instalar.sh 12 | grep -q 'nada foi executado'"
t "instalador recusa número inválido" "! ./scripts/instalar.sh 16"
t "guia PT/EN/ES existem" "[ -f guia/index.html ] && [ -f guia/en/index.html ] && [ -f guia/es/index.html ]"
t "guia cita as 15 skills" "python3 -c '
import json,re
h=open(\"guia/index.html\").read()
for x in json.load(open(\"catalogo.json\")): assert x[\"url\"] in h, x[\"slug\"]'"
echo; echo "$ok OK, $falha falha(s)"; [ $falha -eq 0 ]
