# Ocampo, Hans Christian S.
# CS-301
# 6IMODSIM
# Module Activity 1 - Digital Clock Simulation.

from ClockModel import ClockModel
from ClockUI import ClockUI

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