# skills15 — as 15 skills para o Claude que valem a pena

[![skills15](guia/assets/banner.jpg)](https://inematds.github.io/skills15/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

Existem mais de um milhão de skills para agentes de IA, e a maioria não serve para nada. Este repositório reúne as **15 que valem a pena** para quem usa o Claude Code (e outros agentes): o problema que cada uma resolve, como funciona por dentro, o comando oficial de instalação, um exemplo de pedido e o link para o projeto original. Serve para quem quer escolher **uma** skill para a dor de hoje, sem instalar tudo de uma vez.

## 📖 Guia de uso

Landing + guia com as 15, exemplos e vídeo: **https://inematds.github.io/skills15/guia/**

## As 15 (da 15ª para a 1ª)

<!-- tabela -->
| # | Skill | Para quê | ★ 18/10 | Problema que resolve |
|---|---|---|---|---|
| 15 | [NotebookLM](skills/15-notebooklm-py.md) | economia de tokens | 19,8 mil | Quando você joga muitos PDFs no Claude, ele lê tudo palavra por palavra e o seu limite de uso acaba rápido. |
| 14 | [I Have ADHD](skills/14-i-have-adhd.md) | respostas | 57,7 mil | O Claude enrola: escreve três parágrafos antes de dar a resposta que você precisava. |
| 13 | [Billion Context](skills/13-billion-context.md) | economia de tokens | 1,9 mil | Em conversa longa, a cada mensagem o modelo relê tudo desde o início, e isso consome o limite muito rápido. |
| 12 | [Find Skills](skills/12-find-skills.md) | descoberta | 35,5 mil | Existem milhares de skills e você não sabe se já tem uma pronta para o que precisa. |
| 11 | [De-AI Writing](skills/11-de-ai-writing.md) | escrita | — | Texto com cara de IA ('situado no coração da cidade, um testemunho da rica herança cultural') faz o leitor desconfiar e parar de ler. |
| 10 | [Archify](skills/10-archify.md) | diagramas | 85,4 mil | Explicar como funciona uma automação, um sistema ou um plano numa reunião, e o cliente só balança a cabeça sem entender. |
| 9 | [NanoClaw](skills/09-nanoclaw.md) | assistente | 31 mil | Ter um assistente de IA pessoal no celular sem entregar a sua vida a um programa enorme que ninguém entende. |
| 8 | [CLAUDE.md do Karpathy](skills/08-karpathy-claude-md.md) | regras | 220 mil | Você pede para o Claude mudar uma linha e ele reescreve metade do projeto e ainda inventa recursos que ninguém pediu. |
| 7 | [HyperFrames](skills/07-hyperframes.md) | vídeo | 66,8 mil | Fazer um vídeo com título animado, música e cortes leva uma hora num editor, e no fim o tempo ainda fica errado. |
| 6 | [Skills do Matt Pocock](skills/06-mattpocock-skills.md) | código | 296 mil | O Claude escreve milhares de linhas em minutos e depois você passa dias descobrindo o que quebrou, porque ele começou antes de entender o que você queria. |
| 5 | [Career Ops](skills/05-career-ops.md) | carreira | 75,5 mil | Mandar 50 currículos e 50 cartas para receber duas respostas. |
| 4 | [Graphify](skills/04-graphify.md) | conhecimento | 128 mil | Notas, PDFs, prints, vídeos e código numa mesma pasta, e ninguém sabe o que liga com o quê. |
| 3 | [AI Website Cloner](skills/03-ai-website-cloner.md) | web | 37 mil | Refazer um site (fontes, cores, layout) pode levar dias de um designer ou desenvolvedor. |
| 2 | [Anatomy](skills/02-anatomy.md) | visual | 16,1 mil | Você pergunta como algo funciona e recebe um paredão de texto; pergunta de novo e o paredão cresce. |
| 1 | [REA (Reverse Engineer Anything)](skills/01-rea.md) | engenharia reversa | 323 mil | Você vê um recurso no aplicativo de outra pessoa e quer no seu, mas não tem o código, então chuta e erra. |
<!-- /tabela -->

Estrelas contadas no GitHub em 18/10/2026. A #11 não tem repositório: é um post do Reddit (a alternativa instalável é o [Humanizer](https://github.com/blader/humanizer)).

## Como instalar qualquer uma

O jeito universal: copie o link do repositório, cole no Claude Code e diga **"instale isso para mim"**.

Ou use o instalador deste repo, que só mostra os comandos oficiais (e roda se você pedir):

```bash
git clone https://github.com/inematds/skills15.git && cd skills15
./scripts/instalar.sh              # lista as 15
./scripts/instalar.sh 12           # mostra como instalar a #12 (find-skills)
./scripts/instalar.sh 12 --executar  # roda os comandos de terminal da #12
```

> Não instale todas. Cada skill a mais é contexto que o agente carrega e pode disparar sem você querer. Escolha a que resolve o seu problema de hoje.

## Conteúdo

| arquivo | o quê |
|---|---|
| `catalogo.json` | as 15 em dados (problema, como funciona, instalação, exemplo, cuidado, link) |
| `skills/NN-nome.md` | uma ficha por skill |
| `scripts/instalar.sh` | mostra/roda o comando oficial de cada uma |
| `scripts/gerar.py` | regenera as fichas e a tabela a partir do catálogo |
| `tests/run.sh` | checagens do catálogo, fichas e guia |
| `guia/` | landing + guia (PT/EN/ES) |

## Licenças

Este repositório **não copia** o código das skills: cada uma continua no projeto original, com a licença dele (a maioria MIT; HyperFrames e Graphify são Apache-2.0; o CLAUDE.md do Karpathy e o billion-context não declaram licença reconhecida pelo GitHub). O texto deste catálogo é MIT.

## No INEMA

- REA (a #1) explicado e testado: https://inematds.github.io/rea-engenharia-reversa/guia/
- Skills do Matt Pocock (a #6) organizadas com Addy e pstack: https://inematds.github.io/trio-skills/guia/
- HyperFrames (a #7) é o motor dos vídeos do INEMA: https://inematds.github.io/explicavideos/guia/

Projetos e cursos gratuitos: https://inema.club
