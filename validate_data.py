def validate_details(details):
    if not details:  # Checks if details is None or an empty value
        raise ValueError("Details cannot be None or empty.")
    return True
##