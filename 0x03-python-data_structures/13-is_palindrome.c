#include "lists.h"



/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *mid = NULL;
    int isPalindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    prev->next = NULL;


    listint_t *current = slow;
    listint_t *next = NULL;
    listint_t *prev2 = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev2;
        prev2 = current;
        current = next;
    }

    
    listint_t *first = *head;
    listint_t *second = prev2;

    while (second != NULL)
    {
        if (first->n != second->n)
        {
            isPalindrome = 0;
            break;
        }
        first = first->next;
        second = second->next;
    }

    
    current = prev2;
    prev2 = NULL;
    while (current != NULL)
    {
        next = current->next;
        current->next = prev2;
        prev2 = current;
        current = next;
    }

    if (mid != NULL) 
    {
        prev->next = mid;
        mid->next = prev2;
    }
    else
    {
        prev->next = prev2;
    }

    return isPalindrome;
}