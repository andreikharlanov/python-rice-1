def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    return present_value * (1 + rate_per_period) ** periods

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

print "$1000 at 4% compounded monthly for 1 years yields $", future_value(1000, .04, 12, 1)

print "$100000 at 13% compounded quarterly for 5 years yields $", future_value(100000, .13, 4, 5)
