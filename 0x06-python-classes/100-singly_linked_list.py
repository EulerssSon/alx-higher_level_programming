#!/usr/bin/python3
'''SinglyLinkedList module'''


class Node:
    '''Node Class'''
    def __init__(self, data, next_node=None) -> None:
        """Constructor for Node class

        Args:
            data (int): data to be stored in the node
            next_node (Node, optional): next node in the list. Defaults to Non

        Returns:
            None
        """
        self.data = data
        self.next = next_node

    @property
    def data(self):
        """Getter for data attribute

        Returns:
            int: data attribute
        """
        return self.__data

    @data.setter
    def data(self, data: int):
        """Setter for data attribute

        Args:
            data (int): data to be stored in the node

        Raises:
            TypeError: if data is not an integer
        """
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

    @property
    def next_node(self) -> 'Node':
        """Getter for next attribute

        Returns:
            Node: next attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node: 'Node'):
        """Setter for next attribute

        Args:
            next_node (Node): next node in the list

        Raises:
            TypeError: if next_node is not a Node object
        """
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node


class SinglyLinkedList:
    """linked List Class with a single link(head)"""
    def __init__(self) -> None:
        """Constructor Method

        Args:
            head (Node): the head to the linked list intially = Null
        """
        self.__head = None

    def sorted_insert(self, value: int) -> None:
        """Insert elment in asscendingly Sorted Order

        Args:
            value (int): the value of the Node to be pushed
        """
        new_node = Node(value)
        dummy_head = Node(-1, self.__head)
        save_dummy = dummy_head

        # Traverse the list untill the next node is greater than the value
        while dummy_head and dummy_head.next and dummy_head.next.data < value:
            dummy_head = dummy_head.next

        # Insert the new node change the links and assign the new head
        new_node.next = dummy_head.next
        dummy_head.next = new_node
        self.__head = save_dummy.next

        # del the dummy_head for the gabadge collector dont trust it
        del save_dummy

    def __str__(self) -> str:
        """String Representation of the Linked List

        Returns:
            str: the string representation of the linked list
        """
        result = ""
        current = self.__head
        if (current):
            while current.next:
                result += f"{current.data}\n"
                current = current.next
            result += f"{current.data}"
        return result
