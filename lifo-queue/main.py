import queue

my_book_stack = queue.LifoQueue(maxsize=0)

my_book_stack.put("Don Quixote")

my_book_stack.get()
