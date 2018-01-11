from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Flux, FluxGroup, FluxContent, FluxLog
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures
    group = FluxGroup(name='Default group', order=1)
    db_session.add(group)

    flux = Flux(group=group, name="python",
                source="https://www.python.org/dev/peps/peps.rss/",
                last_time_check=datetime.now(), check_cycle=60,
                last_hash_content="", tags="", created_at=datetime.now())
    db_session.add(flux)

    content = FluxContent(flux=flux, hash="hash1", title="title1",
                          link="link1", is_read=False, is_bookmarked=False,
                          is_important=False, tags="tags1")
    db_session.add(content)

    log = FluxLog(flux=flux, error_name="error1", description="desc1")
    db_session.add(log)

    db_session.commit()
