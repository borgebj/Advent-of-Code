import sys
from collections import deque

class Teque:
    def __init__(self):
        self.front = deque()
        self.back = deque()

    def push_front(self, x):
        self.front.appendleft(x)
        self.balance()

    def push_back(self, x):
        self.back.append(x)
        self.balance()

    def push_middle(self, x):
        self.front.append(x)
        self.balance()

    def get(self, index):
        return self.front[index] if index < len(self.front) else self.back[index - len(self.front)]

    def balance(self):
        while len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        while len(self.back) > len(self.front):
            self.front.append(self.back.popleft())

def main():
    lines = int(sys.stdin.readline())
    teque = Teque()

    for _ in range(lines):
        action, arg = sys.stdin.readline().split()

        if action == "push_front":
            teque.push_front(int(arg))
        elif action == "push_back":
            teque.push_back(int(arg))
        elif action == "push_middle":
            teque.push_middle(int(arg))
        elif action == "get":
            sys.stdout.write(str(teque.get(int(arg))) + '\n')

if __name__ == "__main__":
    main()
