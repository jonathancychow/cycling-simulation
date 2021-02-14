import numpy as np


class CriticalPowerModel:
    """
    Optimisation of Skiba's algorithm by Dave Waterworth.
    Source:
    http://markliversedge.blogspot.nl/2014/10/wbal-optimisation-by-mathematician.html
    Source:
    Skiba, Philip Friere, et al. "Modeling the expenditure and reconstitution of work capacity above critical power."
    Medicine and science in sports and exercise 44.8 (2012): 1526-1532.
    """

    def __init__(self, cp, w_prime):
        self.cp = cp
        self.w_prime = w_prime

    def compute_tau(self, power):
        power_below_cp = power[power < self.cp]
        if np.any(power_below_cp):
            avg_power_below_cp = np.mean(power_below_cp)
        else:
            avg_power_below_cp = 0
        delta_cp = self.cp - avg_power_below_cp
        return 546 * np.exp(-0.01 * delta_cp) + 316

    def w_prime_balance(self, power, sampling_rate=1):
        tau = self.compute_tau(power)
        w_prime_balance = []
        w_prime_exp_sum = 0
        for t, p in enumerate(power):
            w_prime_exp = max(0, p - self.cp)
            w_prime_exp_sum += w_prime_exp * np.exp(t * sampling_rate / tau)
            w_prime_balance.append(self.w_prime - w_prime_exp_sum * np.exp(-t * sampling_rate / tau))
        return w_prime_balance
