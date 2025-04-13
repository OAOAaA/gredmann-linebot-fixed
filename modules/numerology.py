def calculate_numbers(year: int, month: int, day: int) -> dict:
    core = sum(int(c) for c in str(year)[-2:])
    base = int(f"{year}{month:02}{day:02}")
    total = sum(int(d) for d in str(base))
    outer = sum(int(d) for d in str(total))
    if outer > 22:
        outer -= 22
    inner = outer if outer < 22 else sum(map(int, str(outer)))
    return {
        "core": core,
        "outer": outer,
        "inner": inner
    }
# modules/numerology.py

def get_numerology_info(birthdate: str) -> dict:
    # 這裡簡化：將生日轉為總數字
    digits = [int(ch) for ch in birthdate if ch.isdigit()]
    core_number = sum(digits)
    while core_number >= 10:
        core_number = sum([int(d) for d in str(core_number)])
    
    return {
        "core_number": core_number,
        "description": f"你的西元命數為 {core_number}，代表堅持、創造與原則的能量。"
    }
