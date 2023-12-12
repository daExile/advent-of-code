import java.io.File

class SecurityScanner(val depth: Int, val range: Int)

fun main() {
    val firewall = File("../__in/13.txt").readLines()
        .map { line -> line.split(": ").map { it.toInt() } }
        .map { SecurityScanner(it[0], it[1]) }

    var severity = 0
    for (layer in firewall) severity += if (layer.depth % (2 * (layer.range - 1)) == 0) layer.depth * layer.range else 0
    
    var delay = 0
    do {
        var caught = false
        delay++
        for (layer in firewall) {
            caught = (delay + layer.depth) % (2 * (layer.range - 1)) == 0
            if (caught) break
        }
    } while (caught)

    println("Part 1: $severity")
    println("Part 2: $delay")
}