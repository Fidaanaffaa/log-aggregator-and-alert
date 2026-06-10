import Data.Log

class logs:

    def __init__(self):
        pass

    async def create_log(self, log: dict):
        # Create a Log object from the input dictionary
        log_entry = Data.Log.Log(
            log_id=log.get("log_id"),
            service_name=log.get("service_name"),
            level=log.get("level"),
            message=log.get("message"),
            timestamp=log.get("timestamp")
        )

        return {"message": "Log created successfully!", "log": log_entry.__dict__}