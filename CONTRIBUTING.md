# Contributing

Thank you for improving this list.

## Add or correct a paper

Edit `data/papers.json`, then regenerate the README:

```bash
python scripts/update_papers.py --render-only
python -m unittest discover -s tests -v
```

Every record needs a title, publication year, venue, category, and stable paper URL. Add `code_url` only when the repository is an official implementation or is explicitly linked by the authors. Use `null` when no official code is known.

The accepted categories and precedence rules are defined in
`scripts/taxonomy.py`. Assign each paper to exactly one category based on its
primary task. Training or system properties such as self-supervision,
efficiency, and scalability are not standalone categories. The preferred
venues are CVPR, ICCV, ECCV, TPAMI, IROS, ICRA, TRO, RA-L, ICLR, 3DV, and
arXiv.

Entries from `chicleee/End-to-End-3D-Reconstruction-Paper-List` are synchronized
by `scripts/import_reference.py`. Correct those records upstream when possible;
the weekly workflow may otherwise restore their source metadata. The upstream
heading is retained in `source_category` for provenance, while `category`
always follows this repository's mutually exclusive taxonomy.

## Automated entries

Records with `"curated": false` were found automatically. If one is irrelevant, remove it and open an issue explaining the false positive so the discovery filters can be improved.
