# Local PDF Digest

Extract text from a PDF, summarize it in bounded chunks, and write a Markdown brief using a local Ollama model by default. The app sends document text only to the endpoint you configure; the default endpoint is `localhost`.

## Quick start

1. Install Ollama and pull a model, for example `ollama pull llama3.2`.
2. Install this project: `python -m pip install -e .`
3. Copy `.env.example` to `.env`, then run:

```bash
pdf-digest handbook.pdf --model llama3.2 --output handbook-summary.md
```

Large PDFs are split into overlapping character chunks, summarized individually, then condensed into one Markdown report. Scanned PDFs need OCR before this tool can extract their text.

## Privacy and limits

The default model endpoint is local. If `OLLAMA_BASE_URL` points to a remote host, extracted text leaves your machine and is sent to that host. Treat PDF contents as untrusted input, review the result, and do not use a remote endpoint for confidential documents without authorization.

## Learning notes

Practice file parsing with `pypdf`, bounded chunking, HTTP JSON requests, configuration from environment variables, and graceful empty-document errors.

## Development

```bash
python -m pip install -e ".[dev]"
pytest
```

## License

MIT. See [LICENSE](LICENSE).
