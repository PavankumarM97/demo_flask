from main import app,api,author,article
from main import db
db.create_all()
api.add_resource(author, "/demo/author/<int:demo_id>")
api.add_resource(article, "/demo/article/<int:demo1_id>")
if __name__ == "__main__":
    app.run(debug=True)
