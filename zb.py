 
from datetime import datetime, timedelta

nine_hours_from_now = datetime.now() - timedelta(hours=9)
print(nine_hours_from_now)