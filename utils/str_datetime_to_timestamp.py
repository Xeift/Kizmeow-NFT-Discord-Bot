from datetime import datetime


def str_datetime_to_timestamp(str_datetime):
    dt_obj = datetime.fromisoformat(str_datetime)
    timestamp = dt_obj.timestamp()

    return str(int(timestamp))

# --------------------     TEST        --------------------
# print(str_datetime_to_timestamp('2025-01-09T13:54:51.615182'))
