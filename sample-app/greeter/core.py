def greet(name: str = "World") -> str:
    """Return a friendly greeting, falling back to World for blank names."""
    cleaned = name.strip()
    return f"Hello, {cleaned or 'World'}!"


def shout(name: str = "World") -> str:
    """Return the greeting in capitals."""
    return greet(name).upper()
