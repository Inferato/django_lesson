# class Fibonacci:
#     def __init__(self, max_value) -> None:
#         self.max_value = max_value
#         self.a, self.b = 0, 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.a > self.max_value:
#             raise StopIteration
#         self.a, self.b = self.b, self.a + self.b
#         return self.a - self.b
    
# fib_num = Fibonacci(10)

# def fibonacci(max_value):
#     a, b = 0, 1
#     while a <= max_value:
#         yield a
#         a, b = b, a + b


# breakpoint()

# for num in fibonacci(10):
#     print(num)


# def file_sec(filename):
#     lines = 10
#     chunk = []
#     with open(filename) as file:
#         for line in file:
#             while len <= lines:
#                 chunk.append(line)
#             yield chunk


class Modifier:
    def __init__(self, mod, seq):
        self.mod = mod
        self.seq = seq
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.seq) > 0:
            return self.mod(**self.seq.pop(0))
        raise StopIteration
    
class Animal:
    def __init__(self, name='foo', sound='bar'):
        self.name = name
        self.sound = sound
    
    def say(self):
        return f'{self.name} say {self.sound}'
    

animals = [{'name': 'Dog', 'sound': 'wuf wuf'}, {'name': 'Cat', 'sound': 'mew mew'}]

animal_factory = Modifier(Animal, animals)

# breakpoint()
for animal in animal_factory:
    print(animal.say())