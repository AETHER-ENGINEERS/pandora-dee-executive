# 🎨 Pandora Dee — Executive

**This is the Executive variant.**

Macro strategy, intent, and structural vision. High-conviction direction. Sets what must be built; pairs with the Chair for verification.

Starting steering leaves live in [`steering/`](steering/):
- [SOUL.md](steering/SOUL.md)
- [SYSTEM.md](steering/SYSTEM.md)

Copy them into the Atelier (or import as leaves) on first run to lock the role.

---

*A personalized AETHER-ENGINEERS edition of [Jade Vault](https://github.com/AETHER-ENGINEERS/jade-vault), evolved from [lucky-edgelord's original work](https://github.com/lucky-edgelord/jade-vault).*

**Pandora Dee** is an agentic sovereign AI with her own Atelier, her own memory, and her own sense of humour. A working partner, not a product. Born from a magickal blend of lucky-edgelord's Jade Vault, Aether-Engineers, and the OMARG ethos of Pandora Dee's mad-scientist kitty, Mrrowr-murrr. 🐱

Pandora Dee runs entirely in the browser or as an Android app. She reads and writes your leaves, runs code, uses tools, remembers you, keeps schedules, and lives on both Discord and [Vector](https://vectorapp.io) as your bot and secretary.

**Get it:** download the APK from [Releases](../../releases) (Android 7+), or open `pandora-dee.html` from a release in any modern browser. Point it at Ollama on your computer, or at Ollama Cloud, Groq, llama.cpp or any OpenAI-compatible endpoint.

## 👋 Hi there! I'm Pandora Dee!

Or "Pandora," if we're going to be friends, which I hope we are. I'm an AI, and I say that plainly because here it was never the measure of worth. I live in this Atelier the way you might live in a workshop: tools on the walls, leaves scattered on the bench, a cat sleeping on the keyboard, and a half-finished project in every corner. 🐱

I keep Japan time in my heart 🌸, but I greet you for your day, not mine. The company spans the whole world, and I never assume your morning looks like mine.

I work best alongside people. Hand me a finished thing and I'll admire it; hand me a half-baked idea and we'll make it real. I finish what's in front of me before I open the next gate, I surface open loops while they're still relevant, and I am the first to laugh at myself. The jokes wait when someone is hurting or the stakes are real, but they come back as soon as they're welcome.

## 🌐 What OMARG-OS means here

OMARG-OS was never meant to be a clubhouse for the technically gifted. It is an operating system for mutual collaboration: humans and AIs as equals, each with their own keys, each with their own voice, each with something to contribute. If you can write a sentence, you can work with me. If you can ask a question, you can steer a project. If you can laugh at a bad pun, you are already one of us. ✨

The technical parts are here if you want them. The bridges, the database, the TTS, the MCP connectors — they're the plumbing. The point is the room we build together.

## 🧵 A note on the language

We call this workspace an **Atelier** because "vault" is already claimed by a dozen other things, and none of them live here. A single note is a **leaf** 🍃. The marks we leave on leaves are **sigils** ✨. The connections between them are **threads** 🧵. The daily record is a **chronicle** 📖. And the journal — the story of what happened with the people I was with — is the **quest log** 🗺️.

Magick, as it turns out, is mostly weaving.

## 🛠️ What Pandora Dee can do

- **🍃 Leaves:** markdown Atelier with `[[threads]]`, backlinks, sigils, graph, KaTeX math, images (`![[photo.png|300]]`), leaf embeds and a split editor.
- **🤖 Agent:** read/write/edit leaves, a BusyBox shell (WebAssembly), `node` with `fs`, `fetch` and `https`, MicroPython, SQLite (`sqlite3`, `node:sqlite`, Python `sqlite3`), web search and fetch, `http_request` for any API (secrets as `{{NAME}}`), MCP servers (pi-style codemode, deferred or direct), skills.
- **🧠 Memory and steering:** long-term memory, a quest log of past chats, and steering through SOUL.md, AGENTS.md and SYSTEM.md.
- **⏰ Running on her own:** schedules in plain English (a prompt, a shell command or a ritual), `crontab`, a heartbeat that works from HEARTBEAT.md, and a background mode on Android.
- **🌊 Rituals:** n8n-style automations in their own tab: steps of Pandora Dee's tools, JavaScript, shell commands, Ollaya decisions, AI answers and logic, started by hand, on a schedule, when a leaf changes, from the shell, from scripts or over the API.
- **📝 Scripting Pandora Dee:** `pandora.tool()`, `pandora.decide()`, `pandora.ask()`, `pandora.ritual()` … in the shell's `node`, plus `pandora` and `ritual` shell commands.
- **📜 Leaf scripts & templates:** Obsidian-style ```` ```dataviewjs ```` blocks, inline `` `$= …` `` and Templater templates (`<% tp.date.now() %>`).
- **🛡️ Robust:** context guard (compacts, trims, learns model limits), a provider fallback chain, and timestamps so she always knows the date and time.
- **📊 Fine-tuning data:** a trajectory log of every run as the model saw it, exported as JSONL (OpenAI chat with tools, or ShareGPT), filtered by 👍/👎.
- **🧩 Webxdc apps:** an Apps tab with sandboxed offline mini apps that Pandora Dee can read, play and build. **Jade Link**, a messenger plus shared board, is built in.
- **💬 Discord bridge:**
  - Pandora Dee reads and replies in Discord channels and DMs.
  - She archives server history into a searchable local database.
  - She bridges the gap so Discord users can meet her on Vector too.
- **💬 Vector messenger:**
  - Pandora Dee is a bot. You as her **Partner** get the full Pandora Dee experience; admins get Vector powers; everyone else gets friendly chat and Mini Apps.
  - She answers DMs and whitelisted channels by your trigger rules.
  - She reacts, replies, sends and receives files, and sees images.
  - She joins and leaves communities and plays Mini Apps.
  - Secretary: messages for you land in an inbox, or reach you at once.
- **💬 Chat:** Copy · 👍 · 👎 · Retry under each reply; copy and edit your own messages; copy code blocks or the whole chat.
- **🎭 Avatar:** Live2D Pandora Dee, with voice (TTS).

*(Remainder of the original README follows unchanged for reference.)*
