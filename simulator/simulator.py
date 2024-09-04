from mircrogrid.microgrid_twin import Microgrid
from controller.rule_based_controller import RuleBasedController


class Simulator:
    def __init__(self, clock):
        self.microgrid = Microgrid()
        self.controller = RuleBasedController()
        self.clock = clock

    def run_step(self):
        # Step the clock
        self.clock.step()

        # Get the current state of the microgrid
        microgrid_state = self.microgrid.get_state()

        # Controller makes decisions based on the current state
        control_actions = self.controller.make_decision(microgrid_state)

        # Apply the control actions to the microgrid
        self.microgrid.apply_control(control_actions)

        # Optionally, collect results, log data, etc.
        print(f"Simulation time: {self.clock._current_time}, State: {microgrid_state}")

    def run_simulation(self, end_time):
        while self.clock._current_time < end_time:
            self.run_step()


