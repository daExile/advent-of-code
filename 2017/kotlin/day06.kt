import java.io.File

fun main() {
    val banks = File("06.txt").readText().split("""\s+""".toRegex()).map { it.toInt() }.toMutableList()
    var opCount = 0
    val log = mutableMapOf<String, Int>()
    
    while (true) {
        opCount++
        val k = banks.indexOf(banks.max())
        with (banks[k]) {
            banks[k] -= this
            for (i in 1..this) banks[(k + i) % banks.size]++
        }
        if (log[banks.toString()] == null) log[banks.toString()] = opCount else break
    }
    
    println("Part 1: $opCount")
    println("Part 2: ${opCount - log[banks.toString()]!!}")
}