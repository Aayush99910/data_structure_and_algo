class Node: 
  def __init__(self, key):
    self.key = key 
    self.next = None 

class HashMapSeperateChaining: 
  def __init__(self, size):
    self.size = size 
    self.hash_map = [None] * self.size 
  
  def display(self):
    for i in range(self.size):
      print("Bucket " + str(i) + ":", end=" ")
      current = self.hash_map[i]
      while current is not None:
        print(current.key, end=" -> ")
        current = current.next
      print("None")

class HashMap(HashMapSeperateChaining):
  def calculate_ascii(self, string):
    i = 1
    weighted_sum = 0
    while i <= len(string):
      ascii_value = ord(string[i - 1])
      multiplied = ascii_value * i 
      weighted_sum += multiplied
      i += 1
    
    return weighted_sum
  
  def hash_function(self, key):
    weighted_sum = self.calculate_ascii(key)
    squared_key = str(weighted_sum ** 2)
    if len(squared_key) != 0:
      squared_key = '0' + squared_key 
    
    mid_index = len(squared_key) // 2
    mid_digits = squared_key[mid_index-1:mid_index+1]
    return int(mid_digits) % self.size
  
  def insert(self, key):
    hash_key = self.hash_function(key)
    if self.hash_map[hash_key] == None:
      self.hash_map[hash_key] = Node(key) # type: ignore 
    else: 
      head = self.hash_map[hash_key] 
      new_node = Node(key)
      self.hash_map[hash_key] = new_node #type:ignore
      new_node.next = head 

  def search(self, key):
    hash_key = self.hash_function(key)
    current = self.hash_map[hash_key]
    while current is not None:
      if current.key == key:
        print("Plagiarism Detected:", key)
        return True
      current = current.next
    return False
  

def main():
  original_transcript = "The impact of artificial intelligence in modern education has sparked intense debate among educators and parents alike. While AI tools can personalize learning experiences and provide instant feedback, concerns about over-reliance on technology persist. Students now have access to powerful learning resources that can analyze their progress and adapt to their needs. However, this technological integration raises questions about critical thinking skills and authentic learning experiences. Teachers must carefully balance incorporating these innovative tools while ensuring students develop fundamental analytical and problem-solving abilities without becoming dependent on AI assistance."

  prompt_one = "Technology in education is evolving rapidly. While AI tools can personalize learning experiences and provide instant feedback, concerns about over-reliance on technology persist. Modern educators need to find ways to integrate these tools effectively while maintaining educational standards."

  prompt_two = "The role of technology in classrooms continues to expand. Though artificial intelligence offers customized educational support and real-time assessment capabilities, some worry about students becoming too dependent on digital tools. Educators face the challenge of implementing these advances thoughtfully."

  hash_map = HashMap(50)

  for i in range(len(original_transcript) - 30 + 1):
      sub_string = original_transcript[i:i + 30]
      hash_map.insert(sub_string)
  
  def check_plagiarism(hashmap, prompt):
    plagiarised = False

    for i in range(len(prompt) - 30 + 1):
      sub_string = prompt[i: i + 30]
      plagiarised = hashmap.search(sub_string)
      if plagiarised:
        break
    
    print("No plagiarism detected")

  print("Searching First Prompt")
  check_plagiarism(hash_map, prompt_one)

  print("Searching Second Prompt")
  check_plagiarism(hash_map, prompt_two)


main()