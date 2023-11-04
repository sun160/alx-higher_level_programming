#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - function checks Linked list cycle.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t* list)
{
    listint_t* now, *test;

    if (list == NULL || list->next == NULL)
        return (0);
    now = list;
    test = now->next;

    while (now != NULL && test->next != NULL
        && test->next->next != NULL)
    {
        if (now == test)
            return (1);
        now = now->next;
        test = test->next->next;
    }
    return (0);
}
