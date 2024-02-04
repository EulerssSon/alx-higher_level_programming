#include "lists.h"

/**
 * reverse_list - reverses a listint_t linked list
 * @head: pointer to the head of the list
 * Return: pointer to the first node of the reversed list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

listint_t *find_middle(listint_t *head)
{
	listint_t *slow = head, *fast = head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (slow);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *middle, *rev, *current = *head;

	if (!head || !*head || !(*head)->next)
		return (1);

	middle = find_middle(*head);
	rev = middle;
	reverse_list(&rev);

	while (rev)
	{
		if (current->n != rev->n)
			return (0);
		current = current->next;
		rev = rev->next;
	}
	return (1);
}
