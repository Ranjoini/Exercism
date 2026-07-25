EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaning."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes(2 minutes per layer)."""
    return number_of_layers * 2
    
def elapsed_time_in_minutes(number_of_layers , elapsed_bake_time):
    """Calculate elapsed bake time."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

    





