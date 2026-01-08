#include <stdio.h>
#include <stdlib.h>

struct node
{
    int coef;
    int index;
    struct node *next;
};

struct node *Read()
{
    struct node *head, *tail, *p;
    int i, n;
    head = (struct node *)malloc(sizeof(struct node));
    head->next = NULL;
    tail = head;
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        p = (struct node *)malloc(sizeof(struct node));
        scanf("%d %d", &p->coef, &p->index);
        p->next = NULL;
        tail->next = p;
        tail = p;
    }
    tail->next = NULL;
    return head;
}

struct node *addition(struct node *L1, struct node *L2)
{
    struct node *t1, *t2, *L3, *p, *head;
    t1 = L1->next;
    t2 = L2->next;
    head = (struct node *)malloc(sizeof(struct node));
    head->next = NULL;
    L3 = head;
    while (t1 && t2)
    {
        p = (struct node *)malloc(sizeof(struct node));
        if (t1->index == t2->index)
        {
            p->coef = t1->coef + t2->coef;
            p->index = t1->index;
            t1 = t1->next;
            t2 = t2->next;
        }
        else if (t1->index < t2->index)
        {
            p->coef = t2->coef;
            p->index = t2->index;
            t2 = t2->next;
        }
        else if (t1->index > t2->index)
        {
            p->coef = t1->coef;
            p->index = t1->index;
            t1 = t1->next;
        }
        L3->next = p;
        L3 = L3->next;
    }
    if (t1)
        L3->next = t1;
    else if (t2)
        L3->next = t2;
    return head;
}

void Print(struct node *L)
{
    struct node *p = L->next;
    int flag = 1;
    for (; p; p = p->next)
    {
        if (flag == 0 && p->coef)
        {
            printf(" ");
        }
        if (p->coef)
        {
            printf("%d %d", p->coef, p->index);
            flag = 0;
        }
    }
    if (flag == 1)
        printf("0 0");
    printf("\n");
}

int main()
{
    struct node *L1, *L2, *head;
    L1 = Read();
    L2 = Read();
    head = addition(L1, L2);
    Print(head);
    return 0;
}