def say_hello(name: str) -> str:
    if not name:
        raise ValueError("name cannot be empty")
    return f"Hello, {name}!"