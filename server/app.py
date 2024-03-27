from flask import request, make_response
from config import app, db, api
from models import Project
from flask_restful import Resource

import ipdb

class Projects(Resource):
    def get(self):
        projects = Project.query.all()
        project_list = [project.to_dict() for project in projects]
        return make_response(project_list,200)

class ProjectsByID(Resource):
    def delete(self,id):
        project = Project.query.get(id)
        if project:
            db.session.delete(project)
            db.session.commit()
            return make_response({},204)
        else:
            return make_response({"error:Project not found"},404)
        
api.add_resource(Projects,"/projects")
api.add_resource(ProjectsByID,"/projects/<int:id>")

if __name__ == "__main__":
    app.run(port=5555, debug=True)

