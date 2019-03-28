class Time:

    SECONDS_IN_MINUTE = 60

    def __init__(self, minutes = 0, seconds = 0):
        self.minutes = minutes
        self.seconds = seconds

    def convert_to_seconds(self):
        return self.minutes * Time.SECONDS_IN_MINUTE + self.seconds

    def __str__(self):
        if (self.seconds < 10):
            return "{}:0{}".format(self.minutes, self.seconds)
        else:
            return "{}:{}".format(self.minutes, self.seconds)
