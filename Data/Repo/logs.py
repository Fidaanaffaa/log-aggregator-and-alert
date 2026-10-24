from sqlalchemy import text

import Data.Log
from Data.database import Session

class logs:

    def __init__(self, session:Session):
        self.session = session

    async def create_log(self, log: dict):
        # Create a Log object from the input dictionary
        log_entry = Data.Log.Log(
            id=log.get("id"),
            service_name=log.get("service_name"),
            level=log.get("level"),
            message=log.get("message"),
            timestamp=log.get("timestamp")
        )

        self.session.add(log_entry)
        self.session.commit()
        self.session.refresh(log_entry)

        return {"message": "Log created successfully!", "log": log_entry.__dict__}
    
    async def get_logs(self):
        logs = self.session.exec(text('SELECT * FROM events'))
        logs_list = logs.fetchall()
        return {"logs": [dict(log._mapping) for log in logs_list]}