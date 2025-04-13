def get_tarot_card(month: int, day: int) -> str:
    cards = ["愚人", "魔術師", "女祭司", "皇后", "皇帝", "教皇", "戀人", "戰車", "力量", "隱者",
             "命運之輪", "正義", "吊人", "死神", "節制", "惡魔", "高塔", "星星", "月亮", "太陽", "審判", "世界"]
    index = (month + day) % len(cards)
    return cards[index]

def compare_tarot_cards(card1: str, card2: str) -> dict:
    interaction = "轉化型關係" if (card1, card2) != (card2, card1) else "鏡像效應"
    score = 85 if interaction == "轉化型關係" else 70
    return {"interaction": interaction, "compatibility_score": score}

def get_tarot_compatibility(card_a: str, card_b: str) -> dict:
    # 塔羅主牌互動邏輯（簡化版）
    interaction_map = {
        ("力量", "死神"): {
            "type": "轉化型關係",
            "detail": "力量與死神象徵重生與堅持的力量",
            "compatibility_score": 87
        },
        # 可依照更多組合擴充
    }

    key = (card_a, card_b)
    reverse_key = (card_b, card_a)

    result = interaction_map.get(key) or interaction_map.get(reverse_key)

    return result or {
        "type": "一般互動",
        "detail": f"{card_a} 與 {card_b} 組合待擴充",
        "compatibility_score": 70
    }
