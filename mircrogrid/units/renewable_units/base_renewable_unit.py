import abc


class BaseREUnit(metaclass=abc.ABCMeta):

    def __init__(self, capex: float, annual_opex: float, replacement_cost: float, project_lifetime: int):
        self._capex = capex
        self._annual_opex = annual_opex
        self._replacement_cost = replacement_cost
        self._project_lifetime = project_lifetime