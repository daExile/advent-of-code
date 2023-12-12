import java.io.File

class Program(var weight: Int = 0, var downLink: String?, val upLink: MutableList<String> = mutableListOf())

class ProgramTower {
    val tower = mutableMapOf<String, Program>()
    var unbalanced: String? = null
    var delta = 0
    
    fun findImbalance(name: String): Int {
        var total = tower[name]!!.weight
        val held = mutableListOf<Pair<Int, String>>()
        for (item in tower[name]!!.upLink) with(findImbalance(item)) { unbalanced?.let { return 0 } ?: held.add(this to item).also { total += this } }
        if (held.map { it.first }.toSet().size == 2) {
            held.sortBy { it.first }
            val i = if (held[0].first == held[1].first) held.lastIndex else 0
            unbalanced = held[i].second
            delta = held[1].first - held[i].first
        }
        return total
    }
}

fun main() {
    val t = ProgramTower()
    for (entry in File("../__in/07.txt").readLines().map { it.split(" -> ") }) {
        // input parse still terrible
        val name = entry[0].substringBefore(" ")
        val weight = entry[0].substringAfter("(").substringBefore(")").toInt()
        if (t.tower[name] == null) t.tower[name] = Program(weight, null) else t.tower[name]!!.weight = weight
        if (entry.size > 1) for (item in entry[1].split(", ")) {
            if (t.tower[item] != null) t.tower[item]!!.downLink = name else t.tower[item] = Program(0, name)
            t.tower[name]!!.upLink += item
        }
    }
    
    println("Part 1: ${t.tower.keys.find {t.tower[it]!!.downLink == null }.also { t.findImbalance(it!!) }}")
    println("Part 2: ${t.tower[t.unbalanced]!!.weight + t.delta}")
}