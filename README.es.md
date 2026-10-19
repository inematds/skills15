# skills15 — las 15 skills para Claude que valen la pena

[![skills15](guia/assets/banner-es.jpg)](https://inematds.github.io/skills15/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Hay más de un millón de skills para agentes de IA, y la mayoría no sirve para nada. Este repositorio reúne las **15 que valen la pena** para quienes usan Claude Code (y otros agentes): el problema que resuelve cada una, cómo funciona por dentro, el comando oficial de instalación, un ejemplo de solicitud y el enlace al proyecto original. Sirve para quien quiere elegir **una** skill para el problema de hoy, sin instalarlo todo de una vez.

## 📖 Guía de uso

Landing + guía con las 15, ejemplos y vídeo: **https://inematds.github.io/skills15/guia/es/**

## Las 15 (de la 15.ª a la 1.ª)

<!-- tabela -->
| # | Skill | Para qué | ★ 18/10 | Problema que resuelve |
|---|---|---|---|---|
| 15 | [NotebookLM](skills/15-notebooklm-py.md) | ahorro de tokens | 19,8 mil | Cuando le pasas muchos PDF a Claude, los lee palabra por palabra y tu límite de uso se agota rápido. |
| 14 | [I Have ADHD](skills/14-i-have-adhd.md) | respuestas | 57,7 mil | Claude se enrolla: escribe tres párrafos antes de dar la respuesta que necesitabas. |
| 13 | [Billion Context](skills/13-billion-context.md) | ahorro de tokens | 1,9 mil | En una conversación larga, con cada mensaje el modelo vuelve a leerlo todo desde el principio, y eso consume el límite muy rápido. |
| 12 | [Find Skills](skills/12-find-skills.md) | descubrimiento | 35,5 mil | Hay miles de skills y no sabes si ya tienes una lista para lo que necesitas. |
| 11 | [De-AI Writing](skills/11-de-ai-writing.md) | escritura | — | Un texto con aire de IA («situado en el corazón de la ciudad, testimonio de una rica herencia cultural») hace que el lector desconfíe y deje de leer. |
| 10 | [Archify](skills/10-archify.md) | diagramas | 85,4 mil | Explicar cómo funciona una automatización, un sistema o un plan en una reunión, y que el cliente solo asienta sin entender. |
| 9 | [NanoClaw](skills/09-nanoclaw.md) | asistente | 31 mil | Tener un asistente personal de IA en el móvil sin entregar tu vida a un programa enorme que nadie entiende. |
| 8 | [CLAUDE.md do Karpathy](skills/08-karpathy-claude-md.md) | reglas | 220 mil | Le pides a Claude que cambie una línea y reescribe la mitad del proyecto, además de inventar funciones que nadie pidió. |
| 7 | [HyperFrames](skills/07-hyperframes.md) | vídeo | 66,8 mil | Hacer un vídeo con título animado, música y cortes lleva una hora en un editor, y al final la duración sigue estando mal. |
| 6 | [Skills do Matt Pocock](skills/06-mattpocock-skills.md) | código | 296 mil | Claude escribe miles de líneas en minutos y luego pasas días descubriendo qué se rompió, porque empezó antes de entender lo que querías. |
| 5 | [Career Ops](skills/05-career-ops.md) | carrera | 75,5 mil | Enviar 50 currículums y 50 cartas para recibir dos respuestas. |
| 4 | [Graphify](skills/04-graphify.md) | conocimiento | 128 mil | Notas, PDF, capturas, vídeos y código en una misma carpeta, y nadie sabe qué está relacionado con qué. |
| 3 | [AI Website Cloner](skills/03-ai-website-cloner.md) | web | 37 mil | Recrear un sitio web (fuentes, colores, diseño) puede llevar días a un diseñador o desarrollador. |
| 2 | [Anatomy](skills/02-anatomy.md) | visual | 16,1 mil | Preguntas cómo funciona algo y recibes un muro de texto; vuelves a preguntar y el muro crece. |
| 1 | [REA (Reverse Engineer Anything)](skills/01-rea.md) | ingeniería inversa | 323 mil | Ves una función en la aplicación de otra persona y la quieres en la tuya, pero no tienes el código, así que improvisas y te equivocas. |
<!-- /tabela -->

(las fichas de skills/ están en portugués)

Estrellas contadas en GitHub el 18/10/2026. La #11 no tiene repositorio: es una publicación de Reddit (la alternativa instalable es [Humanizer](https://github.com/blader/humanizer)).

## Cómo instalar cualquiera

La forma universal: copia el enlace del repositorio, pégalo en Claude Code y di **«instala esto por mí»**.

O usa el instalador de este repo, que solo muestra los comandos oficiales (y los ejecuta si se lo pides):

```bash
git clone https://github.com/inematds/skills15.git && cd skills15
./scripts/instalar.sh              # lista as 15
./scripts/instalar.sh 12           # mostra como instalar a #12 (find-skills)
./scripts/instalar.sh 12 --executar  # roda os comandos de terminal da #12
```

> No instales todas. Cada skill adicional es contexto que el agente carga y puede activar sin que quieras. Elige la que resuelve tu problema de hoy.

## Contenido

| archivo | qué contiene |
|---|---|
| `catalogo.json` | las 15 en datos (problema, funcionamiento, instalación, ejemplo, precaución, enlace) |
| `skills/NN-nome.md` | una ficha por skill |
| `scripts/instalar.sh` | muestra/ejecuta el comando oficial de cada una |
| `scripts/gerar.py` | regenera las fichas y la tabla a partir del catálogo |
| `tests/run.sh` | comprobaciones del catálogo, las fichas y la guía |
| `guia/` | landing + guía (PT/EN/ES) |

## Licencias

Este repositorio **no copia** el código de las skills: cada una sigue en el proyecto original, con su licencia (la mayoría MIT; HyperFrames y Graphify son Apache-2.0; CLAUDE.md do Karpathy y billion-context no declaran una licencia reconocida por GitHub). El texto de este catálogo es MIT.

## En INEMA

- REA (la #1), explicado y probado: https://inematds.github.io/rea-engenharia-reversa/guia/
- Skills do Matt Pocock (la #6), organizadas con Addy y pstack: https://inematds.github.io/trio-skills/guia/
- HyperFrames (la #7) es el motor de los vídeos de INEMA: https://inematds.github.io/explicavideos/guia/

Proyectos y cursos gratuitos: https://inema.club
