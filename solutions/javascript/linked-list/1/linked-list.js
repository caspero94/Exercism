//
// This is only a SKELETON file for the 'Linked List' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

export class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(data) {
    this.size++;
    const nodeNew = new Node(data);
    if (!this.head) {
      this.head = nodeNew;
      this.tail = nodeNew;
    } else {
      this.tail.next = nodeNew;
      nodeNew.prev = this.tail;
      this.tail = nodeNew;
    }
  }

  pop() {
    if (!this.head) return;

    const nodeDelete = this.tail.data;

    if (this.head === this.tail) {
      this.tail = null;
      this.head = null;
    } else {
      this.tail = this.tail.prev;
      this.tail.next = null;
    }
    this.size--;
    return nodeDelete;
  }

  shift() {
    if (!this.head) return;
    const nodeDelete = this.head;
    this.head.prev = null;
    this.head = this.head.next;
    this.size--;
    return nodeDelete.data;
  }

  unshift(data) {
    this.size++;
    const nodeNew = new Node(data);
    if (!this.head) {
      this.head = nodeNew;
      this.tail = nodeNew;
    } else {
      const oldHead = this.head;
      oldHead.prev = nodeNew;
      this.head = nodeNew;
      this.head.next = oldHead;
    }
  }

  delete(data) {
    if (!this.head) return;
    if (this.head.data === data) {
      if (this.head === this.tail) {
        this.head = null;
        this.tail = null;
      } else {
        this.head = this.head.next;
        this.head.prev = null;
      }
      this.size--;
      return;
    }

    let current = this.head;
    while (current && current.data !== data) {
      current = current.next;
    }
    if (current) {
      if (current === this.tail) {
        this.tail = current.prev;
        this.tail.next = null;
      } else if (current.next) {
        current.next.prev = current.prev;
      }
      if (current.prev) {
        current.prev.next = current.next;
      }

      this.size--;
      return;
    }
  }

  count() {
    return this.size;
  }
}
