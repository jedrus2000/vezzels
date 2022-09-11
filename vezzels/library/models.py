import enum
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Numeric
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()


class DataSourceEnum(enum.Enum):
    MARINE_TRAFFIC = "marine_traffic"


class VesselTrackingData(Base):
    __tablename__ = 'vessel_tracking_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, comment='datetime when data was acquired')
    data_source = Column(Enum(DataSourceEnum), nullable=False, comment='service origin of data')

    course = Column(Integer, nullable=True)
    destination = Column(String, nullable=True)
    dwt = Column(Integer, nullable=True)
    elapsed = Column(Integer, nullable=True)
    flag = Column(String, nullable=True)
    gt_shiptype = Column(Integer, nullable=True)
    heading = Column(Numeric(precision=6), nullable=True)
    lat = Column(Numeric(precision=6), nullable=True)
    length = Column(Numeric(precision=6), nullable=True)
    lon = Column(Numeric(precision=6), nullable=True)
    l_fore = Column(Numeric(precision=6), nullable=True)
    rot = Column(Numeric(precision=6), nullable=True)
    shipname = Column(String, nullable=True)
    shiptype = Column(String, nullable=True)
    ship_id = Column(String, nullable=True)
    status_name = Column(String, nullable=True)
    speed = Column(Numeric(precision=6), nullable=True)
    width = Column(Numeric(precision=6), nullable=True)
    w_left = Column(Numeric(precision=6), nullable=True)
