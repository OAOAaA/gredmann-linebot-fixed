from zodiac import get_zodiac_compatibility
from tarot import get_tarot_compatibility
from wuxing import get_wuxing_interaction
from ziwei import get_ziwei_info
from yijing import get_yijing_hexagram
from numerology import get_numerology_info
from suggestion import get_pairing_suggestion

def extract_traits(birth: str) -> dict:
    return {
        "birth": birth,
        "zodiac": get_zodiac_compatibility(birth),
        "tarot": get_tarot_compatibility(birth),
        "wuxing": get_wuxing_interaction(birth),
        "ziwei": get_ziwei_info(birth),
        "yijing": get_yijing_hexagram(birth),
        "numerology": get_numerology_info(birth),
    }
