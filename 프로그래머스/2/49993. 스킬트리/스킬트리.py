def solution(skill, skill_trees):
    return len([s for s in [''.join([x for x in i if x in skill]) for i in skill_trees] if skill.startswith(s)])