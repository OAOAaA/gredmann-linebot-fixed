from modules.zodiac import get_zodiac_compatibility
from modules.tarot import get_tarot_compatibility
from modules.wuxing import get_wuxing_interaction
from modules.ziwei import get_ziwei_info
from modules.yijing import get_yijing_hexagram
from modules.numerology import get_numerology_info
from modules.suggestion import get_suggestion

def extract_pair_traits(a_birth: str, b_birth: str) -> dict:
    return {
        "zodiac_result": get_zodiac_compatibility(a_birth, b_birth),
        "tarot_result": get_tarot_compatibility(a_birth, b_birth),
        "wuxing_result": get_wuxing_interaction(a_birth, b_birth),
        "ziwei_result": get_ziwei_info(a_birth),
        "yijing_result": get_yijing_hexagram(a_birth),
        "numerology_result": get_numerology_info(a_birth),
        "suggestion": get_suggestion(a_birth, b_birth),
    }  # ✅ ← 結尾的大括號絕對不能漏

def extract_traits(birth: str) -> dict:
    # 示例函式：請根據實際邏輯完善內容
    return {
        "zodiac_result": {},
        "tarot_result": {},
        "wuxing_result": {},
        "ziwei_result": {},
        "yijing_result": {},
        "numerology_result": {},
        "base_energy": 0
    }
