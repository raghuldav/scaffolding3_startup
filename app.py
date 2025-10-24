from flask import Flask, request, jsonify, render_template
from starter_preprocess import TextPreprocessor
import re

app = Flask(__name__, template_folder="templates")
preprocessor = TextPreprocessor()

@app.route("/")
def home():
    """Render a simple HTML form for URL input"""
    return render_template("index.html")

# Simple health check (optional)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True, "message": "alive"}), 200

@app.route("/api/clean", methods=["POST"])
def clean_text():
    """
    API endpoint that accepts a URL and returns cleaned text
    Expected JSON: {"url": "<gutenberg .txt url>"}
    Returns:
      {
        "success": true/false,
        "cleaned_text": "...",   # first 500 chars
        "statistics": {...},
        "summary": "...",        # 3 sentences
        "error": "..."           # if applicable
      }
    """
    try:
        data = request.get_json(force=True, silent=True) or {}
        url = (data.get("url") or "").strip()
        if not url:
            return jsonify({"success": False, "error": "Missing 'url'"}), 400

        # 1) Fetch raw and remove Gutenberg header/footer
        raw = preprocessor.fetch_from_url(url)
        cleaned = preprocessor.clean_gutenberg_text(raw)

        # 2) Trim to the real narrative:
        #    a) Cut everything before the first chapter (handles numeric or Roman)
        m = re.search(r'^\s*(?:chapter|book)\s+(?:[0-9]+|[ivxlcdm]+)\b', cleaned, flags=re.I | re.M)
        if m:
            cleaned = cleaned[m.start():]
        #    b) Drop the first heading line (e.g., "CHAPTER I. The ...")
        cleaned = re.sub(
            r'^\s*(?:chapter|book)\s+(?:[0-9]+|[ivxlcdm]+)\.?\s*[^\n]*\n',
            '', cleaned, flags=re.I | re.M
        )
        #    c) Strip simple formatting artifacts
        cleaned = re.sub(r'[_*]+', '', cleaned)

        # 3) Normalize (preserve sentence punctuation for sentence stats)
        normalized = preprocessor.normalize_text(cleaned, preserve_sentences=True)

        # 4) Stats + 3-sentence summary
        stats = preprocessor.get_text_statistics(normalized)
        summary = preprocessor.create_summary(normalized, num_sentences=3)

        return jsonify({
            "success": True,
            "cleaned_text": normalized[:500],  # first 500 chars per spec
            "statistics": stats,
            "summary": summary
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route("/api/analyze", methods=["POST"])
def analyze_text():
    """
    API endpoint that accepts raw text and returns statistics only
    Expected JSON: {"text": "Your raw text here..."}
    """
    try:
        data = request.get_json(force=True, silent=True) or {}
        text = data.get("text", "")
        if text is None:
            text = ""
        stats = preprocessor.get_text_statistics(text)
        return jsonify({"success": True, "statistics": stats})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == "__main__":
    # host=0.0.0.0 helps with Codespaces port forwarding
    app.run(debug=True, port=5000, host="0.0.0.0")
