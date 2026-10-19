# #3 · AI Website Cloner

**Categoria:** web · **Estrelas (18/10/2026):** 37 mil · **Licença:** MIT

**Fonte:** <https://github.com/JCodesMore/ai-website-cloner-template>

## O problema

Refazer um site (fontes, cores, layout) pode levar dias de um designer ou desenvolvedor.

## O que faz

Um projeto modelo com a skill /clone-website: você passa o endereço e o agente recria o site como um aplicativo Next.js limpo e editável, com as mesmas fontes, cores e estrutura. Parte do site real, não de um print.

## Como funciona

1. Mapear: liga as páginas do site original às páginas do projeto
2. Observar: examina o site no computador e no celular e extrai imagens e fontes reais
3. Construir: monta os componentes e as interações
4. Comparar: põe original e cópia lado a lado, corrige as diferenças e roda a checagem final

## Como instalar

Colar no Claude Code: 'Set up https://github.com/JCodesMore/ai-website-cloner-template as a standalone project in a new folder on my computer...' (prompt do README) e depois, dentro do projeto: /clone-website https://seusite.com. Precisa de Node.js 24+.

Este é um passo manual (dentro do Claude Code ou interativo). `./scripts/instalar.sh 3` mostra o passo.

## Exemplo

**Você pede:** /clone-website https://meusite-antigo.com.br

**Volta:** Um projeto Next.js com o site recriado, prints comparando original e cópia e a lista do que ainda ficou diferente.

## Cuidado

Clone só site seu ou que você tem permissão. O README proíbe golpe (phishing), se passar por outra marca e copiar design alheio como seu; logos e textos pertencem aos donos.

---

Projetos e cursos gratuitos: https://inema.club
