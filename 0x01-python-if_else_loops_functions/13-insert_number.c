#include "lists.h"
#include <stdlib.h>

/**
  * insert_node - Inserts a number into the singly linked list
  * @head: The head of the sorted singly linked list
  * @number: The number to be inserted in the singly linked list
  * Return: The singly linked list with the new number added
  */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *x = NULL, *newnode = NULL, *temp = NULL;

newnode = malloc(sizeof(listint_t));
if (newnode == NULL)
return (NULL);

newnode->n = number;
if (*head)
{
x = *head;
if (number <= x->n)
{
newnode->next = x;
*head = newnode;
}
else
{
while (x->next)
{
if (number <= x->next->n)
{
temp = x->next;
x->next = newnode;
newnode->next = temp;
return (*head);
}
x = x->next;
}
temp = x->next;
x->next = newnode;
newnode->next = temp;
}
return (*head);
}
newnode->next = NULL;
*head = newnode;
return (*head);
}
