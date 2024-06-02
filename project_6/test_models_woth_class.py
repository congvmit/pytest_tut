import pytest
from models import Article, Author, Base, Session, engine
from sqlalchemy.exc import IntegrityError


class TestBlog:

    def setup_class(self):
        Base.metadata.create_all(engine)
        self.session = Session()
        self.valid_author = Author(firstname="John", lastname="Doe")

    def teardown_class(self):
        self.session.rollback()
        self.session.close()

    def test_author_valid(self):
        self.session.add(self.valid_author)
        self.session.commit()

        author = self.session.query(Author).filter_by(firstname="John").first()
        assert author.firstname == "John"
        assert author.lastname == "Doe"

    @pytest.mark.xfail(raises=IntegrityError)
    def test_author_no_firstname(self):
        author = Author(lastname="Doe")
        self.session.add(author)

        try:
            self.session.commit()
        except IntegrityError as e:
            self.session.rollback()

    def test_article_valid(self):
        valid_article = Article(
            title="Hello World", content="This is a test article", author=self.valid_author
        )
        self.session.add(valid_article)
        self.session.commit()

        article = self.session.query(Article).filter_by(title="Hello World").first()
        assert article.title == "Hello World"
        assert article.content == "This is a test article"
