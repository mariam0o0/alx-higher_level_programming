#include "lists.h"
#include <stdio.h>


/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: ptr to the linked list
 * Return: 1 if cycle detected and 0 otherwise
 */


int check_cycle(listint_t *list)
{
	listint_t *fast_ptr = list;
	listint_t *slow_ptr = list;

	while (fast_ptr && fast_ptr->next)
	{
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;
		if (slow_ptr == fast_ptr)
			return (1);
	}

	return (0);
}
