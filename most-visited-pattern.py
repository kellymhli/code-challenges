def most_visited_pattern(users, timestamp, website) -> list:
    visits = [(users[i], timestamp[i], website[i]) for i in range(len(users))]
    visits.sort(key = lambda x: x[1])  # sort by timestamp

    user_paths = {}
    for visit in visits:
        user_paths[visit[0]] = user_paths.get(visit[0], []) + [visit[2]]  # user:[path1, path2, etc.]

    seqs = {}
    for user, paths in user_paths.items():
        for i in range(len(paths)-2):
            for j in range(i+1, len(paths)-1):
                for k in range(j+1, len(paths)):
                    seqs[(paths[i], paths[j], paths[k])] = seqs.get((paths[i], paths[j], paths[k]), []) + [user]

    path_counts = [(path, len(set(usr))) for path, usr in seqs.items()]
    path_counts.sort(key = lambda x: x[1], reverse = True)

    res_arr = [x for x in path_counts if x[1] == path_counts[0][1]]
    res_arr.sort(key = lambda x: x[0])

    return list(res_arr[0][0])

print(most_visited_pattern(["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"], [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930], ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]))
print(most_visited_pattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"], [1,2,3,4,5,6,7,8,9,10], ["home","about","career","home","cart","maps","home","home","about","career"]))
print(most_visited_pattern(["u1","u1","u1","u2","u2","u2"], [1,2,3,4,5,6], ["a","b","c","a","b","a"]))
