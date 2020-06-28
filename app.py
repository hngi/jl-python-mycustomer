import os.path
from config import base_dir, connex_app, app

connex_app.add_api(os.path.join(base_dir, 'swagger.yaml'))

if __name__ == '__main__':
    app.run(debug=True, port=5207)
