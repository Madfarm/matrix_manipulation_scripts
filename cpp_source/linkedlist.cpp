#include <iostream>

using namespace std;

class Node {
public:
  int data;
  Node* next;

  Node(int data) {
    this->data = data;
    this->next = NULL;
  }
};

class Linkedlist {
public:
  Node* head;

  Linkedlist() {
    this->head = NULL;
  }

  void add(int data) {
    Node* new_node = new Node(data);

    if (this->head == NULL) {
      this->head = new_node;
    } else {
      Node* temp = this->head;

      while (temp->next != NULL) {
        temp = temp->next;
      }

      temp->next = new_node;
    }
  }

  void deleteNode(int data) {
    Node* temp = this->head;
    Node* prev = NULL;

    if (temp != NULL && temp->data == data) {
      this->head = temp->next;
      delete temp;
      return;
    }

    while (temp != NULL && temp->data != data) {
      prev = temp;
      temp = temp->next;
    }

    if (temp == NULL) {
      cout << "Node not found" << endl;
      return;
    }

    prev->next = temp->next;
    delete temp;
  }

  bool search(int data) {
    Node* temp = this->head;

    while (temp != NULL) {
      if (temp->data == data) {
        return true;
      }

      temp = temp->next;
    }

    return false;
  }

  void print() {
    Node* temp = this->head;

    while (temp != NULL) {
      cout << temp->data << " ";
      temp = temp->next;
    }

    cout << endl;
  }
};

int main() {
  Linkedlist list;

  int choice;

  do {
    cout << "===============By Your Name================ " << endl;
    cout << " ~~ WELCOME to Linked List program ~~ " << endl;
    cout << " ============================================= " << endl;
    cout << "Select and Enter Your Choice from the Menu __ " << endl;
    cout << " ============================================= " << endl;
    cout << "1. Add" << endl;
    cout << "2. Delete" << endl;
    cout << "3. Search" << endl;
    cout << "4. Print" << endl;
    cout << "5. Exit" << endl;
    cout << " ============================================= " << endl;

    cin >> choice;

    switch (choice) {
      case 1:
        int data;
        cout << "Enter data to add: ";
        cin >> data;
        list.add(data);
        break;
      case 2:
        cout << "Enter data to delete: ";
        cin >> data;
        list.deleteNode(data);
        break;
      case 3:
        cout << "Enter data to search: ";
        cin >> data;
        if (list.search(data)) {
          cout << "Data found" << endl;
        } else {
          cout << "Data not found" << endl;
        }
        break;
      case 4:
        list.print();
        break;
      case 5:
        cout << "Thank you for using Linked List program" << endl;
        break;
      default:
        cout << "Invalid choice" << endl;
    }
  } while (choice != 5);

  return 0;
}