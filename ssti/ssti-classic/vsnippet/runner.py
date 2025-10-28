# vsnippet/runner.py
import importlib.util

SRC = "/app/6-ssti-classic.py"  # path inside the container

spec = importlib.util.spec_from_file_location("lab", SRC)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

# Expect the snippet to expose `app = Flask(__name__)` (possibly wrapped by design)
app = getattr(mod, "app", None)
if app is None:
    raise RuntimeError(f"'app' not found in {SRC}. Make sure the file defines app = Flask(__name__).")

# Bind to 0.0.0.0:1337 for Docker
app.run(host="0.0.0.0", port=1337, debug=False)
