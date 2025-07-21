def import_and_countdown(module):
    print("Countdown")
    module.countdown()

if __name__ == "__main__":
    class MockModule:
        @staticmethod
        def countdown():
            print("3, 2, 1, Go!")
    import_and_countdown(MockModule) 