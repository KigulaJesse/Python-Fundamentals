import re

# pattern = re.compile(r"<(/?)(\w+)([^>]*)>")
# pattern = re.compile(r"<(/?)(\w+)([^>]*)>")

# # Example HTML-like string
# text = """
#     <div class='container' name="james" id="james">
#         Content
#         <br/>
#     </div>
# """

# matches = pattern.findall(text)

# for match in matches:
#     print(match)


import time
import memory_profiler

# Memory Inefficient Version
def read_large_file_inefficient(file_path):
    with open(file_path, "r") as f:
        return f.readlines()  # Loads entire file into memory

# Memory Efficient Version
def read_large_file_efficient(file_path):
    with open(file_path, "r") as f:
        for line in f:
            yield line  # Yields one line at a time (generator)

# Function to measure memory usage and execution time
def measure_memory_and_time(func, file_path):
    start_time = time.time()
    mem_before = memory_profiler.memory_usage()[0]

    if callable(func):  
        if hasattr(func, '__iter__'):  # For generators
            for _ in func(file_path):
                pass  # Consume generator
        else:
            func(file_path)  # Run normal function
    
    mem_after = memory_profiler.memory_usage()[0]
    end_time = time.time()

    print(f"Function: {func.__name__}")
    print(f"Memory Used: {mem_after - mem_before:.2f} MB")
    print(f"Execution Time: {end_time - start_time:.2f} seconds")
    print("-" * 40)

# Test on a large text file
file_path = "large_text_file.txt"

print("Testing Memory Inefficient Version:")
measure_memory_and_time(read_large_file_inefficient, file_path)

print("Testing Memory Efficient Version:")
measure_memory_and_time(read_large_file_efficient, file_path)



# Test on a large tex
