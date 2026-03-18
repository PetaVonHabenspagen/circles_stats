def analyze_password(password, min_length = 8, require_digit = True, require_upper = True, require_symbol = True, banned_words = None):
    counter_used = 0
    counter_active = 0
    score_percent = ((100 / counter_active) * counter_used)
    missing_rules =[]
    if require_symbol == True:
        counter_active += 1
    if require_digit == True:
        counter_active += 1
    if require_upper == True:
        counter_active += 1
    if banned_words != []:
        counter_active += 1
    try:
        if len(password) >= min_length:
            counter_used += 1
        else:
            missing_rules.append("length")
        for i in password:
            if require_digit == True:
                if i.isdigit():
                    counter_used += 1
                    continue
                else:
                    missing_rules.append("digit")
            if require_upper == True:
                if i.isupper():
                    counter_used += 1
                    continue
                else:
                    missing_rules.append("upper")
            if require_symbol == True:
                if i is :
                    counter_used += 1
                    continue
                else:
                    missing_rules.append("symbol")
    
    return
    except ValueError:

