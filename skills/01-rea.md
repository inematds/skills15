# #1 · REA (Reverse Engineer Anything)

**Categoria:** engenharia reversa · **Estrelas (18/10/2026):** 323 mil · **Licença:** MIT

**Fonte:** <https://github.com/morluto/rea>

## O problema

Você vê um recurso no aplicativo de outra pessoa e quer no seu, mas não tem o código, então chuta e erra.

## O que faz

Conecta o seu agente a ferramentas que examinam um aplicativo pronto sem precisar do código-fonte. O agente descobre como o recurso funciona, mostra as provas de cada conclusão e constrói uma versão parecida no seu projeto.

## Como funciona

1. Você roda o setup, que liga o REA ao seu agente (via MCP)
2. Pede para investigar um recurso de um aplicativo
3. O REA examina o aplicativo (programas nativos, apps JavaScript/Electron, .NET, sites) no seu computador
4. Devolve o que achou com as provas e o que ficou sem resposta
5. O agente explica o funcionamento e escreve e testa uma versão no seu projeto

## Como instalar

npx rea-agents setup (escolher o Claude Code, aprovar as mudanças e reiniciar o agente). Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 1 --executar`):

```bash
npx rea-agents setup
```

## Exemplo

**Você pede:** Entenda como funciona a busca no app de Notas, me mostre as provas e construa algo parecido no meu projeto.

**Volta:** Uma explicação de como a busca funciona por dentro, com os trechos e referências que provam cada ponto, e uma versão parecida implementada e testada no seu projeto.

## Cuidado

Só para software que é seu ou que você tem autorização para examinar (pesquisa, ensino, compatibilidade); o README pede uso legal. Análise de programas nativos pode precisar de ferramentas como Hopper, Ghidra ou IDA, e as comerciais exigem licença. Baixe só das fontes oficiais (morluto/rea, rea.tools, pacote npm rea-agents).

## No INEMA

[Guia completo do REA no INEMA (testes de verdade, vídeos)](https://inematds.github.io/rea-engenharia-reversa/guia/)

---

Projetos e cursos gratuitos: https://inema.club
