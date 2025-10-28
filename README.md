# SSTI Classic — Server-Side Template Injection Lab

**SSTI Classic** is an intentionally vulnerable Flask application demonstrating Server-Side Template Injection (SSTI) for learning and testing in an isolated environment.

> ⚠️ **Warning:** This repository contains deliberately insecure code. Run only in local/isolated lab environments. Do **not** expose to the public internet.

---

## Project structure

ssti-classic/
├── vsnippet/ # Flask app source and templates
├── config/ # supervisor / service configuration
├── Dockerfile # Docker build instructions
├── docker-compose.yml # (optional) compose file
├── requirements.txt # Python dependencies
└── README.md # (this file)

yaml
Copy code

---

## Quick start (Docker — recommended)

```bash
cd ssti/ssti-classic

# build
docker build -t ssti-classic:local .

# run
docker run --rm -p 5000:5000 ssti-classic:local

# open in browser
http://localhost:5000
Quick start (Python / venv)
bash
Copy code
cd ssti/ssti-classic

# create & activate venv
python -m venv venv
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# macOS / Linux
# source venv/bin/activate

pip install -r requirements.txt

# run the app (adjust path if needed)
python vsnippet/app.py
Open http://127.0.0.1:5000 in your browser.

What this lab covers
How user input can be interpreted by a template engine (Jinja2).

Simple SSTI payloads and how they evaluate (e.g. {{7*7}}).

Demonstrations of information disclosure and code execution vectors in templates.

Safe alternatives and mitigation strategies.

Example payloads to try
{{ 7*7 }} → should render 49

{{ config.items() }} → may list Flask configuration keys

{{ ''.__class__.__mro__[1].__subclasses__() }} → advances into Python internals (use with caution)

Mitigations (high level)
Do not pass raw user input into render_template_string() or directly into templates.

Prefer render_template("template.html", safe_value=...) and escape or validate user input.

Use least-privilege, sandboxing, and input validation to reduce risk.

Unsafe

python
Copy code
# vulnerable
return render_template_string(user_input)
Safer

python
Copy code
# safer approach
return render_template("page.html", user_input=user_input)
Security & Responsible Use
Use only on local machines, isolated VMs, or controlled lab networks.

Remove any real credentials, secrets, or private data before sharing the repository.

Do not use this code in production or on public servers.

Contributing
PRs welcome. When contributing:

Open an issue for significant changes.

Avoid committing secrets or private keys.

Add clear usage notes or tests for new labs.

License
Add a LICENSE file to your repo (MIT is recommended for educational repos).

Author
Razzkr — Educational vulnerability labs and demos
