# #11 · De-AI Writing

**Categoria:** escrita · **Estrelas (18/10/2026):** — · **Licença:** —

**Fonte:** <https://www.reddit.com/r/claudeskills/comments/1wpbkmy/a_free_claude_skill_to_deai_your_written_content/>

## O problema

Texto com cara de IA ('situado no coração da cidade, um testemunho da rica herança cultural') faz o leitor desconfiar e parar de ler.

## O que faz

Instruções publicadas no Reddit que viram uma skill para reescrever texto tirando as marcas de escrita de IA. A base é a lista 'Signs of AI writing' da Wikipedia, mantida pelo WikiProject AI Cleanup. Quem quer instalar com um comando pode usar o Humanizer (blader/humanizer), que usa a mesma base.

## Como funciona

1. Você copia as instruções do post do Reddit
2. Cola no Claude e diz 'transforme isso em skill'
3. Manda o seu texto para a skill
4. Ela troca as marcas de IA (palavras da moda, travessões em excesso, frases de efeito) por frases diretas
5. Mostra o que mudou para você desfazer o que não gostar

## Como instalar

Não tem repositório: copiar as instruções do post do Reddit, colar no Claude e dizer 'transforme isso em skill'. Alternativa instalável com a mesma base (Humanizer): /plugin marketplace add blader/humanizer → /plugin install humanizer@humanizer.

No terminal (ou `./scripts/instalar.sh 11 --executar`):

```bash
claude plugin marketplace add blader/humanizer
claude plugin install humanizer@humanizer
```

## Exemplo

**Você pede:** Reescreva este texto do meu café sem cara de IA: 'Situado no coração da cidade, nosso café é um testemunho da rica herança cultural da região.'

**Volta:** Algo como 'Nosso café fica na praça principal, num prédio que é padaria desde 1911', com a lista do que foi trocado.

## Cuidado

Não há código nem repositório para conferir; o conteúdo do post não foi verificado aqui. A promessa de reduzir a detecção de IA em 70 a 95% é do autor do post. O README do Humanizer, que usa a mesma base, diz o contrário: enganar detector não é objetivo e os detectores ainda marcam a maior parte do texto dele.

---

Projetos e cursos gratuitos: https://inema.club
