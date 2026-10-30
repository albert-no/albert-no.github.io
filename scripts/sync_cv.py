#!/usr/bin/env python3
"""Regenerate the auto-synced publication sections of cv/main.tex from
publications.html.

The webpage is the source of truth for five sections, marked in the tex with
``% BEGIN AUTO: <key>`` / ``% END AUTO: <key>`` pairs:

  preprints   <- panel  <h3 id="preprints">
  conference  <- panel  <h3 id="conference-papers">
  workshop    <- panel  <h3 id="workshop-papers">
  journal     <- panel  <h3 id="journal-papers">
  patent      <- panel  <h3 id="patents">

Workshop entries use the same venue format as conference entries
(``Name (<acronym>YEAR[, detail])``). Patent entries are rendered as
title / inventors / patent info (no enumerate), e.g.
``Korean Patent (<acronym>KR 10-2016125 B1</acronym>), granted 2019``.

Stdlib only; runs identically locally and in CI (see .github/workflows/build-cv.yml).
"""

import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB_HTML = ROOT / "publications.html"
TEX = ROOT / "cv" / "main.tex"

UNICODE_MAP = {
    "“": "``", "”": "''",
    "‘": "`", "’": "'",
    "–": "--", "—": "---",
    " ": " ",
}


def tex_escape(s):
    for k, v in UNICODE_MAP.items():
        s = s.replace(k, v)
    for ch in "&%#_$":
        s = s.replace(ch, "\\" + ch)
    return s


def plain(fragment):
    """HTML fragment -> escaped LaTeX text."""
    s = re.sub(r"<[^>]+>", "", fragment)
    s = html.unescape(s)
    s = tex_escape(s)
    return re.sub(r"\s+", " ", s).strip()


def authors_tex(fragment):
    s = fragment.replace("<sup>&dagger;</sup>", "@DAG@")
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = s.replace("*", "@AST@")
    s = tex_escape(s)
    s = s.replace("@DAG@", "$^\\dagger$").replace("@AST@", "$^*$")
    s = s.replace("Albert No", "{{\\bf Albert No}}")
    return re.sub(r"\s+", " ", s).strip()


def title_tex(fragment):
    t = plain(fragment)
    t = re.sub(r"^\[[^\]]+\]\s*", "", t)  # drop the [C39]-style tag
    # titles are wrapped in ``...'' so inner quotes become single quotes
    return t.replace("``", "`").replace("''", "'")


def conference_venue_tex(fragment):
    m = re.match(
        r'^(.*?)\(\s*<span class="publication-acronym">(.*?)</span>\s*\)\s*$',
        fragment.strip(), re.S)
    if not m:
        raise ValueError("unrecognized conference venue: %r" % fragment)
    name, acro = plain(m.group(1)), plain(m.group(2))
    ym = re.search(r"(19|20)\d{2}", acro)
    if not ym:
        raise ValueError("no year in venue acronym: %r" % acro)
    year = ym.group(0)
    acro_wo_year = (acro[:ym.start()] + acro[ym.end():]).strip(" ,")
    if acro_wo_year:
        return "{\\it %s (%s)}, %s" % (name, acro_wo_year, year)
    return "{\\it %s}, %s" % (name, year)


def journal_venue_tex(fragment):
    v = plain(fragment)
    m = re.match(r"^(.*),\s*(\w+ \d{4})$", v)
    if not m:
        raise ValueError("unrecognized journal venue: %r" % v)
    return "{\\it %s}, %s." % (m.group(1), m.group(2))


def panel_entries(page, anchor_id):
    m = re.search(
        r'<h3 id="%s">.*?<ul class="publication-list">(.*?)</ul>' % anchor_id,
        page, re.S)
    if not m:
        raise ValueError("panel not found: #%s" % anchor_id)
    items = []
    for li in re.findall(r"<li>(.*?)</li>", m.group(1), re.S):
        parts = [p.strip() for p in re.split(r"<br\s*/?>", li) if p.strip()]
        if len(parts) < 3:
            raise ValueError("entry with <3 lines: %r" % parts)
        items.append(parts[:3])  # title / authors / venue ([Project Page] ignored)
    return items


def block(entries, venue_fn):
    out = []
    for title_html, authors_html, venue_html in entries:
        out.append("\\item %s,\n``%s,''\n%s" % (
            authors_tex(authors_html), title_tex(title_html), venue_fn(venue_html)))
    # match existing CV style: every item but the last ends with \\
    return "\n\n".join(
        it + ("\\\\" if i < len(out) - 1 else "") for i, it in enumerate(out))


def patent_block(entries):
    out = []
    for title_html, authors_html, info_html in entries:
        out.append("{{\\bf %s}}\\\\\n%s\\\\\n{{%s}}\\\\" % (
            title_tex(title_html), authors_tex(authors_html), plain(info_html)))
    return "\n\n".join(out)


def splice(tex, key, content):
    begin, end = "% BEGIN AUTO: " + key, "% END AUTO: " + key
    pat = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    new, n = pat.subn(lambda _: begin + "\n" + content + "\n" + end, tex)
    if n != 1:
        raise ValueError("marker pair for %r matched %d times" % (key, n))
    return new


def main():
    page = PUB_HTML.read_text(encoding="utf-8")
    tex = TEX.read_text(encoding="utf-8")

    sections = [
        ("preprints", panel_entries(page, "preprints"),
         lambda v: "{\\it %s}" % plain(v)),
        ("conference", panel_entries(page, "conference-papers"),
         conference_venue_tex),
        ("workshop", panel_entries(page, "workshop-papers"),
         conference_venue_tex),
        ("journal", panel_entries(page, "journal-papers"),
         journal_venue_tex),
    ]
    new_tex = tex
    for key, entries, venue_fn in sections:
        new_tex = splice(new_tex, key, block(entries, venue_fn))
        print("synced %-10s %2d entries" % (key, len(entries)))

    patents = panel_entries(page, "patents")
    new_tex = splice(new_tex, "patent", patent_block(patents))
    print("synced %-10s %2d entries" % ("patent", len(patents)))

    if new_tex != tex:
        TEX.write_text(new_tex, encoding="utf-8")
        print("cv/main.tex updated")
    else:
        print("cv/main.tex unchanged")


if __name__ == "__main__":
    sys.exit(main())
