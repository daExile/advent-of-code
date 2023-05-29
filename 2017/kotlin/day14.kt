import java.io.File

operator fun Pair<Int, Int>.plus(other: Pair<Int, Int>) = Pair(this.first + other.first, this.second + other.second)

fun toBinaryString(n: Int) = n.toString(2).padStart(8, '0')

// all the hashing functions are being loaded from day10.kt
fun main() {
    val input = File("14.txt").readText()
    var count1s = 0
    val map = List(128) {
        i -> denseHash(knotHash(List(256) { j -> j }, ("$input-$i").map { it.code } + listOf(17, 31, 73, 47, 23), 64), ::toBinaryString)
        .also { count1s += it.count { it == '1' } }
    }
    println("Part 1: $count1s")
    
    var countRegions = 0
    val checked = mutableSetOf<Pair<Int, Int>>()
    for (i in 0 until map.size) {
        for (j in 0 until map[i].length) {
            if (!checked.contains(Pair(i ,j)) && map[i][j] == '1') {
                countRegions++

                val q = ArrayDeque<Pair<Int, Int>>()
                q.add(Pair(i, j))
                while (true) {
                    with(q.removeFirstOrNull() ?: break) {
                        checked += this
                        for (item in listOf(Pair(0, 1), Pair(1, 0), Pair(-1, 0), Pair(0, -1)))
                            with (this + item) { try {
                                if (!q.contains(this) && !checked.contains(this) && map[this.first][this.second] == '1')
                                    q.add(this)
                            } catch (e: IndexOutOfBoundsException) {} // i know this is bad style
                                // i'll try to make something less sketchy to skip out-of-bounds indices later
                        }
                    }
                }
            }
        }
    }
    println("Part 2: $countRegions")
}