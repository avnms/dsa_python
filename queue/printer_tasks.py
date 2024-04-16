from main import Queue


class PrinterTasks:
    def __init__(self):
        self.queue = Queue()

    def add_document(self, document):
        self.queue.enqueue(document)

    def print_documents(self):
        while self.queue.has_elements():
            document = self.queue.dequeue()
            if document:
                print("Printing", document)


if __name__ == "__main__":
    printer_tasks = PrinterTasks()
    printer_tasks.add_document("Document 1")
    printer_tasks.add_document("Document 2")
    printer_tasks.add_document("Document 3")
    printer_tasks.print_documents()
