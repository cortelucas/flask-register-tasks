from flask_restful import Resource

tasks = [
  {
    "id": 0,
    "title": "Estudar",
    "description": "Estudar Python",
  },
  {
    "id": 1,
    "title": "Comprar PC",
    "description": "Procurar os melhores",
  },
  {
    "id": 2,
    "title": "Comprar Frutas",
    "description": "Ir ao mercado comprar frutas",
  }
]

class Tasks(Resource):
  def get(self):
    return {'tasks': tasks}


