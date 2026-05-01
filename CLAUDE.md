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
| Yoonjun Cho | https://cyoonjun.github.io/ |
| Wonje Jeung | https://wonjejeung.github.io/ |
| Dongjae Jeon | https://dongjae0324.github.io/ |
| Sangyeon Yoon | https://ssangyeon.github.io/ |
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

## Other site conventions

- Each HTML page links the favicon: `<link rel="icon" type="image/x-icon" href="favicon.ico" />`.
  Current `favicon.ico` is a placeholder (Avengers logo from the old Jekyll
  theme); replace at the repo root when the real AI-ISL logo is available — no
  HTML changes needed.
- Bold styling in publication entries is scoped to the title link only
  (`.publication-list li > a:first-of-type`). Author-name links and
  `[Project Page]` links should render with normal weight.
