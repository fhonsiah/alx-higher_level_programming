#include <stdlib.h>
/**
 *struct listint_s - singly linked list
 *@n: integer
 *@next: points to the next node
 *
 *Description: sinlgy linked list node structure
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;
	new_node-> = number;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return new_node;
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;

	return new_node;
}
