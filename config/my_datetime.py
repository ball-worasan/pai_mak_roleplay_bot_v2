import pytz
from datetime import datetime

async def get_local_time(timezone_name="Asia/Bangkok", format="%Y-%m-%d %H:%M:%S"):
    if timezone_name not in pytz.all_timezones:
        timezone_name = "Asia/Bangkok"

    local_timezone = pytz.timezone(timezone_name)
    local_time = datetime.now(local_timezone)
    try:
        return local_time.strftime(format)
    except ValueError:
        return local_time.strftime("%Y-%m-%d %H:%M:%S")