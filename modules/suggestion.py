def get_pairing_suggestion(relation: str, score: int, traits_a: list, traits_b: list) -> str:
    base = {
        "戀人": ["💖 愛是理解與成長的試煉場"],
        "朋友": ["🤝 真誠是關係最穩的橋梁"],
        "同事": ["📈 信任與協作，讓你們共創價值"],
        "家人": ["🏡 血緣是起點，理解是永恆的功課"]
    }
    if score >= 90:
        return f"{base.get(relation, ['💫'])[0]} 你們如星辰交會，是命定的知音。"
    elif score >= 75:
        return f"{base.get(relation, ['✨'])[0]} 默契良好，偶有差異，誠意是關鍵。"
    elif score >= 60:
        return f"{base.get(relation, ['⚖️'])[0]} 若願彼此包容，將成穩固搭檔。"
    else:
        return f"{base.get(relation, ['🌫'])[0]} 差異明顯，靠智慧修煉，方可長久同行。"
def get_suggestion(a_birth: str, b_birth: str) -> str:
    return "✨ 彼此多些理解與尊重，將能創造長久默契的關係。"
