class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # find all the possible 2 pairs for a , b 
        # and store them in the map

        hashmap = {position : num for position , num in enumerate(nums)}
        size = len(hashmap)

        ab_pair_products = {}

        for position_a in range(size):
            for position_b in range((position_a + 1) , size):
                ab_pair_product = hashmap[position_a] * hashmap[position_b]
                if ab_pair_product not in ab_pair_products:
                    ab_pair_products[ab_pair_product] = 0
                ab_pair_products[ab_pair_product] = ab_pair_products[ab_pair_product] + 1

        count = 0
        for ab_pair_product in ab_pair_products:
            frequency_of_product = ab_pair_products[ab_pair_product]
            if frequency_of_product > 1:
                # if you have a the same product appearing for more than 1 time
                # then you need to find the number of combinatios that you can form
                # nCk that is factorial(n) / factorial(k) * factorial(n - k)
                value_to_be_added = (frequency_of_product - 1) * frequency_of_product // 2
                value_to_be_added = value_to_be_added * 8
                count = count + value_to_be_added
        
        return count
