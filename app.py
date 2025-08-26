from flask import Flask, render_template, request, jsonify, send_from_directory, session, current_app
from dotenv import load_dotenv
import os
from chatbot import chatbot_response 
load_dotenv()

here = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=os.path.join(here, "static"), template_folder=os.path.join(here, "templates"))
app.secret_key = "your_secret_key_here (put it in .env)"

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        if 'target_lang' not in session:
            session['target_lang'] = 'en'
    return render_template("index.html")

@app.route("/set_language", methods=["POST"])
def language_select():
    try:
        data = request.get_json(silent=True) or {}
        target_lang = data.get("language")
        if not target_lang:
            return jsonify({"error": "No language provided"}), 400

        current_app.logger.info(f"Target language set to: {target_lang}")

        session["target_lang"] = target_lang 

        return jsonify({"target_lang": target_lang})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/chat", methods=["POST"])
def api_chat():
    try:
        data = request.get_json(silent=True) or {}
        message = data.get("message") or request.form.get("message")

        target_lang = session.get("target_lang", "english")

        if not message:
            return jsonify({"error": "No message provided"}), 400
        
        reply = chatbot_response(message, target_lang)
        return jsonify({"reply": reply})
    
    except Exception as e:
        app.logger.exception("Error in /api/chat")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

