class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0
        n = len(words)
        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            line_words = words[i:j]
            num_words = j - i
            total_chars = sum(len(w) for w in line_words)
            if j == n or num_words == 1:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                spaces = maxWidth - total_chars
                slots = num_words - 1
                each = spaces // slots
                extra = spaces % slots
                parts = []
                for k in range(slots):
                    parts.append(line_words[k])
                    parts.append(' ' * (each + (1 if k < extra else 0)))
                parts.append(line_words[-1])
                line = ''.join(parts)
            res.append(line)
            i = j
        return res