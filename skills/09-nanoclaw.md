# #9 · NanoClaw

**Categoria:** assistente · **Estrelas (18/10/2026):** 31 mil · **Licença:** MIT

**Fonte:** <https://github.com/nanocoai/nanoclaw>

## O problema

Ter um assistente de IA pessoal no celular sem entregar a sua vida a um programa enorme que ninguém entende.

## O que faz

Um assistente pessoal que você conversa pelo WhatsApp, Telegram, Slack, Discord, iMessage e outros. Ele lembra do que você contou, roda tarefas agendadas e cada agente trabalha isolado num contêiner próprio. Roda sobre o Claude Agent SDK da Anthropic.

## Como funciona

1. Você baixa o projeto e roda o script de instalação
2. O script instala Node, pnpm e Docker se faltarem e monta o contêiner do agente
3. Liga o seu primeiro canal (WhatsApp, Telegram, Slack...)
4. Você manda mensagem com a palavra de chamada (padrão: @Andy)
5. Ele responde, guarda memória e executa tarefas no horário combinado

## Como instalar

git clone https://github.com/nanocoai/nanoclaw.git nanoclaw-v2 → cd nanoclaw-v2 → bash nanoclaw.sh (rodar no terminal, fora de uma sessão do Claude). Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

Este é um passo manual (dentro do Claude Code ou interativo). `./scripts/instalar.sh 9` mostra o passo.

## Exemplo

**Você pede:** @Andy toda segunda às 8h, junte as notícias de IA da semana e me mande um resumo.

**Volta:** Toda segunda às 8h chega no seu WhatsApp/Telegram uma mensagem com o resumo das notícias.

## Cuidado

É um projeto maior que uma skill: exige Docker e o cadastro da sua credencial da Anthropic. O setup manda diagnósticos anônimos (desliga com NANOCLAW_NO_DIAGNOSTICS=1). A história do acordo com a Docker, do Hacker News e do post do Karpathy não está no README.

---

Projetos e cursos gratuitos: https://inema.club
