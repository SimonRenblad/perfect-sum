# by Simon Renblad

# Solution:
# - enumerates all combinations of n indices, where n goes from 1 to the number of elements in the array
# - for a size n, combinations are represented as bitstrings where 1s are included in the sum and 0s are not
# - the next bitstring (the Nth bitstring) is generated based on the previous one (the N-1th)
# - guarantees the first solution will be the smallest set of indices,
#   allowing for a better average-case complexity than enumerating over all possible combinations

# Acceptable Inputs:
# - integer values (positive, negative and zero) within the practical limit of the Python language
# - strings*
# - lists*
# - potential other python objects that can be concatenated using '+' and compared with '=='
#
# * order matters for these, as A + B != B + A unless A == B for strings and lists

# Limitations:
# - if there are two sets of indices of smallest size, it will ONLY find one

# function for returning smallest set of indices in 'array' for which the elements add up to 'target'
def perfect_sum(array, target):

    num_elements = len(array)

    # need to keep track of previous combination (represented as binary)
    previous_combination = [0]*num_elements

    # check sizes of the varying subsets
    for subset_size in range(1, num_elements + 1):

        # reset combination
        previous_combination = [0]*num_elements

        # final combination with a given number of 1s in binary representation
        final_combination_of_size = [0] * (num_elements - subset_size) + [1] * subset_size

        # iterate over combinations of size 'subset_size'
        while not str(final_combination_of_size) == str(previous_combination):

            ## GENERATE COMBINATION AS BITSTRING

            # first bitstring of size 'subset_size'
            if str(previous_combination) == str([0]*num_elements):
                previous_combination = [1] * subset_size + [0] * (num_elements - subset_size)

            # not first bitstring of size 'subset_size'
            else:

                # backwards passing index
                i = num_elements - 1

                # depth tracks the number of 'blocked' 1s in the previous bitstring
                depth = 0

                # loop until next combination is found
                while i >= 0:

                    # ignore 0s
                    if previous_combination[i] == 1:

                        # blocked i, increase depth and move pointed down
                        if i == (num_elements - 1) or previous_combination[i + 1] == 1:
                            depth += 1
                            i -= 1

                        # i not blocked, move forward bit and add past blocked bits according to depth variable
                        else:

                            # forward passing index
                            j = i + 1

                            # move unblocked bit forward
                            previous_combination[i] = 0
                            previous_combination[j] = 1

                            # iterate over remaining right side bits, adding 1s according to depth, 0s otherwise
                            while j < num_elements - 1:
                                j += 1
                                if depth > 0:
                                    previous_combination[j] = 1
                                    depth -= 1
                                else:
                                    previous_combination[j] = 0

                            # combination created
                            break

                    # 0 in previous combination, decrement backwards passing index
                    else:
                        i -= 1

            ## SUM ELEMENTS AND CHECK

            # index list for printing
            indices = []

            # sum variable, set as None to allow strings and lists as well
            sum_found = None

            # execute sum on combination
            for i, bit in enumerate(previous_combination):

                if bit == 1:

                    indices.append(i)

                    if sum_found == None:
                        sum_found = array[i]
                    else:
                        sum_found += array[i]

            #check sum, stop if found
            if sum_found == target:
                return indices

    #no indices found, return empty list
    return []









