Import the world.sql database into cities_db in local Postgres instance, then modify the environment configuration in config.py
Activate python virtual environment with the following set of commands
$ pipenv shell 
$ pipenv install
$ python run.py -> starts the server at localhost:8000

(optional) navigate to src/static folder and initiate the following set of 'npm' commands to activate 'react' environment
$ npm install --save-dev webpack && npm install -D webpack-cli
$ npm install --save-dev babel-core babel-loader babel-preset-es2015 babel-preset-react
$ npm install --save-dev react-router-dom history
$ npm install --save-dev style-loader css-loader
(optional) $ npm install --save-dev babel-loader@^7
