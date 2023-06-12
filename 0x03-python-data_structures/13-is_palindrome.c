#include "lists.h"

void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *ptr1, *ptr2;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    prev->next = NULL;
    reverse_list(&slow);
    ptr1 = *head;
    ptr2 = slow;

    while (ptr1 != NULL && ptr2 != NULL)
    {
        if (ptr1->value != ptr2->value)
        {
            reverse_list(&slow);
            prev->next = slow;
            return 0;
        }
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }

    reverse_list(&slow);
    prev->next = slow;
    return 1;
}
