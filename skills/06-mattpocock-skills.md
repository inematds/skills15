# #6 · Skills do Matt Pocock

**Categoria:** código · **Estrelas (18/10/2026):** 296 mil · **Licença:** MIT

**Fonte:** <https://github.com/mattpocock/skills>

## O problema

O Claude escreve milhares de linhas em minutos e depois você passa dias descobrindo o que quebrou, porque ele começou antes de entender o que você queria.

## O que faz

O conjunto de skills que o professor de programação Matt Pocock usa todo dia. Elas atacam quatro problemas: o agente não fez o que você queria, fala demais, o código não funciona e o projeto vira uma bagunça. O /grill-me faz perguntas até o plano ficar claro, o /tdd escreve teste antes do código e o /code-review revisa o próprio trabalho.

## Como funciona

1. Você instala o pacote e roda /setup-matt-pocock-skills uma vez por projeto
2. Antes de construir, o /grill-me te entrevista até o plano ficar claro
3. O /tdd escreve o teste primeiro e depois o código que faz passar
4. O /code-review revisa a mudança antes de você aceitar
5. Outras, como /diagnosing-bugs e /improve-codebase-architecture, cuidam de erros e da organização

## Como instalar

claude plugin install mattpocock-skills@claude-plugins-official → depois rodar /setup-matt-pocock-skills no projeto. Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 6 --executar`):

```bash
claude plugin install mattpocock-skills@claude-plugins-official
```

## Exemplo

**Você pede:** /grill-me quero fazer uma página de inscrição para o meu curso.

**Volta:** Em vez de sair programando, o Claude faz uma série de perguntas (quem se inscreve, que dados pedir, o que acontece depois) até o plano ficar fechado.

## Cuidado

Feito para quem programa: o setup pergunta qual sistema de tarefas e etiquetas você usa. Não instalar pelo plugin e pelo skills.sh ao mesmo tempo, senão cada skill aparece duas vezes.

## No INEMA

[trio-skills: Pocock + Addy + pstack organizados](https://inematds.github.io/trio-skills/guia/)

---

Projetos e cursos gratuitos: https://inema.club
