from datetime import datetime
from flask import Flask
from flask_restful import Api
from resources.task import Tasks, Task

app = Flask(__name__)
api = Api(app)


api.add_resource(Tasks, '/tasks')
api.add_resource(Task, '/tasks/<int:id>')

if __name__ == '__main__':
  app.run(debug=True)