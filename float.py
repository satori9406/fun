def decimal_to_binary(n):
    binary = "0."
    while n > 0:
        n *= 2
        if n >= 1:
            binary += "1"
            n -= 1
        else:
            binary += "0"
        
        # 安全機制：防止無限循環
        if len(binary) > 50: 
            break
    return binary

print(decimal_to_binary(0.8125))
# 輸出: 0.1101
