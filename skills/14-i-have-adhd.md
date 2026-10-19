# #14 · I Have ADHD

**Categoria:** respostas · **Estrelas (18/10/2026):** 57,7 mil · **Licença:** MIT

**Fonte:** <https://github.com/ayghri/i-have-adhd>

## O problema

O Claude enrola: escreve três parágrafos antes de dar a resposta que você precisava.

## O que faz

Uma skill com 10 regras que obriga o assistente a começar pela ação, numerar os passos e cortar enfeites. Nada de 'Ótima pergunta!' no começo nem 'Espero ter ajudado' no fim.

## Como funciona

1. Você instala o plugin e chama /i-have-adhd (ou deixa ligado sempre)
2. A resposta começa pela próxima ação: comando, arquivo ou trecho
3. Tarefas com várias etapas vêm numeradas, listas com no máximo 5 itens
4. Sem introdução, sem resumo repetido, sem frase de despedida
5. Termina com um único próximo passo concreto

## Como instalar

claude plugin marketplace add ayghri/i-have-adhd → claude plugin install i-have-adhd@i-have-adhd (depois digite /i-have-adhd). Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 14 --executar`):

```bash
claude plugin marketplace add ayghri/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```

## Exemplo

**Você pede:** Como eu arrumo o meu site que está lento?

**Volta:** Volta uma lista curta e numerada do que fazer, na ordem, e um único próximo passo no final, sem explicação longa antes.

## Cuidado

O nome é só um apelido: não é ferramenta de saúde nem exige diagnóstico. A regra de sempre ligar é opcional (arquivo ~/.claude/.i-have-adhd-always).

---

Projetos e cursos gratuitos: https://inema.club
