#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	lsitint_t *fast = list;

	if (list == NULL)
	{
		return (0);
	}
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
