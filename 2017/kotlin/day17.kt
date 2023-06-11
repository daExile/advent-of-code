import java.io.File

fun main() {
    val input = File("17.txt").readText().toInt()

    val buffer = IntArray(2018){ 0 }
    var n = 0; var pos = 0
    
    while (n < 2017) {
        n++
        repeat(input) { pos = buffer[pos] }
        buffer[n] = buffer[pos]
        buffer[pos] = n
        pos = buffer[pos]
    }
    println("Part 1: ${buffer[2017]}")

    var target = 0
    n = 0; pos = 0
    
    while (n < 50000000) {
        n++
        pos = (pos + input) % n + 1
        if (pos == 1) target = n
    }
    println("Part 2: $target")
}