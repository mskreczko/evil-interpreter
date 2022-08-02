from evil import EvilInterpreter


def main():
    ev = EvilInterpreter()
    ev.load_file("hello_world.evl")
    ev.run()


if __name__ == "__main__":
    main()
