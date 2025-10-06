from flask import Flask, render_template_string, request, send_file
import qrcode
import io

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>QR Code Generator</title>
<h1>QR Code Generator</h1>
<form method=post>
  <input type=text name=text placeholder="Enter text/URL">
  <input type=submit value=Generate>
</form>
{% if qr %}
  <img src="{{url_for('qr_code')}}" alt="Your QR code">
  <p><a href="{{url_for('qr_code')}}" download="qr.png">Download QR</a></p>
{% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def index():
    show_qr = False
    if request.method == "POST" and request.form.get("text"):
        app.config["QR_TEXT"] = request.form["text"]
        show_qr = True
    return render_template_string(HTML, qr=show_qr)

@app.route('/qr_code')
def qr_code():
    qr_text = app.config.get("QR_TEXT", "")
    img = qrcode.make(qr_text)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
