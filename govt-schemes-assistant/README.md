# Government Schemes Assistant (Telugu + English)

This is a Streamlit app that explains Indian government schemes in **Telugu** first, then in **English**.

## 🚀 Setup

1. Install Python 3.10+
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .\.venv\Scripts\Activate.ps1   # Windows PowerShell
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env` and put your Hugging Face token inside:
   ```
   HF_TOKEN=hf_xxx
   GH_TOKEN=gh_xxx
   ```
5. Run the app:
   ```bash
   streamlit run app.py
   ```

## 📝 Notes
- Ensure you accepted the license for `meta-llama/Meta-Llama-3-8B-Instruct` on Hugging Face.
- Your token stays local in `.env`.
