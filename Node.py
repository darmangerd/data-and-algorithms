class Node:
    previous_node = None
    current_node = None
    next_node = None
    def __init__(self, previous_node = None, current_node = None, next_node = None):
        self.current_node = current_node
        self.previous_node = previous_node
        self.next_node = next_node
    
    def get(self):
        return self.current_node
    
    def set(self, node):
        self.current_node = node
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, node):
        self.next_node = node
        
    def get_previous(self):
        return self.previous_node
    
    def set_previous(self, node):
        self.previous_node = node
