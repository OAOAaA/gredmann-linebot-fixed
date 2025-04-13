def get_element_from_year(year: int) -> str:
    elements = ["金", "水", "木", "火", "土"]
    return elements[year % 5]

def compare_elements(e1: str, e2: str) -> dict:
    relations = {
        ("水", "木"): "相生", ("木", "火"): "相生", ("火", "土"): "相生", ("土", "金"): "相生", ("金", "水"): "相生",
        ("木", "水"): "相剋", ("火", "金"): "相剋", ("土", "水"): "相剋", ("金", "火"): "相剋", ("水", "土"): "相剋"
    }
    key = (e1, e2)
    relation = relations.get(key, "中性")
    score = 90 if relation == "相生" else 60 if relation == "相剋" else 75
    return {"relation": relation, "score": score}

def get_wuxing_interaction(a_element: str, b_element: str) -> dict:
    """
    根據五行的相生相剋關係，計算兩者互動與分數。
    """
    interaction_map = {
        ("木", "火"): ("相生", 90, "木生火，助力強大"),
        ("火", "土"): ("相生", 90, "火生土，協作穩定"),
        ("土", "金"): ("相生", 90, "土生金，資源互補"),
        ("金", "水"): ("相生", 90, "金生水，潛力激發"),
        ("水", "木"): ("相生", 90, "水生木，成長動能"),
        ("火", "金"): ("相剋", 60, "火剋金，易生衝突"),
        ("金", "木"): ("相剋", 60, "金剋木，受限明顯"),
        ("木", "土"): ("相剋", 60, "木剋土，競合關係"),
        ("土", "水"): ("相剋", 60, "土剋水，壓力存在"),
        ("水", "火"): ("相剋", 60, "水剋火，理念差異"),
    }

    key = (a_element, b_element)
    reversed_key = (b_element, a_element)

    if key in interaction_map:
        relation, score, detail = interaction_map[key]
    elif reversed_key in interaction_map:
        relation, score, detail = interaction_map[reversed_key]
    else:
        relation, score, detail = "中性", 75, "五行無明顯相剋相生"

    return {
        "interaction": relation,
        "score": score,
        "detail": detail
    }
