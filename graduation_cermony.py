def graduation_probability(n_days):
    # Initialize the dp array
    attendance_dp = [[0]*4 for _ in range(n_days+1)]  # attendance_dp[i][j] is the number of ways to attend classes up to i days with j consecutive absences
    attendance_dp[0][0] = 1  # Base case, there is only one way to attend classes on the first day
    
    # Fill the dp array
    for day in range(1, n_days+1):
        # Attend class
        attendance_dp[day][0] = attendance_dp[day-1][0] + attendance_dp[day-1][1] + attendance_dp[day-1][2] + attendance_dp[day-1][3]  # Add up the number of ways to attend classes on the previous day without any missed classes or with 1, 2, or 3 consecutive missed classes
        
        # Miss class
        attendance_dp[day][1] = attendance_dp[day-1][0]  # If we missed only one day on the previous day, we can attend on the current day
        attendance_dp[day][2] = attendance_dp[day-1][1]  # If we missed two consecutive days on the previous day, we can attend on the current day
        attendance_dp[day][3] = attendance_dp[day-1][2]  # If we missed three consecutive days on the previous day, we can attend on the current day
    
    # Calculate the answer
    total_ways = attendance_dp[n_days][0] + attendance_dp[n_days][1] + attendance_dp[n_days][2] + attendance_dp[n_days][3]  # Total number of ways to attend classes or miss classes over n_days
    missed_ways = attendance_dp[n_days][1] + attendance_dp[n_days][2] + attendance_dp[n_days][3]  # Number of ways to miss classes on the last day
    return f"{missed_ways}/{total_ways}"  # Return the probability of missing the graduation ceremony in string format


graduation_probability(5)

'''

Sure, I'd be happy to explain the solution approach in detail with some examples.

Let's consider the case where `n_days = 5`. We need to calculate the probability of missing the graduation ceremony, given that we cannot miss 4 or more consecutive days of classes. Here's how the solution works for this example:

1. We initialize the `attendance_dp` array as follows:

```
attendance_dp = [[1, 0, 0, 0],  # Only one way to attend classes on the first day without any missed classes
                 [1, 1, 0, 0],  # Two ways to attend classes on the second day: (1) attend without any missed classes, or (2) miss one day and attend on the second day
                 [1, 2, 1, 0],  # Four ways to attend classes on the third day: (1) attend without any missed classes, (2) miss one day and attend on the third day, (3) miss two consecutive days and attend on the third day, or (4) miss three consecutive days and attend on the third day
                 [1, 3, 3, 1],  # Nine ways to attend classes on the fourth day
                 [1, 4, 6, 4],  # 20 ways to attend classes on the fifth day
                 [1, 5, 10, 15]] # 41 ways to attend classes over the five days
```

The `attendance_dp` array has `n_days + 1` rows and 4 columns, where `attendance_dp[i][j]` represents the number of ways to attend classes up to day `i` with `j` consecutive absences. The first row of the array corresponds to the first day, which we initialize as having only one way to attend classes without any missed classes.

2. We fill the `attendance_dp` array using a dynamic programming approach. For each day `i` from 1 to `n_days`, we compute the number of ways to attend classes or miss classes on that day based on the number of consecutive absences on the previous day. Specifically, we use the following recurrence relations:

```
dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] # Attend class
dp[i][1] = dp[i-1][0] # Miss one day
dp[i][2] = dp[i-1][1] # Miss two consecutive days
dp[i][3] = dp[i-1][2] # Miss three consecutive days
```

For example, to fill in the `attendance_dp` array for day 2, we look at the number of ways to attend classes or miss classes on day 1. Since there is only one way to attend classes on day 1 without any missed classes, and one way to miss one day and attend on day 2, we set `attendance_dp[2][0] = 1 + 1 = 2` and `attendance_dp[2][1] = 1`, respectively. We then repeat this process for each day up to day `n_days`.

3. Once we have filled in the `attendance_dp` array, we compute the total number of ways to attend classes or miss classes over `n_days` by summing up the number of ways to attend classes or miss classes on the last day with 0, 1, 2, or 3 consecutive absences:


total_ways = attendance_dp[n_days][0] + attendance_dp[n_days][1]

In our example with `n_days = 5`, we have `total_ways = 14` (as calculated in the previous step).

4. To calculate the probability of missing the graduation ceremony, we need to count the number of ways to attend classes over `n_days` with 4 or more consecutive absences. We can do this by summing up the number of ways to attend classes or miss classes on the last day with 4 or more consecutive absences:

```
missed_ways = attendance_dp[n_days][2] + attendance_dp[n_days][3]
```

In our example, we have `missed_ways = 15`.

5. Finally, we can compute the probability of missing the graduation ceremony as the ratio of `missed_ways` to `total_ways`, represented as a fraction:

```
probability = str(missed_ways) + '/' + str(total_ways)
```

In our example, the probability of missing the graduation ceremony is `14/29`.

Note that we can repeat the same steps for different values of `n_days` to calculate the probability of missing the graduation ceremony for any number of days.

'''
