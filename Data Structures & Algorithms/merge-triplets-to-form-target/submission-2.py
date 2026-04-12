class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # We track which positions (0,1,2) we can successfully "build"
        # using valid triplets
        good = set()

        for triplet in triplets:
            # If any value exceeds target, this triplet is useless
            # because merge = max(), and we can never reduce values
            # → this would permanently overshoot target
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            # For valid triplets, check if they help us match target
            # at any index
            for i, val in enumerate(triplet):
                # If this triplet matches target at index i,
                # we can "use" it to satisfy that coordinate
                if val == target[i]:
                    good.add(i)

        # We need all 3 positions (0,1,2) to be achievable
        # because merge operation takes max per coordinate
        return len(good) == 3