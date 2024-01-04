include "lists.h"

/**
*check_cycle - checks if a singly linked list has a cycle in it
*@list: pointer to the head of the list
*Return: 1 if there is a cycle, 0 if not
*/
int check_cycle(listint_t *list)
{
listint_t *cycle1 = list;
listint_t *cycle2 = list;

while (cycle1 && cycle2 && cycle2->next)
{
cycle1 = cycle1->next;
cycle2 = cycle2->next->next;

if (cycle1 == cycle2)
return (1);
}

return (0);
}
