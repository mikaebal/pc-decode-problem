# use dp where dp[i] is ways to decode up to i
# start with dp[0] = 1, and dp[1] is 0 if first char is 0 else 1
# go left to right and build dp
# try taking 1 digit if it is not 0
# try taking 2 digits if it makes a number from 10 to 26
# watch out for 0 as it can only work as part of 10 or 20
# return dp at the end


def decode(code):
    if code == "":
        return 0

    if code[0] == "0":
        return 0

    code_length = len(code)
    dp = [0] * (code_length + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, code_length + 1):
        one_digit = code[i - 1]
        two_digits = code[i - 2:i]

        if one_digit != "0":
            dp[i] += dp[i - 1]

        if "10" <= two_digits <= "26":
            dp[i] += dp[i - 2]

    return dp[code_length]



assert (decode('12106')) == 2
assert (decode('339')) == 1
assert (decode('306')) == 0

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
