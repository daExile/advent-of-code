import java.io.File

fun main() {
    val input = File("../__in/17.txt").readText().toInt()

    val buffer = IntArray(2018)
    var pos = 0
    
    for (n in 1..2017) {
        repeat(input) { pos = buffer[pos] }
        buffer[n] = buffer[pos]
        buffer[pos] = n
        pos = buffer[pos]
    }
    println("Part 1: ${buffer[2017]}")

    var target = 0
    pos = 0
    
    for (n in 1..50000000) {
        pos = (pos + input) % n + 1
        if (pos == 1) target = n
    }
    println("Part 2: $target")
}