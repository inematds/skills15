# #8 · CLAUDE.md do Karpathy

**Categoria:** regras · **Estrelas (18/10/2026):** 220 mil · **Licença:** MIT (declarada no README; o GitHub não detecta arquivo de licença)

**Fonte:** <https://github.com/multica-ai/andrej-karpathy-skills>

## O problema

Você pede para o Claude mudar uma linha e ele reescreve metade do projeto e ainda inventa recursos que ninguém pediu.

## O que faz

Um único arquivo CLAUDE.md com quatro regras, tiradas das observações de Andrej Karpathy sobre os erros dos modelos ao programar: pensar antes de codar, simplicidade primeiro, mudanças cirúrgicas e execução guiada por objetivo.

## Como funciona

1. Pensar antes de codar: dizer as suposições e perguntar quando estiver em dúvida
2. Simplicidade primeiro: o mínimo de código que resolve, nada a mais
3. Mudanças cirúrgicas: mexer só no que foi pedido
4. Execução guiada por objetivo: transformar o pedido em meta verificável (ex.: um teste que precisa passar)

## Como instalar

/plugin marketplace add forrestchang/andrej-karpathy-skills → /plugin install andrej-karpathy-skills@karpathy-skills (ou baixar o CLAUDE.md para a pasta do projeto: curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md). Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 8 --executar`):

```bash
claude plugin marketplace add forrestchang/andrej-karpathy-skills
claude plugin install andrej-karpathy-skills@karpathy-skills
```

## Exemplo

**Você pede:** Corrija só o erro de digitação no título da página inicial.

**Volta:** O Claude muda só aquela linha e não mexe no resto; se tiver dúvida, pergunta antes.

## Cuidado

Não foi escrito pelo Karpathy: é um arquivo 'inspirado' num post dele, feito por outro autor (forrestchang, hoje na organização multica-ai). O README avisa que deixa o Claude mais cauteloso e um pouco mais lento em tarefas triviais.

---

Projetos e cursos gratuitos: https://inema.club
