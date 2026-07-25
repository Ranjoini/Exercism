"""Functions to prevent a nuclear meltdown."""
def is_criticality_balanced(temperature , neurons_emitted):
    """Check balance of the reactor"""
    if temperature < 800 and neurons_emitted > 500 and (temperature * neurons_emitted) < 500000:
        return True
    return False         


def reactor_efficiency(voltage , current , theoretical_max_power):
    """Check reactor efficiency based on voltage, current and theoretical max power""" 
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    if efficiency >= 80:
        return 'green'
    if efficiency >= 60:
        return 'orange'
    if efficiency >= 30:
        return 'red'
    return 'black'


def fail_safe(temperature , neutrons_produced_per_second , threshold):
    """Access safety status of the reactor"""
    product = temperature * neutrons_produced_per_second
    if product < 0.9 * threshold:
        return 'LOW'
    if 0.9 * threshold <= product <= 1.1 * threshold: 
        return 'NORMAL'
    return 'DANGER'
