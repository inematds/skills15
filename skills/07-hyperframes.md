# #7 · HyperFrames

**Categoria:** vídeo · **Estrelas (18/10/2026):** 66,8 mil · **Licença:** Apache-2.0

**Fonte:** <https://github.com/heygen-com/hyperframes>

## O problema

Fazer um vídeo com título animado, música e cortes leva uma hora num editor, e no fim o tempo ainda fica errado.

## O que faz

Ferramenta de código aberto da HeyGen que transforma páginas HTML com animações em vídeo MP4. Você descreve o vídeo em palavras e o agente monta, confere e renderiza, com títulos, animações, vídeo de fundo e música.

## Como funciona

1. Você descreve o vídeo em linguagem comum
2. O agente planeja as cenas e escreve o vídeo como página HTML
3. Adiciona animações, mídia e música
4. Confere e mostra uma prévia no navegador
5. Renderiza: o navegador captura quadro a quadro e o FFmpeg gera o MP4

## Como instalar

claude plugin marketplace add heygen-com/hyperframes → claude plugin install hyperframes@hyperframes (depois use /hyperframes:hyperframes). Precisa de Node.js 22+ e FFmpeg. Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 7 --executar`):

```bash
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```

## Exemplo

**Você pede:** Usando o /hyperframes, crie uma abertura de 10 segundos para o meu produto com título aparecendo devagar, vídeo de fundo e música suave.

**Volta:** Um arquivo MP4 pronto com o título animado, o fundo e a trilha.

## Cuidado

Exige Node.js 22+ e FFmpeg instalados. A HeyGen também vende serviços pagos; o HyperFrames em si é aberto e roda local.

## No INEMA

[explicavideos: o motor de vídeo do INEMA (usa HyperFrames)](https://inematds.github.io/explicavideos/guia/)

---

Projetos e cursos gratuitos: https://inema.club
