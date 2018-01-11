from sqlalchemy import Column, DateTime, ForeignKey, \
                       Integer, String, func, Boolean
from sqlalchemy.orm import backref, relationship, class_mapper

from database import Base


class FluxGroup(Base):
    __tablename__ = 'flux_group'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    order = Column(Integer, unique=True)


class Flux(Base):
    __tablename__ = 'flux'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('flux_group.id'))
    name = Column(String)
    source = Column(String)
    last_time_check = Column(DateTime, default=func.now())
    check_cycle = Column(Integer)
    last_hash_content = Column(String)
    tags = Column(String)
    created_at = Column(DateTime, default=func.now())

    group = relationship('FluxGroup', backref=backref('fluxs',
                                                      cascade='delete,all'))


class FluxContent(Base):
    __tablename__ = 'flux_content'
    id = Column(Integer, primary_key=True)
    flux_id = Column(Integer, ForeignKey('flux.id'))
    hash = Column(String)
    retrieved_at = Column(DateTime, default=func.now())
    title = Column(String)
    link = Column(String)
    is_read = Column(Boolean, default=False)
    is_bookmarked = Column(Boolean, default=False)
    is_important = Column(Boolean, default=False)
    tags = Column(String)

    flux = relationship('Flux', backref=backref('contents',
                                                cascade='delete,all'))


class FluxLog(Base):
    __tablename__ = 'flux_log'
    id = Column(Integer, primary_key=True)
    flux_id = Column(Integer, ForeignKey('flux.id'))
    error_name = Column(String)
    description = Column(String)
    occured_at = Column(DateTime, default=func.now())
    is_check = Column(Boolean, default=False)

    flux = relationship('Flux', backref=backref('logs',
                                                cascade='delete,all'))


class_mapper(FluxGroup)
class_mapper(Flux)
class_mapper(FluxContent)
class_mapper(FluxLog)
