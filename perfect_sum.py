

def perfect_sum(array, target):

    #declaring variables
    num_elements = len(array)

    # solved recursively, hence need to keep track of previous combination (represented as binary)
    previous_combination = [0]*num_elements

    # check sizes of the varying subsets
    for subset_size in range(1, num_elements + 1):

        #check if last combination has been found
        is_last_combination_of_size = False

        #reset combination
        previous_combination = [0]*num_elements

        # final combination with a given number of 1s in binary representation
        final_combination_of_size = [0] * (num_elements - subset_size) + [1] * subset_size

        # bitstring of N - 1 combination matches final combination bitstring, hence increase the subset_size and reset previous_combination
        while not str(final_combination_of_size) == str(previous_combination):

            # first bit string
            if str(previous_combination) == str([0]*num_elements):
                previous_combination = [1] * subset_size + [0] * (num_elements - subset_size)

            # not first bit string
            else:

                # backwards passing index
                i = num_elements - 1

                # depth tracks the number of 'blocked' 1s in the previous bitstring
                depth = 0

                # loop until next combination is found
                while i >= 0:

                    # we only care about moving around the active bits
                    if previous_combination[i] == 1:

                        # blocked i, increase depth and move pointed down
                        if i == (num_elements - 1) or previous_combination[i + 1] == 1:
                            depth += 1
                            i -= 1
                            continue

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
                    else:
                        i -= 1

            # index list for printing
            indices = []

            # sum variable
            sum_found = None

            # execute sum on combination
            for i, bit in enumerate(previous_combination):
                if bit == 1:
                    indices.append(i)
                    if sum_found == None:
                        sum_found = array[i]
                    else:
                        sum_found += array[i]

            # catch errors
            if len(indices) != subset_size:
                print("error encountered")
                return

            #check sum
            if sum_found == target:
                return indices

    return []


### TESTING FUNCTIONS, IGNORE
def run_test(input_arr, target, output):
    result = perfect_sum(input_arr, target)
    print(str(input_arr) + ", " + str(target) + ": " + str(result) + " " + str(output == result))

def tests():
   # run_test([2, 3, 4, 8], 2, [0])
  #  run_test([2, 3, 4, 8], 8, [3])
 #   run_test([2, 3, 4, 8], 7, [1, 2])
#    run_test([2, 3, 4, 8], 17, [0, 1, 2, 3])
  #  run_test([], "horse", [])
  #  run_test(["w", "h", "yp"], "wyp", [0, 2])
  #  run_test([0.4, 2.3, 5.4, 7.2], 5.8, [0, 2]) FAILED -> PRECISION WITH FLOAT ISSUE
 #   run_test([-4, 2, 3, 8], 6, [0, 1, 3])
 run_test([39, 38, 6, 2], 46, [1, 2, 3])

tests()











