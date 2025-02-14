class ProductOfNumbers:

    def __init__(self):
        # self.queue = deque([])
        self.running_product = deque([])
        self.size = 0

    def add(self, num: int) -> None:
        if self.size == 0 and num > 0:
            # self.queue.append(num)
            self.running_product.append(num)
            self.size = self.size + 1
        else:
            if num == 0:
                number_of_elements_present = self.size
                while number_of_elements_present > 0:
                    # self.queue.popleft()
                    self.running_product.popleft()
                    self.size = self.size - 1
                    number_of_elements_present = number_of_elements_present - 1
            else:
                last_product = self.running_product[-1]
                current_product = last_product * num
                self.running_product.append(current_product)
                self.size = self.size + 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        elif k == self.size:
            return self.running_product[-1]
        else:
            last_product = self.running_product[-1]
            starting_product_index = self.size - 1 - k
            product_at_starting_index = self.running_product[starting_product_index]
            final_product_of_last_k_numbers = int(last_product / product_at_starting_index)
            return final_product_of_last_k_numbers

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)