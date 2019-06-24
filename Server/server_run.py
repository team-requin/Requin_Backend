import os

from .app import create_app
from .config.app_Config import LocalLevelConfig

if __name__ == '__main__':
    app = create_app(LocalLevelConfig)

    app.run(**app.config['RUN_SETTINGS'])