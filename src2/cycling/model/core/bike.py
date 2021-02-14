import logging

logger = logging.getLogger()


class Bike:
    def __init__(self, name, mass, cda, crr, eff_drive=0.977, cda_climb=None, r_gradient_switch=None):
        self.name = name
        self.mass = mass
        self.cda = cda  # aerodynamic drag coefficient

        if cda_climb:
            self.cda_climb = cda_climb
        else:
            logger.warning('No cda_climb defined for Bike: defaulting equal to cda')
            self.cda_climb = cda

        if r_gradient_switch:
            self.r_gradient_switch = r_gradient_switch
        else:
            self.r_gradient_switch = 1000

        self.crr = crr  # tyre rolling resistance coefficient
        self.crr_front = crr  # assume front and rear tyres are the same
        self.crr_rear = crr
        self.eff_drive = eff_drive  # efficiency of the drive system, assumed to be 97.7%
        # (c.f. Martin, James & Gardner, Andrew & Barras, Martin & Martin, David. (2006). Modeling Sprint Cycling Using
        # Field-Derived Parameters and Forward Integration. Medicine and science in sports and exercise. 38. 592-7.
        # 10.1249/01.mss.0000193560.34022.04.)

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}>'
