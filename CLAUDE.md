# CLAUDE.md

Conventions for the AI-ISL lab website (`albert-no.github.io`). When editing
`publications.html`, follow these rules.

## Author formatting in publications.html

### Symbols (legend appears at the top of the page)

- `*` — equal contribution (placed immediately after the name, before the comma)
- `<sup>&dagger;</sup>` — co-correspondence (placed immediately after the name)
- `<u>...</u>` — lab member (current or alumni; see list below)

### Name ordering

- 3+ authors: use Oxford comma + "and" before the last author.
  Example: `A, B, and C`
- 2 authors: use "and" with no comma.
  Example: `A and B`

### Personal webpages

If an author has a personal webpage (see list below), wrap their name in an
anchor that opens in a new tab. The `<u>` tag (if applicable) goes *inside*
the `<a>`, so the underline still renders.

```html
<a href="https://name.github.io/" target="_blank" rel="noopener"><u>Name</u></a>
```

### Venue formatting

Wrap the text inside venue parentheses with `publication-acronym` so the
acronym, track, and presentation details render in bold while the parentheses
remain regular weight.

```html
Conference Name (<span class="publication-acronym">XXX2026 Main</span>)
```

### Project pages

If a publication has a project page, add a separate line after the venue line:

```html
Venue (<span class="publication-acronym">XXX2026</span>)<br />
<a href="https://project-url/">[Project Page]</a>
```

## Lab members (underline these names)

Both casing variants below should be underlined when they appear.

### Current

- Albert No
- Yoonjun Cho
- Yeachan Jun
- Kyelim Lee
- Wonje Jeung
- Hyesoo Hong
- Soeun Kim
- BumJun Kim / Bumjun Kim
- Dueun Kim
- Sangwoo Shin
- Moongyu Jeon
- Dongjae Jeon
- Sangyeon Yoon
- MinSoo Kim
- Shin So
- Jongbum Won
- Sunghyun Park
- Minhyeok Jo

### Alumni

- Pyo Min Hong
- Halyn Yu
- Beom Soo Lee / Beomsoo Lee
- Junseok Jang
- JiHyun Jung
- Ki-wook Hong / Ki-Wook Hong
- Dayeon Kim
- Beomseok Seo
- Yebin Wang
- Sanghoon Kang
- Yunfei Gao
- Minhyeok Cho
- Jinhyuk Park
- Haonan Yang

The source of truth for current/alumni status is `team.html`. If a name is
removed/added there, update the underline list here too.

## Personal webpages

| Author | URL |
| --- | --- |
| Hyesoo Hong | https://hyesoo0411.github.io/ |
| Yoonjun Cho | https://cyoonjun.github.io/ |
| Wonje Jeung | https://wonjejeung.github.io/ |
| Dongjae Jeon | https://dongjae0324.github.io/ |
| Sangyeon Yoon | https://ssangyeon.github.io/ |
| Sunghyun Park | https://sunghyunp-ark.github.io/ |
| Pyo Min Hong | https://pyomin.github.io/ |

Pyo Min Hong is a visiting researcher alumna (listed in `team.html`), so her
name is both linked and underlined in publication entries.

## Project pages already linked

| Paper | URL |
| --- | --- |
| [C32] dgMARK | https://dgmark-watermarking.github.io/ |
| [C29] DUSK | https://ai-isl.github.io/dusk |
| [C26] A2D | https://ai-isl.github.io/A2D |
| [C25] Rainbow Padding | https://ai-isl.github.io/rainbow-padding |

## CV auto-build

The CV source is `cv/main.tex`. On every push to `master`, the `Build CV`
GitHub Actions workflow (`.github/workflows/build-cv.yml`):

1. runs `scripts/sync_cv.py`, which regenerates the PREPRINT, CONFERENCE
   PUBLICATIONS, PEER-REVIEWED WORKSHOP, JOURNAL PUBLICATIONS, and PATENT
   sections of `cv/main.tex` from `publications.html` (the regions between
   `% BEGIN AUTO:` / `% END AUTO:` markers — never edit inside those markers
   by hand);
2. recompiles the tex file;
3. commits `cv/main.tex` + root `cv.pdf` if anything changed
   (served at `https://albert-no.github.io/cv.pdf`).

So new publications, workshop papers, and patents only need to be added to
`publications.html`; the CV follows automatically. Workshop papers whose
content was later published at a conference or journal are intentionally
left off the webpage (and therefore the CV); do not re-add them. Never edit the root PDF
directly. `albert-no.html` links `cv.pdf` below the email line.

Patents live in the `#patents` panel of `publications.html` (tags `[PT1]`,
`[PT2]`, ...). Each entry is three lines like the other panels: title link,
inventors, then `<Kind> (<span class="publication-acronym">number</span>),
<status/year>`.

The CV has no FUNDINGS or TEACHING EXPERIENCE section. Funding is listed on
`fundings.html` (linked from `albert-no.html` as `[Fundings]`, not in the
site nav); update that page directly when a grant is added or ends.

## Other site conventions

- Pages link `assets/images/logo/lab_logo.png` as their icon; the root
  `favicon.ico` (multi-size, generated from the lab logo) covers direct
  `/favicon.ico` requests.
- `404.html` at the root is the GitHub Pages custom not-found page; it reuses
  the standard header/footer with root-absolute paths (so it renders correctly
  at any URL depth).
- Bold styling in publication entries is scoped to the title link only
  (`.publication-list li > a:first-of-type`). Author-name links and
  `[Project Page]` links should render with normal weight.
