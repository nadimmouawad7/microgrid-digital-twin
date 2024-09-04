import datetime as dt
import calendar


class Clock:
    def __init__(self, start_time, time_step_size):
        self._start_time = start_time
        self._time_step_size = time_step_size
        self._hour_frac = time_step_size / dt.timedelta(hours=1)
        self._current_index = 0
        self._current_time = self._start_time

    def step(self):
        self._current_time += self._time_step_size
        self._current_index += 1

    @property
    def current_time(self):
        return self._current_time

    @property
    def current_index(self):
        return int(self._current_index)

    @property
    def hour_frac(self):
        return self._hour_frac

    @property
    def time_step_size(self):
        return self._time_step_size

    @property
    def start_time(self):
        return self._start_time

    def set_time_and_index(self, time, index):
        self._current_time = time
        self._current_index = index

    @property
    def years_simulated(self):
        hours_simulated = self._current_time - self._start_time
        hours_per_year = dt.timedelta(hours=8784) if calendar.isleap(self._start_time.year) else dt.timedelta(
            hours=8760)
        return int(hours_simulated / hours_per_year)