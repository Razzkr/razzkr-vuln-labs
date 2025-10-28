from flask import Flask, render_template, render_template_string, request, url_for

app = Flask(__name__)

def MySQL_Get(table, data):   # dummy
    return False, ""

def searchResult():           # dummy
    return ""

def NoItemFound(user_input):
    def NoItemFound(user_input):
    tpl = f'''
    <script src="{ url_for('static', filename='main.js') }"></script>
    <h3 id="search">No result for: {user_input}</h3>
    '''
    return render_template_string(tpl)
    <script src="{ url_for('static', filename='main.js') }"></script>
    <h3 id="search">No result for: {user_input}</h3>
    '''
    return render_template_string(tpl)

@app.route("/")
def index():
    q = request.args.get("search", "")
    if q == "":
        return render_template("index.html", result="No search provided")
    db_status, db_data = MySQL_Get("products", q)
    result = searchResult(db_data) if db_status else NoItemFound(q)
    return render_template("index.html", result=result)

@app.route("/healthz")
def healthz():
    return "ok", 200

if __name__ == "__main__":
    # IMPORTANT: listen on 5000 (compose maps 1337->5000)
    app.run(host="0.0.0.0", port=5000, debug=False)
