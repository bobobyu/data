class KMP:
    def suffix_prefix_public(self, string: str) -> int:
        result_p: list = []
        result_s: list = []
        for ele_p, ele_s in zip(string[:-1], string[::-1][:-1]):
            result_p.append(result_p[-1] + [ele_p] if len(result_p) else [ele_p])
            result_s.append([ele_s] + result_s[-1] if len(result_s) else [ele_s])
        bool_combine = [i for i in result_p if i in result_s]
        return len(bool_combine[-1]) if bool_combine else 0

    def suffix_prefix_list(self, string: str) -> list:
        current_string: str = ''
        result: list = []
        for i in string:
            current_string += i
            result.append(self.suffix_prefix_public(current_string))
        return result

    def __init__(self, template_string: str, source_string: str):
        self.template: str = template_string
        self.source: str = source_string
        self.PMT: list = self.suffix_prefix_list(string=source_string)

    def kmp(self):
        source_point: int = 0
        for template_point, _ in enumerate(self.template):
            if len(self.template) - template_point >= len(self.source) - source_point:
                if self.template[template_point] == self.source[source_point]:
                    if source_point + 1 == len(self.source):
                        return len(self.template) - (source_point + 1)
                    source_point += 1
                else:
                    template_point -= 1
                    source_point -= template_point - self.PMT[source_point - 1]
            else:
                return False

example = KMP(template_string='ababababca', source_string='abababca')
print(example.kmp())