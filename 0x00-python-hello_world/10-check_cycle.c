#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Checks if a singly linked list has a cycle in it
  * @list: The singly linked list to be checked
  * Return: 1 if has a cycle in it or 0 if not
  */
int check_cycle(listint_t *list)
{
int total = 0;
listint_t *a = list, *b = list;

while ((a && b) && b->next)
{
a = a->next;

if (b->next || b->next->next)
b = b->next->next;
else
break;
if (a == b)
{
total = 1;
break;
}
}
return (total);

}
