import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_gain(omega_ratios: np.array, attenuation_coefficient : float) -> np.array:
    argument = 1 / np.sqrt( (1 - (omega_ratios)**2)**2 + (2*attenuation_coefficient*omega_ratios)**2 )
    return 20*np.log10(argument)

def calculate_attenuation_coef(resistance: float) -> float:
    return 0.0025*resistance