from ClockModel import ClockModel

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
