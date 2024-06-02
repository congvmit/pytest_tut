import pytest
from models import Article, Author, Base, Session, engine
from sqlalchemy.exc import IntegrityError

# Fixtures may be moved to a separate file called conftest.py


# scope="module" means that the fixture will be created once per module
# and will be shared among all tests in the module
@pytest.fixture(scope="module")
def db_session():
    if not engine.url.get_backend_name() == "sqlite":
        raise RuntimeError("Use SQLit backend to run tests.")

    Base.metadata.create_all(engine)
    try:
        with Session() as session:
            yield session
        session.rollback()
        session.close()
    finally:
        Base.metadata.drop_all(engine)


@pytest.fixture(scope="module")
def valid_author():
    return Author(firstname="John", lastname="Doe")


# ===== Test cases =====
class TestBlog:

    def test_author_valid(self, db_session, valid_author):
        db_session.add(valid_author)
        db_session.commit()

        author = db_session.query(Author).filter_by(firstname="John").first()
        assert author.firstname == "John"
        assert author.lastname == "Doe"

    @pytest.mark.xfail(raises=IntegrityError)
    def test_author_no_email(self, db_session):
        author = Author(firstname="James", lastname="Clear")
        db_session.add(author)
        try:
            db_session.commit()
        except IntegrityError:
            db_session.rollback()

    def test_article_valid(self, db_session, valid_author):
        valid_article = Article(
            title="Hello World", content="This is a test article", author=valid_author
        )
        db_session.add(valid_article)
        db_session.commit()

        article = db_session.query(Article).filter_by(title="Hello World").first()
        assert article.title == "Hello World"
        assert article.content == "This is a test article"
