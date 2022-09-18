import enum
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Numeric
from sqlalchemy.orm import declarative_base, relationship

# declarative base class
Base = declarative_base()


class DataSourceEnum(enum.Enum):
    MARINE_TRAFFIC = "marine_traffic"


# ship
class Ship(Base):
    __tablename__ = 'ship'

    created_at = Column(DateTime, nullable=False, comment='datetime when data was acquired')
    data_source = Column(Enum(DataSourceEnum), nullable=False, comment='service origin of data')

    id = Column(String, primary_key=True)
    flag = Column(String, nullable=True)
    gt_shiptype = Column(Integer, nullable=True)
    shipname = Column(String, nullable=True)
    shiptype = Column(String, nullable=True)
    length = Column(Numeric(precision=6), nullable=True)
    width = Column(Numeric(precision=6), nullable=True)
    l_fore = Column(Numeric(precision=6), nullable=True)
    w_left = Column(Numeric(precision=6), nullable=True)


# tracking data
class ShipTrackingData(Base):
    __tablename__ = 'ship_tracking_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ship_id = Column(Integer, ForeignKey(Ship.id))
    ship = relationship(Ship)

    created_at = Column(DateTime, nullable=False, comment='datetime when data was acquired')
    data_source = Column(Enum(DataSourceEnum), nullable=False, comment='service origin of data')

    course = Column(Integer, nullable=True)
    destination = Column(String, nullable=True)
    dwt = Column(Integer, nullable=True)
    last_position_dt = Column(DateTime, nullable=True)
    heading = Column(Numeric(precision=6), nullable=True)
    lat = Column(Numeric(precision=6), nullable=True)
    lon = Column(Numeric(precision=6), nullable=True)
    rot = Column(Numeric(precision=6), nullable=True)
    status_name = Column(String, nullable=True)
    speed = Column(Numeric(precision=6), nullable=True)
