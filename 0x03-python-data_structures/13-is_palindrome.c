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
	listint_t *rev_list = malloc(sizeof(listint_t));
	listint_t *temp = malloc(sizeof(listint_t));

    if (!temp || !rev_list)
    {
        exit(EXIT_FAILURE);
    }

	if (!(*head))
		return (0);
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
