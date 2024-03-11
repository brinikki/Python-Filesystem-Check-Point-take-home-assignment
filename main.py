class Node:
  def __init__(self, name, is_directory=False):
      self.name = name
      self.is_directory = is_directory
      self.children = []
# initialized with a root directory and used to keep track of current working directory
class FileSystem:
  def __init__(self):
      self.root = Node("/", is_directory=True)
      self.current_directory = self.root

  # prints files/folders in current directory
  def ls(self):
      print('Contents of directory', self.get_path() + ':')
      for child in self.current_directory.children:
          print(child.name)

  # creates a new directory and adds node to linkedlist 
  def mkdir(self, directory_name):
      new_directory = Node(directory_name, is_directory=True)
      self.current_directory.children.append(new_directory)

  # change current directory to the directory specified
  def cd(self, directory_name):
      if directory_name == "..":
          self._move_up()
      else:
          child_directory = self._get_child_directory(directory_name)
          if child_directory:
              self.current_directory = child_directory
          else:
              print(f"Directory '{directory_name}' not found")
# makes new file and appends it to current directory 
  def touch(self, file_name):
      new_file = Node(file_name)
      self.current_directory.children.append(new_file)
# finds the child directory in the current directory
  def _get_child_directory(self, name):
      for child in self.current_directory.children:
          if child.is_directory and child.name == name:
              return child
      return None
# cd .. to move up one directory
  
  def _move_up(self):
      if self.current_directory != self.root:
          parent = self._get_parent_directory(self.root, self.current_directory)
          if parent:
              self.current_directory = parent
            
# finds the parent directory of the current directory
  def _get_parent_directory(self, current, origin):
      if origin in current.children:
          return current

      for child in current.children:
          if child.is_directory:
              parent = self._get_parent_directory(child, origin)
              if parent:
                  return parent

      return None
# return path from the root to the current dir
  def get_path(self):
      path = []
      current = self.current_directory
      while current != self.root:
          path.insert(0, current.name)
          current = self._get_parent_directory(self.root, current)
      return "/" + "/".join(path)


# Interface for end user
def main():
  file_system = FileSystem()

  while True:
      command = input("Enter a shell command + <name> (ls, mkdir, cd, touch, exit): ").split()
      cmd = command[0]

      if cmd == "exit":
        print("You have exited the shell.")
        break
      elif cmd == "ls":
          file_system.ls()
      elif cmd == "mkdir" and len(command) == 2:
          file_system.mkdir(command[1])
      elif cmd == "cd" and len(command) == 2:
          file_system.cd(command[1])
      elif cmd == "touch" and len(command) == 2:
          file_system.touch(command[1])
      else:
          print("Invalid prompt. Please try again.")


if __name__ == "__main__":
  main()
