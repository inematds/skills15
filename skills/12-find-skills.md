# #12 · Find Skills

**Categoria:** descoberta · **Estrelas (18/10/2026):** 35,5 mil · **Licença:** MIT

**Fonte:** <https://github.com/vercel-labs/skills/tree/main/skills/find-skills>

## O problema

Existem milhares de skills e você não sabe se já tem uma pronta para o que precisa.

## O que faz

Uma skill que procura outras skills. Você pergunta em português comum e ela busca no diretório aberto de skills (skills.sh) e devolve as opções com o comando de instalação de cada uma.

## Como funciona

1. Você pergunta se existe skill para alguma tarefa
2. Ela identifica o assunto e a tarefa
3. Confere o ranking do skills.sh e roda a busca (npx skills find)
4. Filtra por qualidade: número de instalações, quem publicou, estrelas
5. Mostra as opções com o comando para instalar

## Como instalar

npx skills add vercel-labs/skills --skill find-skills. Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 12 --executar`):

```bash
npx skills add vercel-labs/skills --skill find-skills
```

## Exemplo

**Você pede:** Existe uma skill para escrever guias em PDF?

**Volta:** Volta uma lista de skills encontradas, com quantas instalações cada uma tem, quem publicou e o comando npx skills add para instalar.

## Cuidado

Ela só sugere; quem decide instalar é você. A própria skill manda desconfiar de skills com menos de 100 instalações ou de repositórios pequenos.

---

Projetos e cursos gratuitos: https://inema.club
