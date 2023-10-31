#include "lists.h"
/**
 * insert_node - a function that inserts a no into a sorted s-l list.
 * @head: pointer to head
 * @number: number to insert.
 * Return: Null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert = *head;
	listint_t *update;

	update = malloc(sizeof(listint_t));

	if (!update)
		return (NULL);
	update->n = number;

	if (insert == NULL || insert->n >= number)
	{
		update->next = insert;
		*head = update;
		return (update);
	}

	while (insert && insert->next && insert->next->n < number)
		insert = insert->next;
	update->next = insert->next;
	insert->next = update;

	return (update);
}
