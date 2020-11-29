#The parent_directory function returns the name of the directory that's located
#just above the current working directory. Remember that '..' is a relative path
#alias that means "go up to the parent directory"

def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  dir = os.getcwd()
  relative_parent = os.path.join("..",dir)

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())
