#!/usr/bin/env bash
# Mostra (e, com --executar, roda) os comandos OFICIAIS de instalação de uma skill do catálogo.
# Uso: ./scripts/instalar.sh            → lista as 15
#      ./scripts/instalar.sh 12         → mostra como instalar a #12
#      ./scripts/instalar.sh 12 --executar → roda os comandos de terminal da #12
# Nada roda sem --executar. Os comandos vêm do README de cada projeto (catalogo.json).
set -euo pipefail
cd "$(dirname "$0")/.."
POS="${1:-}"; EXEC="${2:-}"
if [ -z "$POS" ]; then
  python3 -c "
import json
for x in json.load(open('catalogo.json')): print(f\"{x['pos']:>2}  {x['nome']:<22} {x['categoria']}\")"
  echo; echo "Ver uma: ./scripts/instalar.sh <número>"; exit 0
fi
python3 - "$POS" > /tmp/skills15-cmds.$$ <<'EOF'
import json, sys
p = int(sys.argv[1])
x = next((x for x in json.load(open('catalogo.json')) if x['pos'] == p), None)
if not x: sys.exit(f"não existe a #{p} (1 a 15)")
print(f"# #{x['pos']} {x['nome']} — {x['url']}", file=sys.stderr)
print(f"# {x['instalar']}", file=sys.stderr)
for c in x['instalar_shell']: print(c)
EOF
if [ ! -s /tmp/skills15-cmds.$$ ]; then echo "(passo manual ou interativo: siga o texto acima)"; rm -f /tmp/skills15-cmds.$$; exit 0; fi
echo "Comandos:"; sed 's/^/  $ /' /tmp/skills15-cmds.$$
if [ "$EXEC" = "--executar" ]; then
  while IFS= read -r c; do echo "→ $c"; bash -c "$c"; done < /tmp/skills15-cmds.$$
else
  echo "(nada foi executado; acrescente --executar para rodar)"
fi
rm -f /tmp/skills15-cmds.$$
