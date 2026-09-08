#!/usr/bin/env python3
"""Local preview server with clean-URL support (/about -> about.html)."""

from __future__ import annotations

import argparse
import functools
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class CleanURLHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):  # noqa: N802
        path = self.path.split("?", 1)[0].split("#", 1)[0]
        candidate = self._resolve(path)
        if candidate is not None:
            # Serve the mapped file while keeping the clean request URL.
            self.path = "/" + candidate.relative_to(ROOT).as_posix()
        return super().do_GET()

    def _resolve(self, url_path: str) -> Path | None:
        if url_path in ("", "/"):
            index = ROOT / "index.html"
            return index if index.is_file() else None

        rel = url_path.lstrip("/")
        direct = ROOT / rel
        if direct.is_file():
            return direct
        if direct.is_dir() and (direct / "index.html").is_file():
            return direct / "index.html"

        # /about -> about.html, /investment-teams/ -> investment-teams.html
        stem = rel.rstrip("/")
        if "." not in Path(stem).name:
            html = ROOT / f"{stem}.html"
            if html.is_file():
                return html
        return None

    def log_message(self, fmt: str, *args) -> None:
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()

    handler = functools.partial(CleanURLHandler)
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Serving {ROOT}")
    print(f"Open http://{args.host}:{args.port}/")
    print("Clean URLs enabled (/about, /sponsors, ...)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
