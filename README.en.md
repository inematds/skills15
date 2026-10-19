# skills15 — 15 Claude skills worth your time

[![skills15](guia/assets/banner-en.jpg)](https://inematds.github.io/skills15/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

There are more than a million skills for AI agents, and most of them are useless. This repository brings together the **15 worth your time** if you use Claude Code (and other agents): the problem each one solves, how it works under the hood, the official installation command, an example prompt, and a link to the original project. It helps you choose **one** skill for today's problem, without installing everything at once.

## 📖 User guide

Landing page + guide to all 15, with examples and video: **https://inematds.github.io/skills15/guia/**

## The 15 (from #15 to #1)

<!-- tabela -->
| # | Skill | For | ★ 18/10 | Problem it solves |
|---|---|---|---|---|
| 15 | [NotebookLM](skills/15-notebooklm-py.md) | token savings | 19,8 mil | When you give Claude a lot of PDFs, it reads every word and quickly uses up your usage limit. |
| 14 | [I Have ADHD](skills/14-i-have-adhd.md) | answers | 57,7 mil | Claude rambles: it writes three paragraphs before giving you the answer you needed. |
| 13 | [Billion Context](skills/13-billion-context.md) | token savings | 1,9 mil | In a long conversation, the model rereads everything from the beginning with every message, quickly using up your limit. |
| 12 | [Find Skills](skills/12-find-skills.md) | discovery | 35,5 mil | There are thousands of skills, and you don't know whether one already exists for what you need. |
| 11 | [De-AI Writing](skills/11-de-ai-writing.md) | writing | — | AI-sounding text ('situated in the heart of the city, a testament to its rich cultural heritage') makes readers suspicious and stop reading. |
| 10 | [Archify](skills/10-archify.md) | diagrams | 85,4 mil | Explaining how an automation, system, or plan works in a meeting, while the client just nods without understanding. |
| 9 | [NanoClaw](skills/09-nanoclaw.md) | assistant | 31 mil | Having a personal AI assistant on your phone without handing your life over to a huge program nobody understands. |
| 8 | [Karpathy's CLAUDE.md](skills/08-karpathy-claude-md.md) | rules | 220 mil | You ask Claude to change one line, and it rewrites half the project and invents features nobody asked for. |
| 7 | [HyperFrames](skills/07-hyperframes.md) | video | 66,8 mil | Making a video with an animated title, music, and cuts takes an hour in an editor, and the timing is still wrong at the end. |
| 6 | [Matt Pocock's Skills](skills/06-mattpocock-skills.md) | code | 296 mil | Claude writes thousands of lines in minutes, and then you spend days finding out what broke because it started before understanding what you wanted. |
| 5 | [Career Ops](skills/05-career-ops.md) | career | 75,5 mil | Sending 50 résumés and 50 cover letters to get two replies. |
| 4 | [Graphify](skills/04-graphify.md) | knowledge | 128 mil | Notes, PDFs, screenshots, videos, and code in one folder, with nobody knowing how they connect. |
| 3 | [AI Website Cloner](skills/03-ai-website-cloner.md) | web | 37 mil | Recreating a website (fonts, colors, layout) can take a designer or developer days. |
| 2 | [Anatomy](skills/02-anatomy.md) | visual | 16,1 mil | You ask how something works and get a wall of text; you ask again, and the wall gets bigger. |
| 1 | [REA (Reverse Engineer Anything)](skills/01-rea.md) | reverse engineering | 323 mil | You see a feature in someone else's app and want it in yours, but you don't have the code, so you guess and get it wrong. |
<!-- /tabela -->

(the entries in skills/ are in Portuguese)

Stars counted on GitHub on 18/10/2026. #11 has no repository: it's a Reddit post (the installable alternative is [Humanizer](https://github.com/blader/humanizer)).

## How to install any of them

The universal way: copy the repository link, paste it into Claude Code, and say **"install this for me"**.

Or use this repo's installer, which only shows the official commands (and runs them if you ask):

```bash
git clone https://github.com/inematds/skills15.git && cd skills15
./scripts/instalar.sh              # lists the 15
./scripts/instalar.sh 12           # shows how to install #12 (find-skills)
./scripts/instalar.sh 12 --executar  # runs #12's terminal commands
```

> Don't install them all. Each additional skill is context the agent loads and may trigger without you wanting it to. Choose the one that solves today's problem.

## Contents

| file | what |
|---|---|
| `catalogo.json` | the 15 in data (problem, how it works, installation, example, caveat, link) |
| `skills/NN-nome.md` | one entry per skill |
| `scripts/instalar.sh` | shows/runs each skill's official command |
| `scripts/gerar.py` | regenerates the entries and table from the catalog |
| `tests/run.sh` | checks the catalog, entries, and guide |
| `guia/` | landing page + guide (PT/EN/ES) |

## Licenses

This repository **does not copy** the skills' code: each one remains in its original project, under its own license (most are MIT; HyperFrames and Graphify are Apache-2.0; Karpathy's CLAUDE.md and billion-context don't declare a license recognized by GitHub). This catalog's text is MIT.

## At INEMA

- REA ( #1) explained and tested: https://inematds.github.io/rea-engenharia-reversa/guia/
- Matt Pocock's Skills (#6) organized with Addy and pstack: https://inematds.github.io/trio-skills/guia/
- HyperFrames (#7) powers INEMA videos: https://inematds.github.io/explicavideos/guia/

Free projects and courses: https://inema.club
