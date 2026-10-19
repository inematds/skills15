# #5 · Career Ops

**Categoria:** carreira · **Estrelas (18/10/2026):** 75,5 mil · **Licença:** MIT

**Fonte:** <https://github.com/career-ops-hq/career-ops>

## O problema

Mandar 50 currículos e 50 cartas para receber duas respostas.

## O que faz

Um agente de busca de emprego que roda no seu computador. Você cola uma vaga e ele confere se ainda está aberta, dá uma nota de quanto você combina, adapta o currículo e a carta para aquela vaga e rascunha as respostas. Quem revisa e aperta Enviar é você.

## Como funciona

1. Você instala, coloca o seu currículo (cv.md) e conta o que busca
2. Cola o link ou o texto de uma vaga (/career-ops)
3. Ele confere se a vaga continua no ar
4. Dá a nota de encaixe com o seu currículo e avisa quando não vale a pena
5. Gera currículo em PDF, carta e respostas; você revisa e envia

## Como instalar

npx @santifer/career-ops init (cria a pasta career-ops; depois abra o Claude Code dentro dela e use /career-ops). Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 5 --executar`):

```bash
npx @santifer/career-ops init
```

## Exemplo

**Você pede:** /career-ops https://empresa.com/vagas/analista-de-dados

**Volta:** Um relatório dizendo se a vaga está aberta, a nota de encaixe com o seu currículo, um currículo em PDF adaptado e o rascunho das respostas, tudo salvo no seu computador.

## Cuidado

Nunca envia candidatura sozinho. O seu currículo vai para o provedor de IA que você usa. Os números (740 vagas, 68 candidaturas, 12 entrevistas, 1 oferta) são do próprio autor.

---

Projetos e cursos gratuitos: https://inema.club
