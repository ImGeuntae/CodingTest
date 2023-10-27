def solution(s):
    replace = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for idx, i in enumerate(replace):
        s = s.replace(i, str(idx))
    return int(s)