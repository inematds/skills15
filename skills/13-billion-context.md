# #13 · Billion Context

**Categoria:** economia de tokens · **Estrelas (18/10/2026):** 1,9 mil · **Licença:** não identificada pelo GitHub (NOASSERTION)

**Fonte:** <https://github.com/ranxianglei/billion-context>

## O problema

Em conversa longa, a cada mensagem o modelo relê tudo desde o início, e isso consome o limite muito rápido.

## O que faz

Fica no meio do caminho entre o seu assistente e o modelo e comprime a parte antiga da conversa em resumos detalhados. O próprio modelo decide quando e o que resumir, e pode desfazer o resumo se precisar do detalhe de volta.

## Como funciona

1. Você instala o comando bili e liga o Claude Code por ele
2. Cada pedido passa por um intermediário (proxy) antes de ir ao modelo
3. O intermediário dá ao modelo ferramentas para comprimir, descomprimir e buscar no histórico
4. Trechos antigos viram resumos; o importante fica, o resto sai
5. Você continua conversando e a compressão acontece por trás

## Como instalar

No Claude Code: /plugin marketplace add ranxianglei/billion-context → /plugin install billion-context@billion-context → /billion-context:bili-setup (e reiniciar). Alternativa: npm install -g billion-context --prefix=~/.local e depois bili claude. Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 13 --executar`):

```bash
claude plugin marketplace add ranxianglei/billion-context
claude plugin install billion-context@billion-context
```

## Exemplo

**Você pede:** Instale o billion-context e abra o Claude Code por ele para eu continuar este projeto na mesma conversa.

**Volta:** A conversa segue normalmente; as partes antigas são resumidas em segundo plano e o comando /acp mostra quanto do contexto está em uso.

## Cuidado

Os números (5 vezes menos tokens, sessões de meses, 174 mil chamadas em 4,5 meses) são do próprio autor, no artigo dele; ninguém de fora mediu. Ele intercepta o tráfego entre o assistente e o modelo (proxy, em alguns modos com certificado próprio), então teste antes de usar em coisa séria.

---

Projetos e cursos gratuitos: https://inema.club
