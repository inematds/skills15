# #2 · Anatomy

**Categoria:** visual · **Estrelas (18/10/2026):** 16,1 mil · **Licença:** MIT

**Fonte:** <https://github.com/wheresryan22/anatomy>

## O problema

Você pergunta como algo funciona e recebe um paredão de texto; pergunta de novo e o paredão cresce.

## O que faz

Em vez de explicar com texto, constrói um objeto ilustrado e interativo (vista isométrica) cujo funcionamento é a própria ideia. Você mexe com o mouse, aproxima e desmonta peça por peça no navegador. Exemplo da galeria: o motor de foguete Raptor da SpaceX, ligando e depois se desmontando em 11 partes.

## Como funciona

1. Você pede /anatomy e a sua pergunta
2. O Claude inventa um objeto físico que mostra a ideia funcionando
3. Monta o objeto com dezenas de peças pequenas e sombreadas, num cartão com título e leitura ao vivo
4. Confere o próprio trabalho dando zoom em cada encaixe
5. Entrega uma página HTML (ou SVG) que você abre e explora no navegador

## Como instalar

npx skills add wheresryan22/anatomy -g -a claude-code (depois: /anatomy e a pergunta). Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 2 --executar`):

```bash
npx skills add wheresryan22/anatomy -g -a claude-code
```

## Exemplo

**Você pede:** /anatomy explique como funciona um limitador de requisições, interativo.

**Volta:** Uma página no navegador com uma máquina ilustrada que mostra o mecanismo funcionando; você passa o mouse e ela se mexe e mostra os números.

## Cuidado

É lento de propósito: cada figura leva uma sessão longa (o Raptor leva alguns minutos). Desenha máquinas, instrumentos e objetos, não pessoas nem mapas exatos. O modo 3D ainda é beta.

---

Projetos e cursos gratuitos: https://inema.club
