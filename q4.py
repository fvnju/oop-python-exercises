class Time:
    def __init__(self, seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        minutes = self.seconds // 60
        remaining_seconds = self.seconds % 60
        return f"{minutes}:{remaining_seconds:02}"
        # NOTE: the :02 formats integers i.e. "2" => "02" 

    def convert_to_hours(self):
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        remaining_seconds = self.seconds % 60
        return f"{hours}:{minutes:02}:{remaining_seconds:02}"

# Test usage:
time = Time(230)
print(time.convert_to_minutes())
print(time.convert_to_hours())

time2 = Time(3665)
print(time2.convert_to_minutes())
print(time2.convert_to_hours())
