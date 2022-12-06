#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: - a pointer to the head node
 *
 * Return: 0 if list is not a palindrome,
 * otherwise, 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *rev_list;
	listint_t *temp;

	if (!(*head))
		exit(EXIT_FAILURE);
	temp = *head;
	rev_list = NULL;
	while (temp)
	{
		add_nodeint_end(&rev_list, temp->n);
		temp = temp->next;
	}
	temp = *head;
	reverse_listint(&rev_list);

	while (temp)
	{
		if (temp->n != rev_list->n)
		{
			return (0);
		}
		temp = temp->next;
		rev_list = rev_list->next;
	}
	return (1);
}

/**
 * reverse_listint - reverses a listint_t linked list
 * @head: a pointer to the head node of the list
 *
 * Return: a pointer to the reversed list
*/

listint_t *reverse_listint(listint_t **head)
{
	listint_t *next, *prev;

	next = NULL;
	prev = NULL;

	if (!head || !(*head))
		return (*head);
	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = next;
	}
	*head = prev;
	return (*head);
}
