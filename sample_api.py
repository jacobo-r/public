from flask import Flask, render_template_string

app = Flask(__name__)

# Using render_template_string for a quick demo; you can also use render_template with an HTML file.
@app.route('/')
def index():
    html_content = """
    <!doctype html>
    <html>
      <head>
         <title>Flask Index Page</title>
      </head>
      <body>
         <h1>Hello, this is your Flask API running on port 88443!</h1>
      </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    # Listen on all interfaces to ensure external connectivity
    app.run(host='0.0.0.0', port=88443, debug=True)
