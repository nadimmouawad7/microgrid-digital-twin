from .base_renewable_unit import BaseREUnit
class PVPowerPlant(BaseREUnit):

    def __init__(self, clock, power_profile: list, pv_peak_power: float,  project_lifetime: int, tilt_angle: float,
                 azimuth: float, number_of_time_steps: int, capex: float = 0,
                 annual_opex: float = 0, replacement_cost: float = 0):

        self._clock = clock
        self._power_profile = power_profile
        self._pv_peak_power = pv_peak_power
        self._current_power = 0
        self._excess_power = 0
        self._number_of_time_steps = number_of_time_steps
        self._tilt_angle = tilt_angle
        self._azimuth = azimuth
