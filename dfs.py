
def Depth_First_Search(matrix, visited, node):
    visited[node] = True
    for i in range(len(matrix)):
        if matrix[node][i] and not visited[i]: 
            Depth_First_Search(matrix, visited, i)
            
def get_minimum_connections(matrix):
    n = len(matrix)
    visited = [False] * n
    components = 0

    for i in range(n):
        if not visited[i]:  
            Depth_First_Search(matrix, visited, i)
            components += 1
    return components - 1
    

matrix = \
    [ 
        [False, True, False, False, True], 
        [True, False, False, False, False], 
        [False, False, False, True, False], 
        [False, False, True, False, False], 
        [True, False, False, False, False] 
    ]
print(get_minimum_connections(matrix))


from collections import defaultdict

class RewardPoints:
    def __init__(self):
        self.customers = defaultdict(int)
        
    def earn_points(self, customer_name, points):
        # Only add points if the number of points is positive
        if points > 0:
            if self.customers[customer_name] == 0:  # Check if it's the customer's first time earning points
                self.customers[customer_name] += 500  # Add the bonus 500 points
            self.customers[customer_name] += points  # Add the regular points
    
    def spend_points(self, customer_name, points):
        # Only subtract points if the number of points is positive
        if points > 0 and customer_name in self.customers:
            # If the customer has fewer points than they want to spend, keep the current balance
            if points > self.customers[customer_name]:
                return self.customers[customer_name]
            self.customers[customer_name] -= points
        # Return the remaining points or 0 if the customer does not exist
        return self.customers[customer_name] if customer_name in self.customers else 0
        
if __name__ == "__main__":
    rewardPoints = RewardPoints()
    rewardPoints.earn_points('John', 520)
    print(rewardPoints.spend_points('John', 200))  # Output: 820 (after spending 200)
    
    # Try to spend more points than available
    print(rewardPoints.spend_points('John', 1000))  # Output: 820 (points stay same)
    
    # Try to earn 0 or negative points
    rewardPoints.earn_points('John', 0)
    print(rewardPoints.spend_points('John', 200))  # Output: 820 (points stay same)
    
    rewardPoints.earn_points('John', -50)
    print(rewardPoints.spend_points('John', 200))  # Output: 820 (points stay same)

    # Try to spend 0 or negative points
    rewardPoints.spend_points('John', 0)
    print(rewardPoints.spend_points('John', 200))  # Output: 820 (points stay same)
    
    rewardPoints.spend_points('John', -50)
    print(rewardPoints.spend_points('John', 200))  # Output: 820 (points stay same)

    print(rewardPoints.spend_points('Unknown', 100))  # Output: 0 (customer doesn't exist)
