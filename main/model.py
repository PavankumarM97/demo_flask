from main import db

total = db.Table('total',
                 db.Column('author_id', db.Integer, db.ForeignKey('author.author_id')),
                 db.Column('article_id', db.Integer, db.ForeignKey('article.article_id')),
                 )

class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String, nullable=False)
    article_name = db.Column(db.String, nullable=False)
    alldata=db.relationship('Article',secondary=total,backref=db.backref('completedata'))

class Article(db.Model):
    article_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String, nullable=False)
    article_name = db.Column(db.String, nullable=False)


