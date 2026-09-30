def get_room_state(room_name):
    """Prompt user to choose 'Dirty' or 'Clean' for a given room."""
    while True:
        state = input(f"Enter state for Room {room_name} (1 for Dirty, 2 for Clean): ").strip()
        if state == '1':
            return 'Dirty'
        elif state == '2':
            return 'Clean'
        print("Invalid choice! Please enter 1 for Dirty or 2 for Clean.")


# Let the user set up the environment
print("--- Setup Environment ---")
environment = {
    'A': get_room_state('A'),
    'B': get_room_state('B')
}

# Start the agent at location A
agent_location = 'A'


def vacuum_agent(location, status):
    """Reflex agent logic using suck, left, and right."""
    if status == 'Dirty':
        return 'suck'
    elif location == 'A':
        return 'right'
    elif location == 'B':
        return 'left'


def run_simulation(steps=4):
    global agent_location
    print("\n--- Vacuum Cleaner Simulation ---")
    print(f"Initial State: {environment}\n")

    for step in range(1, steps + 1):
        status = environment[agent_location]
        action = vacuum_agent(agent_location, status)

        print(f"Step {step}: Agent is at Location {agent_location} [{status}]")
        print(f"Action taken: {action.upper()}")

        # Execute the action
        if action == 'suck':
            environment[agent_location] = 'Clean'
        elif action == 'right':
            agent_location = 'B'
        elif action == 'left':
            agent_location = 'A'

        print(f"Current State: {environment}\n")


if __name__ == "__main__":
    run_simulation()
