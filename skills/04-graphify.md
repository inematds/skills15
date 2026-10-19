# #4 · Graphify

**Categoria:** conhecimento · **Estrelas (18/10/2026):** 128 mil · **Licença:** Apache-2.0

**Fonte:** <https://github.com/Graphify-Labs/graphify>

## O problema

Notas, PDFs, prints, vídeos e código numa mesma pasta, e ninguém sabe o que liga com o quê.

## O que faz

Você digita /graphify e ele lê a pasta inteira e monta um mapa (grafo de conhecimento) de como cada coisa se liga. Depois o agente consulta esse mapa em vez de reler todos os arquivos.

## Como funciona

1. Você roda /graphify . na pasta
2. O código é lido localmente, sem IA e sem sair do computador
3. Documentos, PDFs, imagens e vídeos passam pelo modelo do seu assistente para extrair o sentido
4. Cada ligação é marcada como lida direto da fonte ou deduzida
5. Saem três arquivos: o mapa clicável (graph.html), um relatório e o grafo completo para consultas

## Como instalar

uv tool install graphifyy → graphify install (detecta o assistente e registra a skill) → no Claude Code: /graphify . — precisa de Python 3.10+ e uv (ou pipx). Também vale: colar o link no Claude Code e dizer 'instale isso para mim'.

No terminal (ou `./scripts/instalar.sh 4 --executar`):

```bash
uv tool install graphifyy
graphify install
```

## Exemplo

**Você pede:** /graphify . e depois me diga como o módulo de pagamentos se conecta com o de e-mails.

**Volta:** Um mapa clicável no navegador mais a resposta com o caminho entre os dois módulos e os arquivos envolvidos.

## Cuidado

Atenção ao nome do pacote: graphifyy (com dois y). Arquivos que não são código usam o modelo do assistente (gasta uso). Os '80% menos tokens' do README são da versão paga (Graphify Cloud). A dúvida sobre estrelas e os '75% menos tokens' vêm de comentários citados no vídeo, não do README.

---

Projetos e cursos gratuitos: https://inema.club
