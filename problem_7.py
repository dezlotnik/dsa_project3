## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root
        # path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for sub_path in path_list:
            current_node.insert(sub_path)
            current_node = current_node.children[sub_path]
        current_node.handler = handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for sub_path in path_list:
            if sub_path not in current_node.children:
                return None
            current_node = current_node.children[sub_path]
        return current_node.handler

## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode()

## The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.route_trie.insert(path_list, handler)
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if not isinstance(path, str):
            return self.not_found_handler
        path_list = self.split_path(path)
        handler = self.route_trie.find(path_list)
        if handler is None:
            return self.not_found_handler
        else:
            return handler
    
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        out_list = path.strip('/').split('/')
        # Remove empty strings from the list
        # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
        out_list = [x for x in out_list if x]
        return out_list

# Test Cases
## create the router and add a route
router = Router("root handler", "not found handler") 
router.add_handler("/home/about", "about handler")  # add a route

# Nominal test cases
print("Pass" if router.lookup("/home/about/") == "about handler" else "Fail") 
print("Pass" if router.lookup("/home/about") == "about handler" else "Fail") 
print("Pass" if router.lookup("home/about/") == "about handler" else "Fail") 
print("Pass" if router.lookup("/home/about") == "about handler" else "Fail") 

print("Pass" if router.lookup("/") == "root handler" else "Fail") 
print("Pass" if router.lookup("") == "root handler" else "Fail") 

# Edge Case 1: Handler doesn't exist
print("Pass" if router.lookup("/should/not/exist") == "not found handler" else "Fail") 

# Edge Case 2: Invalid input
print("Pass" if router.lookup(None) == "not found handler" else "Fail") 
