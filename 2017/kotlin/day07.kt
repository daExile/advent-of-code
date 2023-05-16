import java.io.File

// this is a convoluted mess
// i'm sort of lost in its logic chain for now to make it prettier :D
// let's just solve it for now

class Program(var weight: Int = 0, var downLink: String?, val upLink: MutableList<String> = mutableListOf()) {
    var total: Int? = null
}

class ProgramTower {
    val tower = mutableMapOf<String, Program>()
    var unbalanced: String? = null
    var delta = 0
    
    fun getTotalWeight(name: String): Int {
        var totalWeight = tower[name]!!.weight
        val weightsAbove = mutableMapOf<String, Int>()
        for (item in tower[name]!!.upLink) weightsAbove += item to (tower[item]!!.total ?: getTotalWeight(item)).also { totalWeight += it }
        if (unbalanced == null && weightsAbove.values.toSet().size > 1) {
            var wrong = 0
            val weights = weightsAbove.values.toSet().toMutableList()
            for (n in weights) if (weightsAbove.values.count { it == n } == 1) wrong = n
            weights.remove(wrong)
            delta = weights[0] - wrong
            unbalanced = weightsAbove.keys.find { weightsAbove[it] == wrong }
        }
        return totalWeight.also {tower[name]!!.total = totalWeight}
    }
}

fun main() {
    val t = ProgramTower()
    val towerBase: String
    for (entry in File("07.txt").readLines().map { it.split(" -> ") }) {
        // regex this or something
        val name = entry[0].substringBefore(" ")
        val weight = entry[0].substringAfter("(").substringBefore(")").toInt()
        if (t.tower[name] == null) t.tower[name] = Program(weight, null) else t.tower[name]!!.weight = weight
        if (entry.size > 1) for (item in entry[1].split(", ")) {
            if (t.tower[item] != null) t.tower[item]!!.downLink = name else t.tower[item] = Program(0, name)
            t.tower[name]!!.upLink += item
        }
    }
    
    println("Part 1 answer: ${t.tower.keys.find {t.tower[it]!!.downLink == null }.also { towerBase = it!! }}")
    t.getTotalWeight(towerBase)
    println("Part 2 answer: ${t.unbalanced} should have a weight of ${t.tower[t.unbalanced]!!.weight + t.delta}")
}