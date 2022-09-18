from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import datetime, tzinfo, timedelta

from library.models import Ship, ShipTrackingData, DataSourceEnum, Base
from library.mt import get_ships_position_data

engine = create_engine("sqlite+pysqlite:///mydb.db", echo=True, future=True)
Base.metadata.create_all(engine)

# create session and add objects
with Session(engine) as session:
    entry_dt = datetime.utcnow()
    rows = get_ships_position_data([(4518, 2610)])
    for r in rows:
        ship_id = r.get('SHIP_ID', None)
        ship = session.get(Ship, ship_id)
        if ship is None:
            ship = Ship(
                id=ship_id,
                created_at=entry_dt,
                data_source=DataSourceEnum.MARINE_TRAFFIC,
                flag=r.get('FLAG', None),
                gt_shiptype=r.get('GT_SHIPTYPE', None),
                shipname=r.get('SHIPNAME', None),
                shiptype=r.get('SHIPTYPE', None),
                length=r.get('LENGTH', None),
                width=r.get('WIDTH', None),
                w_left=r.get('W_LEFT', None),
                l_fore=r.get('L_FORE', None),
            )
            session.add(ship)
        v = ShipTrackingData(
            created_at=entry_dt,
            data_source=DataSourceEnum.MARINE_TRAFFIC,
            ship_id=ship.id,
            course=r.get('COURSE', None),
            destination=r.get('DESTINATION', None),
            dwt=r.get('DWT', None),
            last_position_dt=entry_dt+timedelta(minutes=int(r.get('ELAPSED', 0))),
            heading=r.get('HEADING', None),
            lat=r.get('LAT', None),
            lon=r.get('LON', None),
            rot=r.get('ROT', None),
            status_name=r.get('STATUS_NAME', None),
            speed=r.get('SPEED', None),
        )
        session.add(v)
    session.commit()
