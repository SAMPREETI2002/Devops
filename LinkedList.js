class Item {
    constructor(itemName, price) {
        this.itemName = itemName;
        this.price = price;
    }
}
 
class Node {
    constructor(item) {
        this.item = item;  
        this.next = null;
    }
}
class LinkedList {
    constructor() {
        this.head = null;
    }
 
    add(item) {
        const newNode = new Node(item);
 
        if (this.head === null) {
            this.head = newNode;
        } else {
            let current = this.head;
            while (current.next !== null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }
 
    printList() {
        let current = this.head;
        while (current !== null) {
            console.log(`Item: ${current.item.itemName}, Price: ${current.item.price}`);
            current = current.next;
        }
    }
}
 
const itemList = new LinkedList();
 
itemList.add(new Item('Apple', 1.5));
itemList.add(new Item('Banana', 0.8));
itemList.add(new Item('Cherry', 2.2));
 
itemList.printList();
 
has context menu