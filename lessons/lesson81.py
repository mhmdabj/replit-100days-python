def robot_detector(metal, infinity, food):
    if metal == "Yes":
        return "You're a robot!"
    elif "error" in infinity.lower():
        return "You're a robot!"
    elif food == "synthetic oil":
        return "You're a robot!"
    else:
        return "Hi there fellow human"

if __name__ == "__main__":
    print(robot_detector("Yes", "2", "human food"))
    print(robot_detector("No", "error123", "human food"))
    print(robot_detector("No", "infinity", "synthetic oil"))
    print(robot_detector("No", "infinity", "human food")) 