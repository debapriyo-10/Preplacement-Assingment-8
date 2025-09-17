#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

struct Node {
    int data;
    struct Node *left, *right;
};

struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = node->right = NULL;
    return node;
}

int isBSTUtil(struct Node* node, int min, int max) {
    if (node == NULL) return 1;
    if (node->data <= min || node->data >= max) return 0;
    return isBSTUtil(node->left, min, node->data) &&
           isBSTUtil(node->right, node->data, max);
}

int isBST(struct Node* node) {
    return isBSTUtil(node, INT_MIN, INT_MAX);
}

int main() {
    struct Node* root = newNode(10);
    root->left = newNode(5);
    root->right = newNode(20);
    printf("%s", isBST(root) ? "Yes" : "No");
    return 0;
}