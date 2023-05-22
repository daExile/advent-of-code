import java.io.File
import kotlin.math.abs; import kotlin.math.max; import kotlin.math.sign

val move = mapOf("n" to Pair(0, 1), "ne" to Pair(1, 0), "se" to Pair(1, -1), "s" to Pair(0, -1), "sw" to Pair(-1, 0), "nw" to Pair(-1, 1))

fun hexManhattanDist(pos: Pair<Int, Int>): Int = if (pos.first.sign == pos.second.sign) abs(pos.first) + abs(pos.second) else max(abs(pos.first), abs(pos.second))

fun main() {
    val steps = File("11.txt").readText().split(",")
    var pos = Pair(0, 0)
    var maxDist = 0
    
    for (step in steps) {
        pos = Pair(pos.first + move[step]!!.first, pos.second + move[step]!!.second)
        with(hexManhattanDist(pos)) { if (maxDist < this) maxDist = this }
    }
    
    println("Part 1 answer: ${hexManhattanDist(pos)}")
    println("Part 1 answer: $maxDist")
}