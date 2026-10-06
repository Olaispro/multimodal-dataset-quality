# Multimodal Dataset Quality Control

> Auditable checks for image folders and annotation manifests.

Scans an image asset directory and JSONL annotation manifest for missing files, exact duplicate hashes, and malformed normalized bounding boxes. Uses Python standard library only; semantic and visual correctness remains a human review task.

## Why this project

This project reflects portfolio interests in AI operations, careful evaluation, annotation quality, and reproducible data workflows. It is a personal demonstration built from synthetic or sample data; it does not represent client work or measured professional outcomes.

## Quick start

Python 3.10+ is recommended. Run from the repository root:

```bash
python src/qc.py data/images data/annotations.jsonl
```

## Repository contents

- `src/` contains the core implementation.
- `data/` contains small illustrative fixtures where applicable.
- Outputs are generated locally and are not checked in.

## Method and interpretation

The implementation favors readable baselines and explicit assumptions. Scores from demonstration data are not general performance estimates. Human review remains necessary for semantic correctness, evidence quality, and policy or safety judgments.

## Limitations

- Included records are synthetic or illustrative and are not client data.
- No production deployment, external model API, or independently validated result is claimed.
- Review the assumptions and adapt the workflow before using it on consequential data.

## License

MIT. See [LICENSE](LICENSE).
