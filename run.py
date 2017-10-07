import os

from src.instance import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)

if __name__ == '__main__':
	host = os.environ.get('IP', '0.0.0.0')
	port = int(os.environ.get('PORT', 8080))
	app.run(host=host, port=port, threaded=True)