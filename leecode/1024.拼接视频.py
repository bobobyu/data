class Solution:
    def videoStitching(self, clips: list, T: int) -> int:
        if not clips:
            return -1
        clips.sort(key=lambda x: (x[0], x[1]))
        if clips[0][0] != 0:
            return -1
        point = 0
        alternative = []
        while point < len(clips) - 1:
            if clips[point + 1][0] != clips[point][0]:
                alternative.append(clips[point])
            point += 1
        if clips[point][0] != alternative[-1][0]:
            alternative.append(clips[-1])
        current_clip = []
        print(alternative)
        for i in alternative:
            if current_clip:
                if i[0] > current_clip[-1][-1]:
                    return -1
                if i[-1] > current_clip[-1][-1]:
                    if len(current_clip) >= 2:
                        # print(current_clip, i, 'a')
                        if i[0] <= current_clip[-2][-1] and current_clip[-1][0] <= current_clip[-2][-1] and \
                                current_clip[-1][-1] <= i[-1]:
                            current_clip.pop(-1)
                            current_clip.append(i)
                            if i[-1] >= T:
                                print(current_clip)
                                return len(current_clip)
                            continue
                    current_clip.append(i)
            else:
                current_clip.append(i)
            if i[-1] >= T:
                print(current_clip)
                return len(current_clip)
        return -1


s = Solution()
print(s.videoStitching(
    [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15], [11, 16], [12, 17],
     [13, 18], [14, 19], [15, 20], [16, 21], [17, 22], [18, 23], [19, 24], [20, 25], [21, 26], [22, 27], [23, 28],
     [24, 29], [25, 30], [26, 31], [27, 32], [28, 33], [29, 34], [30, 35], [31, 36], [32, 37], [33, 38], [34, 39],
     [35, 40], [36, 41], [37, 42], [38, 43], [39, 44], [40, 45], [41, 46], [42, 47], [43, 48], [44, 49], [45, 50],
     [46, 51], [47, 52], [48, 53], [49, 54]]
,50))
