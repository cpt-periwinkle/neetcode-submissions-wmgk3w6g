class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # ---------------- CORE IDEA ----------------
        # Instead of using a heap to repeatedly get the largest stones,
        # we count how many stones exist for each weight.
        #
        # bucket[x] = number of stones with weight x
        #
        # This lets us simulate smashing from largest → smallest efficiently.

        maxStone = max(stones)

        # Create frequency array (bucket)
        bucket = [0] * (maxStone + 1)

        # Fill counts
        for stone in stones:
            bucket[stone] += 1


        # ---------------- POINTERS ----------------
        # first  = current largest stone we are processing
        # second = next largest stone to smash with
        first = second = maxStone


        # ---------------- MAIN LOOP ----------------
        # We process from largest weight downward
        while first > 0:

            # ---------------- EVEN COUNT CASE ----------------
            # If we have an EVEN number of stones of this weight:
            # they all cancel each other out (x vs x → 0)
            #
            # So we can skip this weight entirely
            if bucket[first] % 2 == 0:
                first -= 1
                continue


            # ---------------- FIND NEXT LARGEST ----------------
            # We have ONE leftover stone of weight "first"
            # Now we need the next largest stone to smash it with
            #
            # Start searching from below "first"
            j = min(first - 1, second)

            # Move downward until we find a weight that exists
            while j > 0 and bucket[j] == 0:
                j -= 1


            # ---------------- NO SECOND STONE ----------------
            # If we can't find another stone,
            # this leftover stone is the answer
            if j == 0:
                return first


            # ---------------- SMASH OPERATION ----------------
            # Smash:
            # first (largest) with second (next largest)
            #
            # Remove one stone from each
            second = j
            bucket[first] -= 1
            bucket[second] -= 1

            # Add the resulting stone (difference)
            # Example: 8 - 7 = 1 → bucket[1] += 1
            bucket[first - second] += 1


            # ---------------- UPDATE POINTER ----------------
            # After smashing:
            # The new stone is (first - second)
            # OR second might still be larger than that
            #
            # So we update "first" to the larger of the two possibilities
            first = max(first - second, second)


        # If all stones cancel out, return 0
        return first