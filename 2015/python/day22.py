print("Puzzle input")
hp_b = int(input("Boss health: "))
dmg_b = int(input("Boss damage: "))

          #mana, turns, dmg, +hp, +mana, +def

spells = {"Magic Missile": [53, 0],
          "Drain": [73, 0],
          "Shield": [113, 5],
          "Poison": [173, 5],
          "Recharge": [229, 4]}

get_logs = False
def turn(player = (50, 500), boss = (hp_b, dmg_b), effects = {}, total = 0, m_min = None, log = []):
    for s in spells:
        log_n = log[:]
        log_n.append(s)
        hp_p, mana_p = player
        hp_b, dmg_b = boss
        #print(s, hp_p, mana_p, hp_b)

        #player turn
        if hard:
            hp_p -= 1
            if hp_p <= 0: continue
        
        e_pt = {}
        if "Poison" in effects: hp_b -= 3 
        if "Recharge" in effects: mana_p += 101 
        for e in effects:
            if effects[e] > 0: e_pt[e] = effects[e] - 1

        if s in e_pt: continue
        if spells[s][0] > mana_p: continue

        mana_p -= spells[s][0]
        total_next = total + spells[s][0]
        if m_min and total_next >= m_min: continue
        
        if s == "Magic Missile":
            hp_b -= 4
        elif s == "Drain":
            hp_b -= 2
            hp_p += 2
        else:
            e_pt[s] = spells[s][1]

        if hp_b <= 0:
            if not m_min or total_next < m_min:
                print("Found win sequence for {} mana".format(total_next))
                if get_logs: print(log_n)
                m_min = total_next
                continue

        #boss turn
        if hard:
            hp_p -= 1
            if hp_p <= 0: continue
            
        e_bt = {}
        def_p = 7 if "Shield" in e_pt else 0
        if "Poison" in e_pt: hp_b -= 3
        if "Recharge" in e_pt: mana_p += 101 
        for e in e_pt:
            if e_pt[e] > 0: e_bt[e] = e_pt[e] - 1
        if hp_b <= 0:
            if not m_min or (total_next and total_next < m_min):
                print("Found win sequence for {} mana (boss turn)".format(total_next))
                if get_logs: print(log_n)
                m_min = total_next
                continue

        else:
            hp_p -= max(dmg_b - def_p, 1)
            if hp_p > 0:
                log_n = log[:]
                log_n.append(s)
                total_next = turn((hp_p, mana_p), (hp_b, dmg_b), e_bt, total_next, m_min, log_n)
                if not m_min or (total_next and total_next < m_min):
                    m_min = total_next
        #print(m_min)
    return m_min     

hard = False
print("Part 1 answer:", turn())
hard = True
print("Part 2 answer:", turn())
