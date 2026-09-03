class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Remove the first node matching data, if found."""
        current = self.head
        prev = None

        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def find(self, data):
        """Return True if data exists in the list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def to_list(self):
        """Return the linked list as a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        return " -> ".join(str(item) for item in self.to_list()) or "(empty)"

    def __add__(self, other):
        """Concatenate two linked lists: list1 + list2"""
        new_list = LinkedList()
        for item in self.to_list() + other.to_list():
            new_list.append(item)
        return new_list

    def __len__(self):
        """Support len(linked_list)"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        """Support for-loops: for item in linked_list"""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __getitem__(self, index):
        """Support linked_list[i]"""
        if index < 0:
            raise IndexError("Negative indexing not supported")
        current = self.head
        for _ in range(index):
            if not current:
                raise IndexError("Index out of range")
            current = current.next
        if not current:
            raise IndexError("Index out of range")
        return current.data

    def __contains__(self, data):
        """Support: value in linked_list"""
        return self.find(data)

    def __eq__(self, other):
        """Support: list1 == list2"""
        if not isinstance(other, LinkedList):
            return NotImplemented
        return self.to_list() == other.to_list()

    def __repr__(self):
        """Unambiguous representation, e.g. for debugging"""
        return f"LinkedList({self.to_list()!r})"


# --- Interactive example ---
if __name__ == "__main__":
    ll = LinkedList()
    print("Linked List Builder")
    print("Commands: add <value> | prepend <value> | delete <value> | find <value> | show | quit")

    while True:
        command = input("\n> ").strip().split(maxsplit=1)

        if not command:
            continue

        action = command[0].lower()

        if action == "quit":
            print("Final list:", ll)
            break

        elif action == "add" and len(command) > 1:
            ll.append(command[1])
            print("Added.", ll)

        elif action == "prepend" and len(command) > 1:
            ll.prepend(command[1])
            print("Prepended.", ll)

        elif action == "delete" and len(command) > 1:
            found = ll.delete(command[1])
            print("Deleted." if found else "Not found.", ll)

        elif action == "find" and len(command) > 1:
            found = ll.find(command[1])
            print("Found!" if found else "Not found.")

        elif action == "show":
            print(ll)

        else:
            print("Unknown command or missing value. Try: add <value>")
