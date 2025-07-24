# Ocampo, Hans Christian S.
# CS-301
# 6IMODSIM
# Module Activity 1 - Digital Clock Simulation.

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

class ClockUI:
    def __init__(self):
        self.clock_model = ClockModel()
        
    DIGITS = {
        '0': [" _ ",
              "| |",
              "|_|"],
        '1': ["   ",
              "  |",
              "  |"],
        '2': [" _ ",
              " _|",
              "|_ "],
        '3': [" _ ",
              " _|",
              " _|"],
        '4': ["   ",
              "|_|",
              "  |"],
        '5': [" _ ",
              "|_ ",
              " _|"],
        '6': [" _ ",
              "|_ ",
              "|_|"],
        '7': [" _ ",
              "  |",
              "  |"],
        '8': [" _ ",
              "|_|",
              "|_|"],
        '9': [" _ ",
              "|_|",
              " _|"]
    }

    colon = ["   ",
             " . ",
             " . "]
    
    def digital_clock(self, time=None):
        if time is None:
            time = self.clock_model.get_current_time()
            
        hour_12 = time.hour % 12
        if hour_12 == 0:
            hour_12 = 12
        h = f"{hour_12:02d}"
        m = f"{time.minute:02d}"
        digits = h + m 

        # the magic where we turn the digits to their 'Digital UI'.
        lines = ["", "", ""]
        for i in range(3):
            lines[i] += self.DIGITS[digits[0]][i] + " "
            lines[i] += self.DIGITS[digits[1]][i] + " "
            lines[i] += self.colon[i] + " "
            lines[i] += self.DIGITS[digits[2]][i] + " "
            lines[i] += self.DIGITS[digits[3]][i]
            
        digital_clock = "\n".join(lines)
        digital_clock += f" {time.second:02d}"
        return digital_clock

    def display_digital_clock(self):
        print(self.digital_clock())

cm = ClockModel()
cux = ClockUI()
# testing the clock
def test_clock_functions():
    print("Test clock model functions:")
    print("Current time:", cm.format_time(cm.get_current_time()))
    print("Current date:", cm.format_date(cm.get_current_date()))
    print("Current datetime:", cm.format_datetime(cm.get_current_datetime()))
    print("Current day of the week:", cm.get_day_of_week(cm.get_current_date()))
    print("Current month name:", cm.get_month_name(cm.get_current_date().month))
    print("Reformatted monthdate:", cm.reformatted_monthdate())

def test_clock_module():
    print("Clock Model Module")
    print(f'{cm.format_time(cm.get_current_time())}')
    print(f'{cm.reformatted_monthdate()}\t {cm.get_day_of_week(cm.get_current_date())}')

def test_clock_ui():
    print("Clock UI Module")
    cux.display_digital_clock()
# ---

def terminal_clear():
    print("\033[H\033[J", end="")

def run_clock():
    last_ran_time = ""
    while True:
        time = cm.get_current_time() 
        # this could use the "dt" directly. But, I use the ClockModel instead 
        # to show class functions if I were to seperate the classes to their own files.
        current_running_time = time.strftime("%H:%M:%S")
        am_pm = "AM" if time.hour < 12 else "PM"
        if current_running_time != last_ran_time:
            terminal_clear()
            print(f"\t\t    {am_pm}")
            cux.display_digital_clock()
            print(f'\n{cm.reformatted_monthdate()}\t{cm.get_day_of_week(cm.get_current_date())}')
            last_ran_time = current_running_time

if __name__ == "__main__":
    green = "\033[0;32m"
    clear = "\033[0m"
    print(green)
   
    try: 
        run_clock()
    except KeyboardInterrupt:
        print(clear)