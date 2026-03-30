class MinStack {
    ArrayList<Integer> list;
    Stack<Integer> minStack;
    int top;
    public MinStack() {
        list = new ArrayList<>();
        minStack = new Stack<>();
        this.top = -1;
    }
    
    public void push(int val) {
        if (minStack.isEmpty() || val <= minStack.peek())   {
            minStack.add(val);
        }
        list.add(++top, val);

    }
    
    public void pop() {
        if (top == -1) {
            throw new RuntimeException("Stack is empty");
        }
        if (list.get(top).equals(minStack.peek()))  {
            minStack.pop();
        }
        list.remove(top--);
    }
    
    public int top() {
        if (top == -1) {
            throw new RuntimeException("Stack is empty");
        }
        return list.get(top);
    }
    
    public int getMin() {
        if (minStack.isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return minStack.peek();
    }
}
