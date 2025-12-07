def merge_k_lists(lists: list[list]) -> list:
    size = len(lists)
    result = []

    seen_idx = dict[int, int]()
    drained_lists = set()
    # iterate until all lists are drained
    while len(drained_lists) < size:
        # find min value acrsoss all lists and the idx of the list
        min_value, min_idx, min_cur_list_idx = None, None, None
        # iterate over each list, get the first unread index
        for i in range(size):
            if i in drained_lists:  # skip lists that have already been drained
                continue
            # get the value of the next idx for the list
            cur_list_idx = seen_idx.get(i, 0)
            cur_value = lists[i][cur_list_idx]
            # update min value for the itertion
            if (min_value is None) or min_value > cur_value:
                min_value = cur_value
                min_idx = i
                min_cur_list_idx = cur_list_idx

        result.append(min_value)
        seen_idx[min_idx] = min_cur_list_idx + 1
        if seen_idx[min_idx] >= len(lists[min_idx]):
            drained_lists.add(min_idx)

    return result


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
