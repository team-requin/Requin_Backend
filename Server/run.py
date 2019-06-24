from app import create_app
from config.app_config import LocalConfig


if __name__ == '__main__':
    app = create_app(LocalConfig)
    
    app.run(**app.config['RUN_SETTINGS'])