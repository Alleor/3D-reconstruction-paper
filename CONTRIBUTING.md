# Contributing

Thank you for improving this list.

## Add or correct a paper

Edit `data/papers.json`, then regenerate the README:

```bash
python scripts/update_papers.py --render-only
python -m unittest discover -s tests -v
```

Every record needs a title, publication year, venue, category, and stable paper URL. Add `code_url` only when the repository is an official implementation or is explicitly linked by the authors. Use `null` when no official code is known.

The accepted categories are defined in `scripts/update_papers.py`. The preferred venues are CVPR, ICCV, ECCV, TPAMI, IROS, ICRA, TRO, RA-L, ICLR, 3DV, and arXiv.

## Automated entries

Records with `"curated": false` were found automatically. If one is irrelevant, remove it and open an issue explaining the false positive so the discovery filters can be improved.

