class NumberRangeChecker:
    def __init__(self, lower_limit, upper_limit):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def is_within_range(self, number) -> bool:
        return self.lower_limit <= number <= self.upper_limit