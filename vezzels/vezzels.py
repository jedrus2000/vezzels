from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import datetime, tzinfo

from library.models import VesselTrackingData, DataSourceEnum, Base
from library.mt import get_all_vessels_postion_data

engine = create_engine("sqlite+pysqlite:///mydb.db", echo=True, future=True)
Base.metadata.create_all(engine)

# create session and add objects
with Session(engine) as session:
    entry_dt = datetime.utcnow()
    rows = get_all_vessels_postion_data()
    for r in rows:
        v = VesselTrackingData(
            created_at=entry_dt,
            data_source=DataSourceEnum.MARINE_TRAFFIC,
            course=r.get('COURSE', None),
            destination=r.get('DESTINATION', None),
            dwt=r.get('DWT', None),
            elapsed=r.get('ELAPSED', None),
            flag=r.get('FLAG', None),
            gt_shiptype=r.get('GT_SHIPTYPE', None),
            heading=r.get('HEADING', None),
            lat=r.get('LAT', None),
            length=r.get('LENGTH', None),
            lon=r.get('LON', None),
            l_fore=r.get('L_FORE', None),
            rot=r.get('ROT', None),
            shipname=r.get('SHIPNAME', None),
            shiptype=r.get('SHIPTYPE', None),
            ship_id=r.get('SHIP_ID', None),
            status_name=r.get('STATUS_NAME', None),
            speed=r.get('SPEED', None),
            width=r.get('WIDTH', None),
            w_left=r.get('W_LEFT', None),
        )
        session.add(v)
    session.commit()
