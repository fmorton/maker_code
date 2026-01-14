from pynput import keyboard

# The event listener will be running in this block
while True:
    print("Running...")

    with keyboard.Events() as events:
        # Block at most one second to get an event
        event = events.get(1.0)
        if event is None:
            print("No key pressed within one second.")
        else:
            # Check if the event is a key press and extract the character
            if isinstance(event, keyboard.Events.Press):
                if hasattr(event.key, "char"):
                    print(f"Received character: {event.key.char}")
                else:
                    print(f"Received special key: {event.key}")
            elif isinstance(event, keyboard.Events.Release):
                # Handle key release events if needed
                pass
