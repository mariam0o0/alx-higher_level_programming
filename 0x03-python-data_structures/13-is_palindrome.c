#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * _reverse - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the head of the reversed list
 */
listint_t *_reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of listint_t list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *head_sec;
	listint_t *temp;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	head_sec = _reverse(&slow);
	temp = head_sec;
	while (*head && head_sec)
	{
		if ((*head)->n != head_sec->n)
		{
			_reverse(&temp);
			return (0);
		}
		*head = (*head)->next;
		head_sec = head_sec->next;
	}
	_reverse(&temp);

	return (1);
}

