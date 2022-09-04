import json


def load_candidates(file):
    """Загружает данные из файла"""
    with open(file, 'r', encoding='utf-8') as f:
        all_candidates = json.load(f)

    return all_candidates


def get_all(all_candidates):
    """Показывает всех кандидатов"""

    result = '<pre>\n'
    for candidate in all_candidates:
        result += f"{candidate['name']}\n" \
                  f"{candidate['position']}\n" \
                  f"{candidate['skills']}\n\n"
    result += '</pre>'
    return result


def get_by_pk(all_candidates, pk):
    """Возвращает кандидата по pk"""

    for candidate in all_candidates:
        if candidate['pk'] == pk:
            result = f"<img src='{candidate['picture']}'>\n\n" \
                     f"<pre>\n" \
                     f"{candidate['name']}\n" \
                     f"{candidate['position']}\n" \
                     f"{candidate['skills']}\n" \
                     f"</pre>"
            return result
    return None


def get_by_skill(all_candidates, skill):
    """Возвращает кандидатов по навыку"""

    skill_lower = skill.lower()
    candidates_with_skill = []

    for candidate in all_candidates:
        candidate_skills_list = candidate['skills'].lower().split(", ")

        if skill_lower in candidate_skills_list:
            candidates_with_skill.append(candidate)

    result = get_all(candidates_with_skill)
    return result


# тестирование функций
if __name__ == '__main__':
    candidates_file = 'candidates.json'

    decor = "\n" + "-" * 20
    print(f"{decor} load test")
    candidates = load_candidates(candidates_file)
    print(candidates)

    print(f"{decor} get all test")
    print(get_all(candidates))

    print(f"{decor} get by pk test")
    print(get_by_pk(candidates, 2))

    print(f"{decor} get by pk test")
    print(get_by_pk(candidates, 33))

    print(f"{decor} get by skill test")
    print(get_by_skill(candidates, 'pythoN'))

    print(f"{decor} get by skill test")
    print(get_by_skill(candidates, 'asdf'))
