import queue

# Create the queue
my_orders_queue = queue.SimpleQueue()

# Add an element to the queue
my_orders_queue.put("samosas")

# Remove an element from the queue
my_orders_queue.get()
