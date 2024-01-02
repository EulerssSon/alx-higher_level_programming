#include "lists.h"
/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list.
 * @head: Pointer to the head of the list.
 * @n: Data to be added to the new node.
 *
 * Return: Address of the new element, or NULL if it failed.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	/* Assign data to new_node and make it poits to what was the */
	/* the head pointing to and makes the head points to it*/
	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the list.
 * @number: Number to be inserted.
 *
 * Return: Address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	if (*head == NULL || number < (*head)->n)
	{
		return (add_nodeint(head, number));
	}

	/*base case*/
	if (number <= (*head)->n || (*head)->next == NULL)
	{
		return (add_nodeint(&((*head)->next), number));
	}

	return (insert_node(&((*head)->next), number));
}
