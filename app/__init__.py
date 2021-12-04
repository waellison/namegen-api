import os
from flask import Flask
from .views import bp

def create_app():
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY="CHANGE THIS",
  )

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass
  
  app.register_blueprint(bp)
  
  return app
  
