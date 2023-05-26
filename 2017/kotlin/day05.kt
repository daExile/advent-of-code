import java.io.File

fun jumpAround(input: List<Int>, rule: Int = 1): Int {
    val jumps = input.toMutableList()
    var index = 0
    var count = 0
    
    while (true) {
        try {
            index += jumps[index].also{ if (rule == 2 && jumps[index] >= 3) jumps[index]-- else jumps[index]++ }
            count++
        } catch (e: IndexOutOfBoundsException) {
            return count
        }
    }
}

fun main() {
    val input = File("05.txt").readLines().map { it.toInt() }
    
    println("Part 1: ${jumpAround(input)}")
    println("Part 2: ${jumpAround(input, 2)}")
}