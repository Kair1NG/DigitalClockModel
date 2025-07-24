import datetime as dt

class ClockModel:
    # majority of the methods here are used for testing.
    @staticmethod
    def get_current_time():
        return dt.datetime.now().time()

    @staticmethod
    def get_current_date():
        return dt.datetime.now().date()

    @staticmethod
    def get_current_datetime():
        return dt.datetime.now()

    @staticmethod
    def format_date(date, format_string="%m %d %Y"):
        return date.strftime(format_string)

    @staticmethod
    def format_time(time, format_string="%I %M %S %p"):
        return time.strftime(format_string)

    @staticmethod
    def format_datetime(datetime_obj, format_string="%m-%d-%Y %I:%M:%S %p"):
        return datetime_obj.strftime(format_string)

    @staticmethod
    def get_month_name(month_number):
        return dt.date(1900, month_number, 1).strftime('%B')

    @staticmethod
    def get_day_of_week(date_object):
        return date_object.strftime('%A')

    @staticmethod
    def reformatted_monthdate():
        cd = ClockModel.get_current_date()
        return f"{ClockModel.get_month_name(cd.month)} {cd.day} {cd.year}"
