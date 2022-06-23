from flask import Flask, Blueprint, render_template, abort

app = Flask(__name__)

site_bp = Blueprint('site',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/site'
                    )


@site_bp.route('/')
def serve_site():
    return render_template('index.html')


@site_bp.route('/<path:text>', methods=['GET'])
def redirect_to_site(text):
    if text.startswith('site'):
        return serve_site()
    else:
        abort(404)


app.register_blueprint(site_bp)


@app.route("/api/hello")
def hello_world():
    return "Hello, World!"
