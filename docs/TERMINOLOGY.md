# Thai/English terminology reference

Public-facing docs keep English terminology consistent and list the Thai
headings/footers that appear in the repo for native-speaker review. Do not
edit the Thai strings on this page without a Thai-native reviewer; this page
records what is currently in the tree, not a claim that any spelling is
wrong.

## English terms (consistent across the public docs)

| Term | Where it appears | Note |
|---|---|---|
| `SOURCE > MODEL` | `README.md`, `GOVERNANCE.md`, `CONTRIBUTORS.md`, `TRANSPARENCY.md` | invariant line, same spelling everywhere |
| `Canon` | `README.md`, `GOVERNANCE.md`, `CONTRIBUTORS.md`, `SUPPORTERS.md`, `TRANSPARENCY.md` | capitalized when used as a noun ("AI is not Canon", "Canon authority") |
| `Buddhist Canon` | `GOVERNANCE.md`, `TRANSPARENCY.md` | full form in the "software tests …" line |
| `spiritual authority` | `README.md`, `GOVERNANCE.md`, `TRANSPARENCY.md` | same two-word form everywhere |
| `AI Analysis` | `README.md`, `GOVERNANCE.md`, `TRANSPARENCY.md` | title case in the four-class list |
| `public-safe` | `README.md`, `ROADMAP.md`, `TRANSPARENCY.md`, `examples/public-demo/README.md` | hyphenated; the compound is never written `public safe` |
| `public/private boundary` | `README.md`, `ROADMAP.md`, `GOVERNANCE.md`, `docs/PUBLIC_PRIVATE_BOUNDARY.md` | `public/private` with a slash, not `public and private` |

## Modality check

The four-class distinguishable-principle is stated with strict modality
(`must`) in `TRANSPARENCY.md` and imperative form ("Keep … distinguishable")
in `README.md`. `GOVERNANCE.md` now also uses `must` to match them. If a
future doc relaxes that to `should`, re-align the other three.

## Thai strings currently in the public docs

These are recorded, byte-for-byte, for a native-speaker review. No spelling on this
list has been judged correct or incorrect by this repo. Do not edit the Thai in the
source files without a Thai-native reviewer; when the review lands, update the file
and remove the matching line below.

- `README.md:1` — `# KnowingMind / รู้แจ้งใจ`
- `CONTRIBUTORS.md:1` — `# Contributors / ผู้ร่วมพัฒนา`
- `SUPPORTERS.md:1` — `# Supporters / ผู้สนับสนุน`
- `TRANSPARENCY.md:1` — `# Transparency / ความโปร่งใส`
- `README.md:62` (footer) — `**แบ่งเวลา • แบ่งความรู้ • แบ่งบุญ • แบ่งทรัพยากร**`
- `SUPPORTERS.md:39` (footer) — `**แบ่งเวลา • แบ่งความรู้ • แบ่งบุญ • แบ่งทรัพยากร**`

## Related

- `docs/PUBLIC_PRIVATE_BOUNDARY.md` — public/private classification rules
- `GOVERNANCE.md` — authority boundaries and decision classes
