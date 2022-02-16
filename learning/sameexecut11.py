from operator import truediv


class Prime:
    def __init__(self, number):
        self.number = number

    def is_prime(self):
        is_prime_number = True
        index = 2
        while(index < self.number//2):
          if self.number%index == 0:
              is_prime_number = False
              break
        index = index+1
        return is_prime_number

def main():
    value = 7
    prime =Prime(value)
    if prime.is_prime():
     print("prime number")
    else:
     print("not a prime number")

if __name__ == "__main__":
    #this module is executed directly.
    main()