from __future__ import annotations

import argparse
import os
from pathlib import Path

from dotenv import load_dotenv

from .summarizer import extract_pdf_text, summarize


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Summarize PDF text with a local Ollama model.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--model", default="llama3.2")
    parser.add_argument("--output", type=Path, default=Path("summary.md"))
    parser.add_argument("--chunk-size", type=int, default=6000)
    parser.add_argument("--overlap", type=int, default=400)
    args = parser.parse_args(argv)
    try:
        text = extract_pdf_text(args.pdf)
        result = summarize(text, model=args.model, base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
                           timeout=float(os.getenv("OLLAMA_TIMEOUT_SECONDS", "120")),
                           chunk_size=args.chunk_size, overlap=args.overlap)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
    except (OSError, ValueError, RuntimeError) as error:
        parser.error(str(error))
    print(f"Wrote summary to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
