from dotenv import load_dotenv, find_dotenv
from src.app import create_app

load_dotenv(find_dotenv())
app = create_app('development')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000)