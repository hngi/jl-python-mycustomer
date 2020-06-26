import os.path
from config import connex_app
from config import base_dir

connex_app.add_api(os.path.join(base_dir, 'api_specification.yaml'))

if __name__ == '__main__':
    connex_app.run(debug=True, port=5207)

