import math

class Event:
    def __init__(self, rate: float, revenue: float):
        if rate < 0 or revenue < 0:
            raise ValueError("Rate and revenue must be non-negative.")
        self.rate = rate
        self.revenue = revenue

class Investment:
    def __init__(self, id: str, success_events: list[Event], failure_events: list[Event]):
        self.id = id
        if sum(event.rate for event in success_events) + sum(event.rate for event in failure_events) != 1:
            raise ValueError("The sum of rates for all events must equal 1.")
        self.success_events = success_events
        self.failure_events = failure_events

    def math_expect(self) -> float:
        m = 0
        for event in self.success_events:
            m += event.rate * event.revenue
        for event in self.failure_events:
            m += event.rate * event.revenue
        return m

    def variance(self) -> float:
        m = self.math_expect()
        v = 0
        for event in self.success_events:
            v += (event.revenue - m) ** 2 * event.rate
        for event in self.failure_events:
            v += (event.revenue - m) ** 2 * event.rate
        return v

    def rms_deviation(self) -> float:
        return math.sqrt(self.variance())

    def variation_coefficient(self) -> float:
        m = self.math_expect()
        if m == 0:
            raise ValueError("Mathematical expectation is zero, cannot compute variation coefficient.")
        return self.rms_deviation() / m

    def semiquadratic_deviation(self) -> float:
        m = self.math_expect()
        v = 0
        for event in self.failure_events:
            if event.revenue < m:
                v += (event.revenue - m) ** 2 * event.rate
        return math.sqrt(v)

    def semivariation_coefficient(self) -> float:
        m = self.math_expect()
        if m == 0:
            raise ValueError("Mathematical expectation is zero, cannot compute semivariance coefficient.")
        return self.semiquadratic_deviation() / m

    def __str__(self):
        format_str = f"Investment ID: {self.id}\n"
        format_str += "Success Events:"
        for event in self.success_events:
            format_str += f"\n  Rate: {event.rate}, Revenue: {event.revenue}"
        format_str += "\nFailure Events:"
        for event in self.failure_events:
            format_str += f"\n  Rate: {event.rate}, Revenue: {event.revenue}"
        return format_str