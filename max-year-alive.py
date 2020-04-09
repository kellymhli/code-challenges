def max_year_alive(years) -> int:
    pop = {}
    for born, death in years:
        pop[born] = pop.get(born, 0) + 1
        pop[death] = pop.get(death, 0) - 1

    mx_pop, running_pop = 0, 0
    res_year = None
    for year in sorted(pop.keys()):
        running_pop += pop[year]
        if running_pop > mx_pop:
            mx_pop = running_pop
            res_year = year
    return res_year

print(max_year_alive([(2000, 2010), (1975, 2005), (1975, 2003), (1803, 1809),
                      (1750, 1869), (1840, 1935), (1803, 1921), (1894, 1921)]))