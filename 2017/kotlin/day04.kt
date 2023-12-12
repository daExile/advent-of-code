import java.io.File

fun main() {
    val input = File("../__in/04.txt").readLines()
    
    var count1 = 0
    var count2 = 0
    
    for (line in input) {
        val list = line.split(" ")
        if (list.size == list.toSet().size) count1++
        if (list.size == list.map { it.toList().sorted().toString() }.toSet().size) count2++
    }
    
    println("Part 1: $count1")
    println("Part 2: $count2")
}