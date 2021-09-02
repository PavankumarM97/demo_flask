from flask_restful import Resource,abort,reqparse,marshal_with,fields
from main.model import Author,Article
from main import db

task_args=reqparse.RequestParser()
task_args.add_argument("author_name",type=str,help="task is required",required=True)
task_args.add_argument("article_name",type=str,help="task is required",required=True)

demo_resource_field={
    "author_id":fields.Integer,
    "author_name": fields.String,
    "article_name": fields.String
}

demo1_resource_field={
    "article_id":fields.Integer,
    "author_name": fields.String,
    "article_name": fields.String
}

class author(Resource):
    @marshal_with(demo_resource_field)
    def get(self, demo_id):
        demo=Author.query.filter_by(author_id=demo_id).first()
        if demo:
            return demo
        else:
            abort (404,message="tool not found")

    @marshal_with(demo_resource_field)
    def post(self,demo_id):
        args=task_args.parse_args()
        demo = Author.query.filter_by(author_id=demo_id).first()
        if demo:
            abort(409,message="it is already there in table")
        demo=Author(author_id=demo_id,author_name=args["author_name"],article_name=args["article_name"])
        db.session.add(demo)
        db.session.commit()
        return demo

    @marshal_with(demo_resource_field)
    def put(self,demo_id):
        args = task_args.parse_args()
        demo = Author.query.filter_by(author_id=demo_id).first()
        if demo:
            demo.author_name= args["author_name"]
            demo.article_name=args["article_name"]
            db.session.add(demo)
            db.session.commit()
            return demo
        else:
            abort(404, message="Not available")

    @marshal_with(demo_resource_field)
    def delete(self, demo_id):
        demo = Author.query.filter_by(author_id=demo_id).first()
        if demo:
            db.session.delete(demo)
            db.session.commit()
            return demo
        else:
            abort(404, message="Not available")

class article(Resource):
    @marshal_with(demo1_resource_field)
    def get(self, demo1_id):
        demo1=Article.query.filter_by(article_id=demo1_id).first()
        if demo1:
            return demo1
        else:
            abort (404,message="tool not found")

    @marshal_with(demo1_resource_field)
    def post(self,demo1_id):
        args=task_args.parse_args()
        demo1 = Article.query.filter_by(article_id=demo1_id).first()
        author=Author.query.filter_by(author_name=args['author_name']).first()
        if demo1:
            abort(409,message="it is already there in table")
        demo1=Article(article_id=demo1_id,author_name=args["author_name"],article_name=args["article_name"])
        author.alldata.append(demo1)
        db.session.add(author)
        db.session.add(demo1)
        db.session.commit()
        return demo1

    @marshal_with(demo1_resource_field)
    def put(self,demo1_id):
        args = task_args.parse_args()
        demo1 = Article.query.filter_by(article_id=demo1_id).first()
        if demo1:
            demo1.author_name= args["author_name"]
            demo1.article_name=args["article_name"]
            db.session.add(demo1)
            db.session.commit()
            return demo1
        else:
            abort(404, message="Not available")

    @marshal_with(demo1_resource_field)
    def delete(self, demo1_id):
        demo1 = Article.query.filter_by(article_id=demo1_id).first()
        if demo1:
            db.session.delete(demo1)
            db.session.commit()
            return demo1
        else:
            abort(404, message="Not available")



