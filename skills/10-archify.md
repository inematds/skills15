# #10 · Archify

**Categoria:** diagramas · **Estrelas (18/10/2026):** 85,4 mil · **Licença:** MIT

**Fonte:** <https://github.com/tt-a1i/archify>

## O problema

Explicar como funciona uma automação, um sistema ou um plano numa reunião, e o cliente só balança a cabeça sem entender.

## O que faz

Transforma uma descrição em uma frase (ou um código existente) em um diagrama interativo num único arquivo HTML. Quem recebe clica em cada etapa, segue caminhos e vê o que acontece depois, sem instalar nada.

## Como funciona

1. Você descreve o processo em uma frase (não precisa de código)
2. O agente monta a estrutura do diagrama
3. Verificadores embutidos conferem e corrigem a estrutura
4. Sai um único arquivo HTML que abre no navegador
5. Você pede ajustes na conversa: 'destaque esse caminho', 'tema claro'

## Como instalar

npx skills add tt-a1i/archify -g. Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 10 --executar`):

```bash
npx skills add tt-a1i/archify -g
```

## Exemplo

**Você pede:** Use o Archify para desenhar como funciona o meu atendimento: o cliente manda mensagem no WhatsApp, o agente responde e, se não souber, passa para um humano.

**Volta:** Um arquivo HTML com o fluxo desenhado; dá para clicar em cada etapa, ver os detalhes e seguir o caminho de ponta a ponta.

## Cuidado

Pode consultar um endereço fixo uma vez por dia só para avisar de atualização (desliga com ARCHIFY_UPDATE_CHECK_DISABLED=1). Serviços pagos de terceiros com o nome não são do projeto.

---

Projetos e cursos gratuitos: https://inema.club
